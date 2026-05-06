# Day 1 - Python Basics
# Topic: Regex Date Extraction

import re

log = "2026-05-06 ERROR Server Down"

match = re.search(r"\d{4}-\d{2}-\d{2}", log)

print(match.group())
