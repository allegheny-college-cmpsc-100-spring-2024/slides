# Indentation in Python

 **Indentation** tells Python where a block of code begins and ends. So extending last slide's example...

 ```python

count = 0 # set count
while count < 5:
    # anything at this indendation level
    # executes inside the while loop
    print(count) 
    count += 1
# once we indent back out, any code that follows is not in the loop
count = 0 # reset count
```

[-> Fear Infinity](/while-loops/05_fearInfinity.md)