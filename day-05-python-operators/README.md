# Day 5 - Python Operators for DevOps

## Overview

Day 5 focused on understanding Python Operators and their real-world DevOps applications.

Operators are fundamental building blocks used in:
- monitoring systems
- CI/CD pipelines
- cloud automation
- infrastructure management
- Kubernetes scaling
- deployment logic

This day introduced:
- Arithmetic Operators
- Assignment Operators
- Relational Operators
- Logical Operators
- Identity Operators

The goal was not just learning syntax, but understanding how operators drive decision-making in production systems.

---

# Why Operators are Important in DevOps

DevOps automation constantly makes decisions based on conditions.

Examples:
- CPU > 80
- memory < 20
- deployment_status == success
- pod_count >= 3
- server_id % 2 == 0

Without operators:
- automation cannot make decisions
- monitoring systems cannot trigger alerts
- pipelines cannot validate deployments

Operators are heavily used in:
- Kubernetes autoscaling
- AWS monitoring
- CI/CD validation
- infrastructure health checks
- deployment rollback systems

---

# Topics Covered

## 1. Arithmetic Operators

Used for mathematical operations.

### Operators Covered

| Operator | Purpose |
|---|---|
| + | addition |
| - | subtraction |
| * | multiplication |
| / | division |
| // | floor division |
| % | modulus |

### Example

```python
total_cost = servers * cost_per_server
```

### Real DevOps Use Cases

- resource calculations
- cost estimation
- scaling computations
- storage calculations

---

## 2. Assignment Operators

Used to assign and update variable values.

### Operators Covered

| Operator | Meaning |
|---|---|
| = | assign value |
| += | add and assign |
| -= | subtract and assign |

### Example

```python
deployment_count += 1
```

### Real DevOps Use Cases

- deployment counters
- scaling updates
- monitoring statistics

---

## 3. Relational Operators

Used for comparisons.

### Operators Covered

| Operator | Purpose |
|---|---|
| > | greater than |
| < | less than |
| >= | greater than equal |
| <= | less than equal |
| == | equal comparison |
| != | not equal |

### Example

```python
if cpu > 80:
    print("Critical Alert")
```

### Real DevOps Use Cases

- alert systems
- threshold monitoring
- deployment validation
- scaling triggers

---

## 4. Logical Operators

Used to combine multiple conditions.

### Operators Covered

| Operator | Purpose |
|---|---|
| and | both conditions true |
| or | one condition true |
| not | reverse boolean |

### Example

```python
if cpu > 80 and memory > 80:
    print("Critical Infrastructure Alert")
```

### Real DevOps Use Cases

- infrastructure validation
- multi-condition monitoring
- CI/CD decision logic

---

## 5. Identity Operators

Used to check object identity.

### Operators Covered

| Operator | Purpose |
|---|---|
| is | same object |
| is not | different object |

### Example

```python
a is b
```

### Real DevOps Use Cases

- configuration comparisons
- object validation
- deployment state checks

---

# Difference Between = and ==

This is one of the most important beginner concepts.

| Symbol | Meaning |
|---|---|
| = | assignment |
| == | comparison |

### Assignment Example

```python
cpu = 80
```

### Comparison Example

```python
if cpu == 80:
```

---

# Difference Between == and is

| Operator | Purpose |
|---|---|
| == | compares values |
| is | compares memory objects |

### Example

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```

---

# Real DevOps Example

```python
cpu = 90
memory = 85
deployment_status = "success"

if cpu > 80 and memory > 80 and deployment_status == "success":
    print("Scale Infrastructure")
```

This demonstrates:
- relational operators
- logical operators
- automation decision-making

---

# Files Included

## scripts/

Contains practical DevOps-style automation examples.

## notes/

Contains detailed operator explanations and concepts.

## outputs/

Contains script execution outputs.

---

# Key Takeaways

Day 5 introduced the foundations of automation decision-making.

Operators are heavily used in:
- monitoring systems
- cloud automation
- CI/CD pipelines
- Kubernetes autoscaling
- deployment systems

Understanding operators deeply is essential for becoming a strong DevOps engineer.

---

# Next Learning Goals

- Lists
- Dictionaries
- Tuples
- Sets
- File Handling
- JSON
- APIs

---

# Author

Krishna Kala

Python for DevOps Learning Repository