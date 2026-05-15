# File Handling in Python

## What is File Handling?

File handling means:
reading, writing, appending, and managing files using Python.

Python automation scripts often work with:
- logs
- reports
- configs
- backups
- monitoring outputs

---

# Opening Files

## Syntax

```python
open("filename", "mode")
```

---

# Common Modes

| Mode | Meaning |
|------|----------|
| r | Read |
| w | Write |
| a | Append |
| x | Create new file |
| rb | Read binary |
| wb | Write binary |

---

# Reading Files

```python
file = open("test.txt", "r")

content = file.read()

print(content)

file.close()
```

---

# Writing Files

```python
file = open("output.txt", "w")

file.write("Hello DevOps")

file.close()
```

---

# Appending Files

```python
file = open("logs.txt", "a")

file.write("New log entry\n")

file.close()
```

---

# Best Practice

```python
with open("file.txt", "r") as file:
```

Files close automatically.

---

# Real DevOps Usage

- reading logs
- generating reports
- deployment monitoring
- backup reports
- server automation