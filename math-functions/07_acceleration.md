# Acceleration

Acceleration is the change in velocity over time. It is defined in distance divided by time-squared (e.g. m/s\*\*2).

Let's say you wanted an object with a certain initial (or starting) velocity to come to zero within a certain time frame. You could write a function to calculate the necessary acceleration to make this happen:

```python
# create acceleration to zero function given initial velocity (in units per second)
# seconds to stop, and frame rate
def accelToZero(initial_velocity, seconds_to_zero, fps):
	acceleration = -initial_velocity/seconds_to_zero # calculate per s^2 accel
	acceleration /= fps # convert to per frame acceleration
	return acceleration # return acceleration

```

See this function in action \[on Trinket\](https://trinket.io/glowscript/c27ed58711).
