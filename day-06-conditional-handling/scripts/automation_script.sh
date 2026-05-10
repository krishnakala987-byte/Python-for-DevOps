#!/bin/bash

echo "Running Python Conditional Handling Scripts"
echo "==========================================="

echo "Executing basic_if_demo.py"
python3 basic_if_demo.py
echo "--------------------------------"

echo "Executing if_else_demo.py"
python3 if_else_demo.py
echo "--------------------------------"

echo "Executing elif_demo.py"
python3 elif_demo.py
echo "--------------------------------"

echo "Executing cpu_monitor.py"
python3 cpu_monitor.py 85
echo "--------------------------------"

echo "Executing disk_monitor.py"
python3 disk_monitor.py 95
echo "--------------------------------"

echo "Executing deployment_validator.py"
python3 deployment_validator.py failed
echo "--------------------------------"

echo "Executing ec2_instance_checker.py"
python3 ec2_instance_checker.py t2.medium
echo "--------------------------------"

echo "Executing server_health_checker.py"
python3 server_health_checker.py 85 90
echo "--------------------------------"