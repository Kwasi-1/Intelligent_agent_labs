#!/bin/bash
# Script to configure and start Prosody XMPP server

echo "=== Configuring Prosody XMPP Server ==="

# Create log and PID directories
sudo mkdir -p /var/log/prosody
sudo mkdir -p /var/run/prosody
sudo chown -R prosody:prosody /var/log/prosody 2>/dev/null || echo "Note: User prosody may not exist yet"
sudo chown -R prosody:prosody /var/run/prosody 2>/dev/null || true

# Copy configuration (backup existing if present)
if [ -f /etc/prosody/prosody.cfg.lua ]; then
    sudo cp /etc/prosody/prosody.cfg.lua /etc/prosody/prosody.cfg.lua.backup
fi

echo "Copying Prosody configuration..."
sudo cp prosody.cfg.lua /etc/prosody/prosody.cfg.lua

# Start Prosody
echo "Starting Prosody XMPP server..."
if command -v systemctl &> /dev/null; then
    sudo systemctl restart prosody
    echo "Using systemctl to start Prosody"
else
    sudo prosodyctl start
    echo "Using prosodyctl to start Prosody"
fi

# Wait a bit for server to start
sleep 2

# Create agent accounts
echo ""
echo "=== Creating Agent Accounts ==="
echo "Creating admin account..."
sudo prosodyctl register admin localhost admin123

echo "Creating test agent account..."
sudo prosodyctl register agent1 localhost agent123

echo "Creating sensor agent account..."
sudo prosodyctl register sensor1 localhost sensor123

echo ""
echo "=== Prosody Status ==="
sudo prosodyctl status

echo ""
echo "=== Agent Credentials ==="
echo "Admin: admin@localhost / admin123"
echo "Agent1: agent1@localhost / agent123"
echo "Sensor1: sensor1@localhost / sensor123"
echo ""
echo "XMPP Server is ready!"
