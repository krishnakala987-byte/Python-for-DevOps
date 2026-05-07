# notes/error_handling_notes.md

# Python Error Handling Notes

## What is Error Handling?

Error handling prevents programs from crashing unexpectedly.

---

## try-except Example

```python
try:
    number = int("hello")
except:
    print("Conversion failed")
```

---

## Why Important in DevOps

Production systems can fail because of:
- network issues
- API failures
- server downtime
- invalid inputs

---

## Benefits

- safer automation
- stable scripts
- better debugging
- production-ready code