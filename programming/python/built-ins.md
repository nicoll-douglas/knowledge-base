# Built-ins

## Most Used

### abs

_**abs(number: int | float | complex | Any) -> int | float | complex | Any**_

- Returns the absolute value of a number
- Can also be implemented for a custom class using the `__abs__` method

```python
abs(-10)    # Result: 10, int
abs(5)      # Result: 5, int
abs(-3.14)  # Result: 3.14, float
```

### all

_**all(iterable: Iterable[object]) -> bool**_

- Returns `True` if all elements of the given iterable are truthy otherwise `False`

```python
# equivalent function
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

# examples
all([True, 2 > 0]) # True
all([]) # True
```

### any

_**any(iterable: Iterable[object]) -> bool**_

- Returns`True` if at least 1 element in the iterable is truthy otherwise `False`

```python
# equivalent function
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

# examples
any([True, 0 < 2, False]) # True
any([]) # False, must be at least 1
any([False]) # False
```

### ascii

_**ascii(obj: object) -> str**_

- Converts an object to an ASCII string representation whilst escaping non-ASCII characters

```python
# examples
ascii("Héllo") # Result: "H\xe9llo", second character (8-bit non-ASCII) escaped
ascii("π") # Result: "\u03c0", 16-bit unicode escaped
ascii("🐍") # Result: "\U0001f40d", 32-bit unicode character escaped
```

### bin

_**bin(number: int | SupportsIndex) -> str**_

- Convert an integer to a binary string representation (sign-magnitude)
- Can also be implemented for a custom class using the `__index__` method which tells Python that the class can be treated like an integer

```python
# examples
bin(10) # Result: "0b1010"
bin(-10) # Result: "-0b1010"
```

### bool

_**class bool(object: object = False)**_

- Create a boolean from the given value
- Is a subclass of `int` and the only instances are singletons `True` and `False`

### bytearray

_**class bytearray(source: Iterable[int] | int = b"")**_<br>
_**class bytearray(source: str, encoding: str, errors: str = "strict")**_

- Create an array of bytes
- `source` parameter:
  - If empty, an empty `bytearray` will be initialises
  - If is an `int`, an `bytearray` will be initialised with that many null bytes
  - If is an `Iterable` (including bytes) it must be an iterable of integers ranging from 0 to 255
  - If is a string, the encoding must be provided
- `errors` parameter:
  - If `"strict"`, raises a `UnicodeEncodeError` for any invalid characters
  - If `"ignore"`, drops the unencodable character
  - If `"replace"`, replaces the character with a `?` or `\ufffd` (�, replacement character)

### bytes

_**class bytes(source: Iterable[int] | int = b"")**_<br>
_**class bytes(source: str, encoding: str, errors: str = "strict")**_

- Constructor behaviour is the same as that for `bytearray`

### callable

_**callable(obj: object) -> bool**_

- Returns `True` if the given argument is callable or `False` otherwise
- Returns `True` if the given object implements the `__call__` method

### chr

_**chr(i: int | SupportsIndex) -> str**_

- Returns the character associated with the given unicode codepoint (codepoint as an integer)
- Thus the valid range is 0 to 1,114,111
- A `ValueError` is raised outside that range
- If an object implements `__index__` it may also be passed

### delattr

_**delattr(obj: object, name: str) -> None**_

- Deletes an attribute from the specified object
- The `name` parameter must be an attribute that exists on the object
- Is equivalent to `del object.name`

### dict

_**class dict(\*\*kwargs)**_<br>
_**class dict(Iterable[object] | Mapping, \*\*kwargs)**_

- Creates a new dictionary
- First argument:
  - If is an iterable, each item in the iterable is set inside the dictionary as key-value pairs (`for k, v in iterable`)
  - If is a `Mapping` then each item is set inside the dictionary as key-value pairs (mapping must implement `__getitem__`, `__iter__` and `__len__`)
- Keyword arguments:
  - All keyword arguments are set inside the new dictionary as key-value pairs (argument name, argument value)

### dir

_**dir() -> list[str]**_<br>
_**dir(o: object) -> list[str]**_

- If no argument is given, returns the list of names in the current local scope
- `o` argument:
  - Attempts to return a list of valid attributes for that object
  - If the object has a method named `__dir__` this method will be called and must return a list of attributes (allows objects that implement a `__getattr__` to customise `dir` behaviour)
  - If the object is a module object, the list contains the names of the modules attributes
  - If the object is a type or class, the list contains the names of its attributes and attributes of parent classes
  - Otherwise, the list contains the object's attributes' names, the names of its class's attributes and attributes of its parent classes
- The resulting list is sorted alphabetically

### divmod

_**divmod(a: int , b: int) -> tuple[int, int]**_<br>
_**divmod(a: float , b: int) -> tuple[float, float]**_<br>
_**divmod(a: int , b: float) -> tuple[float, float]**_<br>
_**divmod(a: float , b: float) -> tuple[float, float]**_

- Returns a tuple containing the quotient and remainder as a result of dividing the two given numbers
- Is more efficient thatn using `//` and `%` separately because division logic is only performed once

### enumerate

_**enumerate(iterable: Iterable, start: int = 0) -> Iterator[tuple[int, T]]**_

- Returns an enumerate object
- The `__next__` method of the iterator returned by the `enumerate()` returns a tuple containing the index (`int`) and the value obtained from iterating over the iterable (iterable of item type `T`)
- `start` argument:
  - Changes the starting index (defaults to 0)

Example:

```python
# 2: a
# 3: b
# 4: c
for index, item in enumerate(["a", "b", "c"], start=2):
  print(f"{index}: {item}")
```

### filter

_**filter(function: Callable[[T], bool], iterable: Iterable[T]) -> Iterator[T]**_

- Returns an iterator that constructs elements from the given iterable such that when calling the given function with the element it returns `True`

### float

_**class float(float | int | string = 0.0)**_<br>

- Construct a float from the given number or string
- First argument:
  - If a string, should look like a number
  - If none given, return value defaults to `0.0`

Examples:

```python
float("+1.23") # 1.23
float("   -12345\n") # -12345.0
float("1e-003") # 0.001
float("+1E6") # 1000000.0
float("-Infinity") # -inf
float("nan") # nan
```

### format

## Others

- `breakpoint`
- `compile`
- `complex`
- `eval`
- `exec`
