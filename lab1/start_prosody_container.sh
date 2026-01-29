#!/bin/bash
# Container-friendly Prosody startup script

echo "=========================================="
echo "Starting Prosody (Container Mode)"
echo "=========================================="

# Stop any existing instances
sudo service prosody stop 2>/dev/null || true
sudo prosodyctl stop 2>/dev/null || true
sleep 1

# Ensure directories exist with proper permissions
sudo mkdir -p /var/run/prosody /var/log/prosody
sudo chmod 755 /var/run/prosody /var/log/prosody

# Start using service command (works in containers)
echo "Starting Prosody with service command..."
sudo service prosody start

sleep 2

# Check status
echo ""
echo "Checking Prosody status..."
if sudo service prosody status | grep -q "running"; then
    echo "✓ Prosody is running!"
    
    # Create accounts if they don't exist
    echo ""
    echo "Ensuring agent accounts exist..."
    sudo prosodyctl register admin localhost admin123 2>/dev/null || echo "  admin already exists"
    sudo prosodyctl register agent1 localhost agent123 2>/dev/null || echo "  agent1 already exists"
    sudo prosodyctl register sensor1 localhost sensor123 2>/dev/null || echo "  sensor1 already exists"
    
    echo ""
    echo "=========================================="
    echo "✓ Prosody is ready!"
    echo "=========================================="
    echo ""
    echo "You can now run: python3 basic_agent.py"
else
    echo "⚠ Prosody may not be running properly"
    echo "Try: sudo prosody -D"
fi
