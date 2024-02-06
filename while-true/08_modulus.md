# Animations with Modulus

You can use a modulus to make the same animation run on a loop. Let's update the previous example:

```
b = box(pos = vector(-5, 0, 0))
while True:
    rate(10)
    b.pos.x = (b.pos.x + 0.1)%5
```