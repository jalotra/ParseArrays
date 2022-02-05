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
    **Too Lazy to write this now.**