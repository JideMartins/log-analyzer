from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
from log_analyzer import (
    get_level,
    parse_line,
    analyze_lines,
    analyze_file,
    filter_lines,
)


class TestLogAnalyzer(TestCase):

    # set up
    def setUp(self):
        # temporary
        self.tmp_directory_object = TemporaryDirectory()

        # temporary directory
        self.tmp_dir = Path(self.tmp_directory_object.name)

        # target file path
        self.target_file_path = self.tmp_dir / "temp_log.log"

        # clean up after
        self.addCleanup(self.tmp_directory_object.cleanup)

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
            parse_line("  WARNING Disk  space low  "),
            {"level": "WARNING", "message": "Disk  space low"},
        )

    def test_parse_line_none(self):
        self.assertIsNone(parse_line("ERROR"))

    def test_analyze_files_mixed_entries(self):
        self.target_file_path.write_text(
            "INFO Café ready\nERROR Failed\n\nWARNING", encoding="utf-8"
        )
        self.assertEqual(
            analyze_file(self.target_file_path),
            {"INFO": 1, "WARNING": 0, "ERROR": 1, "malformed": 2},
        )

    def test_analyze_files_empty_file(self):
        self.target_file_path.write_text("", encoding="utf-8")
        self.assertEqual(
            analyze_file(self.target_file_path),
            {"INFO": 0, "WARNING": 0, "ERROR": 0, "malformed": 0},
        )

    def test_analyze_files_one_blank_line(self):
        self.target_file_path.write_text("\n", encoding="utf-8")
        self.assertEqual(
            analyze_file(self.target_file_path),
            {"INFO": 0, "WARNING": 0, "ERROR": 0, "malformed": 1},
        )

    def test_analyze_files_missing_file(self):

        with self.assertRaises(FileNotFoundError):
            analyze_file(self.target_file_path)
