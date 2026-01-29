#!/bin/bash
# Lab 2 Quick Test Script

echo "========================================================================"
echo " LAB 2: QUICK TEST"
echo " Testing Disaster Environment and SensorAgent"
echo "========================================================================"
echo ""

cd "$(dirname "$0")"

echo "Step 1: Testing Disaster Environment Simulation"
echo "----------------------------------------------------------------"
echo "Running standalone environment test (10 seconds)..."
echo ""
timeout 10 python3 disaster_environment.py || echo "(Test completed or interrupted)"
echo ""

echo "========================================================================"
echo "Step 2: Check if Prosody is running"
echo "----------------------------------------------------------------"
if sudo service prosody status | grep -q "running"; then
    echo "✓ Prosody is running"
else
    echo "⚠ Prosody not running. Starting it..."
    sudo service prosody start
    sleep 2
    if sudo service prosody status | grep -q "running"; then
        echo "✓ Prosody started successfully"
    else
        echo "✗ Could not start Prosody"
        echo "Try: sudo prosody -D"
        echo ""
        echo "You can still test the environment simulation (Step 1 above)"
        echo "But the SensorAgent will need XMPP to run."
        exit 1
    fi
fi

echo ""
echo "========================================================================"
echo " ENVIRONMENT TEST COMPLETE!"
echo "========================================================================"
echo ""
echo "To run the full SensorAgent with XMPP:"
echo "  python3 sensor_agent.py"
echo ""
echo "The agent will monitor for 60 seconds (or until Ctrl+C)"
echo "Event logs will be saved to: disaster_events_log_YYYYMMDD.json"
echo ""
echo "========================================================================"
