# Functions

## Arguments

- Positional arguments must come before keyword arguments otherwise a `SyntaxError` is raised
- Positional arguments must come before default arguments
- Never use mutable objects as a default argument since default arguments are evaluated once when the function is defined

### /

- Indicates that anything to the left must be passed by position and not by keyword

### \*

- Indicates that anything to the right must be passed by keyword

### Collecting Arguments

- `*args` (Positional Packing) - Collects any extra positional arguments into a tuple
- `**kwargs` (Keyword Arguments) - Collects any extra keyword arguments into a dictionary
- Use positional packing for iterables, use keyword unpacking for dictionaries

## Closures & Scope

- A function object that remembers values in its enclosing scope even if those values are no longer pressent in memory because the parent scope has finished executing

Example:

```py
def make_multiplier(x):
    # enclosing scope
    def multiplier(n):
        # function remembers x (read-only)
        return n * x
```

### `nonlocal` Keyword

- Use the `nonlocal` keyword to modify variables in the enclosing (but not global) scope of a closure
- `nonlocal` creeps up the scope tree and finds the first matching name

Example:

```py
def outer():
    x = "original"

    def inner():
        # makes x refer to variable outside rather than declaring anew
        nonlocal x
        x = "modified"
```

### `global` Keyword

- The `global` keyword lets you modify global variables
- If you use `global` for a variable that doesn't exist globally, the declaration will be propagated to the global scope

Example:

```py
x = 1

def modify():
    # makes x refer to variable outside rather than declaring a new
    global x
    x = 2
```
