# else Statement Notes

## What is else?

The else block runs when if condition is False.

---

## Syntax

```python
if condition:
    code

else:
    fallback_code
```

---

## Example

```python
cpu = 40

if cpu > 80:
    print("Critical")

else:
    print("Healthy")
```

---

## DevOps Use Cases

- healthy status reporting
- fallback automation
- deployment verification