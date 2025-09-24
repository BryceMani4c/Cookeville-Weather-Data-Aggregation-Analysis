#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Update and install necessary packages (only if not already installed)
sudo apt update
sudo apt install -y python3 python3-venv python3-pip

# Delete any existing .venv to avoid permission issues
rm -rf .venv

# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required Python packages
pip install pandas numpy matplotlib
