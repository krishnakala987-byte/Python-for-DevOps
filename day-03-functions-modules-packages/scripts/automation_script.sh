#!/bin/bash

echo "Running Python Scripts"
echo "======================"

for file in *.py
do
    echo "Executing $file"

    python3 "$file"

    echo "----------------------"
done