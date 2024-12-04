#!/bin/bash

# Create directories
mkdir -p 2024/Codes 2024/Inputs

# Create 25 python files and input files
for N in $(seq 3 25); do
    # Create Python file in Codes directory
    PYTHON_FILE="2024/Codes/Day$N.py"
    echo -e 'DEMO_PATH = "../Inputs/demo_input'$N'.txt"\nINPUT_PATH = "../Inputs/input'$N'.txt"' > $PYTHON_FILE

    # Create corresponding input files in Inputs directory
    touch 2024/Inputs/demo_input$N.txt
    touch 2024/Inputs/input$N.txt
done

echo "Directories and files have been created."
