
# Module that defines a Tree where each node can have N nodes inside of it.

class  NArrayTree:
    def __init__(self, value):
        self.value = value
        self.children = []

    # Adds a new node and returns the last node
    def add_new_node(self, value = []):
        self.children.append(NArrayTree(value))
        return self.children[-1]
    
    def how_many_children(self):
        return len(self.children)

    def add_char(self, char : str):
        self.value.append(char)
    
    def get_value(self):
        return list(filter(lambda x : len(x) > 0, "".join(self.value).split(",")))

    # Parses tree starting at this node 
    # A assumption is that only leaf nodes will have values.
    def parse_tree(self):       
        res = []
        if len(self.value) > 0:
            for x in self.get_value():
                res.append(x)

        for child in self.children:
            res.append(child.parse_tree())
        return res

if __name__ == '__main__':
    tree = NArrayTree()
    tree_first_child = tree.add_new_node()
    tree_first_first_child = tree_first_child.add_new_node(list("shivam"))
    tree_first_second_child = tree_first_child.add_new_node(list("jalotra"))

    from pprint import pprint
    pprint(tree.parse_tree())