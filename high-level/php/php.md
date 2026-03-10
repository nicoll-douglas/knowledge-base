# PHP Notes

## Table of Contents

1. [Variables & Constants](#1-variables--constants)
   1. [Variables](#11-variables)
   2. [Constants](#12-constants)
2. [Output & Debugging](#2-output--debugging)
3. [Data Types](#3-data-types)
   1. [Introduction](#31-introduction)
   2. [Strings](#32-strings)
   3. [Arrays](#33-arrays)
   4. [Type Casting](#34-type-casting)
   5. [Type Juggling](#35-type-juggling)
4. [Control Flow](#4-control-flow)
   1. [Conditionals](#41-conditionals)
   2. [Loops](#42-loops)
5. [Operators](#5-operators)
   1. [Key Points](#51-key-points)
   2. [Array Operators](#52-array-operators)
6. [Functions](#6-functions)
   1. [Introduction](#61-introduction)
   2. [Parameters & Arguments](#62-parameters--arguments)
   3. [Anonymous Functions](#63-anonymous-functions)
   4. [Arrow Functions](#64-arrow-functions)
7. [References](#7-references)
8. [File Handling](#8-file-handling)
   1. [Importing](#81-importing)
9. [Request Handling](#9-request-handling)
   1. [Superglobals](#91-superglobals)

## 1. Variables & Constants

### 1.1 Variables

#### Basics

- Define variables with `$` symbol
- Uninitialised variables are set to `NULL`
- A variable assignment statement is an expression which evaluates to the value assigned

#### Globals

- Variables declared in the global scope are available in all PHP tags in the same file
- Global variables must be accessed with the `global` keyword

e.g

```php
  $x = 10;
  function myFunction() {
    global $x;
    echo $x;
  }
  myFunction(); // 10
```

#### Superglobals

- PHP has some predefined global variables that are accessible anywhere
- They are called superglobals (e.g `$_POST`, `$_GET`)

### 1.2 Constants

#### Basics

- Fixed values that do not change during script execution
- PHP has some predefined constants like `PHP_INT_MAX` and `PHP_INT_MIN`

#### `define`

- You can define your own constants with the `define` function
- Constants defined with `define` are resolved at runtime
- Can be defined anywhere including conditionals and functions

e.g

```php
  define("PI", 3.14); // can pass true as third param to make constant name case insensitive
  echo PI; // 3.14
```

#### `const`

- Can also define constants with the `const` keyword
- Constants defined with `const` are resolved at compile-time
- They **must** be hard-coded and cannot be defined in conditionals or functions

e.g

```php
  const PI = 3.14;
  echo PI; // 3.14;
```

### 1.3 Magic Constants

- PHP has a few "magic constants" that change depending on where they are used
- [> Full Reference <](https://www.php.net/manual/en/language.constants.magic.php)

e.g

```php
__LINE__ // the current line number of the file
__FILE__ // the full path and filename of the current file
__DIR__ // the directory name of the current file
__FUNCTION__ // the name of the current function or {closure} for anonymous functions
```

## 2. Output & Debugging

#### `echo`

- `echo` used to evaluate a value and output it as string or html
- Can "echo" more than one value with a comma separated list

e.g

```php
  echo "Hello", " ", "World"; // outputs "Hello World"
  echo 2; // outputs "2"
  echo "<p>Hello world</p>"; // outputs html
```

#### `var_dump`

- `var_dump` function can be used to output information about a variable

e.g

```php
  $foo = "bar";
  var_dump($foo); // string(3) "bar"
```

#### `print_r`

- Prints human readable information about variables that range from simple to complex

#### `isset`

- Function that checks if a **variable** is not `NULL`
- For constants, use the `defined` function

## 3. Data Types

### 3.1 Introduction

- All expressions in PHP have one of the following types:

  - `null`
  - `bool`
  - `int`
  - `float`
  - `string`
  - `array`
  - `object`
  - `callable`
  - `resource`

### 3.2 Strings

#### Single Quotes

- Don't support interpolation or escape characters other than `\'` and `\\`

#### Double Quotes

- Supports interpolation and escape characters (e.g `\n`, `\t` `\"`)

#### Heredoc

- Supports interpolation and escape characters

##### Rules:

1. `<<<`, then an indentifier (e.g EOD), then a newline
2. The contents of the string
3. The closing indentifier on its own line with no whitespace before or after and a closing semicolon.

e.g

```php
echo <<<EOD
my cool string
EOD;
```

#### Nowdoc

- The same as heredoc but behaves like a single quoted string

e.g

```php
$var = 3;
echo <<<'EOD'
$var <--- will not be interpolated
EOD;
```

### 3.3 Arrays

#### Basics

- Keys must be ints or strings
- Keys are optional, if not specified, PHP will use the increment of the largest previous int key
- If the same key is used twice, the array will use the latest value
- Access array elements using square brackets (e.g `$arr["foo"]`)
- Add an item to the end of an array using: `$arr[] = `, the key will be the maximum numeric index + 1, **since the last time the array was re-indexed**
- You can call `unset()` function to remove a key-value pair
- If `int`, `float`, `string`, `bool` or `resource` are converted to array, the result is an indexed array with just that one value
- Converting null to an array results in an empty array

#### Syntax

```php
$indexed_array = ["value1", "value2", "value3"];
$associative_array = [
  "key1" => "value1",
  "key2" => "value2",
  "key3" => "value3"
];
```

#### Destructuring

Example 1:

```php
$arr = ["value1", "value2", "value3"];
[$value1, $value2] = $arr;
echo $value1, $value2; // outputs "value1value2"

[, , $value3] = $arr;
echo $value3; // outputs "value3"
```

Example 2:

```php
$arr = ["foo" => 1, "bar" => 2];
["bar" => $two] = $arr;
echo $two; // outputs 2
```

#### References

- Arrays are passed and assigned by value with copy-on-write semantics
- Nested arrays are also copied
- Elements in the array or any sub-array that are a reference type maintain their references

### 3.4 Type Casting

#### To Boolean

- There is a subset of values that are falsy in PHP, all others are truthy

##### Falsy Values:

- `false` (boolean)
- `0` (int)
- `0.0` and `-0.0` (float)
- `""` and `"0"` (string)
- empty array: `[]` (array)
- `NULL`

#### To Integer

- `false` -> `0`, `true` -> `1`
- Numeric strings or leading numeric resolve to the corresponding value otherwise 0 (in arithmetic contexts, a type error is thrown)
- `NULL` -> 0
- Floats `NAN`, `INF` and `-INF` are converted to 0
- Floats get "chopped" when converting to int like other languages

#### To Float

- Numeric strings or leading numeric resolve to the corresponding value otherwise 0
- If converting from another type, it is converted to **int first** and **then float**

#### To String

- Can cast to string using `strval` function or the `(string)` cast
- String casting is automatic in the scope of an expression where a string is needed (e.g in `echo` or `print`, or when a value is compared to a string)
- Floats and ints -> string representations
- Arrays -> `"Array"`
- `NULL` -> `""`
- `true` -> `"1"`, `false` -> `"0"`

### 3.5 Type Juggling

- In **numeric contexts** (when using an arithmetical operator), if one operand is a float (or not interpretable as int), both are interpreted as floats (otherwise ints)
- In **string contexts** (e.g `echo`, string interpolation), value is interpreted as a string.
- In **logical contexts** (e.g conditional statemements, logical operator, ternary), values are interpreted as booleans

## 4. Control Flow

### 4.1 Conditionals

#### Basics

- `if-else` syntax the same as other languages as well as ternary operator
- `switch` statements compare values by loose equality (`==`)
- You can switch on `true`

#### `match`

- There is similar control structure `match` in PHP 8 which compares by strict equality (`===`)
- Like `switch`, `match` will exit out once the first "match" is found
- If no `default` clause is given and no "match" is found, an error is thrown

e.g

```php
  $age = 14;
  $age_group = match (true) {
    $age < 2 => "baby"
    $age >= 13, $age <= 19 => "teenager",
    default => "other"
  };
  echo $age_group; // outputs "teenager"
```

### 4.2 Loops

- `for`, `while` and `do...while` loops work the same as other languages
- `break` and `continue` also the same

e.g

```php
for ($i = 1; $i <= 5; $i++) {
  echo "Iteration: $i", "\n";
}
```

#### `foreach` loops

- Used to iterate over arrays
- Use the `&` operator before `$value` to modify the values in the array
- Break the reference with `$value` outside of the loop, once it ends with `unset()`

e.g

```php
// iterating over values
foreach ($array as $value) {
  // code
}

// iterating over keys and values
foreach ($array as $key => $value) {
  // code
}

// reference break
foreach ($array as &$value) {
  // modify array
}
unset($value);
```

## 5. Operators

### 5.1 Key Points

- Logical operators always produce a boolean value, there is no short-circuiting
- Use the `&` operator to indicate that a value should be referenced
- The `.` operator is use for concatenating strings and can be used in shorthand assigment (i.e `&=`);
- The short-ternary operator (`?:`) behaves like `||` from JS. Returns first value if truthy otherwise second value

### 5.2 Array Operators

- Note: the union operator implements a union based on **keys not values**, using the first array's values if there is an overlap

| Operator | Name         | Result                                                                             |
| -------- | ------------ | ---------------------------------------------------------------------------------- |
| `+`      | Union        | Union of two arrays                                                                |
| `==`     | Equality     | `true` if two arrays have the same key-value pairs                                 |
| `===`    | Identity     | `true` if equal, the key-value pairs are in the same order and have the same types |
| !=       | Inequality   | Opposite of equality                                                               |
| !==      | Non-identity | Opposite of identity                                                               |

### 5.3 Spread Operator

- Allows you to unpack an array or objects implementing the `Traversable` interface into arguments for functions or to merge arrays
- Keys are re-indexed starting from 0 (resolves to a perfectly indexed array)

Example 1:

```php
function sum($a, $b, $c) {
  return $a + $b + $c;
}

$numbers = [1, 2, 3];
echo sum(...$numbers); // $numbers is unpacked and passed as arguments
```

Example 2:

```php
$array1 = [1, 2, 3];
$array2 = [4, 5, 6];

print_r([...$array1, ...$array2]); // output (new merged array): [1, 2, 3, 4, 5, 6]
```

## 6. Functions

### 6.1 Introduction

- Any valid PHP code may appear inside a function, including other functions and class definitions
- Functions can be called before they are defined, except when a function is conditionally defined (safer to call if and only if they are defined)
- It is **not** possible to overload existing functions, undefine them or redefine them
- PHP supports function recursion
- All function declarations have global scope but are only **defined once the interpreter reaches it**

E.g:

```php
function functionThatDefinesAFunction() {
  function myFunction() {
    echo "Hello world";
  }
}

functionThatDefinesAFunction(); // myFunction now available in the global scope

myFunction(); // "Hello world"
```

### 6.2 Parameters & Arguments

#### Basics

- PHP supports default values
- Passing `null` **does not** make the default value get used
- To pass an argument by reference use the `&` operator, to make sure the argument is always passed by reference, use the `&` operator on the parameter
- PHP supports named arguments and they must only appear after positional arguments (if arguing a mix)
- Only use optional arguments after mandatory arguments (otherwise whats the point)
- Use the `&` operator before the function label to return a reference

E.g:

```php
function register($username, $email, $age = 18) {
  return [$username, $age, $email];
}

// using named arguments, order doesnt matter
register(email: "email@example.com", username: "example"); // ["example", 18, "email@example.com"]
```

#### Variable Arguments

- Use the rest paramater to specify variable arguments
- It collects the rest of the arguments into an array (empty array if none given)

E.g

```php
function sum(...$numbers) {
 echo array_sum($numbers);
}

sum(1, 2, 3); // "6"
```

### 6.3 Anonymous Functions

- Functions without names (also know as closures)
- They are implemented using the `Closure` class
- Closures can inherit variables from the parent scope (must be passwed with the `use` keyword, multiple can be passed with comms)
- The inherited value is the value at the **time of function definition** not when called
- The variables are then made available in the local scope of the closure as a copy

Example 1 (Inheritance):

```php
$name = "John";

$greet = function () use ($name) {
  echo "Hello $name";
}

$greet(); // "Hello John"
```

Example 2 (Inheritance by-reference):

```php
$name = "John";

$greet = function () use (&$name) {
  echo "Hello $name";
}

$greet(); // "Hello John"

$name = "Jack"; // change variable

$greet(); // "Hello Jack"; value changes
```

### 6.4 Arrow Functions

#### Syntax:

```php
$y = 1;

$fn1 = fn ($x) => $x + $y;

// equivlanet to using $y by value:
$fn2 = function ($x) use ($y) {
  return $x + $y;
}
```

### Key Points:

- They capture variables by value automatically even when nested
- They behave like other function signatures (so allow ref-return, ref-passing and so on)
- They can only be one line and cannot return void

## 7. References

1 - Imagine this is a memory map:

| Pointer | Value | Variables |
| ------- | ----- | --------- |
| 1       | NULL  |           |
| 2       | NULL  |           |
| 3       | NULL  |           |
| 4       | NULL  |           |
| 5       | NULL  |           |

2 - Create some variables

```php
$a = 10;
$b = 20;
$c = [[1, 2, 3]];
```

3 - Look at memory

| Pointer | Value | Variables |
| ------- | ----- | --------- |
| 1       | 10    | $a        |
| 2       | 20    | $b        |
| 3       | 1     | $c[0][0]  |
| 4       | 2     | $c[0][1]  |
| 5       | 3     | $c[0][2]  |

4 - Create a reference

```php
$a = &$c[0][2];
```

5 - Look at memory

| Pointer | Value | Variables    |
| ------- | ----- | ------------ |
| 1       | NULL  |              |
| 2       | 20    | $b           |
| 3       | 1     | $c[0][0]     |
| 4       | 2     | $c[0][1]     |
| 5       | 3     | $c[0][2], $a |

- Notice how the value of $a is destroyed/moved and the pointer is freed

6 - Create some more references

```php
$b = &$a; // or $b = &$c[0][2]; result is the same as they are both at the same pointer
```

7 - Look at memory

| Pointer | Value | Variables        |
| ------- | ----- | ---------------- |
| 1       | NULL  |                  |
| 2       | NULL  |                  |
| 3       | 1     | $c[0][0]         |
| 4       | 2     | $c[0][1]         |
| 5       | 3     | $c[0][2], $a, $b |

- Notice how the value of $b is destroyed/moved and the pointer is freed

8 - Destroy a reference

```php
unset($c[0][2]);
```

9 - Look at memory

| Pointer | Value | Variables |
| ------- | ----- | --------- |
| 1       | NULL  |           |
| 2       | NULL  |           |
| 3       | 1     | $c[0][0]  |
| 4       | 2     | $c[0][1]  |
| 5       | 3     | $a, $b    |

- Notice how $a and $b still live with the same pointer

10 - Return the reference

```php
$c[0][2] = &$a;
unset($a);
unset($b);
```

11 - Look at memory

| Pointer | Value | Variables |
| ------- | ----- | --------- |
| 1       | NULL  |           |
| 2       | NULL  |           |
| 3       | 1     | $c[0][0]  |
| 4       | 2     | $c[0][1]  |
| 5       | 3     | $c[0][2]  |

- Notice how $c[0][2] is returned to the same pointer and $a and $b are destroyed

## 8. File Handling

### 8.1 Importing

- Use `__DIR__` to refer to the directory of the current file
- Files included/required inside a function behave as if the code was defined within the function

#### `include`

- Imports and executes the specified file at runtime, if not found, script execution continues (warning generated)
- `include_once` ensures that the file is **only included once**
- Returns `false` on failure and `1` on success (unless overriden by a global return statement)

#### `require`

- Similar to `include`, but if the file cannot be found, a fatal error is generated
- Use when file is critical to the application
- `require_once` ensures that the file is **only required once**

## 9. Request Handling

### 9.1 Superglobals

#### `$_GET`

- An associate array of variables passed to the current script via the URL parameters
- Populated for all requests sthat have a query string
- The GET variables are passed through `urldecode()`

#### `$_POST`

- An associative array of variables passed to the current script via the HTTP POST method when using `application/x-www-form-urlencoded` or `multipart/form-data` (key-value pairs) as the Content-Type header

#### `$_REQUEST`

- An associative array that contains the contents of `$_GET`, `$_POST` and `$_COOKIE`

#### `$_SERVER`

- An array containing information such as headers, paths and script locations
- PHP creates additional elements with values from request headers using the "HTTP\_" prefix (underscores replaced with hyphens and all capitalised in the key)
