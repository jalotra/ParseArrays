
from .n_array_tree import NArrayTree

class ParseMatrices:
    # Data is a big chunk of matrix data.
    # Could be read from a text_file or some other source 
    # Note that the data should be parenthesis_matched. 
    # Balanced_Paranthesis : https://leetcode.com/problems/valid-parentheses/ 
    def __init__(self, data : str):
        self.data = data
        assert isinstance(self.data, str)
        self.types = 3
        self.open_parentheses = ['{', '[', '(']
        self.closed_parentheses = ['}', ']', ')']
    
    # Returns true if data has valid_parenthesis
    def is_balanced(self):  
        count = [0, 0, 0]
        for char in self.data:
            if char in self.open_parentheses:
                idx = self.open_parentheses.index(char)
                count[idx] += 1
            elif char in self.closed_parentheses:
                idx = self.closed_parentheses.index(char)
                count[idx] -= 1
                if count[idx] < 0:
                    return False
        
        for i in range(self.types):
            if count[i] != 0:
                return False
        return True
    
    def parse_matrix(self):
        if not self.is_balanced():
            raise Exception(f"Data {self.data} provided is not balanced.")
        elif len(self.data) == 0:
            return []

        root = NArrayTree([])
        levels = [root]
        current_level = 0

        for _, char in enumerate(self.data):
            if char in self.open_parentheses:
                current_level += 1
                levels.append(levels[current_level - 1].add_new_node([]))
            elif char in self.closed_parentheses:
                current_level -= 1
                levels.pop()
                if current_level == 0:
                    break
            else:
                if char not in [" ", '\n'] and current_level > 0:
                    levels[current_level].add_char(char)

        # Finally parse the tree 
        return root.parse_tree()[0]

if __name__ == "__main__":
    # data = "{name,{name,{jalotra, shivam, machine}}}"
    data = "{}"
    parse_matrix = ParseMatrices(data)
    from pprint import pprint
    pprint(parse_matrix.parse_matrix())