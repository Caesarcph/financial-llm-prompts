"""Lightweight prompt loading utilities for financial-llm-prompts."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from string import Template
from typing import Any, Callable

from .output_validator import OutputValidator, ValidationResult, validate_response


@dataclass(slots=True)
class PromptTemplate:
    """A markdown prompt template loaded from disk."""

    key: str
    content: str

    _VAR_PATTERN = re.compile(r"\{\{\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\}\}")

    @classmethod
    def from_sections(
        cls,
        key: str,
        system: str,
        user: str,
        output_schema: dict[str, Any] | None = None,
    ) -> "PromptTemplate":
        """Build a template from ``System``/``User`` sections.

        Args:
            key: Prompt key used by PromptLibrary.
            system: System instruction text.
            user: User prompt text.
            output_schema: Optional JSON schema example to append.
        """

        sections = ["## System", system.strip(), "", "## User", user.strip()]
        if output_schema:
            pretty_schema = json.dumps(output_schema, indent=2, ensure_ascii=False)
            sections.extend([
                "",
                "**Output Format:**",
                "```json",
                pretty_schema,
                "```",
            ])
        content = "\n".join(sections).strip() + "\n"
        return cls(key=key, content=content)

    def variables(self) -> set[str]:
        """Return the set of ``{{var}}`` placeholder names used in this template."""

        return set(self._VAR_PATTERN.findall(self.content))

    def fill(self, **variables: Any) -> str:
        """Fill ``{{var}}`` placeholders with provided values."""

        # Normalize all ``{{ var }}`` placeholders to ``${var}`` so spacing is supported.
        normalized = self._VAR_PATTERN.sub(r"${\1}", self.content)
        try:
            return Template(normalized).substitute({k: str(v) for k, v in variables.items()})
        except KeyError as exc:
            missing = exc.args[0]
            raise ValueError(f"Missing template variable: {missing}") from exc

    def save(self, path: str | Path) -> None:
        """Save this template to a markdown file.

        Args:
            path: File path to save to (should end with .md).
        """
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(self.content, encoding="utf-8")


class PromptLibrary:
    """Load and retrieve markdown prompts by key path."""

    def __init__(self, prompts_dir: str | Path = "prompts") -> None:
        self.prompts_dir = Path(prompts_dir)

    def get(self, key: str) -> PromptTemplate:
        """Get prompt by key like ``market_analysis/trend_analysis``."""

        path = self.prompts_dir / f"{key}.md"
        if not path.exists():
            raise FileNotFoundError(f"Prompt not found: {path}")
        return PromptTemplate(key=key, content=path.read_text(encoding="utf-8"))

    def list_keys(self) -> list[str]:
        """List all available prompt keys relative to ``prompts_dir``.

        Example returned key: ``market_analysis/trend_analysis``.
        """

        if not self.prompts_dir.exists():
            return []
        keys: list[str] = []
        for path in sorted(self.prompts_dir.rglob("*.md")):
            rel = path.relative_to(self.prompts_dir)
            keys.append(rel.as_posix()[:-3])
        return keys


class LLMClient:
    """Tiny adapter for integrating provider clients.

    Pass a callable via ``analyzer`` that accepts a prompt string and returns text.
    """

    def __init__(
        self,
        provider: str,
        model: str,
        analyzer: Callable[[str], str] | None = None,
    ) -> None:
        self.provider = provider
        self.model = model
        self._analyzer = analyzer

    def analyze(self, prompt: str) -> str:
        """Run analysis with configured callable or fail with clear guidance."""

        if self._analyzer is None:
            raise RuntimeError(
                "No analyzer callable configured. "
                "Pass analyzer=your_client_call in LLMClient(...)."
            )
        return str(self._analyzer(prompt))


class PromptChain:
    """Execute a chain of prompts with weighted results.

    Allows combining multiple prompt analyses into a single comprehensive result.
    """

    def __init__(
        self,
        chain: list[tuple[str, dict[str, Any]]],
        library: PromptLibrary | None = None,
    ) -> None:
        """Initialize prompt chain.

        Args:
            chain: List of (prompt_key, config) tuples. Config can include 'weight'.
            library: PromptLibrary instance (uses default if None).
        """
        self.chain = chain
        self.library = library or PromptLibrary()

    def execute(
        self,
        client: LLMClient,
        context: dict[str, Any] | None = None,
        **variables: Any,
    ) -> list[dict[str, Any]]:
        """Execute all prompts in chain and return weighted results.

        Args:
            client: LLMClient instance for making requests.
            context: Optional shared context passed to all prompts.
            **variables: Additional variables passed to each prompt.

        Returns:
            List of dicts with 'prompt_key', 'weight', 'response', 'parsed' keys.
        """
        results: list[dict[str, Any]] = []
        combined_vars = {**(context or {}), **variables}

        for prompt_key, config in self.chain:
            weight = config.get("weight", 1.0)
            template = self.library.get(prompt_key)
            filled = template.fill(**combined_vars)
            response = client.analyze(filled)

            # Try to parse JSON response
            parsed = None
            validator = OutputValidator()
            validation = validator.validate_json(response)
            if validation.is_valid:
                parsed = validation.data

            results.append({
                "prompt_key": prompt_key,
                "weight": weight,
                "response": response,
                "parsed": parsed,
            })

        return results


__all__ = [
    "PromptLibrary",
    "PromptTemplate",
    "LLMClient",
    "PromptChain",
    "OutputValidator",
    "ValidationResult",
    "validate_response",
]
