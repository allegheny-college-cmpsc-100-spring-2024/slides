# Classes & Methods, Welcome Activity

Below is the beginning of the `sphere()` class as it's written in the [VPython library source code](https://github.com/vpython/vpython-jupyter/blob/master/vpython/vpython.py). This code block includes the **class definition** and **constructor method**: 

```python
class sphere(standardAttributes):
    def __init__(self, **args):
        args['_default_size'] = vector(2,2,2)
        args['_objName'] = "sphere"
        super(sphere, self).setup(args)
        self._sizing = False # no axis/size connection
```

> [!NOTE]
> Some syntax above are advanced and we will learn a slightly simpler verison in the coming lesson. 

In today's Discord thread, see if you can guess the answers to any of the following questions: 

- What is the default size of a sphere? 
- Which piece of code includes the class definition? How does Python know a class's name and arguments?
- Which piece of code defines the classes constructor method? What do you think a constructor method does? 
