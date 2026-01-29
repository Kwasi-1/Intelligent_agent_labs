# Manual Installation Steps for Lab 1

Follow these commands in your terminal one by one:

## Step 1: Update System
```bash
sudo apt-get update
```

## Step 2: Install Prosody XMPP Server
```bash
sudo apt-get install -y prosody lua5.1
```

## Step 3: Install Python Dependencies
```bash
pip3 install --upgrade pip
pip3 install spade aiohttp
```

## Step 4: Verify Installations
```bash
# Check Python
python3 --version

# Check SPADE
python3 -c "import spade; print(f'SPADE version: {spade.__version__}')"

# Check Prosody
prosodyctl about
```

## Step 5: Configure Prosody
```bash
# Backup original config
sudo cp /etc/prosody/prosody.cfg.lua /etc/prosody/prosody.cfg.lua.backup

# Copy our config
sudo cp /workspaces/Intelligent_agent_labs/lab1/prosody.cfg.lua /etc/prosody/prosody.cfg.lua

# Create log directory
sudo mkdir -p /var/log/prosody
```

## Step 6: Start Prosody
```bash
# Create PID directory
sudo mkdir -p /var/run/prosody
sudo chown prosody:prosody /var/run/prosody 2>/dev/null || true

# Start using systemctl (recommended) or prosodyctl
sudo systemctl start prosody

# Alternative if systemctl doesn't work:
# sudo prosodyctl start
```

## Step 7: Create Agent Accounts
```bash
# Create admin account
sudo prosodyctl register admin localhost admin123

# Create agent1 account
sudo prosodyctl register agent1 localhost agent123

# Create sensor1 account
sudo prosodyctl register sensor1 localhost sensor123
```

## Step 8: Verify Prosody Status
```bash
sudo prosodyctl status
```

## Step 9: Verify Environment
```bash
python3 /workspaces/Intelligent_agent_labs/lab1/verify_environment.py
```

## Step 10: Run Basic Agent
```bash
python3 /workspaces/Intelligent_agent_labs/lab1/basic_agent.py
```

---

## If You Encounter Errors

### SPADE Installation Issues
```bash
# Try installing with specific version
pip3 install spade==3.2.3
```

### Prosody Permission Issues
```bash
# Ensure proper permissions
sudo chown -R prosody:prosody /var/log/prosody
sudo chmod 755 /var/log/prosody
```

### Agent Connection Issues
```bash
# Restart Prosody
sudo prosodyctl stop
sudo prosodyctl start

# Check if accounts exist
sudo prosodyctl check
```
