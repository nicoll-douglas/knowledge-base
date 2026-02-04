# SQL Notes

## Table Of Contents

1. [Databases](#1-databases)
2. [Tables](#2-tables)
   1. [Data Types](#21-data-types)
   2. [Creating Tables](#22-creating-tables)
   3. [Showing Data](#23-showing-data)
   4. [Deleting Tables](#24-deleting-tables)
   5. [Updating Columns](#25-updating-columns)
3. [Rows](#3-rows)
   1. [Adding Rows](#31-adding-rows)
   2. [Updating Rows](#32-updating-rows)
   3. [Deleting Rows](#33-deleting-rows)
4. [Queries](#4-queries)
   1. [Basic Queries](#41-basic-queries)
   2. [Conditionals](#42-conditionals)

## 1. Databases

- Creating a database:

  ```sql
  CREATE DATABASE tut;
  CREATE DATABASE IF NOT EXISTS tut; -- safe creation (check if it exists)
  ```

- Deleting a database:

  ```sql
  DROP DATABASE tut;
  ```

- Show tables:

  ```sql
  SHOW TABLES;
  ```

- Select a database:

  ```sql
  USE tut;
  ```

## 2. Tables

### 2.1 Data Types

```sql
INT -- Whole numbers
DECIMAL(M, N) -- Decimal numbers (M number of digits total, N number of digits after the decimal)
VARCHAR(X) -- String of length X (max length)
BLOB -- Binary Large Object (stores large data)
DATE -- 'YYYY-MM-DD'
TIMESTAMP -- 'YYYY-MM-DD HH:MM:SS'
```

### 2.2 Creating Tables

#### Table creation:

```SQL
CREATE TABLE student (
  student_id INT PRIMARY KEY,
  name VARCHAR(20),
  major VARCHAR(20)
);
```

| student_id | name | major |
| ---------- | ---- | ----- |

#### Constraints:

- Can be used after the type declaration

```sql
NOT NULL -- The value cannot be null
UNIQUE -- The value has to be unique for the field
DEFAULT -- 'default_value' 'default_value' is used as the default if no value provided
AUTO_INCREMENT -- The value gets automatically incremented each time a row is added
```

### 2.3 Showing Data

- Show table contents:

  ```sql
  SELECT * FROM student;
  ```

- Show information about a table:

  ```sql
  DESCRIBE student;
  ```

  Output:

  | Field      | Type        | Null | Key | Default | Extra |
  | ---------- | ----------- | ---- | --- | ------- | ----- |
  | student_id | int         | NO   | PRI | NULL    |       |
  | name       | varchar(20) | YES  |     | NULL    |       |
  | major      | varchar(20) | YES  |     | NULL    |       |

### 2.4 Deleting Tables

```sql
DROP TABLE student;
```

### 2.5 Updating Columns

- Adding a column:

  ```sql
  ALTER TABLE student ADD gpa DECIMAL(3, 2);
  ```

- Dropping a column:

  ```sql
  ALTER TABLE student DROP COLUMN gpa;
  ```

## 3. Rows

### 3.1 Adding Rows

- Adding a new row:

  ```sql
  INSERT INTO student VALUES (1, "Jack", "Biology");
  ```

- Adding a new row with specific values:

  ```sql
  INSERT INTO student (student_id, name) VALUES (2, "Kate");
  ```

### 3.2 Updating Rows

- Conditional update:

  ```sql
  UPDATE student -- updating the student table
  SET major = "Bio" -- change the major field to "Bio"
  WHERE major = "Biology"; -- if their major is "Biology"
  ```

- Condtional update for multiple conditions:

  ```sql
  UPDATE student
  SET major = "Biochemistry"
  WHERE major = "Biology" OR major = "Chemistry";
  ```

- Set multiple fields:

  ```sql
  UPDATE student
  SET name = "Tom", major = "undecided"
  WHERE student_id = 1;
  ```

### 3.3 Deleting Rows

- Delete a row:

  ```sql
  DELETE FROM student
  WHERE student_id = 1 AND major = "undecided";
  ```

## 4. Queries

### 4.1 Basic Queries

- Select specific fields:

  ```sql
  SELECT name, major
  FROM student;
  ```

- Ordering rows:

  ```sql
  SELECT name, major
  FROM student
  ORDER BY name; -- will order the returned rows alphabetically by name

  SELECT name, major
  FROM student
  ORDER BY student_id DESC; -- using descending order and can still order by non-selected fields
  ```

- Limiting results:

  ```sql
  SELECT *
  FROM student
  LIMIT 2; -- will only get the first 2 results
  ```

### 4.2 Conditionals

#### Example:

```sql
SELECT name, major
FROM student
WHERE major = "Chemistry" OR name = "Kate";
```

#### Conditional Operators

- `<` : Less than
- `>` : Greater than
- `<=` : Less than or equal to
- `>=` : Greater than or equal to
- `=` : Equal to
- `<>` : Not equal to
- `AND` and `OR`

#### `IN` operator

- Specify upon a set of values

E.g

```sql
SELECT *
FROM student
WHERE name in ("Claire", "Kate", "Mike"); -- only get rows if name field is in the set
```
