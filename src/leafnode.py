from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        super().__init__(tag, value, children=None)
        
        def to_html(self):
            if self.value == None:
                raise ValueError("All leaf nodes must have a value")
            if self.tag == None:
                html_string = self.value
            
            if self.props != None:
                open_tag = f'{self.tag}{props_to_html(self.props)}'
            else:
                open_tag = self.tag
            
            html_string = f'"<{tag}>{self.value}</{self.tag}>"'
            
            return html_string

