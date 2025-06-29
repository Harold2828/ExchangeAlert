#!/bin/bash

# Define project path at the very beginning
PROJECT_DIR="$HOME/Documents/Automation/exchange_alert"

# Ensure the log file is created/appended to, even if the script fails early
echo "[INFO] Exchange Alert Runner started at $(date)" >> /tmp/exchangealert.log

# Check if the virtual environment exists before sourcing
if [ -f "$PROJECT_DIR/venv/bin/activate" ]; then
    echo "[INFO] Activating virtual environment..." >> /tmp/exchangealert.log
    source "$PROJECT_DIR/venv/bin/activate"
else
    echo "[ERROR] Virtual environment not found at $PROJECT_DIR/venv. Please create it." >> /tmp/exchangealert.log
    exit 1 # Exit if venv is not found, as subsequent commands will fail
fi

# Navigate to project directory
# Ensure this directory exists
if [ -d "$PROJECT_DIR" ]; then
    echo "[INFO] Changing directory to $PROJECT_DIR" >> /tmp/exchangealert.log
    cd "$PROJECT_DIR"
else
    echo "[ERROR] Project directory not found at $PROJECT_DIR. Please verify the path." >> /tmp/exchangealert.log
    exit 1 # Exit if project directory is not found
fi

# Run Python script
# Redirect both stdout and stderr to the log file.
# This ensures you see all output and errors from your Python script.
echo "[INFO] Running main.py..." >> /tmp/exchangealert.log
python main.py >> /tmp/exchangealert.log 2>&1

# Deactivate the virtual environment (optional, but good practice if more commands followed)
# deactivate # Uncomment if you need to explicitly deactivate, though it's not strictly necessary as the script exits.

echo "[INFO] Exchange Alert Runner finished at $(date)" >> /tmp/exchangealert.log