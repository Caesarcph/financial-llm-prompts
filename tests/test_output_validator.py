"""Tests for output validation utilities."""

import unittest

from fin_prompts import OutputValidator, ValidationResult, validate_response


class TestOutputValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = OutputValidator()

    def test_extract_json_from_code_block(self) -> None:
        text = '''Here is the analysis:
```json
{"trend": "bullish", "confidence": 0.8}
```
Done.'''
        json_str = self.validator.extract_json(text)
        self.assertIsNotNone(json_str)
        assert json_str is not None
        self.assertIn('"trend"', json_str)

    def test_extract_json_raw(self) -> None:
        text = 'Some text {"key": "value"} more text'
        json_str = self.validator.extract_json(text)
        self.assertIsNotNone(json_str)

    def test_validate_json_success(self) -> None:
        text = '{"trend": "bullish", "confidence": 0.75}'
        result = self.validator.validate_json(text)
        self.assertTrue(result.is_valid)
        self.assertEqual(result.data, {"trend": "bullish", "confidence": 0.75})

    def test_validate_json_with_required_keys(self) -> None:
        text = '{"trend": "bullish", "confidence": 0.75}'
        result = self.validator.validate_json(
            text, required_keys=["trend", "confidence"]
        )
        self.assertTrue(result.is_valid)

    def test_validate_json_missing_required_key(self) -> None:
        text = '{"trend": "bullish"}'
        result = self.validator.validate_json(
            text, required_keys=["trend", "confidence"]
        )
        self.assertFalse(result.is_valid)
        self.assertIn("confidence", result.error or "")

    def test_validate_enum_success(self) -> None:
        data = {"trend": "bullish", "sentiment": "positive"}
        result = self.validator.validate_enum(
            data,
            enum_fields={"trend": ["bullish", "bearish", "ranging"]},
        )
        self.assertTrue(result.is_valid)

    def test_validate_enum_failure(self) -> None:
        data = {"trend": "unknown"}
        result = self.validator.validate_enum(
            data,
            enum_fields={"trend": ["bullish", "bearish", "ranging"]},
        )
        self.assertFalse(result.is_valid)
        self.assertIn("unknown", result.error or "")

    def test_warning_on_null_value(self) -> None:
        text = '{"trend": "bullish", "notes": null}'
        result = self.validator.validate_json(text)
        self.assertTrue(result.is_valid)
        self.assertIsNotNone(result.warnings)
        assert result.warnings is not None
        self.assertTrue(any("null" in w for w in result.warnings))


class TestValidateResponse(unittest.TestCase):
    def test_full_validation_with_enum(self) -> None:
        text = '''
```json
{"trend": "bullish", "confidence": 0.8}
```
'''
        result = validate_response(
            text,
            required_keys=["trend", "confidence"],
            enum_fields={"trend": ["bullish", "bearish", "ranging"]},
        )
        self.assertTrue(result.is_valid)
        assert result.data is not None
        self.assertEqual(result.data["trend"], "bullish")

    def test_invalid_json_response(self) -> None:
        text = "This is not JSON at all"
        result = validate_response(text)
        self.assertFalse(result.is_valid)


if __name__ == "__main__":
    unittest.main()
