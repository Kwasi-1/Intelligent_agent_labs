"""
Lab 1: Basic SPADE Agent
Course: DCIT 403 - Designing Intelligent Agent
Project: Disaster Response & Relief Coordination System

This script demonstrates a basic SPADE agent with:
- Periodic behavior
- Message handling
- Basic logging
"""

import asyncio
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
from spade.message import Message
from datetime import datetime
import time


class BasicBehaviour(PeriodicBehaviour):
    """
    A simple periodic behavior that runs every few seconds
    """
    
    async def run(self):
        """
        This method is called periodically
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] BasicAgent is running...")
        print(f"  - Agent Name: {self.agent.jid}")
        print(f"  - Behavior executing periodic task")
        print(f"  - Status: Active and responsive")
        print("-" * 50)


class BasicAgent(Agent):
    """
    A basic SPADE agent that demonstrates fundamental agent functionality
    """
    
    async def setup(self):
        """
        Called when the agent is started. 
        This is where we initialize behaviors.
        """
        print("\n" + "=" * 50)
        print("BASIC AGENT SETUP")
        print("=" * 50)
        print(f"Agent JID: {self.jid}")
        print(f"Agent initialized at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50 + "\n")
        
        # Add a periodic behavior that runs every 3 seconds
        periodic_behaviour = BasicBehaviour(period=3.0)
        self.add_behaviour(periodic_behaviour)
        
        print("✓ Periodic behavior added (runs every 3 seconds)")
        print("✓ Agent is now active and running\n")


async def main():
    """
    Main function to create and run the agent
    """
    # Agent credentials (must match XMPP server accounts)
    AGENT_JID = "agent1@localhost"
    AGENT_PASSWORD = "agent123"
    
    print("\n" + "=" * 70)
    print(" LAB 1: BASIC SPADE AGENT DEMONSTRATION")
    print(" Course: DCIT 403 - Designing Intelligent Agent")
    print(" Project: Disaster Response & Relief Coordination System")
    print("=" * 70)
    print(f"\nStarting agent: {AGENT_JID}")
    print("Press Ctrl+C to stop the agent\n")
    
    # Create and start the agent
    agent = BasicAgent(AGENT_JID, AGENT_PASSWORD)
    
    # Disable SSL verification for local development
    agent.verify_security = False
    
    await agent.start()
    
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
    print("\n" + "=" * 70)
    print("Agent stopped successfully")
    print("Lab 1 demonstration complete!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
