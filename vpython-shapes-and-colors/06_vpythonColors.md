# VPython Colors

Like VPython coordinates, VPython colors are assignmed using vectors.

Instead of the vector values standing for `(x, y, z)` they stand for `(Red, Green, Blue)`.

Each one has a value between 0 and 1, so pure red woudl be `(1, 0, 0)` and pure blue is `(0, 0, 1)`

You can convert color values from 256 RGB color encoding (easily found online) as follows:

```
#colors encoded in 256 color RBG format
#(a format very commonly found online)
r256 =     0
g256 = 163
b256 = 108

#convert from 256 color scheme to 0-1
r1 = r256/255
g1 = g256/255
b1 = b256/255

t = pyramid() #draw pyramid
#color pyramid using converted colors
t.color = vector(r1, g1, b1)
```
