from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
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
        return (self.text == node2.text and self.text_type == node2.text_type and self.url == node2.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("not a valid Text Type")
    elif text_node.text_type is TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type is TextType.BOLD:
        return LeafNode("b", text_node.text)    
    elif text_node.text_type is TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type is TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type is TextType.LINK:
        return LeafNode("a", text_node.text, props={"herf": text_node.url})
    elif text_node.text_type is TextType.IMAGE:
        return LeafNode("img", value="", props={"src": text_node.url, "alt": text_node.text} )

    