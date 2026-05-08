# requirements.txt Notes

## What is requirements.txt?

A dependency file containing project packages and versions.

Example:

```text
boto3==1.28.57
requests==2.33.1
```

---

## Generate requirements.txt

```bash
pip freeze > requirements.txt
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Why requirements.txt is Important

It helps:
- recreate environments
- maintain consistency
- support teamwork

---

## DevOps Use Cases

- CI/CD pipelines
- Docker containers
- deployment automation
- infrastructure consistency