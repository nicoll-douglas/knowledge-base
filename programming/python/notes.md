# Python

- [Variables](#variables)
  - [Naming Rules](#naming-rules)
  - [Referencing](#referencing)
  - [Mutability](#mutability)
  - [Integer Caching](#integer-caching)
- [Data Types](#data-types)
  - [Numeric Types](#numeric-types)
    - [Integers (`int`)](#integers-int)
    - [Floats (`float`)](#floats-float)
    - [Complex Numbers (`complex`)](#complex-numbers-complex)
  - [Sequence Types](#sequence-types)
    - [Slicing](#slicing)
    - [Operators](#operators)
    - [Strings (`str`)](#strings-str)
      - [Escaping & Formatting](#escaping-formatting)
    - [Lists (`list`)](#lists-list)
      - [Packing & Unpacking](#packing-unpacking)
    - [Tuples (`tuple`)](#tuples-tuple)
      - [Packing & Unpacking](#packing-unpacking-1)
    - [Ranges (`range`)](#ranges-range)
    - [Bytes (`bytes`)](#bytes-bytes)
      - [Slicing](#slicing-1)
    - [Byte Array (`bytearray`)](#byte-array-bytearray)
  - [Mapping & Set Types](#mapping-set-types)
    - [Operators](#operators-1)
    - [Dictionaries (`dict`)](#dictionaries-dict)
    - [Sets (`set`)](#sets-set)
      - [Operators](#operators-2)
    - [Frozen Sets (`frozenset`)](#frozen-sets-frozenset)
      - [Operators](#operators-3)
  - [Unary Types](#unary-types)
    - [None (`NoneType`)](#none-nonetype)
    - [Booleans (`bool`)](#booleans-bool)
- [Built-ins](#built-ins)
  - [Functions](#functions)

## Variables

### General Rules

- Can contain numbers, letters and underscores
- Must start with a letter or underscore
- Convention for naming is lower case snake case
- Constants are usually uppercase
- Can be assigned in parallel (e.g `x, y, z = 1, 2, 3`)
- See [PEP 8](https://peps.python.org/pep-0008/) for more

### Referencing

- Contents of variables are basically all just objects
- The variable name is simply just a label that points to that object
- When you assign one variable to another, they will point to the same object (two labels for the same object)

Example:

```python
a = 5     # 'a' points to an int object 5
b = a     # 'b' points to the same object as 'a'
a = a + 1 # 'a' now labels a new int object that was created; 'b' still points to the old object
```

### Mutability

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

### Integer Caching

- When Python starts up, it pre-alloactes a range of small integers in memory (known as integer caching)
- The range is typically -5 to 256
- Every time you create an integer object with a value in this range, it will point to that already existing object

## Data Types

- Use `type()` built-in to check the data type

### Numeric Types

#### Integers (`int`)

- Can use underscores as visual separators (e.g `1_000_000`)
- Base 10 isn't required, can use binary, octal and hex literals (e.g `0b1011`, `0o10`, `0xff` or `0xFF`)
- `int`s have no upper or lower bound or fixed size so can grow to occupy as much RAM as the host system can provide

#### Floats (`float`)

- Can also use underscores for visual separation
- Uses the IEEE 754 floating-point standard
- Not restricted to standard decimal notation, can use scientific notation (e.g `1.496e8` which is 149,600,000)

Special values:

```python
float('inf') # represents infinity, greater than all other numbers
float('-inf') # represents negative infinity, smaller than all other numbers
float('nan') # not a number, used for undefined results such as 0.0 / 0.0; nan is never equal to itself
```

#### Complex Numbers (`complex`)

- Complex numbers e.g `5 + 2j`

### Sequence Types

#### Slicing

- Sequences can be sliced with the `[start:stop:step]` syntax
- If you leave a section blank, it uses the default values (start=0, stop=len(list), step=1)
- The start value is inclusive, the stop value is exclusive
- The only invalid value for the step value is 0
- The step value allows you to skip elements (1 gives you every element, 2 takes one skips 1, 3 takes 1 skips 2 etc)
- When the step is negative, the start defaults to the end and the stop defaults to the beginning
- When a slice is read, generally speaking a new object is created

List Examples:

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums[0:2]     # [0, 1], includes 0 and up to but not including 2
nums[0:5:2]   # [0, 2, 4] # take 0, skip 1, take 2, skip 3, take 4
nums[::-1]    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], start at 9, take 1 backwards until but not including -1
nums[8:2:-2]  # [8, 6, 4], start at 8, take 8, skip 7, take 6, skip 5, take 4, skip 3
```

- Some sequence types are read-only (which makes sense as they are also immutable types):
  - `str`
  - `tuple`
  - `range`
  - `bytes`
- Lists and byte arrays allow slice assignment
- Slice assignment allows you to delete or replace chunks of data in-place

#### Operators

- Sequence types share some common operators
- Addition (`+`) concatenates two sequences into one and returns a new sequence
- Multiplication (`*`) repeats the sequence, creating a new one of the tuple N times (e.g `(0, 2) * 2 == (0, 2, 0, 2)`)
- With multiplication for lists and tuples, the references inside them are replicated

#### Strings (`str`)

- Unicode text (a sequence of bytes under the hood)
- Can wrap strings using single quotes, double quotes or triple quotes (`'''` or `"""`) which is used for multi-line strings and preserving line breaks exactly as typed

##### Escaping & Formatting

- Backslash is an escape character
- Using the `r` prefix lets you create a raw string where backslashes are just backslashes (e.g `r"C:\Users\jiggy"`)
- Using the `f` prefix (f-string) lets you inline variables and python code inside curly braces
- Using the `b` prefix changes the data type of the string to `bytes`
- Each character is restricted to a single byte (ASCII)
- You can combine some of the prefixes (e.g fr/rf and rb/br, fb is not allowed)

#### Lists (`list`)

- Mutable, ordered collection of heterogeneous items
- Wrapped in square brackets (e.g `[1, 2, 3]`)

##### Packing & Unpacking

- Can extract values from a list into variables (unpacking)
- The \* star operator unpacks the rest of the items into a new list

Examples:

```python
x, y = [10, 20]
# x = 10
# y = 20
first, *middle, last = [1, 2, 3, 4]
# first = 1
# middle = [2, 3]
# last = 4
```

#### Tuples (`tuple`)

- An immutable, ordered collection of items (basically just an immutable list)
- Wrapped in round brackets (e.g `(1, 2, 3)`)

Examples:

```python
a = (1, 2, 3)
b = (5,)       # trailing comma lets you create a tuple of length 1 and avoids the "forced evaluation" property of round brackets
c = (1, 2, 3,) # this is also valid
```

##### Packing & Unpacking

- You can unpack tuples the same way you can with lists

Examples:

```python
a = 1
b = 2
a, b = (b, a) # swaps a and b
a, b = b, a # does the same
```

#### Ranges (`range`)

- An immutable sequence of numbers usually used for looping; stores only the start stop and step values

#### Bytes (`bytes`)

- An immutable sequence of bytes which is just a sequence of numbers from 0 to 255
- Created by prefixing an ASCII string with the `b` prefix (e.g `b"Hello world"`)

##### Slicing

- Slicing returns a new `bytes` object which is the default slicing behaviour
- Indexing returns an `int` which is the ASCII code of the character that was accessed (not the expected default behaviour)

#### Byte Array (`bytearray`)

- Must be created with the `bytearray()` built-in
- Behaves the same as `bytes` except the fact that it is mutable

### Mapping & Set Types

#### Operators

- Mapping and set types share some common operators
- The pipe (`|`) operator updates items of the first operand with the keys of the second operand and returns a new object
- If using augmented assignment with the pipe operator (`|=`) the object is updated in place otherwise if the type of the object is mutable (i.e `set`, `dict`) otherwise a new object is created (i.e `frozenset`)

#### Dictionaries (`dict`)

- Mutable, ordered (by insertion) key-value pairs
- Keys must be hashable (immutable types like strings, numbers or tuples)
- Values can be anything

#### Sets (`set`)

- Mutable, unordered collection of unique items; wrapped in curly brackets (e.g `{1, 2, 3}`)
- Sets use hashing to stay fast so only immutable items are allowed inside sets
- Empty curly brackets (`{}`) create an emtpy dictionary; the `set()` built-in must be used to create an empty set

##### Operators

- `a & b` - Returns the intersection of `a` and `b`
- `a - b` - Returns the set difference between `a` and `b`
- `a ^ b` - Returns the set of items in `a` or `b` but not `both`
- `a | b` - Returns the union of `a` and `b`

#### Frozen Sets (`frozenset`)

- Immutable version of a set
- Must be constructed using the `frozenset()` built-in

##### Operators

- Supports the same operators as sets

### Unary Types

#### None (`NoneType`)

- `None` is a special type representing the absence of a value
- `None` is a singleton so only one instance exists and all references point to it

#### Booleans (`bool`)

- Either `True` or `False`
- Secretly an integer under the hood (something like `True + True` gives `2`, `isinstance(True, int)` gives `True`, etc)

## Built-ins

### Functions
