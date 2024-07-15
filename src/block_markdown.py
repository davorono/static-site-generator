import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    filtered_blocks = []
    for block in blocks:
        if block != "":
            filtered_blocks.append(block)
    return filtered_blocks

# We assume we are getting perfect blocks that have been previously split. We are just "disallowing" bad blocks and categorizing them as paragraph by default.
def block_to_block_type(block):
    if (re.match(r"#{1,6}.*?", block) != None):
        return block_type_heading
    elif (re.match(r"```.*?```", block) != None):
        return block_type_code
    elif (re.match(r">.*?", block) != None):
        return block_type_quote
    elif (len(re.findall(r"((\*|-)\s.*)", block)) == len(block.split("\n"))):
        return block_type_unordered_list
    
    # Something a little more complex for the ordered list needs to happen. Regex (at least to my knowledge) won't be able to support incrementing so im going to need a little for loop
    block_lines = block.split("\n")
    i = 1
    for line in block_lines:
        if (line[0:3] != f"{i}. "):
            return block_type_paragraph
        i += 1
    return block_type_ordered_list
    





