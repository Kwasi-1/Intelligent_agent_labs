# Prosody Troubleshooting Guide

## Issue: "There is no 'pidfile' option in the configuration file"

### Quick Fix
The configuration has been updated. Run these commands:

```bash
# 1. Create required directories
sudo mkdir -p /var/run/prosody /var/log/prosody

# 2. Copy the updated configuration
sudo cp /workspaces/Intelligent_agent_labs/lab1/prosody.cfg.lua /etc/prosody/prosody.cfg.lua

# 3. Set permissions (ignore errors if prosody user doesn't exist)
sudo chown -R prosody:prosody /var/run/prosody /var/log/prosody 2>/dev/null || true

# 4. Start Prosody using systemctl (preferred)
sudo systemctl restart prosody
```

### Alternative: Start Prosody in foreground for testing
If systemctl doesn't work, you can run Prosody in the foreground:

```bash
sudo prosody
```

Press Ctrl+C to stop it when done testing.

### Verify Prosody is Running
```bash
# Check with systemctl
sudo systemctl status prosody

# OR check with prosodyctl
sudo prosodyctl status

# OR check if the process is running
ps aux | grep prosody
```

## Common Errors and Solutions

### Error: "prosody.service not found"
This happens in some container environments.

**Solution:** Run Prosody directly
```bash
# Start in background
sudo prosody -D &

# Or use prosodyctl
sudo prosodyctl start
```

### Error: "Permission denied"
**Solution:** Create directories with proper permissions
```bash
sudo mkdir -p /var/run/prosody /var/log/prosody
sudo chmod 755 /var/run/prosody /var/log/prosody
```

### Error: "Address already in use"
Prosody is already running or another service is using port 5222.

**Solution:** Stop existing Prosody instance
```bash
sudo systemctl stop prosody
# OR
sudo prosodyctl stop
# OR kill the process
sudo killall prosody
```

Then start it again.

## Complete Restart Procedure

If you need to completely restart Prosody:

```bash
# Stop all Prosody processes
sudo systemctl stop prosody 2>/dev/null || true
sudo prosodyctl stop 2>/dev/null || true
sudo killall prosody 2>/dev/null || true

# Wait a moment
sleep 2

# Copy fresh config
sudo cp /workspaces/Intelligent_agent_labs/lab1/prosody.cfg.lua /etc/prosody/prosody.cfg.lua

# Start fresh
sudo systemctl start prosody || sudo prosody -D
```

## Verify Setup is Working

After starting Prosody, test it:

```bash
# 1. Check status
sudo prosodyctl status

# 2. Create test account (if not already done)
sudo prosodyctl register agent1 localhost agent123

# 3. Check account exists
sudo prosodyctl check

# 4. Run verification script
python3 /workspaces/Intelligent_agent_labs/lab1/verify_environment.py
```

## Still Having Issues?

### Option 1: Use Alternative XMPP Server
If Prosody continues to have issues, you can use ejabberd:

```bash
sudo apt-get install -y ejabberd
sudo systemctl start ejabberd
```

### Option 2: Run Agent Without Local XMPP
For testing purposes, you can modify the agent to run without XMPP initially (we can help with this).

### Option 3: Use Public XMPP Server
Use a public XMPP test server like `jabber.org` (note: less secure, only for testing).

---

**Need more help?** Check the main [README.md](README.md) or consult your instructor.
