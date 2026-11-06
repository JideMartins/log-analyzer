from unittest import TestCase
from log_analyzer import (
    get_level,
    parse_line,
    analyze_lines,
    analyze_file,
    filter_lines,
)


class TestLogAnalyzer(TestCase):

    # test get_level()
    def test_get_level_works(self):
        self.assertEqual(get_level("INFO Application started"), "INFO")

    def test_get_level_none(self):
        self.assertIsNone(get_level(""))

    # test parse_line()
    def test_parse_line(self):
        # personal -> should return a dictioary when conditions are met
        self.assertIsInstance(parse_line("  WARNING Disk  space low  "), dict)

        self.assertEqual(
            parse_line("WARNING Disk  space low"),
            {"level": "WARNING", "message": "Disk  space low"},
        )

    def test_parse_line_none(self):
        self.assertIsNone(parse_line("ERROR"))
