"""
Lab 1: Environment Verification Script
This script checks if all required components are properly installed
"""

import sys

def check_python_version():
    """Check if Python version is 3.9 or higher"""
    version = sys.version_info
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 9:
        return True
    else:
        print("  ⚠ Warning: Python 3.9+ recommended")
        return False

def check_spade():
    """Check if SPADE is installed"""
    try:
        import spade
        print(f"✓ SPADE {spade.__version__}")
        return True
    except ImportError:
        print("✗ SPADE not installed")
        return False

def check_aiohttp():
    """Check if aiohttp is installed"""
    try:
        import aiohttp
        print(f"✓ aiohttp {aiohttp.__version__}")
        return True
    except ImportError:
        print("✗ aiohttp not installed")
        return False

def check_prosody():
    """Check if Prosody is running"""
    import subprocess
    try:
        result = subprocess.run(
            ['sudo', 'prosodyctl', 'status'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if 'running' in result.stdout.lower():
            print("✓ Prosody XMPP server is running")
            return True
        else:
            print("✗ Prosody is not running")
            print("  Run: cd lab1 && sudo bash setup_xmpp.sh")
            return False
    except Exception as e:
        print("✗ Could not check Prosody status")
        print(f"  Error: {e}")
        return False

def main():
    """Run all checks"""
    print("\n" + "=" * 60)
    print(" LAB 1: ENVIRONMENT VERIFICATION")
    print("=" * 60 + "\n")
    
    checks = []
    
    print("Checking required components:\n")
    checks.append(check_python_version())
    checks.append(check_spade())
    checks.append(check_aiohttp())
    checks.append(check_prosody())
    
    print("\n" + "=" * 60)
    if all(checks):
        print("✓ All components are properly installed!")
        print("✓ Environment is ready for agent development")
        print("\nNext step: Run the basic agent")
        print("  python3 lab1/basic_agent.py")
    else:
        print("⚠ Some components need attention")
        print("\nTo install missing components:")
        print("  cd lab1")
        print("  chmod +x install_dependencies.sh")
        print("  bash install_dependencies.sh")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
