#!/usr/bin/env python3
import json
import os
import platform
import subprocess
from datetime import datetime, timezone
import pwd

def get_shell_info():
    """Get shell name and version"""
    try:
        shell_path = os.environ.get('SHELL', '/bin/bash')
        shell_name = os.path.basename(shell_path)
        
        # Try to get shell version
        try:
            if shell_name == 'zsh':
                result = subprocess.run(['zsh', '--version'], capture_output=True, text=True)
                version = result.stdout.strip().split()[-1]
            elif shell_name == 'bash':
                result = subprocess.run(['bash', '--version'], capture_output=True, text=True)
                version = result.stdout.split()[3].split('(')[0]
            else:
                version = "unknown"
        except:
            version = "unknown"
            
        return {"name": shell_name, "version": version}
    except:
        return {"name": "unknown", "version": "unknown"}

def get_os_info():
    """Get operating system information"""
    system = platform.system()
    
    if system == "Linux":
        try:
            # Try to get distribution info
            with open('/etc/os-release', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith('NAME='):
                        dist = line.split('=')[1].strip().strip('"')
                        break
                else:
                    dist = "Unknown"
        except:
            dist = "Unknown"
        
        return {"platform": system, "distribution": dist}
    else:
        return {"platform": system, "distribution": "N/A"}

def generate_context():
    """Generate execution context"""
    current_dir = os.getcwd()
    home_dir = os.path.expanduser("~")
    current_time = datetime.now(timezone.utc).isoformat()
    
    context = {
        "execution_context": {
            "directory_state": {
                "pwd": current_dir,
                "home": home_dir
            },
            "operating_system": get_os_info(),
            "current_time": current_time,
            "shell": get_shell_info()
        }
    }
    
    return context

def save_context(filename="context.json"):
    """Save context to JSON file"""
    context = generate_context()
    with open(filename, 'w') as f:
        json.dump(context, f, indent=2)
    print(f"Context saved to {filename}")

def print_context():
    """Print context to stdout"""
    context = generate_context()
    print(json.dumps(context, indent=2))

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--save":
            save_context()
        elif sys.argv[1] == "--help":
            print("Usage:")
            print("  python3 context_generator.py           - Print context to stdout")
            print("  python3 context_generator.py --save    - Save context to context.json")
            print("  python3 context_generator.py --help    - Show this help")
    else:
        print_context()
