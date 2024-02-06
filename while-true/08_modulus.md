# Animations with Modulus

You can use a modulus to make the same animation run on a loop. Let's update the previous example:

```
b = box(pos = vector(0, 0, 0))
while True:
    rate(10)
    b.pos.x = (b.pos.x + 0.2) % 3
```
[See it on Trinket here](https://trinket.io/glowscript/46cce4015f)