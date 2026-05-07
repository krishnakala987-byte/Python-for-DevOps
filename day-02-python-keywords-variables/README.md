# Day 2 - Python Keywords, Variables & Automation Basics

## Overview

Day 2 focused on understanding the core building blocks of Python used in DevOps automation.

This day covered:
- Python keywords
- Variables
- Variable scoping
- Naming conventions
- Functions
- Loops
- Error handling
- Automation scripting concepts

The goal was to build a strong foundation for writing clean, reusable, and scalable automation scripts used in real-world DevOps environments.

---

# Topics Covered

## 1. Python Keywords

Learned commonly used Python keywords such as:

- if
- else
- elif
- for
- while
- def
- try
- except
- return
- import

Example:

```python
if cpu_usage > 80:
    print("High CPU usage")
```

---

## 2. Variables

Learned how variables store dynamic data instead of hardcoding values.

Example:

```python
server_name = "web1"
```

Variables make automation reusable and maintainable.

---

## 3. Variable Scope

### Global Variables

```python
company = "DevOps"
```

### Local Variables

```python
def test():
    message = "Hello"
```

---

## 4. Naming Conventions

### Snake Case

```python
ec2_instance_name
```

Best practices:
- use lowercase
- use descriptive names
- avoid unclear names

---

## 5. Functions

```python
def restart_server(server_name):
    print(f"Restarting {server_name}")
```

Functions help reduce repetition and improve maintainability.

---

## 6. Loops

```python
for server in servers:
    print(server)
```

Loops automate repetitive infrastructure tasks.

---

## 7. Error Handling

```python
try:
    print("Restarting")
except:
    print("Failed")
```

Error handling prevents scripts from crashing unexpectedly.

---

# Mini Automation Project

## Restart Multiple Servers Script

```python
servers = ["web1", "web2", "web3"]

def restart_server(server_name):

    try:
        print(f"Restarting {server_name}")
        print("Restart successful")

    except:
        print("Restart failed")

for server in servers:
    restart_server(server)
```

---

# Output

```text
Restarting web1
Restart successful

Restarting web2
Restart successful

Restarting web3
Restart successful
```

---

# Important DevOps Concepts Learned

- Dynamic scripting
- Reusable functions
- Automation mindset
- Loop-based infrastructure handling
- Error-safe execution
- Clean code practices

---

# Real DevOps Use Cases

- AWS automation
- EC2 management
- Kubernetes scripting
- CI/CD pipelines
- Monitoring systems
- Infrastructure automation

---

# Files Included

## scripts/
Contains all Python practice programs and automation examples.

## notes/
Contains theory notes and concept explanations.

## outputs/
Contains execution outputs of Python scripts.

---

# Tools Used

- Python 3
- VS Code
- Git
- GitHub
- Windows Terminal

---

# Key Takeaways

Day 2 helped build a strong understanding of how Python is used in automation and DevOps engineering.

Main focus areas:
- writing clean code
- avoiding hardcoding
- using reusable functions
- automating repetitive tasks
- handling errors professionally

---

# Next Learning Goals

- Lists and Dictionaries
- File Handling
- Modules
- JSON Handling
- API Automation
- AWS Automation using Python

---

# Author

Krishna Kala

Learning Python for DevOps Engineering 