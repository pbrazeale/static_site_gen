import unittest

from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitnodes(unittest.TestCase):
    def test_pure_text(self):
        node = TextNode("This is a pure text sentence.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "", TextType.TEXT)
        self.assertNotEqual(new_nodes, 
            [
                TextNode("This is a pure text sentence.", TextType.TEXT),
            ]
        )

    def test_blod_text(self):
        node = TextNode("This is a **bold** text sentence.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.TEXT)
        self.assertNotEqual(new_nodes, 
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text sentence.", TextType.TEXT),
            ]
        )

    def test_italic_text(self):
        node = TextNode("This is a _italicized_ text sentence.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.TEXT)
        self.assertNotEqual(new_nodes, 
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("italicized", TextType.ITALIC),
                TextNode(" text sentence.", TextType.TEXT),
            ]
        )

    def test_code_text(self):
        node = TextNode("This is a `code` text sentence.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.TEXT)
        self.assertNotEqual(new_nodes, 
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text sentence.", TextType.TEXT),
            ]
        )

    def test_exception_text(self):
        node = TextNode("This is a `failed text sentence.", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.TEXT)
        self.assertEqual(str(context.exception), '"`" missing at the beginning or end of the selection.')


if __name__ == "__main__":
    unittest.main()
