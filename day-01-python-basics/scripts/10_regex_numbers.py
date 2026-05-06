# Day 1 - Python Basics
# Topic: Regex Number Extraction

import re

text = "CPU usage is 85 percent"

match = re.search(r"\d+", text)

print(match.group())
