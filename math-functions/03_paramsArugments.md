# Parameters vs. Arguments

In Python, parameters and arguments are often used interchangeably, but they have distinct meanings:

- **Parameters**: These are variables declared in the function definition. They represent the inputs that the function expects.

- **Arguments**: These are the actual values passed to the function when it is called. They correspond to the parameters defined in the function.

Example:

```python
def greet(name): # here, name is a parameter
    return f"Hello, {name}!"

print(greet("Alice")) # Alice is an argument
```
