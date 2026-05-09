# Day 4 - Command Line Arguments & Environment Variables

## Overview

Day 4 focused on building dynamic and secure Python scripts using:
- Command Line Arguments
- Environment Variables

These concepts are heavily used in:
- DevOps automation
- AWS CLI tools
- Kubernetes tooling
- CI/CD pipelines
- Infrastructure automation

The goal was to avoid hardcoded values and build production-style scripts.

---

# Topics Covered

## 1. Command Line Arguments

Command line arguments allow users to pass input dynamically from the terminal.

Example:

```bash
python calculator_cli.py 10 add 5
```

### Key Learning

Arguments are accessed using:

```python
sys.argv
```

---

## 2. sys Module

The sys module provides access to:
- command line arguments
- Python interpreter information
- system-level functionality

Example:

```python
import sys
```

---

## 3. Type Conversion

Arguments are received as strings.

Converted using:

```python
int()
float()
```

Example:

```python
num1 = float(sys.argv[1])
```

---

## 4. Environment Variables

Environment Variables securely store sensitive information outside source code.

Example:

```bash
export PASSWORD=admin123
```

Accessed in Python using:

```python
os.getenv()
```

---

## 5. os Module

The os module interacts with operating system features.

Example:

```python
import os
```

---

## 6. Security Best Practices

Sensitive information should NEVER be:
- hardcoded
- pushed to GitHub
- passed directly in terminal arguments

Use:
- environment variables
- secret managers
- CI/CD secrets

---

# Real DevOps Use Cases

These concepts are used in:
- deployment automation
- cloud authentication
- AWS scripting
- CI/CD pipelines
- Kubernetes automation
- monitoring systems

---

# Files Included

## scripts/

Contains practical command line and environment variable examples.

## notes/

Contains theory and explanations.

## outputs/

Contains execution outputs.

---

# Tools Used

- Python 3
- VS Code
- Linux Terminal
- Git
- GitHub

---

# Key Takeaways

Day 4 introduced:
- dynamic scripting
- secure automation
- production-safe coding
- terminal-based interaction

These concepts are foundational for DevOps engineering.

---

# Next Learning Goals

- Lists
- Dictionaries
- JSON
- File Handling
- APIs
- AWS Automation

---

# Author

Krishna Kala

Learning Python for DevOps Engineering 