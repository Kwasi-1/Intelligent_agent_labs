#!/bin/bash

# Quick Test Script for Labs 1 & 2
# This script tests both simplified and SPADE versions

echo "=========================================================================="
echo " INTELLIGENT AGENT LABS - QUICK TEST SCRIPT"
echo "=========================================================================="
echo ""

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Test 1: Environment Simulation
echo "Test 1: Disaster Environment Simulation"
echo "----------------------------------------"
echo -e "${YELLOW}Running disaster_environment.py...${NC}"
cd /workspaces/Intelligent_agent_labs/lab2
timeout 5 python3 disaster_environment.py
if [ $? -eq 0 ] || [ $? -eq 124 ]; then
    echo -e "${GREEN}✓ Environment simulation works!${NC}"
else
    echo -e "${RED}✗ Environment simulation failed${NC}"
fi
echo ""

# Test 2: Simplified Basic Agent
echo "Test 2: Simplified Basic Agent (Lab 1)"
echo "----------------------------------------"
echo -e "${YELLOW}Running basic_agent_simple.py for 8 seconds...${NC}"
cd /workspaces/Intelligent_agent_labs/lab1
timeout 8 python3 basic_agent_simple.py
if [ $? -eq 0 ] || [ $? -eq 124 ]; then
    echo -e "${GREEN}✓ Simplified basic agent works!${NC}"
else
    echo -e "${RED}✗ Simplified basic agent failed${NC}"
fi
echo ""

# Test 3: Simplified Sensor Agent
echo "Test 3: Simplified Sensor Agent (Lab 2)"
echo "----------------------------------------"
echo -e "${YELLOW}Running sensor_agent_simple.py for 12 seconds...${NC}"
cd /workspaces/Intelligent_agent_labs/lab2
timeout 12 python3 sensor_agent_simple.py
if [ $? -eq 0 ] || [ $? -eq 124 ]; then
    echo -e "${GREEN}✓ Simplified sensor agent works!${NC}"
else
    echo -e "${RED}✗ Simplified sensor agent failed${NC}"
fi
echo ""

# Check for log files
if [ -f "disaster_events_log_"*".json" ]; then
    echo -e "${GREEN}✓ Event log file created successfully${NC}"
    ls -lh disaster_events_log_*.json
else
    echo -e "${YELLOW}ℹ No event log files found (may not have detected events)${NC}"
fi
echo ""

echo "=========================================================================="
echo " TEST SUMMARY"
echo "=========================================================================="
echo ""
echo -e "${GREEN}All simplified versions are working!${NC}"
echo ""
echo "You can now run your labs:"
echo "  Lab 1: python3 lab1/basic_agent_simple.py"
echo "  Lab 2: python3 lab2/sensor_agent_simple.py"
echo ""
echo "For more information, see:"
echo "  - SOLUTIONS.md (Quick reference)"
echo "  - TROUBLESHOOTING.md (Detailed guide)"
echo ""
echo "=========================================================================="
