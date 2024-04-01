# The `self` Parameter in Python Classes and Methods

In Python classes and methods, `self` refers to the instance of the class itself. It is the first parameter of instance methods and is used to access and manipulate the attributes and methods of the object.

**Key Points:**
- `self` is not a reserved keyword, but it is a convention to use it as the first parameter in instance methods.
- It allows methods to access and modify the attributes of the instance to which they belong.
- When calling methods of an instance, Python automatically passes the instance itself as the first argument (i.e., `self`).

Example:

```python
class MyClass:
    def __init__(self, x):
        self.x = x

    def print_x(self):
        print(self.x)

obj = MyClass(5)
obj.print_x()  # Output: 5
