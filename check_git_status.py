#!/usr/bin/env python3
"""
Script to check the Git status of the JARVIS project
"""

import os
import subprocess

def check_git_status():
    """Check the Git status of the JARVIS project"""
    project_path = r"c:\Users\Jaikeerthi\Music\jarvis"
    
    if not os.path.exists(project_path):
        print(f"❌ Project path does not exist: {project_path}")
        return False
    
    try:
        # Change to project directory
        os.chdir(project_path)
        print(f"📁 Working in directory: {project_path}")
        
        # Check if it's a git repo
        if not os.path.exists('.git'):
            print("❌ This is not a Git repository")
            return False
        
        print("\n🔍 Git Status:")
        print("=" * 50)
        
        # Get git status
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"❌ Error getting git status: {result.stderr}")
            return False
        
        print("\n🔄 Recent Commits:")
        print("=" * 50)
        
        # Get recent commits
        result = subprocess.run(['git', 'log', '--oneline', '-5'], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print("No commits found or error getting commit history")
        
        print("\n🌐 Remote Repositories:")
        print("=" * 50)
        
        # Get remote repositories
        result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True)
        if result.returncode == 0:
            remotes = result.stdout.strip()
            if remotes:
                print(remotes)
            else:
                print("No remote repositories configured")
        else:
            print("Error getting remote repositories")
        
        return True
        
    except Exception as e:
        print(f"❌ Error checking Git status: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Checking JARVIS Git Repository Status...")
    success = check_git_status()
    if success:
        print("\n✅ Git repository status check completed!")
    else:
        print("\n❌ Error checking Git repository status!")