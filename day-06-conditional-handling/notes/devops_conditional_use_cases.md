# DevOps Conditional Use Cases

## CPU Monitoring

```python
if cpu > 80:
    print("Critical CPU Usage")
```

---

## Disk Monitoring

```python
if disk_usage > 90:
    print("Disk Almost Full")
```

---

## Deployment Validation

```python
if deployment_status != "success":
    print("Rollback Deployment")
```

---

## Infrastructure Scaling

```python
if cpu > 80:
    print("Scale Up")
```

---

## EC2 Instance Validation

```python
if instance_type == "t2.micro":
    print("Low Cost Instance")
```