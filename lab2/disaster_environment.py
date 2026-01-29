"""
Lab 2: Disaster Environment Simulation
Course: DCIT 403 - Designing Intelligent Agent
Project: Disaster Response & Relief Coordination System

This module simulates a disaster environment with various conditions
that agents can perceive and respond to.
"""

import random
import time
from datetime import datetime
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Tuple


class DisasterType(Enum):
    """Types of disasters that can occur"""
    FLOOD = "Flood"
    EARTHQUAKE = "Earthquake"
    FIRE = "Fire"
    STORM = "Storm"
    LANDSLIDE = "Landslide"


class SeverityLevel(Enum):
    """Severity levels for disasters"""
    LOW = 1
    MODERATE = 2
    HIGH = 3
    CRITICAL = 4
    CATASTROPHIC = 5


@dataclass
class Location:
    """Geographic location"""
    latitude: float
    longitude: float
    area_name: str
    
    def __str__(self):
        return f"{self.area_name} ({self.latitude:.4f}, {self.longitude:.4f})"


@dataclass
class DisasterEvent:
    """Represents a disaster event in the environment"""
    event_id: str
    disaster_type: DisasterType
    severity: SeverityLevel
    location: Location
    timestamp: datetime
    affected_population: int
    infrastructure_damage: float  # Percentage 0-100
    casualties: int
    description: str
    
    def __str__(self):
        return (f"Event {self.event_id}: {self.disaster_type.value} "
                f"(Severity: {self.severity.name}) at {self.location.area_name}")


class DisasterEnvironment:
    """
    Simulates a disaster-prone environment with dynamic conditions
    """
    
    def __init__(self, num_locations: int = 10):
        """
        Initialize the disaster environment
        
        Args:
            num_locations: Number of locations to monitor
        """
        self.locations = self._generate_locations(num_locations)
        self.active_events: List[DisasterEvent] = []
        self.event_counter = 0
        self.temperature = 25.0  # Celsius
        self.humidity = 60.0     # Percentage
        self.wind_speed = 10.0   # km/h
        self.rainfall = 0.0      # mm/hour
        
    def _generate_locations(self, num_locations: int) -> List[Location]:
        """Generate random locations to monitor"""
        area_names = [
            "Downtown District", "Riverside Area", "Highland Region",
            "Coastal Zone", "Industrial Park", "Residential Suburb",
            "Mountain Valley", "Port Area", "Agricultural Belt",
            "Commercial Center", "Old Town", "New Development"
        ]
        
        locations = []
        for i in range(num_locations):
            location = Location(
                latitude=random.uniform(5.0, 11.0),   # Ghana-like coordinates
                longitude=random.uniform(-3.0, 1.0),
                area_name=area_names[i % len(area_names)] + f" {i+1}"
            )
            locations.append(location)
        
        return locations
    
    def update_environmental_conditions(self):
        """Simulate changing environmental conditions"""
        # Temperature variation
        self.temperature += random.uniform(-2, 2)
        self.temperature = max(15, min(40, self.temperature))
        
        # Humidity variation
        self.humidity += random.uniform(-5, 5)
        self.humidity = max(20, min(100, self.humidity))
        
        # Wind speed variation
        self.wind_speed += random.uniform(-3, 3)
        self.wind_speed = max(0, min(80, self.wind_speed))
        
        # Rainfall variation
        self.rainfall += random.uniform(-5, 10)
        self.rainfall = max(0, min(150, self.rainfall))
    
    def generate_disaster_event(self) -> DisasterEvent:
        """
        Generate a random disaster event based on environmental conditions
        """
        self.event_counter += 1
        
        # Select disaster type with weighted probabilities
        disaster_weights = {
            DisasterType.FLOOD: 30 if self.rainfall > 50 else 10,
            DisasterType.FIRE: 25 if self.temperature > 35 else 10,
            DisasterType.STORM: 20 if self.wind_speed > 40 else 5,
            DisasterType.EARTHQUAKE: 15,
            DisasterType.LANDSLIDE: 20 if self.rainfall > 70 else 5
        }
        
        disaster_type = random.choices(
            list(disaster_weights.keys()),
            weights=list(disaster_weights.values())
        )[0]
        
        # Determine severity
        severity = random.choice(list(SeverityLevel))
        
        # Select random location
        location = random.choice(self.locations)
        
        # Calculate impact based on severity
        severity_multiplier = severity.value
        affected_population = random.randint(50, 500) * severity_multiplier
        infrastructure_damage = random.uniform(10, 30) * severity_multiplier
        infrastructure_damage = min(100, infrastructure_damage)
        casualties = int(affected_population * random.uniform(0.01, 0.05) * severity_multiplier)
        
        # Generate description
        descriptions = {
            DisasterType.FLOOD: f"Heavy flooding in {location.area_name} due to continuous rainfall",
            DisasterType.FIRE: f"Major fire outbreak in {location.area_name}, spreading rapidly",
            DisasterType.STORM: f"Severe storm with high winds affecting {location.area_name}",
            DisasterType.EARTHQUAKE: f"Earthquake detected in {location.area_name}, magnitude {severity.value + 2}",
            DisasterType.LANDSLIDE: f"Landslide reported in {location.area_name} due to soil saturation"
        }
        
        event = DisasterEvent(
            event_id=f"EVT-{self.event_counter:04d}",
            disaster_type=disaster_type,
            severity=severity,
            location=location,
            timestamp=datetime.now(),
            affected_population=affected_population,
            infrastructure_damage=infrastructure_damage,
            casualties=casualties,
            description=descriptions[disaster_type]
        )
        
        self.active_events.append(event)
        return event
    
    def get_environmental_readings(self) -> Dict[str, float]:
        """Get current environmental sensor readings"""
        return {
            "temperature": round(self.temperature, 1),
            "humidity": round(self.humidity, 1),
            "wind_speed": round(self.wind_speed, 1),
            "rainfall": round(self.rainfall, 1)
        }
    
    def should_generate_event(self) -> bool:
        """
        Determine if a new disaster event should occur
        Based on environmental conditions and randomness
        """
        # Base probability
        base_prob = 0.3
        
        # Increase probability based on harsh conditions
        if self.rainfall > 70:
            base_prob += 0.3
        if self.temperature > 38:
            base_prob += 0.2
        if self.wind_speed > 50:
            base_prob += 0.2
        
        return random.random() < base_prob
    
    def get_active_events(self) -> List[DisasterEvent]:
        """Get list of currently active disaster events"""
        return self.active_events.copy()
    
    def clear_old_events(self, max_age_seconds: int = 300):
        """Remove events older than specified age"""
        current_time = datetime.now()
        self.active_events = [
            event for event in self.active_events
            if (current_time - event.timestamp).seconds < max_age_seconds
        ]


# Test the environment if run directly
if __name__ == "__main__":
    print("=" * 70)
    print(" DISASTER ENVIRONMENT SIMULATION TEST")
    print("=" * 70)
    print()
    
    env = DisasterEnvironment(num_locations=5)
    
    print("Initial Environmental Conditions:")
    print(f"  Temperature: {env.temperature}°C")
    print(f"  Humidity: {env.humidity}%")
    print(f"  Wind Speed: {env.wind_speed} km/h")
    print(f"  Rainfall: {env.rainfall} mm/h")
    print()
    
    print("Monitoring locations:")
    for loc in env.locations:
        print(f"  - {loc}")
    print()
    
    print("Simulating 10 time steps...")
    print("-" * 70)
    
    for step in range(10):
        print(f"\nTime Step {step + 1}:")
        
        # Update environment
        env.update_environmental_conditions()
        readings = env.get_environmental_readings()
        print(f"  Conditions: Temp={readings['temperature']}°C, "
              f"Humidity={readings['humidity']}%, "
              f"Wind={readings['wind_speed']}km/h, "
              f"Rain={readings['rainfall']}mm/h")
        
        # Check for disaster
        if env.should_generate_event():
            event = env.generate_disaster_event()
            print(f"  ⚠ DISASTER DETECTED!")
            print(f"     {event}")
            print(f"     Severity: {event.severity.name}")
            print(f"     Affected: {event.affected_population} people")
            print(f"     Casualties: {event.casualties}")
            print(f"     Infrastructure Damage: {event.infrastructure_damage:.1f}%")
        else:
            print(f"  ✓ No disasters detected")
        
        time.sleep(0.5)
    
    print()
    print("=" * 70)
    print(f"Simulation complete. Total events: {len(env.active_events)}")
    print("=" * 70)
