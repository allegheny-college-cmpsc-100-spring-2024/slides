# Python Dictionaries

Dictionaries in Python are unordered collections of key-value pairs. They are mutable and versatile data structures, allowing for efficient lookup, insertion, and deletion operations. Keys must be unique and immutable, while values can be of any data type.

Example:
```python
# Creating a dictionary
my_dict = {'apple': 5, 'banana': 7, 'orange': 3}

# Accessing values
print(my_dict['banana'])  # Output: 7

# Modifying values
my_dict['apple'] = 8

# Adding new key-value pairs
my_dict['grape'] = 4

# Removing a key-value pair
del my_dict['orange']

# Iterating over keys
for key in my_dict:
    print(key, my_dict[key])
```