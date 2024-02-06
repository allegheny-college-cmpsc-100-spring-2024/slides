# VPython Animations with While Loops

Another way to use while-loops is to create animations in VPython.

```
b = box(pos = vector(-5, 0, 0))
while b.pos.x < 5:
    rate(10)
    b.pos.x += 0.1
```

This code moves box b 0.1 units to the right every 1/10 of a second until it gets to position 5. [See it on Trinket.](https://trinket.io/glowscript/f7d68bb49b)

[-> Rate](/while-true/06_rate.md)