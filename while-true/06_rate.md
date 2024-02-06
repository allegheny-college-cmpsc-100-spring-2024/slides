# Rate

The `rate()` function in VPython tells Python how many frames per second your animation should run.

So:

```
rate(10) # 10 frames per second, a good default
rate(100) # 100 frames per second, may be too fast for comfort
rate(0.5) # half a famer per second, good for testing in slow mo
```
If you don't include a `rate()` function in your animation, in won't run properly, and might crash you browser. 