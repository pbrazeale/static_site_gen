from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        
        if self.children is None or not self.children:
            raise ValueError("All children nodes must have a value")
        
        children_html = "".join([child.to_html() for child in self.children])

        if self.props is None:
            open_tag = self.tag
        else:
            open_tag = f'{self.tag}{self.props_to_html()}'

        return f"<{open_tag}>{children_html}</{self.tag}>"