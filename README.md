# Intelligent Agent Labs - DCIT 403

**Course:** Designing Intelligent Agent  
**Project:** Disaster Response & Relief Coordination System  
**Framework:** SPADE (Smart Python Agent Development Environment)

## Overview

This repository contains laboratory work for building a multi-agent disaster response system. The labs progress from basic agent setup to a fully coordinated multi-agent system.

## Project Structure

```
Intelligent_agent_labs/
├── lab1/              # Environment and Agent Platform Setup
│   ├── basic_agent.py
│   ├── verify_environment.py
│   ├── install_dependencies.sh
│   ├── setup_xmpp.sh
│   ├── prosody.cfg.lua
│   ├── README.md
│   └── MANUAL_INSTALL.md
├── lab2/              # Perception and Environment Modeling (Coming soon)
├── docs/              # Documentation and reports
│   └── Lab1_Report.md
└── requirements.txt   # Python dependencies
```

## Getting Started with Lab 1

### Quick Overview
Lab 1 sets up your development environment with:
- Python 3.12+ 
- SPADE agent framework
- Prosody XMPP server for agent communication
- A basic working agent

### Installation Options

#### Option 1: Automated (Recommended)
```bash
cd lab1
chmod +x install_dependencies.sh setup_xmpp.sh
bash install_dependencies.sh
sudo bash setup_xmpp.sh
```

#### Option 2: Manual
Follow the detailed steps in [lab1/MANUAL_INSTALL.md](lab1/MANUAL_INSTALL.md)

### Quick Test
```bash
# Verify environment
python3 lab1/verify_environment.py

# Run basic agent
python3 lab1/basic_agent.py
```

## Lab Progress

- [x] **Lab 1:** Environment and Agent Platform Setup ✓
- [ ] **Lab 2:** Perception and Environment Modeling (Next)
- [ ] **Lab 3:** Goals, Events, and Reactive Behavior
- [ ] **Lab 4:** Agent Communication using FIPA-ACL
- [ ] **Lab 5:** Coordination and Task Delegation
- [ ] **Lab 6-13:** Advanced topics and system integration

## System Requirements

- Python 3.9 or higher
- Ubuntu/Debian-based Linux (or GitHub Codespaces)
- Internet connection for package installation
- Sudo privileges for XMPP server installation

## Key Technologies

- **SPADE:** Python multi-agent framework
- **XMPP:** Real-time messaging protocol for agent communication
- **Prosody:** Lightweight XMPP server
- **Asyncio:** Asynchronous programming support

## Documentation

- Lab reports are in the `docs/` directory
- Each lab folder contains its own README with specific instructions
- See [lab1/README.md](lab1/README.md) for detailed Lab 1 instructions

## Support

If you encounter issues:
1. Check the troubleshooting section in the lab README
2. Verify all prerequisites are installed
3. Review the manual installation guide
4. Check Prosody server status: `sudo prosodyctl status`

## Next Steps

After completing Lab 1, proceed to Lab 2 for implementing agent perception and environment modeling.