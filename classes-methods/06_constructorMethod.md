# Python Class Constructor Method

The constructor method in Python classes, denoted by `__init__`, is called automatically when an instance of the class is created. It is used to initialize the attributes of the instance.

**Key Points:**
- The constructor method is used to set up the initial state of the object.
- It is defined using the `def __init__(self, ...)` syntax within the class definition.
- The constructor can accept arguments to initialize instance attributes.
- It is called implicitly when an instance of the class is created using the class name followed by parentheses.

Example:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")
