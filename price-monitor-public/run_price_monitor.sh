#!/bin/bash

# Price Monitor Automation Script
# This script activates the virtual environment and runs the price monitor

# Set the project directory
PROJECT_DIR="/home/anmol/Desktop/Automation/price_monitor"

# Activate virtual environment
source /home/anmol/Desktop/Automation/.venv/bin/activate

# Change to project directory
cd "$PROJECT_DIR"

# Run the Python script and log output
/home/anmol/Desktop/Automation/.venv/bin/python main.py >> "$PROJECT_DIR/logs/cron_execution.log" 2>&1

# Exit with status code
exit $?
