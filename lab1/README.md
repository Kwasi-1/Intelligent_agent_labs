# Lab 1: Environment and Agent Platform Setup

## Quick Start Guide

### Step 1: Install Dependencies

```bash
cd lab1
chmod +x install_dependencies.sh
bash install_dependencies.sh
```

This will install:
- Prosody XMPP server
- SPADE framework
- Required Python packages

### Step 2: Configure and Start XMPP Server

```bash
cd lab1
chmod +x setup_xmpp.sh
sudo bash setup_xmpp.sh
```

This will:
- Configure Prosody with the provided settings
- Start the XMPP server
- Create agent accounts (admin, agent1, sensor1)

### Step 3: Verify Environment

```bash
python3 lab1/verify_environment.py
```

This checks if all components are properly installed.

### Step 4: Run the Basic Agent

```bash
python3 lab1/basic_agent.py
```

The agent will run for 20 seconds, displaying periodic status messages. Press Ctrl+C to stop early.

## Expected Output

When you run the basic agent, you should see:

```
======================================================================
 LAB 1: BASIC SPADE AGENT DEMONSTRATION
 Course: DCIT 403 - Designing Intelligent Agent
 Project: Disaster Response & Relief Coordination System
======================================================================

Starting agent: agent1@localhost
Press Ctrl+C to stop the agent

==================================================
BASIC AGENT SETUP
==================================================
Agent JID: agent1@localhost
Agent initialized at: 2026-01-29 15:30:45
==================================================

✓ Periodic behavior added (runs every 3 seconds)
✓ Agent is now active and running

Agent started successfully!
Waiting for agent to run...

[2026-01-29 15:30:48] BasicAgent is running...
  - Agent Name: agent1@localhost
  - Behavior executing periodic task
  - Status: Active and responsive
--------------------------------------------------
[... more periodic outputs ...]
```

## Files Included

- `basic_agent.py` - Basic SPADE agent implementation
- `verify_environment.py` - Environment verification script
- `install_dependencies.sh` - Dependency installation script
- `setup_xmpp.sh` - XMPP server configuration script
- `prosody.cfg.lua` - Prosody configuration file

## Troubleshooting

### Issue: SPADE not found
**Solution:** Run the installation script again
```bash
pip3 install spade aiohttp
```

### Issue: Prosody not running
**Solution:** Start Prosody manually
```bash
sudo prosodyctl start
```

### Issue: Agent can't connect
**Solution:** Verify agent account exists
```bash
sudo prosodyctl check
```

## Lab 1 Deliverables Checklist

- [ ] Screenshot of running agent in GitHub Codespaces
- [ ] Python source code (`basic_agent.py`)
- [ ] Environment setup report (see `docs/Lab1_Report.md`)

## Next Steps

After completing Lab 1, you'll be ready for Lab 2: Perception and Environment Modeling.
