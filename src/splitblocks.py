def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    blocks = []
    for line in lines:
        stripped_lines = [sentence.strip() for sentence in line.strip().splitlines()]
        stripped_block = "\n".join(stripped_lines)
    
        if stripped_block:
            blocks.append(stripped_block) 
    
    return blocks

