# Velocity

Velocity is a word for _speed_ that specifically denotes distance divided by time.

In VPython, it may be easiest to understand velocity in terms of units per second; however, in our animations, we need to adapt a per-second velocity to match up with our frame rate. ​We can write a function that does this.

```python
def frameVelocity(velocity, fps):
  return velocity/fps # return per-frame velocity
```

See an example of this function working [on Trinket](https://trinket.io/glowscript/c08641882c).
