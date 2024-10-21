#!/bin/bash

if ! command -v python3 &> /dev/null
then
    echo "Python is not installed. Installing Python..."
    sudo apt-get update
    sudo apt-get install python3 python3-venv python3-pip -y
else
    echo "Python is already installed."
fi

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing pygame..."
pip install pygame

echo "Running the Python program..."
python3 runprogram.py  

deactivate
