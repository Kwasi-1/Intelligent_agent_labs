#!/bin/bash
# Lab 1 Complete Setup and Test Script

echo "========================================================================"
echo " LAB 1: COMPLETE SETUP AND TESTING"
echo " Course: DCIT 403 - Designing Intelligent Agent"
echo "========================================================================"
echo ""

# Function to check if command succeeded
check_status() {
    if [ $? -eq 0 ]; then
        echo "✓ $1"
    else
        echo "✗ $1 FAILED"
        exit 1
    fi
}

# Navigate to lab1 directory
cd "$(dirname "$0")"

echo "Step 1: Installing dependencies..."
echo "-----------------------------------"
bash install_dependencies.sh
check_status "Dependencies installed"

echo ""
echo "Step 2: Setting up XMPP server..."
echo "-----------------------------------"
sudo bash setup_xmpp.sh
check_status "XMPP server configured"

echo ""
echo "Step 3: Verifying environment..."
echo "-----------------------------------"
python3 verify_environment.py
check_status "Environment verified"

echo ""
echo "========================================================================"
echo " SETUP COMPLETE!"
echo "========================================================================"
echo ""
echo "To run the basic agent, execute:"
echo "  python3 lab1/basic_agent.py"
echo ""
echo "Or from the lab1 directory:"
echo "  cd lab1"
echo "  python3 basic_agent.py"
echo ""
echo "========================================================================"
