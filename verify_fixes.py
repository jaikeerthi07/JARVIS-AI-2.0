import os
import sys
import subprocess

def verify_fixes():
    """Verify that all fixes have been applied correctly"""
    print("Verifying JARVIS fixes...")
    
    # Check if we're in the right directory
    if not os.path.exists("jarvis"):
        print("Error: Not in the correct directory. Please run this script from the root directory.")
        return False
    
    # Change to jarvis directory
    jarvis_path = os.path.join(os.getcwd(), "jarvis")
    if not os.path.exists(jarvis_path):
        print("Error: jarvis directory not found!")
        return False
    
    # Check if database exists
    db_path = os.path.join(jarvis_path, "jarvis.db")
    if not os.path.exists(db_path):
        print("Error: Database file not found!")
        return False
    print("✓ Database file exists")
    
    # Check if config files exist
    config_path = os.path.join(jarvis_path, "engine", "config.py")
    if not os.path.exists(config_path):
        print("Error: Config file not found!")
        return False
    print("✓ Config file exists")
    
    # Check if required module files exist
    command_path = os.path.join(jarvis_path, "engine", "command.py")
    features_path = os.path.join(jarvis_path, "engine", "features.py")
    
    if not os.path.exists(command_path):
        print("Error: command.py file not found!")
        return False
    print("✓ command.py file exists")
    
    if not os.path.exists(features_path):
        print("Error: features.py file not found!")
        return False
    print("✓ features.py file exists")
    
    # Check if database has required tables
    try:
        import sqlite3
        con = sqlite3.connect(db_path)
        cursor = con.cursor()
        
        # Check sys_command table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sys_command'")
        if not cursor.fetchone():
            print("Error: sys_command table not found in database!")
            return False
        print("✓ sys_command table exists")
        
        # Check web_command table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='web_command'")
        if not cursor.fetchone():
            print("Error: web_command table not found in database!")
            return False
        print("✓ web_command table exists")
        
        con.close()
    except Exception as e:
        print(f"Error checking database: {e}")
        return False
    
    print("\nAll checks passed! JARVIS should now work correctly.")
    print("\nTo run JARVIS:")
    print("1. Double-click on run_jarvis_fixed.bat")
    print("2. Or run: cd jarvis && python run.py")
    return True

if __name__ == "__main__":
    verify_fixes()
def verify_fixes():
    """Verify that all fixes have been applied correctly"""
    print("Verifying JARVIS fixes...")
    
    # Check if we're in the right directory
    if not os.path.exists("jarvis"):
        print("Error: Not in the correct directory. Please run this script from the root directory.")
        return False
    
    # Change to jarvis directory
    jarvis_path = os.path.join(os.getcwd(), "jarvis")
    if not os.path.exists(jarvis_path):
        print("Error: jarvis directory not found!")
        return False
    
    # Check if database exists
    db_path = os.path.join(jarvis_path, "jarvis.db")
    if not os.path.exists(db_path):
        print("Error: Database file not found!")
        return False
    print("✓ Database file exists")
    
    # Check if config files exist
    config_path = os.path.join(jarvis_path, "engine", "config.py")
    if not os.path.exists(config_path):
        print("Error: Config file not found!")
        return False
    print("✓ Config file exists")
    
    # Check if required module files exist
    command_path = os.path.join(jarvis_path, "engine", "command.py")
    features_path = os.path.join(jarvis_path, "engine", "features.py")
    
    if not os.path.exists(command_path):
        print("Error: command.py file not found!")
        return False
    print("✓ command.py file exists")
    
    if not os.path.exists(features_path):
        print("Error: features.py file not found!")
        return False
    print("✓ features.py file exists")
    
    # Check if database has required tables
    try:
        import sqlite3
        con = sqlite3.connect(db_path)
        cursor = con.cursor()
        
        # Check sys_command table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sys_command'")
        if not cursor.fetchone():
            print("Error: sys_command table not found in database!")
            return False
        print("✓ sys_command table exists")
        
        # Check web_command table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='web_command'")
        if not cursor.fetchone():
            print("Error: web_command table not found in database!")
            return False
        print("✓ web_command table exists")
        
        con.close()
    except Exception as e:
        print(f"Error checking database: {e}")
        return False
    
    print("\nAll checks passed! JARVIS should now work correctly.")
    print("\nTo run JARVIS:")
    print("1. Double-click on run_jarvis_fixed.bat")
    print("2. Or run: cd jarvis && python run.py")
    return True

if __name__ == "__main__":
    verify_fixes()