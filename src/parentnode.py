from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        
        if self.children.value is None:
            raise ValueError("All children nodes must have a value")
        
        return f"ParentNode({self.tag}, children: {map(lambda child: to_html(child), self.children.value)})"