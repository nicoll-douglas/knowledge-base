# ER Diagrams

## 1. Basics

- **Entity**
  - Definition: An object we want to model & store information about
  - Example: Students in a school
  - Notation: Box
- **Attributes**
  - Definition: Specific pieces of information about an entity
  - Example: Student's name and gpa
  - Notation: Bubble attached to entity
- **Primary Key**
  - Defintion: An attribute that uniquely identify an entity or entry in a database
  - Example: Student's ID number
  - Notation: Bubble with underline

## 2. Other Types of Attributes

- **Composite Attributes**
  - Definition: An attribute that can be broken up into sub-attributes
  - Example: Name made up of fname and lname
  - Notation: Bubble sub-tree
- **Multi-valued Attribute**
  - Definition: An attribute that can have more than one value
  - Example: A student's clubs
  - Notation: Double-ringed bubble
- **Derived Attribute**
  - An attribute who's value can be derived from other attributes
  - Example: If name starts with A (derived from name)
  - Notation: Bubble with dashed ring

## 3. Relationships

- **Multiple Entities**
  - You can define more than one entity in an ER diagram
- **Relationships**
  - Definition: A verb that defines a relationship between two entities
  - Example: Student **takes** class (or class **taken by** student)
  - Links with diamond between entities
- **Total Participation**
  - Definition: All members must participate in the relationship
  - Example: A class must always be in a state of 'class **taken by** student' (at least one)
  - Notation: Single link
- **Partial Participation**
  - Definition: Not all members have to participate in the relationship
  - Example: A student doesn't always have to be in a state of 'student **takes** class' (student doesn't have to take classes)
- **Relationship Attribute**:
  - Definition: An attribute about the relationship
  - Example: A student obtains a grade in a class
- **Relationship Cardinality**:
  - Definition: The number of instances of an entity from a relation that can be associated with the relation
  - Types
    - **N:M**: A student can take any number of classes and a class can be taken by any number of students
    - **1:1**: A student can only take one class and a class can only be taken by one student
    - **1:N**: A student can only take one class and a class can be take by many students
  - Notation: Should read like a sentence on the diagram (e.g (Student) -> takes -> M -> (Class))

## 4. Weak Entities

- **Weak Entity**
  - Definition: An entity that cannot be uniquely identified by its attributes alone
  - Example: An exam **has** to exist as a result of a class entity and cannot exist otherwise
  - Notation: Double-ringed box
- **Identifying Relationship**
  - Definition: A relationship that serves to uniquely identify the weak entity
  - Example: A class **has** an exam and an exam **has** a class
  - Notation: Double-ringed diamond
  - Note: Weak entities always have total participation in the identifying relationship

## 5. Converting ER Diagrams to Schemas

### Step 1: Mapping of Regular Entity Types

- For each regular entity type, create a relation (table) that includes all of the simple attributes (with composite attributes only store the sub-attributes)

### Step 2: Mapping of Weak Entity Types

- For each weak entity type, create a relation (table) taht includes all simple attributes
- Primary key of the new relation should be the partial key of the weak entity plus the primary key of its owner

### Step 3: Mapping of Binary 1:1 Relationships

- Binary Relationship: Relationship between two entities
- Include one side of the relationship as a foreign key in the other (favor total participation; if an entity has total participation, add the foreign key on that entity)

### Step 4: Mapping of Binary 1:N Relationships

- Include the 1 side's primary key as a foreign key on the N side relation (table)

### Step 5: Mapping of Binary M:N Relationships

- Create a new relation (table) who's primary key is a combination of both entities' primary keys (compound key)
- Also include any relationship attributes
- This table represents the relationship
