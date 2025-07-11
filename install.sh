#!/bin/bash

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not found. Please install Python 3 and try again."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
if (( $(echo "$PYTHON_VERSION < 3.8" | bc -l) )); then
    echo "Python 3.8 or higher is required. Found version $PYTHON_VERSION"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install package in development mode
echo "Installing ENOUGH..."
pip install -e .

# Create default directories
mkdir -p templates/{nathaniel_branden_method,custom,starting_strength}
mkdir -p submissions/{nathaniel_branden_method,custom,starting_strength}
mkdir -p main/progress

echo "Installation complete!"
echo "Run 'enough start' to begin." 