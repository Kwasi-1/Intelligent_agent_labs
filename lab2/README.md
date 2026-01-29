# Lab 2: Perception and Environment Modeling

## Overview
Lab 2 implements agent perception of environmental and disaster-related events through:
- Simulated disaster environment
- SensorAgent that periodically monitors conditions
- Event detection and logging

## Files

### 1. disaster_environment.py
Simulates a disaster-prone environment with:
- **Multiple disaster types:** Flood, Earthquake, Fire, Storm, Landslide
- **Severity levels:** Low to Catastrophic
- **Environmental conditions:** Temperature, humidity, wind speed, rainfall
- **Dynamic event generation:** Based on environmental factors
- **Multiple monitoring locations**

### 2. sensor_agent.py
Implements an intelligent SensorAgent that:
- Monitors environmental conditions every 5 seconds
- Detects disaster events
- Analyzes event severity and impact
- Logs events to JSON file
- Provides resource estimates for response

## Quick Start

### Step 1: Test the Environment Simulation
```bash
cd /workspaces/Intelligent_agent_labs/lab2
python3 disaster_environment.py
```

This runs a standalone test showing how the environment generates disasters.

### Step 2: Start Prosody (if not running)
```bash
cd /workspaces/Intelligent_agent_labs/lab1
chmod +x start_prosody_container.sh
bash start_prosody_container.sh
```

### Step 3: Run the SensorAgent
```bash
cd /workspaces/Intelligent_agent_labs/lab2
python3 sensor_agent.py
```

The agent will:
- Connect to the XMPP server
- Start monitoring the environment every 5 seconds
- Detect and log disaster events
- Display comprehensive event information
- Save events to a JSON log file

Press `Ctrl+C` to stop monitoring.

## Expected Output

### Environment Test Output:
```
======================================================================
 DISASTER ENVIRONMENT SIMULATION TEST
======================================================================

Initial Environmental Conditions:
  Temperature: 25.0°C
  Humidity: 60.0%
  Wind Speed: 10.0 km/h
  Rainfall: 0.0 mm/h

Monitoring locations:
  - Downtown District 1 (7.2341, -1.5432)
  - Riverside Area 2 (6.8923, -0.9876)
  ...

Time Step 1:
  Conditions: Temp=26.5°C, Humidity=62.3%, Wind=12.1km/h, Rain=5.4mm/h
  ⚠ DISASTER DETECTED!
     Event EVT-0001: Flood (Severity: HIGH) at Riverside Area 2
     Affected: 1200 people
     Casualties: 45
     Infrastructure Damage: 67.3%
```

### SensorAgent Output:
```
======================================================================
 LAB 2: PERCEPTION AND ENVIRONMENT MODELING
 Course: DCIT 403 - Designing Intelligent Agent
======================================================================

SENSOR AGENT INITIALIZATION
Agent JID: sensor1@localhost
Monitoring 8 locations

[Cycle 1] 2026-01-29 15:45:30
----------------------------------------------------------------------
📊 Environmental Readings:
   Temperature: 27.3°C
   Humidity: 65.2%
   Wind Speed: 15.8 km/h
   Rainfall: 12.4 mm/h

🚨 DISASTER EVENT DETECTED!
   Event ID: EVT-0001
   Type: Fire
   Severity: HIGH (Level 3)
   Location: Industrial Park 5
   Affected Population: 850 people
   Casualties: 32
   Infrastructure Damage: 78.5%

🔍 Event Analysis:
   ⚠️  HIGH PRIORITY: Urgent response needed
   Estimated Resources Needed:
      - Rescue Teams: 3
      - Medical Teams: 2
      - Evacuation Capacity: 850 people
```

## Generated Files

After running the SensorAgent, you'll find:
- `disaster_events_log_YYYYMMDD.json` - JSON log of all detected events

### Log File Format:
```json
[
  {
    "timestamp": "2026-01-29T15:45:30.123456",
    "event_id": "EVT-0001",
    "disaster_type": "Fire",
    "severity": "HIGH",
    "severity_level": 3,
    "location": {
      "name": "Industrial Park 5",
      "latitude": 7.2341,
      "longitude": -1.5432
    },
    "impact": {
      "affected_population": 850,
      "casualties": 32,
      "infrastructure_damage": 78.5
    },
    "environmental_conditions": {
      "temperature": 27.3,
      "humidity": 65.2,
      "wind_speed": 15.8,
      "rainfall": 12.4
    },
    "description": "Major fire outbreak in Industrial Park 5, spreading rapidly"
  }
]
```

## Lab 2 Deliverables

✅ **Required Submissions:**
1. **SensorAgent code** (`sensor_agent.py`) ✓
2. **Event logs** (JSON file generated during execution)
3. **Brief explanation** of percepts (see below)

### Explanation of Percepts

**Percepts** are the sensory inputs the agent receives from its environment:

1. **Environmental Percepts:**
   - Temperature (°C)
   - Humidity (%)
   - Wind Speed (km/h)
   - Rainfall (mm/h)

2. **Event Percepts:**
   - Disaster type (Fire, Flood, Earthquake, etc.)
   - Severity level (Low to Catastrophic)
   - Location coordinates and area name
   - Impact metrics (casualties, affected population, damage)
   - Timestamp

3. **Agent Perception Process:**
   - Agent periodically queries the environment (polling)
   - Reads sensor values
   - Detects pattern changes indicating disasters
   - Logs percepts for decision-making
   - Analyzes percepts to assess response requirements

## Key Concepts Demonstrated

### 1. **Agent Perception**
The SensorAgent perceives its environment through:
- Periodic sensing (every 5 seconds)
- Multiple sensor types (temp, humidity, wind, rain)
- Event detection mechanisms

### 2. **Environment Modeling**
The DisasterEnvironment class models:
- Dynamic environmental conditions
- Multiple monitored locations
- Disaster event generation with realistic parameters
- Temporal evolution of conditions

### 3. **Reactive Behavior**
The agent reactively responds to:
- Environmental changes
- Detected disaster events
- Severity thresholds

## Troubleshooting

### Issue: "Cannot connect to XMPP server"
**Solution:** Ensure Prosody is running
```bash
sudo service prosody start
sudo service prosody status
```

### Issue: "Invalid certificate trust chain"
**Solution:** Already fixed! The code includes `sensor_agent.verify_security = False` for local development. This is standard for testing environments.

### Issue: Module not found errors
**Solution:** Ensure you're in the correct directory
```bash
cd /workspaces/Intelligent_agent_labs/lab2
python3 sensor_agent.py
```

### Issue: No disasters being detected
This is normal! Disaster generation is probabilistic. The agent may run several cycles before detecting an event. High rainfall, temperature, or wind speed increase disaster probability.

## Next Steps

After completing Lab 2:
- Review the generated event logs
- Understand how environmental conditions influence disaster probabilities
- Prepare for Lab 3: Goals, Events, and Reactive Behavior
- Consider how agents might communicate detected events to other agents

## Additional Experiments

Try modifying the code to:
1. Change monitoring interval (modify `period=5.0` in sensor_agent.py)
2. Add more locations (modify `num_locations` parameter)
3. Adjust disaster probabilities (modify weights in `generate_disaster_event()`)
4. Add new disaster types or severity levels
5. Implement alert thresholds for critical events
