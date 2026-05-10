# elif Statement Notes

## What is elif?

elif means "else if".

Used for multiple conditions.

---

## Syntax

```python
if condition1:
    code

elif condition2:
    code

else:
    code
```

---

## Example

```python
cpu = 85

if cpu > 90:
    print("Critical")

elif cpu > 70:
    print("Warning")

else:
    print("Healthy")
```

---

## DevOps Use Cases

- alert severity levels
- scaling logic
- cloud pricing systems