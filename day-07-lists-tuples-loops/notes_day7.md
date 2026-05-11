# Day 7 Notes - Python for DevOps

# Lists, Tuples and Loops in Python

This module focused on understanding collections and loops in Python which are heavily used in DevOps automation.

These concepts are important for:

- AWS Automation
- Kubernetes Automation
- Infrastructure Management
- Monitoring Systems
- CI/CD Pipelines
- Cloud Automation

---

# 1. Lists in Python

## Definition

Lists are sequence data types used to store multiple values in a single variable.

Lists are:

- Mutable
- Ordered
- Dynamic
- Flexible

Lists are created using square brackets `[]`.

---

# List Example

```python
servers = ["web-server", "db-server", "cache-server"]
```

---

# Why Lists Matter in DevOps

DevOps engineers work with collections of resources:

- EC2 Instances
- Kubernetes Pods
- Docker Containers
- S3 Buckets
- Servers
- Logs

Lists help automate operations on these resources efficiently.

---

# Accessing List Elements

Python uses indexing to access list elements.

Indexing starts from 0.

| Element | Index |
|---|---|
| web-server | 0 |
| db-server | 1 |
| cache-server | 2 |

---

# Example

```python
servers = ["web-server", "db-server", "cache-server"]

print(servers[0])
print(servers[1])
```

Output:

```python
web-server
db-server
```

---

# Negative Indexing

Python also supports negative indexing.

| Element | Negative Index |
|---|---|
| cache-server | -1 |
| db-server | -2 |
| web-server | -3 |

---

# Example

```python
print(servers[-1])
```

Output:

```python
cache-server
```

---

# Why Indexing Starts at 0

Python follows memory-offset based indexing from low-level programming concepts.

The first element is located:

- 0 positions away from the starting memory location

Therefore indexing starts from 0.

---

# List Operations

## append()

Used to add elements to a list.

Example:

```python
servers.append("backup-server")
```

---

## remove()

Used to remove elements from a list.

Example:

```python
servers.remove("cache-server")
```

---

## len()

Used to count total elements.

Example:

```python
print(len(servers))
```

---

# List Slicing

Slicing is used to extract portions of a list.

## Syntax

```python
list[start:end]
```

Important:

- Start index included
- End index excluded

---

# Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])
```

Output:

```python
[10, 20, 30]
```

---

# More Slicing Examples

## First Two Elements

```python
print(numbers[:2])
```

Output:

```python
[10, 20]
```

---

## Last Two Elements

```python
print(numbers[-2:])
```

Output:

```python
[40, 50]
```

---

# Sorting Lists

## sort()

Used to sort lists.

Example:

```python
numbers = [5, 1, 9, 3]

numbers.sort()

print(numbers)
```

Output:

```python
[1, 3, 5, 9]
```

---

# Descending Sorting

```python
numbers.sort(reverse=True)
```

---

# 2. Tuples in Python

## Definition

Tuples are sequence data types similar to lists.

Difference:

- Lists are mutable
- Tuples are immutable

Tuples use parentheses `()`.

---

# Tuple Example

```python
regions = ("us-east-1", "ap-south-1", "eu-west-1")
```

---

# Why Tuples Matter in DevOps

Tuples are useful for fixed configurations such as:

- AWS Regions
- Port Numbers
- Constant Values
- Secure Configurations

---

# Tuple Access Example

```python
print(regions[0])
```

Output:

```python
us-east-1
```

---

# Tuple Limitation

Tuples cannot be modified.

Example:

```python
regions.append("eu-west-1")
```

This produces an error.

---

# List vs Tuple

| Feature | List | Tuple |
|---|---|---|
| Mutable | Yes | No |
| Syntax | [] | () |
| Faster | No | Yes |
| Dynamic Data | Yes | No |
| Fixed Data | No | Yes |

---

# 3. Loops in Python

## Definition

Loops are used to perform repetitive tasks automatically.

Instead of writing the same code multiple times, loops repeat operations efficiently.

Loops are heavily used in automation engineering.

---

# Why Loops Matter in DevOps

DevOps engineers automate repetitive operations such as:

- Server Monitoring
- Deployments
- Infrastructure Checks
- Log Analysis
- Backup Operations
- Kubernetes Monitoring

---

# Types of Loops

| Loop Type | Use Case |
|---|---|
| for loop | Known iterations |
| while loop | Condition-based iterations |

---

# 4. For Loops

## Definition

For loops are used when the number of iterations is known.

---

# Syntax

```python
for variable in collection:
    code
```

---

# Example

```python
services = ["EC2", "S3", "Lambda"]

for service in services:
    print(service)
```

Output:

```python
EC2
S3
Lambda
```

---

# DevOps Example

```python
instances = ["i-123", "i-456", "i-789"]

for instance in instances:
    print("Stopping instance:", instance)
```

---

# 5. range() Function

The `range()` function generates sequences of numbers.

---

# Example

```python
for i in range(5):
    print(i)
```

Output:

```python
0
1
2
3
4
```

---

# range(start, stop)

```python
for i in range(1, 6):
    print(i)
```

Output:

```python
1
2
3
4
5
```

---

# range(start, stop, step)

```python
for i in range(0, 10, 2):
    print(i)
```

Output:

```python
0
2
4
6
8
```

---

# 6. While Loops

## Definition

While loops are used when iterations depend on conditions.

The loop continues until the condition becomes False.

---

# Syntax

```python
while condition:
    code
```

---

# Example

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

Output:

```python
1
2
3
4
5
```

---

# Infinite Loops

Example:

```python
while True:
    print("Running")
```

This loop never stops.

Infinite loops are dangerous in production systems.

---

# DevOps Example

```python
deployment_ready = False

while deployment_ready == False:
    print("Waiting for deployment...")
```

---

# 7. break Statement

The `break` statement immediately terminates the loop.

---

# Example

```python
for number in range(1, 11):

    if number == 7:
        break

    print(number)
```

Output:

```python
1
2
3
4
5
6
```

---

# DevOps Use Case

Stop deployment if critical failure occurs.

---

# 8. continue Statement

The `continue` statement skips the current iteration only.

---

# Example

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)
```

Output:

```python
1
2
4
5
```

---

# Difference Between break and continue

| Statement | Action |
|---|---|
| break | Stops entire loop |
| continue | Skips current iteration |

---

# Practical Mini Project

# Server Health Checker

```python
servers = ["web-server", "db-server", "cache-server"]

print("Starting Health Check...\n")

for server in servers:
    print("Checking server:", server)

print("\nTotal Servers:", len(servers))
```

Output:

```python
Starting Health Check...

Checking server: web-server
Checking server: db-server
Checking server: cache-server

Total Servers: 3
```

---

# Key Takeaways

- Lists are mutable collections.
- Tuples are immutable collections.
- Indexing starts from 0.
- Slicing extracts portions of lists.
- Loops automate repetitive tasks.
- range() generates sequences.
- while loops depend on conditions.
- break stops loops completely.
- continue skips specific iterations.

---

# Industry-Level Understanding

A beginner sees:

```python
for server in servers:
```

A DevOps engineer sees:

"Automation of thousands of infrastructure resources."

---

# Final Conclusion

Understanding:

- Lists
- Tuples
- Indexing
- Slicing
- Loops
- break
- continue

is extremely important before moving toward:

- AWS Automation
- Boto3
- Kubernetes Scripting
- CI/CD Pipelines
- API Automation
- Infrastructure as Code

These concepts form the foundation of real-world DevOps automation engineering.