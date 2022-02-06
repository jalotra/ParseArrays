# ParseArrays
This code is along-with a blog post which lists a possible way to parse random( N dimensional) arrays. 

#  Motivation : 
Recently at work, I was working on this problem which incuded parsing a nested array type structure. 

```
Example : 
.data = {
    {
        name1,
        {
            phone_number_1, 
            address_1,
            roll_number_1
        }
    },
    {
        name2,
        {
            phone_number_2, 
            address_2,
            roll_number_2
        }
    }    
}
```

The crux of the problem is to parse this `.data` into a `list([])` which can be indexed, modified, appended to later.

# Possible Approaches
* For illustration purposes, lets take `.data = "{name,{name,{jalotra, shivam, machine}}}"` 

- First one that came to mind is to use `ast.literal_eval()` that ast module gives out of the bat.
    - Just as it is .data will give [errors](https://stackoverflow.com/questions/10113270/python-string-list-to-list-ast-listeral-eval) but if we change values to string types, it would work. 

# My Solution 
- I have been leetcoding for sometime now, so I wanted to see if I could be able to come up with some algorithm to solve this problem on my own (read without looking how ast.literal_eval) works.

- Algorithm : 
    - We start with a root node.
    - And for every open_parentheses a new node in this tree rooted at Root is created.
    - Now the structure that you describe for this node can be used recursively. I call this structure `NArrayTree` 
    - And you can keep on adding the current value (string) this `NArrayTree` node can hold, like if the example was `{
        jalotra, 
        {
            ... something here 
        }
    }` first you encounter a opening bracket `{` and you will create a new Node `NArrayTree([])` and till `jalotra,` you will append `chars` to this node. 
    - Finally, your original node will look like `NArrayTree(['j', 'a', 'l', 'o', 't', 'r', 'a'])` and then once more you encounter a `{` do same for child node recursively.

    - After making this tree, you are left will parsing this tree, which is a trivial algo that uses `dfs or give me the answer for children`.
        ```
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
        ```

# Examples : 
1. 
    - `data = "{name}" ` 
    - `result = ["name"]`

<br/>

2. 
    - `data = "{name, section}"`
    -  `result = ["name", "section"]`

<br/>

3. 
   - `data = "{name, {section}}"`
   - `result = ["name", ["section"]]`

<br/>

4. 
    - `data = "{name, {section, gender, {medadata, {XII, India}}}}"`
    - `result = ['name', ['section', 'gender', ['medadata', ['XII', 'India']]]]`

<br/>

5. - `data(Original Problem)  = {
    {
        name1,
        {
            phone_number_1, 
            address_1,
            roll_number_1
        }
    },
    {
        name2,
        {
            phone_number_2, 
            address_2,
            roll_number_2
        }
    }    
}`'
    - `result = [['name1', ['phone_number_1', 'address_1', 'roll_number_1']],
 ['name2', ['phone_number_2', 'address_2', 'roll_number_2']]]
`