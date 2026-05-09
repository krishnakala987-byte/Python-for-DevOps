# Environment Variables Notes

## What are Environment Variables?

Variables stored in operating system environment.

Used for:
- passwords
- API keys
- tokens
- certificates

---

## Creating Environment Variables

```bash
export PASSWORD=admin123
```

---

## Accessing Variables in Python

```python
import os

password = os.getenv("PASSWORD")
```

---

## Why Environment Variables are Important

They improve:
- security
- portability
- configuration management

---

## DevOps Use Cases

- AWS credentials
- Kubernetes secrets
- CI/CD secrets
- database passwords