# Exception Handling in Python

## What is Exception Handling?

Exception handling prevents programs from crashing.

Professional scripts should:
- survive failures
- continue execution
- show meaningful errors

---

# try and except

```python
try:
    risky_code()

except:
    handle_error()
```

---

# Example

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# FileNotFoundError

```python
try:
    open("missing.txt")

except FileNotFoundError:
    print("File does not exist")
```

---

# Generic Exceptions

```python
except Exception as error:
```

Meaning:
- catch unexpected errors
- store actual error inside variable

---

# Example

```python
try:
    print(10 / 0)

except Exception as error:
    print(error)
```

Output:

```text
division by zero
```

---

# Important Understanding

error is just a variable name.

These also work:

```python
except Exception as e:
```

```python
except Exception as problem:
```

---

# Professional Style

```python
try:
    risky_code()

except FileNotFoundError:
    print("File missing")

except PermissionError:
    print("Permission denied")

except Exception as error:
    print(f"Unexpected error: {error}")
```