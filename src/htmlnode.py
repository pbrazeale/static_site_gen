class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        key, value = self.props.items()
        paths = []
        for i in range(len(key) - 1)
            path = f'{key[i]}="{value[i]}"'
            paths.append(path)
        return " ".join(paths)

    def __repr__(self):
        return f"{self.tag}\n{self.value}\n{self.children}\n{self.props}"
    
    
    