import unittest

from fin_prompts import PromptLibrary, PromptTemplate


class TestPromptLibrary(unittest.TestCase):
    def test_list_keys_includes_known_prompt(self) -> None:
        lib = PromptLibrary("prompts")
        keys = lib.list_keys()
        self.assertIn("market_analysis/trend_analysis", keys)

    def test_template_variables(self) -> None:
        tpl = PromptTemplate(key="x", content="Hello {{name}} on {{ day }}")
        self.assertEqual(tpl.variables(), {"name", "day"})

    def test_fill_supports_spaced_placeholders(self) -> None:
        tpl = PromptTemplate(key="x", content="Hello {{ name }} on {{day}}")
        self.assertEqual(tpl.fill(name="Caesar", day="Monday"), "Hello Caesar on Monday")

    def test_from_sections_builds_markdown_template(self) -> None:
        tpl = PromptTemplate.from_sections(
            key="custom/my_prompt",
            system="You are a {{role}} analyst.",
            user="Analyze {{symbol}}.",
            output_schema={"summary": "...", "confidence": 0.0},
        )
        self.assertIn("## System", tpl.content)
        self.assertIn("## User", tpl.content)
        self.assertIn("```json", tpl.content)
        rendered = tpl.fill(role="macro", symbol="AAPL")
        self.assertIn("macro", rendered)
        self.assertIn("AAPL", rendered)


if __name__ == "__main__":
    unittest.main()
