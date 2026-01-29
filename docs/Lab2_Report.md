# Lab 2: Perception and Environment Modeling Report

**Student Name:** [Your Name]  
**Student ID:** [Your ID]  
**Course:** DCIT 403 - Designing Intelligent Agent  
**Lab:** 2 - Perception and Environment Modeling  
**Date:** January 29, 2026

---

## Objective
To implement agent perception of environmental and disaster-related events.

## Implementation

### 1. Disaster Environment (`disaster_environment.py`)

#### Key Features:
- **Disaster Types:** Flood, Earthquake, Fire, Storm, Landslide
- **Severity Levels:** LOW (1) to CATASTROPHIC (5)
- **Environmental Factors:** Temperature, humidity, wind speed, rainfall
- **Locations Monitored:** 8 different areas

#### Environment Dynamics:
The environment simulates realistic conditions where:
- Temperature varies between 15-40°C
- Rainfall influences flood and landslide probability
- High temperatures increase fire risk
- Wind speed affects storm likelihood

### 2. SensorAgent (`sensor_agent.py`)

#### Percepts (Sensory Inputs):

**Environmental Percepts:**
1. **Temperature (°C):** Continuous measurement of ambient temperature
2. **Humidity (%):** Relative humidity measurement
3. **Wind Speed (km/h):** Wind velocity monitoring
4. **Rainfall (mm/h):** Precipitation rate measurement

**Event Percepts:**
1. **Disaster Type:** Classification of detected event
2. **Severity Level:** Impact assessment (1-5 scale)
3. **Location Data:** Geographic coordinates and area identification
4. **Impact Metrics:**
   - Affected population count
   - Casualty estimates
   - Infrastructure damage percentage
5. **Timestamp:** Temporal information for event sequencing

#### Perception Mechanism:
```
Every 5 seconds:
  1. Query environment for sensor readings
  2. Update internal model of environmental state
  3. Evaluate disaster occurrence probability
  4. If disaster detected:
     - Capture all event details (percepts)
     - Analyze severity and impact
     - Log event with environmental context
     - Estimate required resources
```

#### Behavior Type:
- **PeriodicBehaviour:** Executes monitoring every 5 seconds
- **Reactive:** Responds immediately to detected events
- **Proactive:** Maintains continuous surveillance

## Execution Results

### Test Run Summary

**Duration:** [Fill in - e.g., 60 seconds]  
**Monitoring Cycles:** [Fill in - e.g., 12 cycles]  
**Events Detected:** [Fill in - e.g., 3 events]

### Sample Events Detected:

#### Event 1:
- **Event ID:** EVT-0001
- **Type:** [e.g., Fire]
- **Severity:** [e.g., HIGH (Level 3)]
- **Location:** [e.g., Industrial Park 5]
- **Affected Population:** [e.g., 850 people]
- **Casualties:** [e.g., 32]
- **Infrastructure Damage:** [e.g., 78.5%]
- **Environmental Context:**
  - Temperature: [e.g., 38.2°C]
  - Wind Speed: [e.g., 25.3 km/h]

#### Event 2:
[Fill in with second detected event]

#### Event 3:
[Fill in with third detected event]

### Event Log File
Generated file: `disaster_events_log_20260129.json`  
Total entries: [Fill in]

## Analysis and Observations

### 1. Perception Effectiveness
[Discuss how well the agent perceives its environment]

Example:
"The SensorAgent successfully monitors multiple environmental parameters simultaneously. The 5-second polling interval provides timely detection without excessive computational overhead. The agent correctly correlates environmental conditions (e.g., high temperatures) with disaster types (e.g., fires)."

### 2. Environmental Correlation
[Discuss relationship between environmental conditions and disasters]

Example:
"Observed strong correlation between rainfall levels and flood events. When rainfall exceeded 70mm/h, flood probability increased significantly. Similarly, high temperatures (>35°C) preceded most fire events."

### 3. Perception Accuracy
[Discuss the quality and completeness of percepts]

Example:
"The agent captures comprehensive percepts including location, severity, impact metrics, and environmental context. This rich perceptual information enables effective decision-making for response coordination."

### 4. Reactive Behavior
[Discuss how the agent responds to percepts]

Example:
"The agent demonstrates appropriate reactive behavior by immediately analyzing detected events and estimating required resources. Response recommendations scale with severity level, showing intelligent perception-to-action mapping."

## Explanation of Percepts

### What are Percepts?
Percepts are the sensory inputs an intelligent agent receives from its environment. They form the basis for the agent's understanding of its world and guide its decision-making.

### Percepts in This System:

1. **Environmental Percepts:**
   - Quantitative measurements from simulated sensors
   - Continuous monitoring of temperature, humidity, wind, rainfall
   - Enables prediction of disaster likelihood

2. **Event Percepts:**
   - Discrete disaster occurrences with structured attributes
   - Include type, severity, location, and impact data
   - Trigger immediate agent analysis and response planning

3. **Temporal Percepts:**
   - Timestamps enable event sequencing
   - Support trend analysis and prediction
   - Allow for clearing of old events

### Perception Process:
```
Environment → Sensors → Percepts → Agent Processing → Actions/Logs
```

The agent's perception is:
- **Periodic:** Regular 5-second monitoring cycle
- **Multi-modal:** Multiple sensor types
- **Contextual:** Combines environmental and event data
- **Persistent:** Logs all percepts for future analysis

## Challenges and Solutions

### Challenge 1: [If any - e.g., "Event detection frequency"]
**Problem:** [Describe]  
**Solution:** [Describe - e.g., "Adjusted disaster probability weights based on environmental thresholds"]

### Challenge 2: [If any]
**Problem:** [Describe]  
**Solution:** [Describe]

## Conclusion

Lab 2 successfully demonstrates agent perception capabilities:

✅ **Implemented:**
- Comprehensive disaster environment simulation
- Intelligent SensorAgent with periodic perception
- Multi-modal sensing (temperature, humidity, wind, rainfall)
- Event detection and logging system
- Severity analysis and resource estimation

✅ **Learning Outcomes:**
- Understanding of agent percepts and perception mechanisms
- Implementation of periodic sensing behaviors
- Environmental modeling for disaster scenarios
- Event logging and data persistence

✅ **Readiness:**
The perception infrastructure established in Lab 2 provides the foundation for:
- Goal-oriented behavior (Lab 3)
- Inter-agent communication (Lab 4)
- Coordinated response (Lab 5)

The agent can now perceive its environment and detect disasters. Next steps involve adding goals and reactive behaviors to respond appropriately to perceived events.

---

## Files Submitted
1. `disaster_environment.py` - Environment simulation
2. `sensor_agent.py` - SensorAgent implementation
3. `disaster_events_log_YYYYMMDD.json` - Event log
4. Screenshots showing agent execution
5. This report
