import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_to_html_with_bold_sentence(self):
        child_node = LeafNode("b", "child")
        parent_node = ParentNode("p",[ 
            LeafNode(None, "This is a nested "),
            child_node,
            LeafNode(None, " in a paragraph.")
        ])
        self.assertEqual(
            parent_node.to_html(),
            "<p>This is a nested <b>child</b> in a paragraph.</p>"
        )



if __name__ == "__main__":
    unittest.main()
