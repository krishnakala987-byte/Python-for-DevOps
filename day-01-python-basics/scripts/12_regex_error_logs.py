# Day 1 - Python Basics
# Topic: Regex Error Logs

import re

logs = """
INFO Started
ERROR Database Failed
INFO Running
ERROR Disk Full
"""

matches = re.findall(r"ERROR.*", logs)

print(matches)