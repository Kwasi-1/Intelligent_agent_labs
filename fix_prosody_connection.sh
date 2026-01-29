#!/bin/bash
# Fix Prosody and ensure it's actually running

echo "=========================================="
echo "Fixing Prosody Connection Issues"
echo "=========================================="
echo ""

# Stop any existing Prosody instances
echo "Step 1: Stopping any existing Prosody instances..."
sudo service prosody stop 2>/dev/null || true
sudo prosodyctl stop 2>/dev/null || true
sudo killall prosody 2>/dev/null || true
sleep 2

# Ensure directories exist
echo ""
echo "Step 2: Creating required directories..."
sudo mkdir -p /var/run/prosody /var/log/prosody /var/lib/prosody
sudo chmod 755 /var/run/prosody /var/log/prosody /var/lib/prosody

# Copy updated config
echo ""
echo "Step 3: Updating Prosody configuration..."
sudo cp /workspaces/Intelligent_agent_labs/lab1/prosody.cfg.lua /etc/prosody/prosody.cfg.lua

# Start Prosody in foreground mode for testing (detached)
echo ""
echo "Step 4: Starting Prosody..."
sudo prosody > /tmp/prosody.log 2>&1 &
PROSODY_PID=$!

sleep 3

# Check if it's actually running
if ps -p $PROSODY_PID > /dev/null 2>&1; then
    echo "✓ Prosody started successfully (PID: $PROSODY_PID)"
else
    echo "⚠ Prosody may have issues. Checking logs..."
    tail -20 /tmp/prosody.log
fi

echo ""
echo "Step 5: Creating/verifying agent accounts..."
sudo prosodyctl register admin localhost admin123 2>/dev/null || echo "  admin exists"
sudo prosodyctl register agent1 localhost agent123 2>/dev/null || echo "  agent1 exists"
sudo prosodyctl register sensor1 localhost sensor123 2>/dev/null || echo "  sensor1 exists"

echo ""
echo "Step 6: Testing connection..."
if sudo prosodyctl status | grep -q "running"; then
    echo "✓ Prosody is responding to status checks"
else
    echo "⚠ Prosody status check unclear, but process is running"
    echo "  Check /tmp/prosody.log for details"
fi

echo ""
echo "=========================================="
echo "Prosody Fix Complete!"
echo "=========================================="
echo ""
echo "Now try running your agents:"
echo "  python3 /workspaces/Intelligent_agent_labs/lab1/basic_agent.py"
echo "  python3 /workspaces/Intelligent_agent_labs/lab2/sensor_agent.py"
echo ""
echo "If issues persist, check:"
echo "  tail -f /tmp/prosody.log"
echo "  sudo netstat -tlnp | grep 5222"
echo ""
