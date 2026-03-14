# Variables

## General Rules

- Can contain numbers, letters and underscores
- Must start with a letter or underscore
- Convention for naming is lower case snake case
- Constants are usually uppercase
- Can be assigned in parallel (e.g `x, y, z = 1, 2, 3`)
- See [PEP 8](https://peps.python.org/pep-0008/) for more

## Referencing

- Contents of variables are basically all just objects
- The variable name is simply just a label that points to that object
- When you assign one variable to another, they will point to the same object (two labels for the same object)

Example:

```python
a = 5     # 'a' points to an int object 5
b = a     # 'b' points to the same object as 'a'
a = a + 1 # 'a' now labels a new int object that was created; 'b' still points to the old object
```

## Mutability

- Some variable types are immutable (integers, floats, strings, tuples)
- For immutable types, the underlying object of the variable cannot be changed only replaced with a new object
- The immutable types are:
  - `int`
  - `float`
  - `str`
  - `NoneType`
  - `tuple`
  - `frozenset`
  - `bool`
  - `bytes`
- All other types (`list`, `dict`, etc) are mutable

## Integer Caching

- When Python starts up, it pre-alloactes a range of small integers in memory (known as integer caching)
- The range is typically -5 to 256
- Every time you create an integer object with a value in this range, it will point to that already existing object
