import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Bold me!")
        self.assertEqual(node.to_html(), '<b>Bold me!</b>')

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Italics me!")
        self.assertEqual(node.to_html(), '<i>Italics me!</i>')






if __name__ == "__main__":
    unittest.main()
