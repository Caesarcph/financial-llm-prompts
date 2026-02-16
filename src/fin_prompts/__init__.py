"""Lightweight prompt loading utilities for financial-llm-prompts."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from string import Template
from typing import Any, Callable


@dataclass(slots=True)
class PromptTemplate:
    """A markdown prompt template loaded from disk."""

    key: str
    content: str

    _VAR_PATTERN = re.compile(r"\{\{\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\}\}")

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


__all__ = ["PromptLibrary", "PromptTemplate", "LLMClient"]
