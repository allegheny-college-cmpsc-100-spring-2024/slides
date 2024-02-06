# while True

If you want your animation to run continously, you can use `while True:`, a condition which is always true. 

This is an exception to the no-infinity rule. It is okay to run an infinite loop in this case, because it will include a `rate()` function. This function causes Python to pause periodically as the program runs, so it doesn't get overwhelmed. 

Other time functions like `sleep()` can have the same effect. 