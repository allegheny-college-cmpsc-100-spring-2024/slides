# Python Class Methods

In addition to the constructor method (`__init__`), Python classes can have other methods to perform various tasks or operations on class instances.

**Key Points:**
- Methods are functions defined within a class.
- They operate on the attributes of class instances and can perform specific actions or computations.
- Methods are defined using the `def` keyword within the class definition.
- They typically accept `self` as the first parameter to reference the instance on which the method is called.

Example:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Usage:
circle = Circle(5)
print("Area:", circle.area())  # Output: 78.5
print("Perimeter:", circle.perimeter())  # Output: 31.4
