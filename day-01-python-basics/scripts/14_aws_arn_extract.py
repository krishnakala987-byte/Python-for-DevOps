# Day 1 - Python Basics
# Topic: AWS ARN Username Extraction

import re

arn = "arn:aws:iam::123456789:user/krishna"

match = re.search(r"/\w+", arn)

print(match.group()[1:])