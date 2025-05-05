import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) %2 == 0:
            raise ValueError("invalid markdown, formatted secltion not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

    # pattern = re.escape(delimiter) + r"(.*?)" + re.escape(delimiter)

    # for node in old_nodes:
    #     if node.text_type != TextType.TEXT:
    #         new_nodes.append(node)
    #         continue

    #     matches = re.split(pattern, node.text)

    #     if len(matches) == 1:
    #         raise Exception(f'"{delimiter}" missing at the beginning or end of the selection.')

    #     for i, match in enumerate(matches):
    #         if match == "":
    #             continue
    #         if i % 2 == 0:
    #             new_nodes.append(TextNode(match, TextType.TEXT))
    #         else:
    #             new_nodes.append(TextNode(match, text_type))
    
    # return new_nodes


def extract_markdown_images(text):
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_pattern, text)
    return matches


def extract_markdown_links(text):
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(link_pattern, text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        
        if not images:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            parts = remaining_text.split(image_markdown, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
            
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
     
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
    # new_nodes = []
    # for node in old_nodes:
    #     if node.text_type != TextType.TEXT:
    #         new_nodes.append(node)
    #         continue
    #     links = extract_markdown_links(node.text)
    #     if len(links) == 0:
    #         new_nodes.append(node)
    #         continue

    #     remaining_text = node.text
    #     for display_text, url in links:
    #         link_markdown = f"[{display_text}]({url})"
    #         parts = remaining_text.split(link_markdown, 1)

    #         if parts[0]:
    #             new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
    #         new_nodes.append(TextNode(display_text, TextType.LINK, url))

    #         if len(parts) > 1:
    #             remaining_text = parts[1]
    #         else:
    #             remaining_text = ""
            
    #     if remaining_text:
    #         new_nodes.append(TextNode(remaining_text, TextType.TEXT))
     
    # return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
    # return split_nodes_delimiter(
    #     split_nodes_delimiter(
    #         split_nodes_delimiter(
    #             split_nodes_link(
    #                 split_nodes_image(text)
    #             ), "**", TextType.BOLD
    #         ), "_", TextType.ITALIC
    #     ), "`", TextType.CODE
    # )
