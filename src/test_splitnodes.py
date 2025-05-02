import unittest

from splitnodes import (
    split_nodes_delimiter, 
    extract_markdown_images, 
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
)
from textnode import TextNode, TextType

class TestSplitnodes(unittest.TestCase):
    # Tests split_nodes_delimiter
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

    # Tests extract_markdown_images
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    # Tests extract_markdown_links
    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    # Tests split_nodes_image
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    # Tests split_nodes_link
    def test_split_images(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
