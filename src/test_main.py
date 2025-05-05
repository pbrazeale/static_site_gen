import unittest

from main import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_title(self):
        markdown = "# This is a title\nThis is a second line."
        title = extract_title(markdown)
        self.assertEqual(title, "This is a title")