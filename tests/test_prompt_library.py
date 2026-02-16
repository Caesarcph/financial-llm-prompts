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


if __name__ == "__main__":
    unittest.main()
