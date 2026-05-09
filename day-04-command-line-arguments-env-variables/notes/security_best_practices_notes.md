# Security Best Practices Notes

## Never Hardcode Secrets

Bad Practice:

```python
password = "admin123"
```

---

## Use Environment Variables

Good Practice:

```bash
export PASSWORD=admin123
```

---

## Why?

Hardcoded secrets may:
- leak on GitHub
- expose credentials
- create security risks

---

## DevOps Security Practices

Use:
- environment variables
- CI/CD secret managers
- cloud IAM roles
- vault systems