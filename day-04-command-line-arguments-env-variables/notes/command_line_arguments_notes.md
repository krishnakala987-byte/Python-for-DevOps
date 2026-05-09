# Command Line Arguments Notes

## What are Command Line Arguments?

Inputs passed from terminal to Python programs.

Example:

```bash
python app.py Krishna
```

---

## Accessing Arguments

Using:

```python
import sys

print(sys.argv)
```

---

## sys.argv

sys.argv stores arguments as a list.

Example:

```python
['app.py', 'Krishna']
```

---

## Important Concept

Arguments are stored as strings by default.

Use:
- int()
- float()

for calculations.

---

## DevOps Use Cases

- deployment environments
- server names
- ports
- file paths
- regions