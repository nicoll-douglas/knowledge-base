# Control Flow

## Conditionals

### Match-Case

- Uses structural pattern matching
- The match variable can be a literal like `True` or `None` or `2`
- Compares with `is` for literals (`True`, `False`, `None`) and `==` for everything else
- If you use a variable in a case value, it is a capture pattern so it will assign the match value to the variable name and then use perform pattern matching on the case value
- Default case is represented by `case _`
- Can use the `|` operator to combine cases
- Doesn't support logical comparisons or operations
- Can use class matching with things like `int()`

Examples:

```python
match x:
  # matches an int, puts it in n, then checks > 5
  case int(n) if n > 5:
    print("x greater than 5")
  case n if n > 2: # matches > 2
    print("x greater than 2")
  case _:
    # _ = x here
    print("less than 2")

match [1, 2, 3]:
  # matches list with 3-items with first being 1
  case [1, y, z]:
    print(y) # 2
    print(z) # 2

match day:
  # matches sat or sun
  case "Saturday" | "Sunday":
    print("Weekend")
  case _:
    print("Weekday")
```

### Is

- The `is` keywords if two things point to the same object in memory
- `==` checks if values are the same
- The negation is `is not`

### In

- Checks if a value exists in an iterable
- For strings, it checks if it is a substring
- For dictionaries, it checks keys
- The negation is `not is`

## Loops

- You can use `else` blocks with loops
- The `else` block runs if the loop exited normally (it did not break)

Example:

```python
for n in [1, 2, 3]:
    if n == 5:
        break
else:
    print("5 was never found!") # This runs because the loop finished naturally.
```

## Exceptions

### Common Exceptions

| Name                | Description                                                                                                |
| ------------------- | ---------------------------------------------------------------------------------------------------------- |
| `AssertionError`    | Raised when an `assert` statement fails                                                                    |
| `AttributeError`    | Raised when an attribute reference or assignment fails                                                     |
| `EOFError`          | Raise when `input()` hits EOF without reading data                                                         |
| `IndexError`        | Raised when a sequence subscript is out of range                                                           |
| `KeyError`          | Raised when a mapping key is not found                                                                     |
| `KeyboardInterrupt` | Raised when the interrupt key is hit; inherits from `BaseException`                                        |
| `NameError`         | Raised when a local or global name is not found                                                            |
| `TypeError`         | Raised when an operation or function is applied to an object of inappropriate type                         |
| `ValueError`        | Raised when an operation or function receives an argument of the right type but has an inappropriate value |
| `SystemExit`        | Raised by `sys.exit()`; inerhits from `BaseException`                                                      |
| `RuntimeError`      | Raised when an error occurs that doesn't fall into any other categories                                    |
| `OSError`           | This exception is raised when a system function returns a system-related error                             |

### Try-Except-Finally

- Use `try-except` to catch errors
- Use a tuple of exceptions in `except` to catch multiple
- Use `except ... as ...` to have access to the exception object raised
- Use `raise ... from ...` to chain exceptions and raise an error when it is directly the consequence of another
- Use `finally` for cleanup actions

### Custom Exceptions

- Inherit from the `Exception` class
- Class name should end with "Error" (convention)
