# This lesson will focus on Dynamic Typing and Pomodoro GUI
from tkinter import *
import time
# Canvas Widget
# The Canvas Widget let's us display various graphical elements in our window.

start = time.time()
print(f'Start Time: {start}')
# time.sleep(5)
end = time.time()
print(f'Elapsed Time: {end - start:.2f}')

dict_ = {00:00}
print(dict_.items())

print(divmod(25, 60))

# Strongly Typed Languages
# A strongly typed language enforces the rules of its types at runtime, so it refuses to silently
# mix incompatible types and raises an error instead of guessing what you meant (e.g. 1 + "2").

# Statically Typed Languages
# A statically typed language binds a type to every variable at compile time, so the compiler
# checks and rejects type errors before the program is ever run (e.g. Java, C, C++, Rust).

# Why Python is a Dynamically Typed Language
# Python attaches types to values rather than to variable names, and only resolves those types
# while the code is running, so the same variable can hold an int now and a string later and any
# type mistakes only surface as errors at runtime rather than being caught ahead of time.
