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
import os
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
    # Agent credentials (can be provided via environment variables)
    AGENT_JID = os.getenv("XMPP_JID", "agent1@localhost")
    AGENT_PASSWORD = os.getenv("XMPP_PASSWORD", "agent123")
    # VERIFY_SECURITY: set to "true" to enable cert verification (recommended for remote servers)
    VERIFY_SECURITY = os.getenv("VERIFY_SECURITY", "false").lower() in ("1", "true", "yes")
    
    print("\n" + "=" * 70)
    print(" LAB 1: BASIC SPADE AGENT DEMONSTRATION")
    print(" Course: DCIT 403 - Designing Intelligent Agent")
    print(" Project: Disaster Response & Relief Coordination System")
    print("=" * 70)
    print(f"\nStarting agent: {AGENT_JID}")
    print("Press Ctrl+C to stop the agent\n")
    
    # Create and start the agent
    agent = BasicAgent(AGENT_JID, AGENT_PASSWORD)

    # Control SSL verification via environment variable
    agent.verify_security = VERIFY_SECURITY
    
    try:
        # Try to start with timeout
        await asyncio.wait_for(agent.start(), timeout=10.0)
        
        print("Agent started successfully!")
        print("Waiting for agent to run...\n")
        
        # Keep the agent running
        try:
            # Run for 20 seconds to demonstrate periodic behavior
            await asyncio.sleep(20)
        except KeyboardInterrupt:
            print("\n\nShutting down agent...")
        
    except asyncio.TimeoutError:
        print("\n⚠️  ERROR: Connection timeout!")
        print("\nPossible causes:")
        print("  1. XMPP server (Prosody) is not running")
        print("  2. Incorrect server address or port")
        print("  3. Network connectivity issues")
        print("\nSolutions:")
        print("  1. Start Prosody: cd lab1 && bash start_prosody_container.sh")
        print("  2. Use the simplified version: python3 lab1/basic_agent_simple.py")
        print("\n" + "="*70)
        return
    except Exception as e:
        print(f"\n⚠️  ERROR: Failed to start agent: {e}")
        print(f"\nError type: {type(e).__name__}")
        print("\nSolutions:")
        print("  1. Check if Prosody is running: bash lab1/start_prosody_container.sh")
        print("  2. Try the simplified version: python3 lab1/basic_agent_simple.py")
        print("\n" + "="*70)
        return
    
    # Stop the agent
    await agent.stop()
    print("\n" + "=" * 70)
    print("Agent stopped successfully")
    print("Lab 1 demonstration complete!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
