# 🚀 QUICK REFERENCE - Labs 1 & 2

## START HERE

### First Time Setup (Lab 1)
```bash
cd /workspaces/Intelligent_agent_labs/lab1
bash run_complete_setup.sh
```

### Start Prosody (When Needed)
```bash
cd /workspaces/Intelligent_agent_labs/lab1
bash start_prosody_container.sh
```

---

## RUN THE LABS

### Lab 1: Basic Agent
```bash
cd /workspaces/Intelligent_agent_labs/lab1
python3 basic_agent.py
```
**Runs for:** 20 seconds  
**Shows:** Agent with periodic behavior every 3 seconds

---

### Lab 2: SensorAgent

**Option A - Environment Test Only (No XMPP)**
```bash
cd /workspaces/Intelligent_agent_labs/lab2
python3 disaster_environment.py
```
**Runs for:** 10 time steps  
**Shows:** Disaster generation and environmental changes

**Option B - Full SensorAgent (Requires Prosody)**
```bash
cd /workspaces/Intelligent_agent_labs/lab2
python3 sensor_agent.py
```
**Runs for:** 60 seconds (or Ctrl+C to stop)  
**Shows:** Real-time disaster monitoring  
**Creates:** `disaster_events_log_YYYYMMDD.json`

---

## QUICK TROUBLESHOOTING

### Prosody Not Running?
```bash
sudo service prosody start
```

### Agent Won't Connect?
```bash
# Check Prosody
sudo service prosody status

# Recreate account
sudo prosodyctl register sensor1 localhost sensor123
```

### Need Fresh Start?
```bash
# Stop Prosody
sudo service prosody stop

# Start fresh
cd /workspaces/Intelligent_agent_labs/lab1
bash start_prosody_container.sh
```

---

## FILE LOCATIONS

### Lab 1
```
lab1/basic_agent.py          ← Your first agent
lab1/start_prosody_container.sh  ← Start Prosody
lab1/README.md               ← Full Lab 1 guide
```

### Lab 2
```
lab2/disaster_environment.py  ← Environment sim
lab2/sensor_agent.py          ← SensorAgent
lab2/README.md                ← Full Lab 2 guide
disaster_events_log_*.json    ← Generated logs
```

### Documentation
```
docs/Lab1_Report.md           ← Lab 1 report template
docs/Lab2_Report.md           ← Lab 2 report template
LABS_COMPLETE.md              ← Complete summary
```

---

## WHAT TO SUBMIT

### Lab 1
1. Screenshot of `basic_agent.py` running
2. Source code: `basic_agent.py`
3. Report: Fill out `docs/Lab1_Report.md`

### Lab 2
1. Source code: `sensor_agent.py`, `disaster_environment.py`
2. Event log: `disaster_events_log_YYYYMMDD.json`
3. Report: Fill out `docs/Lab2_Report.md`
4. Brief explanation of percepts (in report)

---

## KEY COMMANDS SUMMARY

| Task | Command |
|------|---------|
| Setup everything | `cd lab1 && bash run_complete_setup.sh` |
| Start Prosody | `sudo service prosody start` |
| Check Prosody | `sudo service prosody status` |
| Run Lab 1 | `python3 lab1/basic_agent.py` |
| Test Lab 2 env | `python3 lab2/disaster_environment.py` |
| Run Lab 2 agent | `python3 lab2/sensor_agent.py` |
| Verify setup | `python3 lab1/verify_environment.py` |

---

## AGENT CREDENTIALS

| Agent | JID | Password |
|-------|-----|----------|
| Admin | admin@localhost | admin123 |
| Agent1 | agent1@localhost | agent123 |
| Sensor1 | sensor1@localhost | sensor123 |

---

## HELP & DOCS

- **Lab 1 Help:** [lab1/README.md](lab1/README.md)
- **Lab 2 Help:** [lab2/README.md](lab2/README.md)
- **Complete Guide:** [LABS_COMPLETE.md](LABS_COMPLETE.md)
- **Quick Start:** [QUICKSTART.md](QUICKSTART.md)
- **Main README:** [README.md](README.md)

---

**Pro Tip:** Run `python3 lab2/disaster_environment.py` first to see how disasters are generated, then run `python3 lab2/sensor_agent.py` to see the full agent in action!
