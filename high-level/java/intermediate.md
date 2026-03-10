# Intermediate Java

Notes on intermediate level Java concepts.

## Table of Contents

1. [Advanced OOP](#1-advanced-oop)

   1. [Interfaces](#11-interfaces)
   2. [Abstract Classes](#12-abstract-classes)
   3. [Enums](#13-enums)
   4. [Anonymous Classes](#14-anonymous-classes)

2. [Generics](#2-generics)

   1. [About Generics](#21-about-generics)
   2. [Generic Methods, Classes & Interfaces](#22-generic-methods-classes--interfaces)
   3. [Bounded Type Parameters](#23-bounded-type-parameters)
   4. [Wildcard Types](#24-wildcard-types)
   5. [Inheritance](#25-inheritance)
   6. [Type Erasure](#26-type-erasure)
   7. [Restrictions](#27-restrictions)

3. [Collections](#3-collections)

   1. [Hierarchies](#31-hierarchies)
   2. [Lists](#32-lists)
   3. [Queues](#33-queues)
   4. [Sets](#34-sets)
   5. [Maps](#35-maps)
   6. [Time Complexity](#36-time-complexity)

4. [JVM](#4-jvm)

   1. [About the JVM](#41-about-the-jvm)
   2. [Architecture](#42-architecture)

5. [Memory](#5-memory)

   1. [Garbage Collection](#51-garbage-collection)
   2. [Memory Leaks](#52-memory-leaks)

6. [Serialization](#6-serialization)

   1. [Overview](#61-overview)
   2. [Deserialization](#62-deserialization)
   3. [SerialVersionUID](#63-serialversionuid)
   4. [Transient Keyword](#64-transient-keyword)
   5. [Limitations](#65-limitations)

7. [Functional Streams](#7-functional-streams)

   1. [Overview](#71-overview)
   2. [Stream Operations](#72-stream-operations)
   3. [Parallel Streams](#73-parallel-streams)

8. [Basics of Threads](#8-basics-of-threads)

   1. [Overview](#81-overview)
   2. [Creating Threads](#82-creating-threads)
   3. [Thread States](#83-thread-states)
   4. [Thread Methods](#84-thread-methods)
   5. [Synchronization](#85-synchronization)

## 1. Advanced OOP

### 1.1 Interfaces

#### Key Points:

- An interface defines a set of methods or behaviours as a **characteristic** that a class can implement
- Achieved with **abstract** methods
- Abstract methods are implicitly `public` and **cannot** be defined otherwise; only static methods may have other modifiers in interfaces
- Classes can implement multiple interfaces (comma separation) allowing Java to overcome limitation of single inheritance (a class can only extend one other class)
- Constants in interfaces are implicitly `public`, `static` and `final`
- The `@FunctionalInterface` directive can be used to indicate a functional interface you define
- Interfaces can inherit from other interfaces like classes with the `extends` keyword

#### Types of Methods:

- **Abstract** - a method with no body; must be given implementations in a class otherwise the class has to be defined with `abstract`
- **Static** - a method that can be called on the interface itself
- **Default** - a method with a default implementation; can be overriden by the implementing class (declared with the `default` keyword)

#### Interfaces & Variables

- You can also declare the type of a variable as an interface
- This means that the variable can refer to any object whose class implements that interface
- Allows for polymorphism since you can change the concrete implementation of the object at runtime without changing the code that uses the interface
- Allows for abstraction since code as such depends on the **behaviours** of the object rather than the specific implementation
- The **interface defines the contract**, meaning you can only call methods that the interface declares
- The **object provides the implementation**, meaning the object provides the code for those methods

##### Example:

```java
interface Animal {
  void makeSound();
}

class Dog implements Animal {
  public void makeSound() {
      System.out.println("Bark");
  }
}

class Cat implements Animal {
  public void makeSound() {
      System.out.println("Meow");
  }
}

Animal myAnimal = new Dog(); // myAnimal can hold any object that implements Animal
myAnimal.makeSound(); // "Bark"

myAnimal = new Cat(); // now it's a cat (run-time polymorphism)
myAnimal.makeSound(); // "Meow"

// the makeSound() method call is an example of abstraction
// declaring myAnimal with Animal means we can care more about the behaviours rather than the implementation
```

### 1.2 Abstract Classes

#### Key Notes:

- Abstract classes are classes that cannot be instantiated and are specified with the `abstract` keyword
- They may have both abstract methods (unimplemented) and concrete methods (implemented)
- Abstract methods should be implemented by an adopting class
- If not all abstract methods implemented, then the class **must** be defined with `abstract`

#### Example:

```java
// abstract class abstracts away a blueprint for implementing classes
abstract class Animal {
  public abstract void makeSound();
}

class Dog extends Animal {
  // method is given concrete implementation
  @Override
  public void makeSound() {
    System.out.println("Dog barks");
  }
}
```

### 1.3 Enums

#### Key Notes:

- Enum is a special type (similar to a class) to denote a group of constants and is denoted with uppercase starting letter
- Enums can have fields, methods, constructors, nested classes, interfaces and enums like other classes
- Type safe so you can only assign enum values to variables of the same enum type
- Enums are immutable, cannot add or remove values once created (implicitly `public`, `static` and `final`, but can be `private` if not at the top level)
- Cannot instantiate new enums, instances are created when the enum is loaded
- Enums inherit methods from the `java.lang.Enum` class
- Java also provides several built in enums (e.g `java.time.Month`)

#### Example:

```java
public enum Day {
  MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY;
}
```

#### Fields, Methods & Constructors in Enums

- Fields in Enums can store additional information about each constant
- Enum constructors are used to initialise these values
- Enum constructors are implicitly `private` and cannot take on any other access modifier
- Enum constructors are called once per constant
- Enums can have instance and static methods to be called on the constants or the enum itself
- For instance members, `this` refers to the current constant

E.g:

```java
public enum Fruit {
  // constants use the Fruit constructor
  APPLE("Red"),
  BANANA("Yellow");

  public final String color; // stores color of fruit constant

  Fruit(String color) {
    this.color = color;
  }
}

Fruit fruit = Fruit.APPLE;
fruit.color; // returns "Red"
```

#### Advanced Enums

- Enums can implement interfaces much like classes
- Enums can also have their own abstract methods
- Each enum constant must provide its own custom implementation of all the abstract methods from their source

##### Example:

```java
public enum Operation {
  // if using a constructor, just utilise the syntax as normal to initiliase the instance fields
  ADD {
    @Override
    public int apply(int x, int y) {
      return x + y;
    }
  },
  SUBTRACT {
    @Override
    public int apply(int x, int y) {
      return x - y;
    }
  }

  public abstract int apply(int x, int y);
}
```

### 1.4 Anonymous Classes

#### Key Points:

- A local class that is declared and instantiated all in one statement
- Used when you want to create a one-time-use subclass or implementation; simplifies code
- Can be more concise with a lambda expression if working with functional interfaces

#### Syntax:

```java
new SuperClassOrInterface() {
  // body
}
```

#### Example:

```java
class Animal {
  public void makeSound() {
    System.out.println("Animal makes a sound");
  }
}

Animal myAnimal = new Animal() { // can use parameters like normal when instantiating
  @Override
  public void makeSound() {
    System.out.println("Woof!");
  }
}; // can also call the method immediately by appending .makeSound without assignment
myAnimal.makeSound();  // Woof!
```

## 2. Generics

### 2.1 About Generics

#### Key Points:

- Generics allow you to parameterize classes, interfaces and methods
- This means you can define a class or method that works with different types without sacrificing type safety

#### Advantages:

- Allows code reusability
- Enforces compile-time type checking reducing the chance of a `ClassCastException` (you can't accidentally insert a value of the wrong type into a collection or object that uses generics
  )
- Generics remove the need for explicit casting

E.g:

```java
List list = new ArrayList();
list.add("Hello");
String str = (String) list.get(0); // Explicit cast needed

List<String> list2 = new ArrayList<>(); // String type in generic
list2.add("Hello");
String str = list.get(0); // No cast needed since type is concrete
```

### 2.2 Generic Methods, Classes & Interfaces

#### Example 1 (Generic Methods)

```java
public <T> void method1(T param) {
  // T is the type parameter
}

public <T, U> U method2(T t, U u) {
  // T and U are the type parameters
  return u; // returns type U
}
```

#### Example 2 (Generic Class)

```java
// Class with type T
class Box<T> {
  T item;

  Box(T item) {
    this.item = item;
  }
}
```

#### Example 3 (Generic Interface)

```java
// interface with type T
interface Reusable<T> {
  void methodName(T param); // abstract method that operates on a param of the supplied type T
}
```

### 2.3 Bounded Type Parameters

- Used in scenarios where you want to restrict the types that can be passed as type arguments to a certain class or its subclasses

Example:

```java
// T must be Number or any subclass of Number
class Box<T extends Number> {
  T item;

  Box(T item) {
      this.item = item;
  }
}
```

### 2.4 Wildcard Types

#### Key Notes:

- You cannot add elements to a collection with a wildcard type as the type cannot be guaranteed during compilation

#### Example 1 (Unbounded)

```java
// ? represents the wildcard (unknown type)
public void printList(List<?> list) {
  for (Object obj : list) {
    System.out.println(obj);
  }
}
```

#### Example 2 (Upper Bounded)

```java
// the list can only accept type Number or any subclass of Number
public void display(List<? extends Number> list) {
  for (Number num : list) {
    System.out.println(num);
  }
}
```

#### Example 3 (Lower Bounded)

```java
// the list can only accept type Integer or any superclass of Integer
public void addNumbers(List<? super Integer> list) {
  list.add(100);
}
```

### 2.5 Inheritance

- Generics in Java do not support polymorphism and inheritance in the way regular types do
- For example, `List<Integer>` is not a subclass of `List<Number>` even though `Integer` is a subclass of `Number`
- They are treated as completely separate types

Example:

```java
List<Number> numbers = new ArrayList<>();
List<Integer> integers = new ArrayList<>();
numbers = integers;  // Compilation error

List<? extends Number> numbers2 = new ArrayList<>();
numbers2 = integers; // correct as the wildcard type can accept Number or any subclass of Number (in this case Integer)
```

### 2.6 Type Erasure

#### Key Notes;

- Generics are implemented using type erasure
- Means generic type information is replaced during compilation
- Before compilation: `List<String>`
- After compilation: `List`

#### Example:

```java
List<String> list = new ArrayList<>();
list instanceof List<String>; // cause compile-time error as the generic type information has been replaced
```

### 2.7 Restrictions

- Static fields and methods cannot utilise generic types since they are tied to the instance of the class
- You cannot use primitives as type arguments for generics (can only use wrappers)
- You cannot instantiate objects of parameterized types (e.g `new T[10]` is illegal, type must be concrete)

## 3. Collections

### 3.1 Hierarchies

#### Iterable Types

<img src="images/collections-iterable.png" width="700" alt="Iterable Hierarchy" />

#### Map Types

<img src="images/collections-map.png" width="700" alt="Map Hierarchy" />

### 3.2 Lists

#### Key Notes:

- The `List` interface represents an **ordered** sequence, **allows duplicate elements** and `null`
- Extends the `Collection` interface which extends the `Iterable` interface
- You can access elements by index, starting with 0
- Provides methods for basic operations (`.get()`, `.add()`, `.remove()`)
- All classes that implement `List` also implement the `ListIterator` interface (allows for forward or backwards traversal)
- `ListIterator` interface is implemented by the abstract class `AbstractList` that lives inbetween `List` and the implementing classes

##### Iterator Example:

```java
List<String> list = new ArrayList<>();

Iterator<String> iterator = list.iterator(); // sequential iterator

while (iterator.hasNext()) {
  String element = iterator.next();
  System.out.println(element);
}
```

#### `ArrayList`

- Class that implements the `List` interface
- Automatic resizing (when elements get inserted or removed, all subsequent elements are shifted or unshifted)
- Read operations are more efficient that write operations

#### `LinkedList`

- Class that implements the `List` interface
- Is a doubly linked list implementation
- Write operations (delete, insert) more efficient than read operations since list has to be traversed to reach element by index

#### `Stack`

- Subclass of `Vector` which implements the `List` interface
- Provides a LIFO (Last-In-First-Out) stack mechanism/implementation
- Has methods like `push()`, `pop()` and `peek()` for stack operations

### 3.3 Queues

#### Key Points:

- Queue based collections implement the `Queue` interface
- Queues are ordered and can allow duplicates
- A queue follows the FIFO (First-In-First-Out) principle
- Elements that remove take the first from the queue, elements that add insert at the end of the queue
- Some queue implementations have bounds (i.e queues have a limit and be full)

#### `Queue` Methods

| Operation | Throws Exception on Failure | Returns Special Value                       |
| --------- | --------------------------- | ------------------------------------------- |
| Insert    | `add(E e)`                  | `offer(E e)` (boolean depending on success) |
| Remove    | `remove()`                  | `poll()` (`null` if none)                   |
| Examine   | `element()`                 | `peek()` (`null` if none)                   |

#### `LinkedList`

- Implements both the `List` and `Queue` interfaces
- Provides a doubly linked-list that follows FIFO when used as a queue
- Is unbounded

E.g

```java
Queue<String> queue = new LinkedList<>();
queue.offer("apple");
queue.offer("banana");
queue.poll(); // removes "apple"
```

#### `PriorityQueue`

- Implements a priority-based queue
- Elements are ordered either based on their natural ordering (if they implement `Comparable`) or using a provided `Comparator`
- Not guaranteed to follow FIFO order; instead, elements with the highest priority (lowest value in terms of comparison) are dequeued first
- Is unbounded

```java
Queue<Integer> pq = new PriorityQueue<>();
pq.offer(5);
pq.offer(2);
pq.offer(10);
pq.poll(); // removes 2 (the smallest element)
```

#### `ArrayDeque`

- Implements a doubly-ended queue (deque / `Deque` interface) which allows for insertion and removal at both ends
- Is more efficient than `LinkedList` for queues
- Is unbounded

### 3.4 Sets

#### Key Notes:

- Does not allow duplicate elements
- If you try to add an element that already exists, the set will ignore it
- Has no guaranteed order for its elements (some implementations like `LinkedHashSet` and `TreeSet` do maintain order)
- Provides various operations for checking membership, adding/removing elements, and set operations like union, intersection, and difference
- Two sets are equal if they contain the same elements, regardless of order
- Sets are useful for ensuring **uniqueness** in a collection

#### `HashSet`

- Class that implements the `Set` interface
- Uses a hash table for storing elements
- Does not guarantee any order of elements
- Is the most commonly used implementation
- Allows **one** null element

#### `LinkedHashSet`

- Extends `HashSet` but maintains a linked list of entries which preservers insertion order
- Iterates over the elements in the order in which they were added
- Allows **one** null element

#### `TreeSet`

- Implements `NavigableSet` (which extends `SortedSet`), meaning it stores elements in a sorted order (natural order or using a custom comparator)
- Does not allow **null** elements (throws `NullPointerException`)

#### Set Operations

- **Union**: Add all elements from one set to another (`.addAll()`)
- **Intersection**: Retain only the common elements between two sets (`.retainAll()`)
- **Difference**: Remove all elements in one set from another (`.removeAll()`)

E.g

```java
List<Integer> set1Items = Arrays.asList(new Integer[]{1, 2, 3, 5});
Set<Integer> set1 = new HashSet<>(set1Items);

List<Integer> set2Items = Arrays.asList(new Integer[]{2, 3, 4});
Set<Integer> set2 = new HashSet<>(set2Items);

// Union of set1 and set2
set1.addAll(set2);  // set1 now contains [1, 2, 3, 4, 5]
System.out.println(set1);

// Intersection of set1 and set2
set1.retainAll(set2);  // set1 now contains [2, 3, 4]
System.out.println(set1);

// Difference between set1 and set2
set1.removeAll(set2);  // set1 now contains []
System.out.println(set1);
```

### 3.5 Maps

#### Key Notes:

- Maps represent a collection of key-value pairs
- Each key is unique and maps to exactly one value
- If you try to insert a key that already exists, the value will simply be overriden
- Supports basic operations (`.put(K key, V value)`, `.get(Object key)`, `.containsKey(Object key)`)
- The `.containsKey()` and `.get()` methods are dependent on the output of the `.hashCode()` and `.equals()` method calls on the object

#### `HashMap`

- Allows one `null` key and multiple `null` values
- Is the most common implementation

#### `Hashtable`

- Does not allow `null` keys or `null` values

#### `LinkedHashMap`

- Maintains a linked list of entries in the order they were inserted (preserves insertion order)
- Allows for predictable iteration

#### `TreeMap`

- Maintains a sorted order of keys (based on natural order if a custom `Comparator` for comparison)
- Useful when you need a sorted map that provides a range of keys based on natural order

### 3.6 Time Complexity

#### Lists

| Implementation | Access | Search | Insertion | Deletion |
| -------------- | ------ | ------ | --------- | -------- |
| ArrayList      | O(1)   | O(n)   | O(n)      | O(n)     |
| LinkedList     | O(n)   | O(n)   | O(1)      | O(1)     |

#### Queues

| Implementation        | Access | Search | Insertion | Deletion |
| --------------------- | ------ | ------ | --------- | -------- |
| LinkedList (as Queue) | O(1)   | O(n)   | O(1)      | O(1)     |
| ArrayDeque            | O(1)   | O(n)   | O(1)      | O(1)     |
| PriorityQueue         | O(1)   | O(n)   | O(log n)  | O(log n) |

#### Sets

| Implementation | Access   | Search   | Insertion | Deletion |
| -------------- | -------- | -------- | --------- | -------- |
| HashSet        | O(1)     | O(1)     | O(1)      | O(1)     |
| LinkedHashSet  | O(1)     | O(1)     | O(1)      | O(1)     |
| TreeSet        | O(log n) | O(log n) | O(log n)  | O(log n) |

#### Maps

| Implementation | Access   | Search   | Insertion | Deletion |
| -------------- | -------- | -------- | --------- | -------- |
| HashMap        | O(1)     | O(1)     | O(1)      | O(1)     |
| LinkedHashMap  | O(1)     | O(1)     | O(1)      | O(1)     |
| HashTable      | O(1)     | O(1)     | O(1)      | O(1)     |
| TreeMap        | O(log n) | O(log n) | O(log n)  | O(log n) |

## 4. JVM

### 4.1 About the JVM

#### Key Points:

- Stands for Java Virtual Machine
- You write Java source code in `.java` files
- The Java source code is compiled by the Java compiler (`javac`) into **bytecode** (`.class` files) which is a platform-independent intermediate representation
- The JVM then loads, verifies and executes the bytecode
- The JVM translates the bytecode into machine code for the host system and interprets code when necessary

#### JDK vs JRE vs JVM

<img src="images/jdk.png" width="500" alt="JDK vs JRE vs JVM" />

### 4.2 Architecture

#### Class Loader

- The class loader is responsible for loading Java class files into memory when they are referenced in the program
- **Loading**: The class loader finds the class file and loads its bytecode
- **Linking**: Verifies the bytecode for correctness, allocates memory for static fields and resolves symbolic references to actual memory addresses
- **Initialization**: The class is initialized, including the execution of static initializers and initialization of static variables

#### Runtime Data Areas

- **Method Area**: Stores class-level data such as static variables, constants, method data and bytecode for methods
- **Heap**: Where all objects and their instance variables are allocated. Is shared by all threads and is managed by the garbage collector
- **Stack**: Each thread has its own stack which stores local variables, partial results and call frames (holds the state for a single method invocation such as parameters, local variables and return addresses)
- **Program Counter (PC) Register**: Each thread has a PC register, which holds the address of the current instruction being executed
- **Native Method Stack**: Used when the JVM calls native (platform-specific) methods written in languages like C or C++

#### Execution Engine

- **Interpreter**: Reads and executes bytecode instructions one at a time but can be slow
- **Just-In-Time (JIT) Compiler**: Compiles frequently executed bytecode sequences into native machine code at runtime. Stores it in the code cache and executes it directly when necessary which significantly boosts performance
- **Garbage Collector**: Identifies and removes objects in the heap that are no longer references by any part of the program, freeing up memory

## 5. Memory

### 5.1 Garbage Collection

#### Key Points:

- Objects stored in the heap where all dynamic memory allocation occurs for objects at runtime
- Is the process of identifying and reclaiming memory that is no longer referenced by the program
- Objects eligible for garbage collection are not **reachable** i.e cannot be traced from **GC Roots**

#### GC Roots:

- Active threads
- Local variables and method parameters in the current execution stack
- Static fields of loaded classes
- JNI (Java Native Interface) references

#### Example:

```java
Object a = new Object(); // unreachable reference is now eligible for GC after being overriden
a = new Object();

```

### 5.2 Memory Leaks

#### Key Points:

- Occurs when objects that are no longer needed by the application continue to be referenced preventing garbage collection

#### Case 1 - Object Retention in Static Fields

- Objects referenced in static fields are retained for the entire lifetime of the application
- No garbage collection until the application shuts down
- Even if no longer used, they will stay in memory
- Avoid overly large static collections of objects

#### Case 2 - Improper Resource Closure

- Forgetting to explicitly close resources like file streams, database connections, or sockets can lead to memory leaks since those resources may not be automatically closed by the garbage collector
- Use a try with resources block to automatically close resources when the block ends

##### Example:

```java
try {
  FileInputStream fis = new FileInputStream("file.txt");
// Forgetting to close the file stream leads to resource leaks
} catch (IOException e) {}
```

## 6. Serialization

### 6.1 Overview

#### Key Points:

- Process of converting an object into a byte stream
- The byte stream represents the object's data, its type (class) and the types of its fields
- Once serialized, can be saved, transferred or sent over a network
- Can later be deserialized by converting the byte stream into a copy of the original object
- A class must implement the `java.io.Serializable` interface in order for its objects to be serialized and deserialized
- The `Serializable` interface is just a marker interface; doesn't declare any methods, just tells the compiler the class's objects are eligible for serialization
- The `.close()` method can be used to close streams or a try-with-resources block
- The `.flush()` method can be used on the `ObjectOutputStream` to write data prematurely without closing the stream

#### Example:

```java
import java.io.*;

class Person implements Serializable {};

Person person = new Person();

// use ObjectOutputStream to write object to a file or stream
try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("person.ser"))) {
  oos.writeObject(person); // Write the object to a file
} catch (IOException e) {
  e.printStackTrace();
}
```

### 6.2 Deserialization

#### Key Points:

- The opposite of deserialization
- The byte stream is converted back into a Java object using `ObjectInputStream`

#### Example (Previous):

```java
try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("person.ser"))) {
  Person person = (Person) ois.readObject(); // Read the object from the file
} catch (IOException | ClassNotFoundException e) {
  e.printStackTrace();
}
```

### 6.3 SerialVersionUID

#### Key Points:

- The `serialVersionUID` is a unique version identifier for each class
- Helps during deserialization to verify that the sender and receiver of a serialized object have loaded classes for that object that are compatible
- If no `serialVersionUID` is declared, Java automatically generates one at runtime
- Recommended to **explicitly** declare one to avoid issues when the class is modified after serialization
- If the class definition changes (e.g a field is added or removed) and the `serialVersionUID` doesn't match, Java will throw an `InvalidClassException` during deserialization

#### Example:

```java
private static final long serialVersionUID = 1L;
```

### 6.4 Transient Keyword

- If you want to prevent a particular field from being serialized, you can mark it as `transient`
- This means that during serialization, the field will not be saved to the byte stream, and its value will be ignored

E.g

```java
transient int age = 10; // field wouldn't be serialized
```

### 6.5 Limitations

- **Versioning Issues**: Changes to the class structure can break the deserialization process if not handled correctly with `serialVersionUID`
- **Performance**: Serialization can be slower than other persistence models like JSON; can also increase the file size or network overhead
- **Security**: Deserializing untrusted data can lead to vulnerabilites like **Remote Code Execution (RCE)**

## 7. Functional Streams

### 7.1 Overview

#### Key points:

- API that lets you process collections of data (e.g `List`, `Set`, `Map`) in a functional manner (`java.util.stream`)
- Provides methods for for performing operations like filtering, mapping, and reducing in a pipeline fashion, supporting parallelism and efficiency
- Streams can be created from Collections, Arrays or other data sources (like files)

#### Key Concepts:

- **Stream**: Represents a sequence of elements supporting sequential and parallel aggregate operations
- **Pipeline**: A stream operation consists of a source, intermediate operations (like filtering or mapping), and a terminal operation (like `collect`, `forEach`, or `reduce`)
- **Lazy Evaluation**: Intermediate operations are lazily evaluated (only executed when a terminal operation is invoked)

### 7.2 Stream Operations

#### Intermediate Operations (return a new stream):

- `.filter(Predicate)`: Filters elements based on a condition
- `.map(Function)`: Transforms elements from one type to another
- `.sorted()`: Sorts the elements of the stream
- `.distinct()`: Removes duplicates from the stream

#### Terminal Operations (produce a result or side-effect):

- `.forEach(Consumer)`: Performs an action on each element
- `.collect(Collector)`: Converts the stream into a collection (e.g., List, Set)
- `.reduce(BinaryOperator)`: Reduces the elements of the stream into a single value (e.g., summing numbers)
- `.count()`: Returns the number of elements in the stream

#### Example:

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");

// Stream pipeline: filter names starting with 'C', map to uppercase, collect to List
List<String> filteredNames = names.stream()
        .filter(name -> name.startsWith("C")) // Intermediate
        .map(String::toUpperCase) // Intermediate
        .collect(Collectors.toList()); // Terminal

System.out.println(filteredNames);  // [CHARLIE]
```

### 7.3 Parallel Streams

- You can easily process large datasets in parallel using parallel streams, which divide the stream into multiple parts and process them concurrently using multiple threads

E.g

```java
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);

// Sum all numbers in parallel
int sum = numbers.parallelStream().reduce(0, Integer::sum);

System.out.println(sum); // 21

```

## 8. Basics of Threads

### 8.1 Overview

#### Key Points:

- A thread is a lightweight sub-process, a small unit of processing that can be executed independently
- In Java, threads allow concurrent execution of two or more parts of a program, meaning that multiple tasks can be performed simultaneously
- This is known as multithreading
- Built-in support for multithreading through the `java.lang.Thread` class and `java.lang.Runnable` interface
- Threads have a priority; a thread with a high priority is executed in preference to a thread with lower priority (priority ranges 1-10, 5 being the default)
- The JVM continues to execute threads until either A, `System.exit()` is called or all **user** threads have died

#### Why Use Threads:

- **Improving performance**: By splitting tasks, threads can make better use of multi-core CPUs
- **Concurrency**: Multiple threads can handle tasks like reading/writing files, database access, or handling multiple client requests in a server simultaneously
- **Background tasks**: Threads allow you to perform background tasks (e.g., downloading files, processing data) without blocking the main application

### 8.2 Creating Threads

- Can be created by implementing the `Runnable` interface into a class
- The `Thread.start()` method internally calls `.run()`

E.g

```java
class MyRunnable implements Runnable {
  @Override
  public void run() {
    // Code to be executed by the thread
  }
}

public class Main {
  public static void main(String[] args) {
    MyRunnable myRunnable = new MyRunnable();
    Thread thread1 = new Thread(myRunnable);
    thread1.start();  // Starts the thread

    Thread thread2 = new Thread(myRunnable);
    thread2.start();  // Starts another thread
  }
}
```

### 8.3 Thread States

#### A thread can be in one of the following states:

- **NEW**: The thread is created but not yet started (`Thread` object created)
- **RUNNABLE**: The thread is eligible to run, either running or waiting for CPU time
- **BLOCKED**: The thread is waiting for a monitor lock (e.g., when waiting for synchronized code)
- **WAITING**: The thread is waiting indefinitely for another thread to perform a particular action (e.g., `Object.wait()`)
- **TIMED_WAITING**: The thread is waiting for a specified amount of time (e.g., `Thread.sleep()`, `Object.wait(long)`)
- **TERMINATED**: The thread has finished execution (either completed normally or was terminated abnormally)

### 8.4 Thread Methods

#### Common Thread Methods:

- `.start()`: Starts the thread and calls its run() method in a new thread
- `.run()`: The entry point for the thread, where the thread’s code is executed
- `.sleep(long millis)`: Pauses the thread for the specified amount of time (in milliseconds)
- `.join()`: Waits for the thread to complete. The main thread can wait for other threads to finish using this method

### 8.5 Synchronization

#### Key Points:

- In a multithreading environment, threads often have access to shared resources (e.g variables, files)
- Java provides synchronization to control access to shared resources and ensure thread-safety
- Without synchronization, race conditions can occur meaning one thread may try to change a shared resource whilst another is trying to read or update it at the same time causing inconsistent data
- Synchronization occurs at the object level so different objects have different locks

#### Synchronized Methods:

```java
public synchronized void print() {
  // Only one thread can access this method at a time
}
```

#### Synchronized Blocks:

##### Syntax:

```java
public void print() {
  synchronized (lockObject) {
    // Only one thread can execute this block at a time
  }
}
```

##### Using `this` as a Lock Object:

- You can also use `this` as the lock object
- This means that only one thread can enter any synchronized block that uses `this` as the lock for the same object at the same time

#### Synchronization In Action

```java
class Counter {
  private int count = 0;

  // Thread-safe; race conditions occur without the synchronized keyword
  public synchronized void increment() {
    count++;
  }

  public int getCount() {
    return count;
  }
}

public class Main {
  public static void main(String[] args) {
    Counter counter = new Counter();

    Thread t1 = new Thread(() -> {
      for (int i = 0; i < 1000; i++) {
        counter.increment();
      }
    });

    Thread t2 = new Thread(() -> {
      for (int i = 0; i < 1000; i++) {
        counter.increment();
      }
    });

    t1.start();
    t2.start();

    try {
      t1.join();
      t2.join();
    } catch (InterruptedException e) {
      e.printStackTrace();
    }

    // final output will consistently be 2000
    System.out.println("Final Count: " + counter.getCount());
  }
}
```
