# Variables Review

When you call a variable's name, Python substitutes the variable for the value it holds.

THIS CODE

```
name = "Ron Cole"
print("Hi " + name + "!")
print("Bye " + name + "!")

```

produces the same reults as 

```
print("Hi Ron Cole!")
print("Bye Ron Cole!")
```

EXCEPT THAT in the first version, you can change the name in the first line and it will affect the next two lines, whereas with the second, if you wanted to change the name, you would have to do it twice.

This might not seem like a big deal when you only have to change two lines of code, but it's a much bigger deal if you have to change 1000...

See [this demo](https://trinket.io/python/8d6dd97818), and imagine what it would be like if you had to change every line each time you adapted your code to address is new person.
