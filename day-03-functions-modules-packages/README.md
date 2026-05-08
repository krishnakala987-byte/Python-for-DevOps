# Day 3 - Functions, Modules, Packages & Virtual Environments

## Overview

Day 3 focused on writing reusable, modular, and professional Python code used in real-world DevOps engineering.

This day covered:
- Functions
- Parameters
- Return keyword
- Modules
- Packages
- pip
- PyPI
- Virtual Environments
- requirements.txt

The goal was to understand how professional engineers structure Python projects for scalability, maintainability, and dependency management.

---

# Topics Covered

## 1. Functions

Functions are reusable blocks of code.

Example:

```python
def greet(name):
    print(f"Hello {name}")
```

### Key Learning

Functions improve:
- readability
- debugging
- reusability
- maintainability

---

## 2. Parameters and Arguments

Parameters receive input dynamically.

Example:

```python
def add(a, b):
    return a + b
```

---

## 3. Return Keyword

The return keyword sends output back from a function.

Example:

```python
def multiply(a, b):
    return a * b
```

### Importance

Return values are heavily used in:
- AWS SDK responses
- API automation
- monitoring systems
- deployment pipelines

---

## 4. Modules

Modules are Python files containing reusable functions.

Example:

```python
import calculator
```

### Key Learning

Modules help avoid code duplication.

---

## 5. Packages

Packages are collections of modules.

Example structure:

```text
cloud_tools/
│
├── aws.py
├── kubernetes.py
```

---

## 6. pip and PyPI

### pip

Python package installer.

Example:

```bash
pip install requests
```

### PyPI

Python Package Index repository.

---

## 7. Virtual Environments

Created isolated Python workspaces using:

```bash
python -m venv myenv
```

Activated using:

```bash
source myenv/bin/activate
```

### Importance

Virtual environments prevent dependency conflicts between projects.

---

## 8. requirements.txt

Saved dependencies using:

```bash
pip freeze > requirements.txt
```

Installed dependencies using:

```bash
pip install -r requirements.txt
```

### Key Learning

requirements.txt helps teams recreate identical environments.

---

# Real DevOps Use Cases

These concepts are heavily used in:
- AWS automation
- CI/CD pipelines
- Infrastructure scripting
- Kubernetes tooling
- API integrations
- Internal DevOps platforms

---

# Files Included

## scripts/

Contains reusable Python modules and examples.

## notes/

Contains detailed theory notes.

## outputs/

Contains execution outputs of scripts.

---

# Tools Used

- Python 3
- VS Code
- Git
- GitHub
- pip
- virtualenv

---

# Key Takeaways

Day 3 introduced professional Python engineering practices used in DevOps.

Main focus areas:
- reusable code
- modular programming
- dependency management
- isolated environments
- scalable automation

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