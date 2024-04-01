# Python Class Instances and Attributes

In Python, instances are individual objects created from a class. Each instance has its own set of attributes, which are variables associated with the instance. Attributes store data specific to each instance.

**Key Points:**
- Instances are created by calling the class as if it were a function.
- Each instance has its own namespace, allowing it to have unique attributes.
- Attributes are accessed using dot notation (`instance.attribute`).
- Attributes can be assigned values during object creation (in the constructor) or dynamically during the object's lifetime.

Example:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

print(car1.make)  # Output: Toyota
print(car2.model)  # Output: Accord
