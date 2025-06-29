#!/bin/bash

# Define project path
PROJECT_DIR="$HOME/Documents/Automation/exchange_alert"

# Activate Python virtual environment
source "$PROJECT_DIR/venv/bin/activate"

# Navigate to project directory
cd "$PROJECT_DIR"

# Run Python script
python main.py
