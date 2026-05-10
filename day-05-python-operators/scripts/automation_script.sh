#!/bin/bash

echo "Running Python Operator Scripts"
echo "================================"

echo "Executing arithmetic_demo.py"
python3 arithmetic_demo.py
echo "-----------------------------"

echo "Executing assignment_demo.py"
python3 assignment_demo.py
echo "-----------------------------"

echo "Executing relational_demo.py"
python3 relational_demo.py
echo "-----------------------------"

echo "Executing logical_demo.py"
python3 logical_demo.py
echo "-----------------------------"

echo "Executing identity_demo.py"
python3 identity_demo.py
echo "-----------------------------"

echo "Executing cpu_monitor.py"
python3 cpu_monitor.py 90
echo "-----------------------------"

echo "Executing auto_scaler.py"
python3 auto_scaler.py 85
echo "-----------------------------"

echo "Executing deployment_checker.py"
python3 deployment_checker.py failed
echo "-----------------------------"

echo "Executing server_classifier.py"
python3 server_classifier.py 4
echo "-----------------------------"