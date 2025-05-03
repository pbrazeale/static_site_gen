from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif re.match(r"^#{1,6} (.*?)", block):
        return BlockType.HEADING
    elif re.match(r"^>(.*?)", block):
        return BlockType.QUOTE
    elif re.match(r"^- (.*?)", block):
        return BlockType.UNORDERED_LIST
    elif re.match(r"^\d+\.", block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    blocks = []
    for line in lines:
        stripped_lines = [sentence.strip() for sentence in line.strip().splitlines()]
        stripped_block = "\n".join(stripped_lines)
    
        if stripped_block:
            blocks.append(stripped_block) 
    
    return blocks
