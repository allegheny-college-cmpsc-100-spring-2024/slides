# If Statemenet in VPython

<img src = "image.png" width = "450px" />

```
# i is equal to 0 then 1 then 2.... then 8
for i in range(9):
  x = i * 2 - 8 # x pos var as function of i
  # draw ring and position with x
  r = ring(pos = vector(x, 0, 0)) 
  if i > 5: # if i > 5, color ring yellow
    r.color = vector(1, 1, 0)
```

[Click here](https://trinket.io/glowscript/02a8eee925) for Trinket. 

[-> If Else VPython](/conditionals/04_ifElseVPython.md)