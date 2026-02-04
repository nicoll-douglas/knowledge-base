# CompanyDB Tutorial

## Table of Contents

1. [Creating the Tables](#1-creating-the-tables)
   1. [Employee Table](#11-employee-table)
   2. [Branch Table](#12-branch-table)
   3. [Client Table](#13-client-table)
   4. [Works With Table](#14-works-with-table)
   5. [Branch Supplier Table](#15-branch-supplier-table)
2. [Inserting Data](#2-inserting-data)
   1. [Corporate Employees](#21-corporate-employees)
   2. [Scranton Employees](#22-scranton-employees)
   3. [Stamford Employees](#23-stamford-employees)
   4. [Branch Suppliers](#24-branch-suppliers)
   5. [Clients](#25-clients)
   6. [Works With](#26-works-with)
3. [Queries](#3-queries)
   1. [Basic Queries](#31-basic-queries)
   2. [Wildcards](#32-wildcards)
   3. [Unions](#33-unions)
   4. [Joins](#34-joins)
   5. [Nested Queries](#35-nested-queries)
4. [Advanced Topics](#4-advanced-topics)
   1. [Handling Deleted Data](#41-handling-deleted-data)
   2. [Triggers](#42-triggers)

## 1. Creating the Tables

### 1.1 Employee Table

```sql
CREATE TABLE employee (
  emp_id INT PRIMARY KEY,
  first_name VARCHAR(40),
  last_name VARCHAR(40),
  birth_day DATE,
  sex VARCHAR(1),
  salary INT,
  super_id INT, -- will bcome a foreign key
  branch_id INT, -- will become a foreign key
);
```

### 1.2 Branch Table

```sql
-- mgr_id is a foreign key that points to an employee based on emp_id
CREATE TABLE branch (
  branch_id INT PRIMARY KEY,
  branch_name VARCHAR(40),
  mgr_id INT,
  mgr_start_date DATE,
  FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);
```

Setting the super_id and branch_id of the employee table as foreign keys:

```sql
ALTER TABLE employee -- modify employee table
ADD FOREIGN KEY(branch_id) -- make branch_id a foreigh key
REFERENCES branch(branch_id) -- Points to a branch based on branch_id
ON DELETE SET NULL;

-- same for the super_id field to point to a supervisor employee
ALTER TABLE employee
ADD FOREIGN KEY(super_id)
REFERENCES employee(emp_id)
ON DELETE SET NULL;
```

### 1.3 Client Table

```sql
CREATE TABLE client (
  client_id INT PRIMARY KEY,
  client_name VARCHAR(40),
  branch_id INT,
  -- foreign key referencing the branch
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL
);
```

### 1.4 Works With Table

```sql
CREATE TABLE works_with (
  emp_id INT,
  client_id INT,
  total_sales INT,
  PRIMARY KEY(emp_id, client_id),
  FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE,
  FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE CASCADE
);
```

### 1.5 Branch Supplier Table

```sql
CREATE TABLE branch_supplier (
  branch_id INT,
  supplier_name VARCHAR(40),
  supply_type VARCHAR(40),
  PRIMARY KEY(branch_id, supplier_name),
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);
```

## 2. Inserting Data

### 2.1 Corporate Employees

```sql
-- insert manager
-- last param (branch_id) should be 1 but that branch (corporate) hasn't been created yet
INSERT INTO employee VALUES(100, "David", "Wallace", "1967-11-17", "M", 250000, NULL, NULL);


-- insert corporate branch and reference manager above ^^^
INSERT INTO branch VALUES(1, "Corporate", 100, "2006-02-09");

-- update the branch_id for David Wallace
UPDATE employee
SET branch_id = 1
WHERE emp_id = 100;

-- insert the last employee that works for the corporate branch
INSERT INTO employee VALUES(101, "Jan", "Levinson", "1961-05-11", "F", 110000, 100, 1);
```

### 2.2 Scranton Employees:

```sql
-- Create manager
INSERT INTO employee VALUES(102, "Michael", "Scott", "1964-03-15", "M", 75000, 100, NULL);

-- Create Scranton branch
INSERT INTO branch VALUES(2, "Scranton", 102, "1992-04-06");

-- Update manager's branch to be Scranton
UPDATE employee
SET branch_id = 2
WHERE emp_id = 102;

-- Insert other employees
INSERT INTO employee VALUES(103, 'Angela', 'Martin', '1971-06-25', 'F', 63000, 102, 2);
INSERT INTO employee VALUES(104, 'Kelly', 'Kapoor', '1980-02-05', 'F', 55000, 102, 2);
INSERT INTO employee VALUES(105, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, 102, 2);
```

### 2.3 Stamford Employees

```sql
-- Create manager
INSERT INTO employee VALUES(106, 'Josh', 'Porter', '1969-09-05', 'M', 78000, 100, NULL);

-- Create branch
INSERT INTO branch VALUES(3, 'Stamford', 106, '1998-02-13');

-- Update manager's branch to be Stamford
UPDATE employee
SET branch_id = 3
WHERE emp_id = 106;

-- Insert other employees
INSERT INTO employee VALUES(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, 3);
INSERT INTO employee VALUES(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);
```

### 2.4 Branch Suppliers

```sql
INSERT INTO branch_supplier VALUES(2, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Patriot Paper', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'J.T. Forms & Labels', 'Custom Forms');
INSERT INTO branch_supplier VALUES(3, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(3, 'Stamford Lables', 'Custom Forms');
```

### 2.5 Clients

```sql
INSERT INTO client VALUES(400, 'Dunmore Highschool', 2);
INSERT INTO client VALUES(401, 'Lackawana Country', 2);
INSERT INTO client VALUES(402, 'FedEx', 3);
INSERT INTO client VALUES(403, 'John Daly Law, LLC', 3);
INSERT INTO client VALUES(404, 'Scranton Whitepages', 2);
INSERT INTO client VALUES(405, 'Times Newspaper', 3);
INSERT INTO client VALUES(406, 'FedEx', 2);
```

### 2.6 Works With

```sql
INSERT INTO works_with VALUES(105, 400, 55000);
INSERT INTO works_with VALUES(102, 401, 267000);
INSERT INTO works_with VALUES(108, 402, 22500);
INSERT INTO works_with VALUES(107, 403, 5000);
INSERT INTO works_with VALUES(108, 403, 12000);
INSERT INTO works_with VALUES(105, 404, 33000);
INSERT INTO works_with VALUES(107, 405, 26000);
INSERT INTO works_with VALUES(102, 406, 15000);
INSERT INTO works_with VALUES(105, 406, 130000);
```

## 3. Queries

### 3.1 Basic Queries

- Use the `AS` keyword to change the returned column names

  ```sql
  SELECT first_name AS forename, last_name AS surname
  FROM employee;
  ```

- Use the `DISTINCT` keyword to see all the distinct values in a column

  ```sql
  SELECT DISTINCT sex
  FROM employee;
  ```

- Use the `COUNT` function to count rows

  ```sql
  SELECT COUNT(emp_id)
  FROM employee; -- 9

  SELECT COUNT(super_id)
  FROM employee; -- 8; excludes CEO David Wallace (only counts where the value is not NULL)
  ```

- Use the `AVG` function find averages

  ```sql
  -- finding the average salary amongst men
  SELECT AVG(salary)
  FROM employee
  WHERE sex = "M";
  ```

- Use the `SUM` function to add up values

  ```sql
  SELECT SUM(salary)
  FROM employee;
  ```

- Use the `GROUP BY` keyword to aggregate queries together

  ```sql
  SELECT COUNT(sex), sex -- Resulting table should have colums COUNT(sex) and sex
  FROM employee -- from the employee table
  GROUP BY sex; -- for all distinct entries in the sex column, there will be a count in the count column

  SELECT SUM(total_sales), emp_id -- columns should be a sum of total_sales and emp_id
  FROM works_with -- from the works_with table
  GROUP BY emp_id; -- for all distinct emp_id entries, there should be a sum column
  ```

### 3.2 Wildcards

- Use the `LIKE` keyword to match against wildcard patterns

  ```sql
  -- retrieve a list of suppliers that probably sell lables
  SELECT *
  FROM branch_supplier
  WHERE supplier_name LIKE '% Label%'; -- % matches any number of characters

  -- retrieve all employees born in October
  SELECT *
  FROM employee
  WHERE birth_date LIKE '____-10%'; -- _ matches any one character
  ```

### 3.3 Unions

- Use `UNION` keyword to select columns from different tables

  ```sql
  -- number of columns selected must be the same in each SELECT statement
  -- data types should also be the same
  SELECT first_name
  FROM employee
  UNION
  SELECT branch_name
  FROM branch;
  ```

### 3.4 Joins

- Use to combine rows from 2 or more tables where they have a related column between them
- As well as the 3 main joins below available in MySQL, there is also:
  - Full Outer Join: Same data if you were to combine left join and right join
  - Self Join: When you join a table with itself (useful for comparing within a table)
  - Cross Join: Combine every row of the first table with every row of the second table

#### Inner Join

- Combining the intersection between the tables based on the condition when it matches

```sql
-- Join together employee and branch with the common mgr_id and emp_id columns
-- Then select emp_id, first_name and branch_name from the resulting table
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee JOIN branch ON employee.emp_id = branch.mgr_id;
```

#### Left Join

- Items from an inner join and all other rows from the selected table (left table)

```sql
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
LEFT JOIN branch
ON employee.emp_id = branch.mgr_id;
```

#### Right Join

- Items from an inner join and all other rows from the joining table (right table)

```sql
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
RIGHT JOIN branch
ON employee.emp_id = branch.mgr_id;
```

### 3.5 Nested Queries

- Queries based on the resulting table of another query

```sql
-- find names of all employees who have sold over 30,000 to a single client
SELECT employee.first_name, employee.last_name
FROM employee
WHERE employee.emp_id IN (
  SELECT works_with.emp_id
  FROM works_with
  WHERE works_with.total_sales > 30000;
);

-- find all clients who are handled by the branch that Michael Scott manages
SELECT client.client_name
FROM client
WHERE client.branch_id = (
  SELECT branch.branch_id
  FROM branch
  WHERE branch.mgr_id = 102
);
```

## 4. Advanced Topics

### 4.1 Handling Deleted Data

#### `ON DELETE SET NULL`

##### Scenario:

- You delete an employee from the employee table (e.g Michael Scott, a branch manager)
- The branch in the branch table still has employee.emp_id as foreign key (branch.mgr_id)

##### Appropriate Solution:

- Use `ON DELETE SET NULL` (soft delete)
- Contextually, he branch will still exist but it will no longer have an associated manager (set to NULL)
- Also, the manager id is **only** a foreign key so it is not essential and can be set to NULL

```sql
-- branch table creation code
CREATE TABLE branch (
  branch_id INT PRIMARY KEY,
  branch_name VARCHAR(40),
  mgr_id INT,
  mgr_start_date DATE
  -- On delete clause said that if employee.emp_id gets deleted, branch.mgr_id (foreign key) is set to NULL
  FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);
```

#### `ON DELETE CASCADE`

##### Scenario:

- You delete a branch from the branch table
- Branch suppliers in the branch_supplier table still have the branch.branch_id as the foreign key (branch_supplier.branch_id)
- Aso, the branch_supplier.branch_id is a foreign key **and** part of the primary key so it is crucial and cannot be NULL (thus whole row gets deleted )

#### Appropriate Solution:

- Contextually, the company will no longer need the suppliers (rows deleted)

```sql
CREATE TABLE branch_supplier (
  branch_id INT,
  supplier_name VARCHAR(40),
  supply_type VARCHAR(40),
  PRIMARY KEY(branch_id, supplier_name),
  -- On delete clauses says that if branch.branch_id gets deleted, branch.supplier_id rows are deleted where they match (cascade)
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);
```

### 4.2 Triggers

- Used to run something when a particular kind of SQL command gets executed (INSERT, UPDATE, DELETE)

  ```sql
  -- have to execute first to change delimiter
  DELIMITER $$

  -- create the rigger
  CREATE TRIGGER my_trigger
  BEFORE INSERT -- can use BEFORE or AFTER to control when it executes
  ON employee
  FOR EACH ROW BEGIN
    INSERT INTO trigger_test VALUES("added new employee");
  END$$

  -- change the delimiter back
  DELIMITER ;
  ```

- Dropping triggers:

  ```sql
  DROP TRIGGER my_trigger;
  ```
