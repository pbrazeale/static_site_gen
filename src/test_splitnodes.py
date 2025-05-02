import unittest

from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitnodes(unittest.TestCase):
    def test_pure_text(self):
        node = TextNode("This is a pure text sentence.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "", TextType.TEXT)
        self.assertEqual(new_nodes, 
            [
                TextNode("This is a pure text sentence.", TextType.TEXT),
            ]
        )



if __name__ == "__main__":
    unittest.main()
