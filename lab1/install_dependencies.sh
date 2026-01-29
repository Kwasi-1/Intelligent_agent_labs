#!/bin/bash
# Lab 1: Installation script for SPADE and dependencies

echo "=== Installing SPADE and Dependencies ==="

# Update package list
echo "Updating package list..."
sudo apt-get update

# Install Prosody XMPP server
echo "Installing Prosody XMPP server..."
sudo apt-get install -y prosody lua5.1

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install --upgrade pip
pip3 install spade aiohttp

# Verify installations
echo ""
echo "=== Verification ==="
echo "Python version:"
python3 --version
echo ""
echo "SPADE installation:"
python3 -c "import spade; print(f'SPADE version: {spade.__version__}')" 2>/dev/null && echo "SPADE installed successfully" || echo "SPADE installation failed"
echo ""
echo "Prosody installation:"
prosodyctl about | head -n 1

echo ""
echo "=== Installation Complete ==="
