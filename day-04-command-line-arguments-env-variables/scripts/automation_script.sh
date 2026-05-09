#!/bin/bash

echo "Running Python Scripts"
echo "======================"

echo "Executing argv_demo.py"
python3 argv_demo.py Krishna
echo "----------------------"

echo "Executing calculator_cli.py"
python3 calculator_cli.py 10 add 5
echo "----------------------"

echo "Executing server_monitor.py"
python3 server_monitor.py 90
echo "----------------------"

echo "Setting Environment Variables"
export USERNAME=krishna
export PASSWORD=admin123

echo "Executing environment_demo.py"
python3 environment_demo.py
echo "----------------------"

echo "Executing secure_login.py"
python3 secure_login.py
echo "----------------------"