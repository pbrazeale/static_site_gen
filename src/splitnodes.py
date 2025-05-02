import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    pattern = re.escape(delimiter) + r"(.*?)" + re.escape(delimiter)

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)

        splits = re.split(pattern, node.text)

        for i, split in enumerate(splits):
            if i % 2 == 0:
                new_nodes.append(TextNode(split), TextType.TEXT)
            new_nodes.append(TextNode(split), text_type)
    
    return new_nodes