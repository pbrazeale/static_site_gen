import unittest

from blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestSplitblocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    # Test block_to_block_type
    def test_title_block_type(self):
        md = "# Title"
        blocks = markdown_to_blocks(md)
        block_type = block_to_block_type(blocks[0]) 
        self.assertEqual(block_type, BlockType.HEADING)

    def test_title_block_type(self):
        md = "> This is a quote"
        blocks = markdown_to_blocks(md)
        block_type = block_to_block_type(blocks[0]) 
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_title_block_type(self):
        md = "```print('hello')```"
        blocks = markdown_to_blocks(md)
        block_type = block_to_block_type(blocks[0]) 
        self.assertEqual(block_type, BlockType.CODE)

    def test_title_block_type(self):
        md = "- list item"
        blocks = markdown_to_blocks(md)
        block_type = block_to_block_type(blocks[0]) 
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_title_block_type(self):
        md = "1. list item"
        blocks = markdown_to_blocks(md)
        block_type = block_to_block_type(blocks[0]) 
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_text_block_type(self):
        md = "Just some text."
        blocks = markdown_to_blocks(md)
        block_type = block_to_block_type(blocks[0]) 
        self.assertEqual(block_type, BlockType.PARAGRAPH)
        