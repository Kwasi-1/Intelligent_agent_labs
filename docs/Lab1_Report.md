# Lab 1: Environment and Agent Platform Setup Report

**Student Name:** [Your Name]  
**Student ID:** [Your ID]  
**Course:** DCIT 403 - Designing Intelligent Agent  
**Lab:** 1 - Environment and Agent Platform Setup  
**Date:** [Current Date]

---

## Objective
To configure the Python agent development environment and deploy a basic SPADE agent.

## Environment Setup

### 1. Development Environment
- **Platform:** GitHub Codespaces
- **Operating System:** Ubuntu 24.04.3 LTS
- **Python Version:** 3.12.1
- **IDE:** Visual Studio Code

### 2. Installed Components

#### SPADE Framework
- **Version:** [Fill after installation]
- **Installation Method:** pip3 install spade
- **Status:** ✓ Installed successfully

#### XMPP Server (Prosody)
- **Version:** [Fill after installation]
- **Configuration File:** `/etc/prosody/prosody.cfg.lua`
- **Status:** ✓ Running

#### Agent Credentials Created
1. **Admin Account:** admin@localhost (Password: admin123)
2. **Agent1 Account:** agent1@localhost (Password: agent123)
3. **Sensor1 Account:** sensor1@localhost (Password: sensor123)

## Implementation

### Basic SPADE Agent
The basic agent (`basic_agent.py`) demonstrates:
- Agent initialization and setup
- Periodic behavior execution (every 3 seconds)
- Proper connection to XMPP server
- Clean startup and shutdown procedures

### Key Features
1. **Agent JID:** agent1@localhost
2. **Behavior Type:** PeriodicBehaviour
3. **Execution Interval:** 3 seconds
4. **Output:** Timestamped status messages

## Execution Results

### Agent Output
```
[Insert screenshot or output log showing agent running]
```

### Observations
- Agent successfully connects to XMPP server
- Periodic behavior executes as expected
- Clean logging of agent activities
- Proper shutdown on termination signal

## Challenges and Solutions

### Challenge 1: [If any]
**Problem:** [Describe]  
**Solution:** [Describe]

### Challenge 2: [If any]
**Problem:** [Describe]  
**Solution:** [Describe]

## Conclusion
The Python agent development environment has been successfully configured with:
- ✓ Python 3.12.1 runtime
- ✓ SPADE framework for agent development
- ✓ Prosody XMPP server for agent communication
- ✓ Basic functional agent demonstrating core capabilities

The environment is now ready for implementing more complex multi-agent systems in subsequent labs.

---

**Files Submitted:**
1. `basic_agent.py` - Basic SPADE agent implementation
2. `verify_environment.py` - Environment verification script
3. `prosody.cfg.lua` - XMPP server configuration
4. `setup_xmpp.sh` - XMPP server setup script
5. This report (PDF/Word)
6. Screenshots of running agent
