# Day 6 - Conditional Handling in Python

## Overview

Day 6 focused on Conditional Handling in Python.

Conditional statements allow programs to make decisions based on conditions.

This is one of the most important concepts in:
- DevOps automation
- monitoring systems
- CI/CD pipelines
- cloud infrastructure management
- deployment validation
- Kubernetes scaling systems

Without conditional handling:
automation systems cannot react intelligently to changing conditions.

---

# Why Conditional Handling is Important

Real-world infrastructure constantly changes.

Examples:
- CPU usage increases
- disk space becomes low
- deployments fail
- services stop running
- instance types vary

Automation systems must evaluate these situations and respond correctly.

Conditional statements make this possible.

---

# Topics Covered

## 1. if Statement

Used to execute code only when a condition is True.

### Example

```python
if cpu > 80:
    print("Critical CPU Usage")
```

### Real DevOps Use Cases

- CPU monitoring
- memory monitoring
- service validation
- infrastructure alerts

---

## 2. else Statement

Provides fallback logic when condition is False.

### Example

```python
if cpu > 80:
    print("Critical CPU Usage")

else:
    print("System Healthy")
```

### Real DevOps Use Cases

- healthy system reporting
- deployment success handling
- backup conditions

---

## 3. elif Statement

Used for handling multiple conditions.

### Example

```python
if cpu > 90:
    print("Critical")

elif cpu > 70:
    print("Warning")

else:
    print("Healthy")
```

### Real DevOps Use Cases

- alert severity classification
- infrastructure scaling decisions
- cloud pricing logic

---

# Importance of Indentation

Python uses indentation to define code blocks.

Incorrect indentation causes errors.

### Correct Example

```python
if cpu > 80:
    print("Critical Alert")
```

### Incorrect Example

```python
if cpu > 80:
print("Critical Alert")
```

---

# Real DevOps Example

```python
cpu = 92

if cpu > 90:
    print("Critical Alert")

elif cpu > 70:
    print("Warning Alert")

else:
    print("Healthy System")
```

This logic is conceptually similar to:
- CloudWatch alarms
- Prometheus monitoring
- Kubernetes autoscaling
- CI/CD validation systems

---

# Files Included

## scripts/

Contains practical DevOps-style condition handling examples.

## notes/

Contains detailed explanations and concepts.

## outputs/

Contains execution outputs.

---

# Key Takeaways

Conditional handling allows:
- intelligent automation
- infrastructure validation
- monitoring systems
- scaling decisions
- deployment verification

This is one of the core foundations of DevOps automation engineering.

---

# Next Learning Goals

- Lists
- Dictionaries
- Tuples
- Sets
- File Handling
- JSON

---

# Author

Krishna Kala

Python for DevOps Learning Repository