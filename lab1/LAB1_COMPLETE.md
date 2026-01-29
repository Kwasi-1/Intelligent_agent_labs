# Lab 1: Complete - Summary & Instructions

## ✅ What We've Created for Lab 1

### Core Files
1. **basic_agent.py** - Your main SPADE agent with periodic behavior
2. **verify_environment.py** - Checks if everything is installed correctly
3. **prosody.cfg.lua** - XMPP server configuration

### Setup Scripts
4. **install_dependencies.sh** - Installs SPADE and Prosody
5. **setup_xmpp.sh** - Configures and starts XMPP server
6. **run_complete_setup.sh** - Runs everything in one go

### Documentation
7. **README.md** - Detailed instructions
8. **MANUAL_INSTALL.md** - Step-by-step manual installation
9. **Lab1_Report.md** - Report template (in docs/)

## 🚀 How to Complete Lab 1

### Option A: One Command (Easiest)
```bash
cd /workspaces/Intelligent_agent_labs/lab1
chmod +x run_complete_setup.sh
bash run_complete_setup.sh
```

### Option B: Step by Step
```bash
cd /workspaces/Intelligent_agent_labs/lab1

# 1. Install dependencies
chmod +x install_dependencies.sh
bash install_dependencies.sh

# 2. Setup XMPP server
chmod +x setup_xmpp.sh
sudo bash setup_xmpp.sh

# 3. Verify installation
python3 verify_environment.py

# 4. Run the agent
python3 basic_agent.py
```

## 📸 Lab 1 Deliverables

For your submission, you need:

1. **Screenshot** - Capture the output when running `basic_agent.py`
2. **Source Code** - Submit `basic_agent.py` (already created ✓)
3. **Report** - Fill out and submit `docs/Lab1_Report.md`

### How to Get Your Screenshot
1. Run: `python3 basic_agent.py`
2. Take a screenshot showing:
   - The terminal with agent output
   - Timestamp and agent messages
   - Your GitHub Codespaces environment
3. Save as `lab1_screenshot.png` in the lab1 folder

## ✅ Checklist

- [ ] Run installation scripts
- [ ] Verify environment with `verify_environment.py`
- [ ] Successfully run `basic_agent.py`
- [ ] Take screenshot of running agent
- [ ] Fill out Lab1_Report.md with your details
- [ ] Submit all deliverables

## 🔍 What the Agent Does

The basic agent:
- Connects to XMPP server at localhost
- Runs a periodic behavior every 3 seconds
- Prints status messages with timestamps
- Demonstrates fundamental SPADE agent structure
- Runs for 20 seconds then cleanly shuts down

## 🐛 Common Issues

### "Command not found: prosody"
```bash
sudo apt-get update
sudo apt-get install -y prosody
```

### "SPADE module not found"
```bash
pip3 install spade aiohttp
```

### "Agent can't connect"
```bash
# Check Prosody is running
sudo prosodyctl status

# Restart if needed
sudo prosodyctl restart
```

## 📚 Understanding the Code

### Key SPADE Concepts in basic_agent.py

1. **Agent Class** - `BasicAgent(Agent)`
   - Main agent definition
   - Inherits from SPADE's Agent class

2. **Behaviour Class** - `BasicBehaviour(PeriodicBehaviour)`
   - Defines what the agent does
   - Runs periodically (every 3 seconds)

3. **setup() method**
   - Called when agent starts
   - Adds behaviors to the agent

4. **run() method**
   - The actual behavior logic
   - Executes periodically

5. **Agent JID** - "agent1@localhost"
   - Jabber ID (similar to email)
   - Identifies the agent on XMPP server

## 🎯 Lab 1 Learning Outcomes Achieved

✅ Configured Python agent development environment  
✅ Deployed SPADE framework  
✅ Set up XMPP server for agent communication  
✅ Created and executed a basic SPADE agent  
✅ Understood agent behaviors and periodic execution  

---

## Next: Lab 2 Preview

Lab 2 will cover:
- Simulating disaster environments
- Creating SensorAgents that detect events
- Implementing perception mechanisms
- Logging disaster events

Ready to proceed to Lab 2? Just let me know!
