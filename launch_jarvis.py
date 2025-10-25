import os
import sys
import subprocess

def launch_jarvis():
    """
    Launch JARVIS with a simple double-click
    """
    try:
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Change to the jarvis directory where run.py is located
        jarvis_dir = os.path.join(script_dir, "jarvis")
        os.chdir(jarvis_dir)
        
        print("Launching JARVIS Assistant...")
        print("Please wait while JARVIS initializes...")
        
        # Run the main JARVIS runner script
        subprocess.run([sys.executable, "run.py"], check=True)
        
    except KeyboardInterrupt:
        print("\nJARVIS shutdown requested.")
    except subprocess.CalledProcessError as e:
        print(f"Error running JARVIS: {e}")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"Unexpected error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    launch_jarvis()