"""
Lab 2: SensorAgent - Perception and Environment Modeling (Simplified Version)
Course: DCIT 403 - Designing Intelligent Agent
Project: Disaster Response & Relief Coordination System

This is a simplified version that runs WITHOUT requiring an XMPP server.
It demonstrates perception, environment modeling, and event detection.
"""

import asyncio
from datetime import datetime
from disaster_environment import DisasterEnvironment, DisasterEvent
import json


class EnvironmentMonitorBehaviour:
    """
    Periodic behavior that monitors environmental conditions
    and detects disaster events
    """
    
    def __init__(self, agent, period=5.0):
        self.agent = agent
        self.period = period
        self.running = False
        self.cycle_count = 0
        self.events_detected = 0
    
    async def on_start(self):
        """Called when the behaviour starts"""
        print("\n" + "=" * 70)
        print(" SENSOR AGENT - ENVIRONMENT MONITORING STARTED")
        print("=" * 70)
        print(f"Agent: {self.agent.name}")
        print(f"Monitoring interval: {self.period} seconds")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70 + "\n")
    
    async def run(self):
        """
        Main sensing loop - executed periodically
        """
        self.cycle_count += 1
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"\n[Cycle {self.cycle_count}] {current_time}")
        print("-" * 70)
        
        # Update environmental conditions
        self.agent.environment.update_environmental_conditions()
        
        # Read environmental sensors
        readings = self.agent.environment.get_environmental_readings()
        print(f"📊 Environmental Readings:")
        print(f"   Temperature: {readings['temperature']}°C")
        print(f"   Humidity: {readings['humidity']}%")
        print(f"   Wind Speed: {readings['wind_speed']} km/h")
        print(f"   Rainfall: {readings['rainfall']} mm/h")
        
        # Check for disaster events
        if self.agent.environment.should_generate_event():
            event = self.agent.environment.generate_disaster_event()
            self.events_detected += 1
            
            print(f"\n🚨 DISASTER EVENT DETECTED!")
            print(f"   Event ID: {event.event_id}")
            print(f"   Type: {event.disaster_type.value}")
            print(f"   Severity: {event.severity.name} (Level {event.severity.value})")
            print(f"   Location: {event.location}")
            print(f"   Description: {event.description}")
            print(f"   Affected Population: {event.affected_population} people")
            print(f"   Casualties: {event.casualties}")
            print(f"   Infrastructure Damage: {event.infrastructure_damage:.1f}%")
            print(f"   Timestamp: {event.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Log the event
            self.agent.log_event(event, readings)
            
            # Analyze and report
            self.analyze_event(event, readings)
        else:
            print("✓ No disasters detected - Environment stable")
        
        # Clear old events periodically
        if self.cycle_count % 5 == 0:
            self.agent.environment.clear_old_events()
        
        print(f"\n📈 Statistics:")
        print(f"   Total Monitoring Cycles: {self.cycle_count}")
        print(f"   Total Events Detected: {self.events_detected}")
        print(f"   Active Events: {len(self.agent.environment.get_active_events())}")
        print("-" * 70)
    
    def analyze_event(self, event: DisasterEvent, readings: dict):
        """
        Analyze the disaster event and provide assessment
        """
        print(f"\n🔍 Event Analysis:")
        
        # Severity assessment
        if event.severity.value >= 4:
            print(f"   ⚠️  CRITICAL: Immediate response required!")
            print(f"   ⚠️  Multiple rescue teams needed")
        elif event.severity.value >= 3:
            print(f"   ⚠️  HIGH PRIORITY: Urgent response needed")
        else:
            print(f"   ℹ️  Standard response protocol")
        
        # Resource estimation
        rescue_teams_needed = max(1, event.severity.value)
        medical_teams_needed = max(1, event.casualties // 50 + 1)
        
        print(f"   Estimated Resources Needed:")
        print(f"      - Rescue Teams: {rescue_teams_needed}")
        print(f"      - Medical Teams: {medical_teams_needed}")
        print(f"      - Evacuation Capacity: {event.affected_population} people")
        
        # Environmental correlation
        print(f"   Environmental Factors:")
        if readings['rainfall'] > 50:
            print(f"      - High rainfall may hamper rescue operations")
        if readings['wind_speed'] > 40:
            print(f"      - Strong winds present additional hazard")
        if readings['temperature'] > 35:
            print(f"      - High temperature - heat stress risk for responders")
    
    async def start(self):
        """Start the behavior loop"""
        self.running = True
        await self.on_start()
        
        while self.running:
            await self.run()
            await asyncio.sleep(self.period)
    
    def stop(self):
        """Stop the behavior"""
        self.running = False


class SensorAgent:
    """
    Intelligent agent that perceives and monitors disaster environment
    (Simplified standalone version)
    """
    
    def __init__(self, name):
        self.name = name
        self.behaviours = []
        self.event_log = []
        self.environment = None
    
    async def setup(self):
        """
        Initialize the SensorAgent
        """
        print("\n" + "=" * 70)
        print(" SENSOR AGENT INITIALIZATION")
        print("=" * 70)
        print(f"Agent Name: {self.name}")
        print(f"Agent Type: Environmental Sensor & Disaster Detector")
        print(f"Initialization Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)
        
        # Initialize disaster environment
        self.environment = DisasterEnvironment(num_locations=8)
        print(f"\n✓ Disaster environment initialized")
        print(f"✓ Monitoring {len(self.environment.locations)} locations")
        
        print(f"\nMonitored Locations:")
        for i, loc in enumerate(self.environment.locations, 1):
            print(f"   {i}. {loc}")
        
        # Add monitoring behavior (runs every 5 seconds)
        monitor_behaviour = EnvironmentMonitorBehaviour(self, period=5.0)
        self.behaviours.append(monitor_behaviour)
        
        print(f"\n✓ Monitoring behavior activated (5-second intervals)")
        print(f"✓ Agent is operational and monitoring environment\n")
    
    def log_event(self, event: DisasterEvent, readings: dict):
        """
        Log a detected event with sensor readings
        """
        log_entry = {
            "timestamp": event.timestamp.isoformat(),
            "event_id": event.event_id,
            "disaster_type": event.disaster_type.value,
            "severity": event.severity.name,
            "severity_level": event.severity.value,
            "location": {
                "name": event.location.area_name,
                "latitude": event.location.latitude,
                "longitude": event.location.longitude
            },
            "impact": {
                "affected_population": event.affected_population,
                "casualties": event.casualties,
                "infrastructure_damage": event.infrastructure_damage
            },
            "environmental_conditions": readings,
            "description": event.description
        }
        
        self.event_log.append(log_entry)
        
        # Save to file
        self.save_log_to_file()
    
    def save_log_to_file(self):
        """Save event log to JSON file"""
        filename = f"disaster_events_log_{datetime.now().strftime('%Y%m%d')}.json"
        try:
            with open(filename, 'w') as f:
                json.dump(self.event_log, f, indent=2)
        except Exception as e:
            print(f"   ⚠️  Error saving log: {e}")
    
    async def start(self):
        """Start the agent and all its behaviors"""
        await self.setup()
        
        # Start all behaviors
        tasks = []
        for behaviour in self.behaviours:
            tasks.append(asyncio.create_task(behaviour.start()))
        
        return tasks
    
    async def stop(self):
        """Stop the agent"""
        for behaviour in self.behaviours:
            behaviour.stop()


async def main():
    """
    Main function to run the SensorAgent
    """
    print("\n" + "=" * 70)
    print(" LAB 2: PERCEPTION AND ENVIRONMENT MODELING (Simplified Version)")
    print(" Course: DCIT 403 - Designing Intelligent Agent")
    print(" Project: Disaster Response & Relief Coordination System")
    print("=" * 70)
    print("\nThis version runs WITHOUT requiring an XMPP server")
    print()
    
    agent_name = "SensorAgent-1"
    
    print(f"Starting SensorAgent: {agent_name}")
    print("Press Ctrl+C to stop monitoring\n")
    
    # Create and start the sensor agent
    sensor_agent = SensorAgent(agent_name)
    
    try:
        tasks = await sensor_agent.start()
        print("✓ SensorAgent started successfully!\n")
        
        # Run for a reasonable time to demonstrate (60 seconds)
        print(f"Monitoring environment... (will run for 60 seconds)")
        print("You can press Ctrl+C anytime to stop\n")
        
        await asyncio.sleep(60)
        
    except KeyboardInterrupt:
        print("\n\n" + "=" * 70)
        print(" MONITORING STOPPED BY USER")
        print("=" * 70)
    finally:
        # Display summary
        print(f"\n📊 MONITORING SESSION SUMMARY")
        print("-" * 70)
        event_count = len(sensor_agent.event_log)
        print(f"Total Events Logged: {event_count}")
        
        if sensor_agent.event_log:
            print(f"\nRecent Events:")
            for log in sensor_agent.event_log[-5:]:  # Show last 5
                print(f"  - {log['event_id']}: {log['disaster_type']} "
                      f"at {log['location']['name']} "
                      f"(Severity: {log['severity']})")
            
            print(f"\n✓ Event log saved to: disaster_events_log_{datetime.now().strftime('%Y%m%d')}.json")
        
        # Stop the agent
        await sensor_agent.stop()
        
        # Cancel all tasks
        for task in tasks:
            task.cancel()
        
        # Wait for tasks to complete
        await asyncio.gather(*tasks, return_exceptions=True)
        
        print("\n" + "=" * 70)
        print(" SensorAgent stopped successfully")
        print(" Lab 2 demonstration complete!")
        print("=" * 70 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
