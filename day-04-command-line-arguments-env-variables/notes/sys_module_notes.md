# sys Module Notes

## What is sys Module?

Built-in Python module for system interaction.

---

## Common Usage

```python
import sys
```

---

## sys.argv

Stores command line arguments.

Example:

```python
python app.py hello
```

Results:

```python
['app.py', 'hello']
```

---

## Important Concepts

- sys.argv is a list
- index 0 stores script name
- remaining indexes store user inputs