import unittest

from splitnodes import split_nodes_delimiter
from textnode import TextNode

class TestSplitnodes(unittest.TestCase):
    def test_pure_text(self):
        node = TextNode("This is a pure text sentence.", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "", TextType.TEXT), "This is a pure text sentence.")



if __name__ == "__main__":
    unittest.main()
