from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, type, url=None):
        self.text = text
        self.text_type = type
        self.url = url
    
    def __eq__(self, node2):
        if (node1.text == node2.text and node1.text_type == node2.text_type and node1.url == node2.url):
            return True
        return False

    def __repr__(node):
        return f"TextNode({node.text!r}, {node.text_type}, {node.url!r})"

