"""
Lab 1: Basic Agent (Simplified Standalone Version)
Course: DCIT 403 - Designing Intelligent Agent
Project: Disaster Response & Relief Coordination System

This is a simplified version that runs WITHOUT requiring an XMPP server.
It demonstrates the core agent concepts without the network complexity.
"""

import asyncio
from datetime import datetime
import time


class BasicBehaviour:
    """
    A simple periodic behavior that runs every few seconds
    """
    
    def __init__(self, agent, period=3.0):
        self.agent = agent
        self.period = period
        self.running = False
    
    async def run(self):
        """
        This method is called periodically
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] BasicAgent is running...")
        print(f"  - Agent Name: {self.agent.name}")
        print(f"  - Behavior executing periodic task")
        print(f"  - Status: Active and responsive")
        print("-" * 50)
    
    async def start(self):
        """Start the behavior loop"""
        self.running = True
        while self.running:
            await self.run()
            await asyncio.sleep(self.period)
    
    def stop(self):
        """Stop the behavior"""
        self.running = False


class BasicAgent:
    """
    A basic agent that demonstrates fundamental agent functionality
    (Simplified standalone version)
    """
    
    def __init__(self, name):
        self.name = name
        self.behaviours = []
    
    async def setup(self):
        """
        Called when the agent is started. 
        This is where we initialize behaviors.
        """
        print("\n" + "=" * 50)
        print("BASIC AGENT SETUP")
        print("=" * 50)
        print(f"Agent Name: {self.name}")
        print(f"Agent initialized at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50 + "\n")
        
        # Add a periodic behavior that runs every 3 seconds
        periodic_behaviour = BasicBehaviour(self, period=3.0)
        self.behaviours.append(periodic_behaviour)
        
        print("✓ Periodic behavior added (runs every 3 seconds)")
        print("✓ Agent is now active and running\n")
    
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
    Main function to create and run the agent
    """
    print("\n" + "=" * 70)
    print(" LAB 1: BASIC AGENT DEMONSTRATION (Simplified Standalone Version)")
    print(" Course: DCIT 403 - Designing Intelligent Agent")
    print(" Project: Disaster Response & Relief Coordination System")
    print("=" * 70)
    print("\nThis version runs WITHOUT requiring an XMPP server")
    print("Press Ctrl+C to stop the agent\n")
    
    agent_name = "BasicAgent-1"
    
    print(f"Starting agent: {agent_name}\n")
    
    # Create and start the agent
    agent = BasicAgent(agent_name)
    tasks = await agent.start()
    
    print("Agent started successfully!")
    print("Waiting for agent to run...\n")
    
    # Keep the agent running
    try:
        # Run for 20 seconds to demonstrate periodic behavior
        await asyncio.sleep(20)
    except KeyboardInterrupt:
        print("\n\nShutting down agent...")
    
    # Stop the agent
    await agent.stop()
    
    # Cancel all tasks
    for task in tasks:
        task.cancel()
    
    # Wait for tasks to complete
    await asyncio.gather(*tasks, return_exceptions=True)
    
    print("\n" + "=" * 70)
    print("Agent stopped successfully")
    print("Lab 1 demonstration complete!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
