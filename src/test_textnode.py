import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node2, node3)

    def test_not_eq2(self):
        node4 = TextNode("This is a text node", TextType.LINK, "https://boot.dev")
        node5 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node4, node5)
    
    def test_eq_url(self):
        node4 = TextNode("This is a text node", TextType.LINK, "https://boot.dev")
        node6 = TextNode("This is a text node", TextType.LINK, "https://boot.dev")
        self.assertEqual(node4, node6)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()