# Accessing Values in Python Dictionaries 

Dictionaries in Python provide efficient ways to access values using keys. You can access a value by naming the dictionary and immediatly following, naming the key between two hard brackets:

`dict[key]`

For example: 
```python
my_dict = {'name': 'Alice', 'age': 25, 'city': 'London'}

# Accessing a value using key
name = my_dict['name'] 
print(name)  # Output: Alice
print(my_dict['city']) # Output: London 
```