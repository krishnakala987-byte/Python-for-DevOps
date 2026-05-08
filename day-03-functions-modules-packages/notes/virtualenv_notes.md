# Virtual Environment Notes

## What is a Virtual Environment?

A virtual environment is an isolated Python workspace.

---

## Create Virtual Environment

```bash
python -m venv myenv
```

---

## Activate Environment

### Linux / WSL

```bash
source myenv/bin/activate
```

---

## Install Packages

```bash
pip install boto3
```

---

## Deactivate Environment

```bash
deactivate
```

---

## Why Virtual Environments are Important

They:
- isolate dependencies
- prevent conflicts
- improve project management

---

## DevOps Use Cases

- multiple client projects
- CI/CD pipelines
- cloud automation
- isolated tooling