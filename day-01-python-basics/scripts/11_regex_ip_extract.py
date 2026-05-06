# Day 1 - Python Basics
# Topic: Regex IP Extraction

import re

log = "Connection failed from 192.168.1.20 at port 8080"

match = re.search(r"\d+\.\d+\.\d+\.\d+", log)

print(match.group())