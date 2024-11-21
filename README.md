# PyQuest-24-Tute

This repository provides Python tutorial exercises covering various programming concepts. Each section contains questions designed to enhance understanding through practical tasks.

---

## **Contents**

### **Question 01: Operators**

#### a. Error Identification and Correction
- Identify and fix errors in the given code:
```python
a = 5
b = a ++ 2
print(b)
```

#### b. Datatype Determination
- Analyze the datatype of a variable:
```python
test = 10
print(type(test))
test = "testbook"
print(type(test))
```

---

### **Question 02: Arithmetic Operators**

#### a. Code Analysis and Output Prediction
Analyze the output of the following program:
```python
num = 4
print(num)            # Output1
print(num := 12)      # Output2
num += 5              
print(num)            # Output3
num //= 2             
print(num)            # Output4
print(7 + 16 % 8)     # Output5
print(num := num % 3) # Output6
```

#### b. Expression Evaluation
- Evaluate the output of the expression:
```python
1 + (3 - 4) * 2 ** 10 // 6
```

#### c. Floor Division
- Analyze the behavior of the floor division operator:
```python
x = 125
y = 13
x //= y
print(x)
```

#### d. Division vs. Floor Division
- Compare the outputs of division types:
```python
print(type(5 / 2))   # Division
print(type(5 // 2))  # Floor Division
```

#### e. Complete Minutes Calculation
Determine the correct statement to calculate complete minutes:
- `mm = ss // 60`
- `mm = ss / 60`
- `mm = ss % 60`
- `mm = ss * 60`

#### f. Variable Value Determination
Given the following statements, determine the values of variables `b` through `g`:
```python
a = 2 
b = a + 1 // 2 
c = a + 1.0 // 2 
d = (a + 1) // 2
e = (a + 1.0) // 2
f = a + 1 / 2 
g = (a + 1) / 2
```

---

### **Question 03: Arithmetic, Comparison & Logical Operators**

#### Analyze and Run
What is the output of the following code?
```python
x = 10
y = 50
print(x ** 2 >= 100 and y < 100)
```

---

### **Question 04: Control Structures**

#### Part 1: If Statements
- Check if a number is positive:
```python
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is a positive number")
print("A statement outside the if statement.")
```

- Write a program to print all prime numbers within a given range.

#### Part 2: If-Else Statements
- Display grades based on user input for percentage:

| Marks (%)  | Grade |
|------------|-------|
| 85-100     | A+    |
| 70-84      | A     |
| 65-69      | A-    |
| 60-64      | B+    |
| 55-59      | B     |
| 50-54      | B-    |
| 45-49      | C+    |
| 40-44      | C     |
| 35-39      | C-    |
| 30-34      | D+    |
| 25-29      | D     |
| Below 25   | E     |


#### Part 3: Elif Statements
- Compare two numbers:
```python
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num1 > num2:
    print("num1 is greater than num2")
elif num1 == num2:
    print("num1 is equal to num2")
else:
    print("num1 is less than num2")
```

- Find the smallest of three numbers using `if...else...elif`.

---

### **Question 05: Loops**

#### a. Loop Execution Count
How many times does the following loop execute?
```python
c = 0
while c < 20:
    c += 2
```

#### b. Loop Output
What is the output of the following loop?
```python
for l in 'Jhon':
    if l == 'o':
        pass
    print(l, end=", ")
```

#### c. Variable Value
Determine the value of `var` after execution:
```python
var = 10
for i in range(10):
    for j in range(2, 10):
        if var % 2 == 0:
            continue
        var += 1
    var += 1
else:
    var += 1
print(var)
```

#### d. Pattern Printing
Write a program to print the following pattern:
```
55555
4444
333
22
1
```

#### e. Convert While Loop to For Loop
Convert this:
```python
x = 4
while x <= 8:
    print(x * 10)
    x += 2
```

#### f. Fibonacci Sequence
Generate the Fibonacci sequence up to 10 terms.

#### g. Reverse an Integer
Write a program to reverse an integer (e.g., `76542 → 24567`).

---

### **Question 06: Lists**

Perform the following tasks:
1. Create a list: `[18, 26, 52, 15, 10]`.
2. Add items: Append `30`, `40`, and `60`.
3. Modify the list: Change `30` to `70`.
4. Remove an item: Remove `60`.
5. Calculate the sum of all elements.
6. Find the average.
7. Identify maximum and minimum values.
8. Sort the list in ascending and descending order.

---

### **Question 07: Sets**

#### Part 1
1. Create a set with six fruits.
2. Add a fruit to the set.
3. Remove a fruit.
4. Check if a fruit exists in the set.

#### Part 2
Write a program to create a set of all even numbers between 1 and 30.

---

### **Question 08: Dictionaries**

Given a dictionary of student grades:
```python
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 88, 'Evan': 95}
```
1. Find the student with the highest grade.
2. Calculate the average grade.
3. List all students who scored above 80.

- Submit the document in PDF format.
