# Function Execution Flow in Python

## Biggest Beginner Confusion

Many beginners think:

```python
def my_function():
```

runs the code.

This is wrong.

---

# Correct Understanding

def only STORES function.

Function runs ONLY when called.

---

# Example

```python
def hello():
    print("Hello")


hello()
```

---

# Execution Flow

1. Python stores function
2. hello() called
3. Python executes function body

---

# Important Rule

Python executes code:
TOP → BOTTOM

---

# Function Call Flow

```python
def father():

    son()


def son():

    print("Son running")


father()
```

---

# Flow

1. store father
2. store son
3. father() called
4. enter father
5. son() reached
6. enter son
7. son ends
8. return to father

---

# return Keyword

return immediately exits function.

---

# Example

```python
def test():

    print("A")

    return

    print("B")
```

Output:

```text
A
```

---

# Main Function

Professional Python programs often use:

```python
def main():
```

main becomes:
- program entry point
- control center