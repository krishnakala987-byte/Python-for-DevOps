# Regex Basics

Regex is used for pattern matching.

Python uses the re module for regex operations.

## Import Regex Module

```python
import re
```

## Find Numbers

```python
\d+
```

## Find IP Address

```python
\d+\.\d+\.\d+\.\d+
```

## Find Error Logs

```python
ERROR.*
```

## Example

```python
import re

text = "CPU usage is 85 percent"

match = re.search(r"\d+", text)

print(match.group())
```

Output:

```text
85
```