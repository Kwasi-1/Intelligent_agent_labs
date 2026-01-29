#!/bin/bash
# Quick fix for Prosody pidfile error

echo "=========================================="
echo "Fixing Prosody Configuration"
echo "=========================================="

cd /workspaces/Intelligent_agent_labs/lab1

echo "Step 1: Creating required directories..."
sudo mkdir -p /var/run/prosody
sudo mkdir -p /var/log/prosody
echo "✓ Directories created"

echo ""
echo "Step 2: Copying updated configuration..."
sudo cp prosody.cfg.lua /etc/prosody/prosody.cfg.lua
echo "✓ Configuration updated (now includes pidfile setting)"

echo ""
echo "Step 3: Setting permissions..."
sudo chown -R prosody:prosody /var/run/prosody /var/log/prosody 2>/dev/null || true
sudo chmod 755 /var/run/prosody /var/log/prosody
echo "✓ Permissions set"

echo ""
echo "Step 4: Starting Prosody..."

# Try systemctl first
if command -v systemctl &> /dev/null; then
    echo "Using systemctl..."
    sudo systemctl restart prosody
    if [ $? -eq 0 ]; then
        echo "✓ Prosody started with systemctl"
    else
        echo "⚠ systemctl failed, trying prosodyctl..."
        sudo prosodyctl start
    fi
else
    echo "Using prosodyctl..."
    sudo prosodyctl start
fi

echo ""
echo "Step 5: Checking status..."
sleep 2
sudo prosodyctl status

echo ""
echo "=========================================="
echo "Fix complete!"
echo "=========================================="
echo ""
echo "Next: Create agent accounts"
echo "  sudo prosodyctl register admin localhost admin123"
echo "  sudo prosodyctl register agent1 localhost agent123"
echo "  sudo prosodyctl register sensor1 localhost sensor123"
echo ""
