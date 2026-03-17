# C Notes

## Types, Operators, Expressions

### Variable Names

- Letters, digits, underscores
- First character must be a letter or underscore (avoid)

### Data Types and Sizes

| Type                  | Size          | Description                                               |
| --------------------- | ------------- | --------------------------------------------------------- |
| `char`                | 1 byte        | Holds one character in the local character set            |
| `int`                 | 4 bytes       | Reflects the natural size of integers on the host machine |
| `float`               | 4 bytes       | Single-precision floating point                           |
| `double`              | 8 bytes       | Double-precision floating point                           |
| `short` / `short int` | 2 bytes       | Smaller integer                                           |
| `long` / `long int`   | 4 / 8 bytes   | Bigger integer                                            |
| `long double`         | 10 / 16 bytes | Extended precision floating-point                         |

- The `signed` and `unsigned` qualifers may be applied to `char` or any integer
- Unsigned numbers are positive or 0
- Unsigned numbers obey the laws of arithmetic modulo 2<sup>n</sup> where n is the number of bits in the type
- `int`, `short` and `long` are all signed by default
- `char` can be unsigned or signed by default (not mandated in C standard) but usually signed

### Constants

#### Integer Constants

##### Suffixes

| Constant Suffix                        | Type                                        | Examples          |
| -------------------------------------- | ------------------------------------------- | ----------------- |
| None, only numbers                     | `int` (`long` if too big)                   | `1234`            |
| `l` or `L`                             | `long`                                      | `1234L`           |
| `u` or `U`                             | `unsigned int` (`unsigned long` if too big) | `1234U`           |
| `ul` or `UL`                           | `unsigned long`                             | `1234UL`          |
| None, with decimal or scientific       | `double`                                    | `1.234`, `1e-5`   |
| `f` or `F`                             | `float`                                     | `1.234F`          |
| `l` or `L`, with decimal or scientific | `long double`                               | `1.234L`, `1e-5L` |

##### Octal and Hex

- An integer constant can be expressed in octal or hex
- A leading `0` means octal
- A leading `0x` or `0X` means hex
- Octal and hex constants may also be followed by `L` to make them `long` and `U` to make them unsigned (e.g `0XFUL` = unsigned long 15)

#### Character Constants

- A character constant is an integer written as one character with single quotes and is equal to the numeric value in the machine's character set
- Character constants can also participate in numeric operations like other integer types

##### Escape Sequences

Characters can be represented by escape sequences as below:

| Sequence | Meaning                                | ASCII Code |
| -------- | -------------------------------------- | ---------- |
| `\0`     | Null character                         | 0          |
| `\a`     | Alert (bell) character                 | 7          |
| `\b`     | Backspace                              | 8          |
| `\f`     | Form Feed                              | 12         |
| `\n`     | Line Feed (newline)                    | 10         |
| `\r`     | Carriage return                        | 13         |
| `\t`     | Horizontal tab                         | 9          |
| `\v`     | Vertical tab                           | 11         |
| `\\`     | Backslash                              | 92         |
| `\?`     | Question mark                          | 63         |
| `\'`     | Single quote                           | 39         |
| `\"`     | Double quote                           | 34         |
| `\ooo`   | Octal representation (o = octal digit) |            |
| `\xhh`   | Hex representation (h = hex digit)     |            |

#### Constant Expressions

- Constant expressions are expressions that involve only constants
- Such expressions are evaluated at compile-time

Example:

```c
#define LEAP 1;

int days[31+28+LEAP+31+30+31+30+31+31+30+31+30+31];
```

#### String Constants (String Literal)

- A sequence of 0 or more characters surrounded by double quotes
- The escape sequences used in characters apply in strings
- String constants can be concatenated at compile-time (e.g `"hello, world"` = `"hello, " "world"`)
- Internally, a string constant is an array of characters with an extra null character at the end

#### Enumeration Constant

- An enum is a list of constant integer values
- Names in enums must be distinct
- Values in enums don't need to be distinct
- If values are left unassigned, they increase in order from the leftmost assigned value (the first will be 0 if unasssigned)

Examples:

```c
enum boolean { NO, YES }; // NO=0, YES=1
enum letters { A = 10, B, C }; // A=10, B=11, C=12
enum letters2 { A, B = 50, C } // A=0, B=50, C=51
```

### Declarations

- All variable declarations must be at the top of a code block and declared before use
- A declaration contains a list of one or more variables of that type
- Automatic variables are local variables that are automatically allocated when the program enters the code block they are defined in
- If a variable is not automatic, its initialization is done only once (before the program starts executing)
- Otherwise, it is initialised each time its code block is entered
- External and static variables are initialised to 0 by default
- Automatic variables with no initializer are undefined (garbage bits leftover in memory)
- The `const` qualifier can be applied to a variable declaration to specify its value will not be changed (for arrays the element will not be altered)
- `const` can also be used with arguments to indicate that the function will not change, or reassign the local copy, of the value passed

### Operators

#### Precedence Table

| Rank | Category       | Operators                                                          | Evaluation/Association |
| ---- | -------------- | ------------------------------------------------------------------ | ---------------------- |
| 1    | Postfix        | `++`, `--`, `()`, `[]`, `->`, `.`                                  | LTR                    |
| 2    | Prefix         | `+`, `-`, `++`, `--`, `!`, `~`                                     | RTL                    |
| 3    | Multiplicative | `*`, `/`, `%`                                                      | LTR                    |
| 4    | Additive       | `+`, `-`                                                           | LTR                    |
| 5    | Bit Shift      | `<<`, `>>`                                                         | LTR                    |
| 6    | Relational     | `<`, `<=`, `>`, `>=`                                               | LTR                    |
| 7    | Equality       | `==`, `!=`                                                         | LTR                    |
| 8    | Bitwise AND    | `&`                                                                | LTR                    |
| 9    | Bitwise XOR    | `^`                                                                | LTR                    |
| 10   | Bitwise OR     | `\|`                                                               | LTR                    |
| 11   | Logical AND    | `&&`                                                               | LTR                    |
| 12   | Logical OR     | `\|\|`                                                             | LTR                    |
| 13   | Ternary        | `?:`                                                               | RTL                    |
| 14   | Assignment     | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `^=`, `\|=`, `<<=`, `>>=` | RTL                    |
| 15   | Comma          | `,`                                                                | LTR                    |

#### Arithemtic

- Arithmetic operators are formed of the additive and multiplicative operators
- The `%` operator cannot be applied to floats or doubles
- The direction for truncation for `/` is machine-dependent
- The sign of the result for `%` is machine-dependent for negative operands (typically takes on the sign of the left operand)

#### Relational and Logical Operators

- The numerical value of relational and logical expressions is `1` if true or `0` if false

#### Increment and Decrement

- Prefix -> increment then consume
- Postfix -> consume then increment
- Inc. and dec. operators can only be applied to variables

#### Bitwise Operators

- Bitwise operators may only be used on integer operands
- Bitwise AND is often used to mask off some bits (e.g `n &= 0xF` sets all bits to `0` except the low-order 4 bits)
- Bitwise OR is often to use to turn bits on (e.g `n |= 0xF` turns on the low-order 4 bits)
- Shift operators `<<` and `>>` shift the bits up and down respectively of the left-hand operator by the non-negative amount in the right-hand operator (e.g `2 << 2` = `8` since 0010 becomes 1000)
- Vacant bits after shifting are filled with 0s usually

#### Conditional Expressions

##### Ternary Operator

- The first expression of the ternary operator is evaluated
- If non-zero (true), the second is evaluated and that is the value of the expression, otherwise (false) the third is evaluated and that is the value of the expression
- If the second and third expressions differ, then type conversion occurs based on the type conversion rules in the next section

### Type Conversions

- Conversions take place in things like expressions and assignments
- When one variable is unsigned and another signed in a binary expression but both are the same type, the signed will be interpreted as unsigned
- Otherwise, in a conversion, sign is interpreted using the signage of the destination type
- Function prototypes enable automatic casting of arguments

#### Promotion

- When a smaller type is used in a binary arithemtic operation, it is automatically promoted to the larger type used in the expression (promotion)
- So the operation is performed as if it was on two operands of the same type
- In an expression, conversion happens incrementally so the expression will be evaluated LTR as standard but any necessary conversions between two operands will be made along the way

#### Sign Extension

- When a smaller type is unsigned, the compiler performs zero-extension
- When a smaller type is signed, the compiler performs sign-extension where it fills the high-order bits with whatever the old sign bit was (0 if was positive, 1 if was negative)

#### Truncation

- Larger integer types are converted to smaller ones by chopping off the excess higher order bits

#### Floats

- If integer types are mixed with float types, the float type always wins

#### Casting

- An expression can be forcibly cast to another type
- A cast behaves the same way as if an expression was being assigned to a variable of the cast type
