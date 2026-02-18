"""Output validation utilities for LLM responses.

Provides JSON extraction and basic schema validation for financial analysis prompts.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ValidationResult:
    """Result of validating an LLM response."""
    is_valid: bool
    data: Any | None = None
    error: str | None = None
    warnings: list[str] | None = None


class OutputValidator:
    """Validate and parse LLM output responses."""

    _JSON_BLOCK_PATTERN = re.compile(r"```(?:json)?\s*\n?([\s\S]*?)\n?```", re.IGNORECASE)

    def __init__(self, strict: bool = False) -> None:
        self.strict = strict

    def extract_json(self, text: str) -> str | None:
        """Extract JSON string from LLM response text."""
        match = self._JSON_BLOCK_PATTERN.search(text)
        if match:
            return match.group(1).strip()
        if not self.strict:
            start, end = text.find("{"), text.rfind("}")
            if start != -1 and end != -1 and end > start:
                candidate = text[start:end + 1]
                try:
                    json.loads(candidate)
                    return candidate
                except json.JSONDecodeError:
                    pass
        return None

    def validate_json(self, text: str, required_keys: list[str] | None = None) -> ValidationResult:
        """Validate JSON output from LLM response."""
        json_str = self.extract_json(text)
        if json_str is None:
            return ValidationResult(is_valid=False, error="No valid JSON found in response")
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError as exc:
            return ValidationResult(is_valid=False, error=f"Invalid JSON: {exc.msg}")
        if not isinstance(data, dict):
            return ValidationResult(is_valid=False, error="JSON root must be an object")
        if required_keys:
            missing = [k for k in required_keys if k not in data]
            if missing:
                return ValidationResult(is_valid=False, error=f"Missing required keys: {missing}")
        warnings = [f"Key '{k}' has null value" for k, v in data.items() if v is None]
        return ValidationResult(is_valid=True, data=data, warnings=warnings or None)

    def validate_enum(self, data: dict[str, Any], enum_fields: dict[str, list[str]]) -> ValidationResult:
        """Validate that fields contain only allowed enum values."""
        for field, allowed in enum_fields.items():
            if field in data and data[field] not in allowed:
                return ValidationResult(
                    is_valid=False,
                    error=f"Field '{field}' value '{data[field]}' not in allowed: {allowed}"
                )
        return ValidationResult(is_valid=True, data=data)


def validate_response(
    text: str,
    required_keys: list[str] | None = None,
    enum_fields: dict[str, list[str]] | None = None,
) -> ValidationResult:
    """Convenience function to validate LLM response."""
    validator = OutputValidator()
    result = validator.validate_json(text, required_keys)
    if not result.is_valid or not enum_fields or not result.data:
        return result
    return validator.validate_enum(result.data, enum_fields)


__all__ = ["OutputValidator", "ValidationResult", "validate_response"]
