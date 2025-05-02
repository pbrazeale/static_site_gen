import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    pattern = re.escape(delimiter) + r"(.*?)" + re.escape(delimiter)

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)

        matches = re.split(pattern, node.text)

        if len(matches) == 1:
            raise Exception(f'"{delimiter}" missing at the beginning or end of the selection.')

        for i, match in enumerate(matches):
            if i % 2 == 0:
                new_nodes.append(TextNode(match, TextType.TEXT))
            else:
                new_nodes.append(TextNode(match, text_type))
    
    return new_nodes


def extract_markdown_images(text):
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_pattern, text)

    return matches

def extract_markdown_links(text):
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.split(link_pattern, text)
    
    return matches