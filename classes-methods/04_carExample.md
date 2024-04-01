# Car Example

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print("Car: " + self.year + " " + self.make + " " + self.model)
```
## Explanation
This code defines a class named Car. It has a constructor method __init__() that initializes the make, model, and year attributes of the car object. The display_info() method prints information about the car's make, model, and year when called.

[See it on Trinket](https://trinket.io/python/2b0b73f09e)