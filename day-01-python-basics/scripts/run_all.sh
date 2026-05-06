#!/bin/bash

echo "Starting Python Automation Scripts"

for file in *.py
do
    echo ""
    echo "Running $file"


    python3 "$file"

    echo ""
done

echo "All scripts executed successfully"