#!/usr/bin/env python3
"""
Script to finalize the Git setup for the JARVIS project
"""

import os
import subprocess

def finalize_git_setup():
    """Finalize the Git setup for the JARVIS project"""
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
        
        print("\n🔄 Adding all files to Git...")
        result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ All files added to Git")
        else:
            print(f"❌ Error adding files: {result.stderr}")
            return False
        
        # Check if we're on master branch and rename to main if needed
        branch_result = subprocess.run(['git', 'branch', '--show-current'], 
                                     capture_output=True, text=True)
        if branch_result.returncode == 0:
            current_branch = branch_result.stdout.strip()
            print(f"\n📍 Current branch: {current_branch}")
            
            if current_branch == "master":
                print("🔄 Renaming branch from master to main...")
                subprocess.run(['git', 'branch', '-m', 'master', 'main'], 
                             capture_output=True, text=True)
                print("✅ Branch renamed to main")
        
        # Check if we have uncommitted changes
        status_result = subprocess.run(['git', 'status', '--porcelain'], 
                                     capture_output=True, text=True)
        if status_result.stdout.strip():
            print("\n💾 Committing remaining changes...")
            commit_result = subprocess.run(['git', 'commit', '-m', 'Add GitHub setup scripts'], 
                                         capture_output=True, text=True)
            if commit_result.returncode == 0:
                print("✅ Changes committed successfully")
            else:
                print(f"⚠️  Commit warning: {commit_result.stderr}")
        else:
            print("\n✅ No changes to commit")
        
        print("\n✅ Git setup finalized successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error finalizing Git setup: {e}")
        return False

def show_final_status():
    """Show the final Git status"""
    try:
        print("\n🔍 Final Git Status:")
        print("=" * 50)
        
        # Get git status
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        
        print("\n🔄 Recent Commits:")
        print("=" * 50)
        
        # Get recent commits
        result = subprocess.run(['git', 'log', '--oneline', '-5'], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        
        print("\n🌐 Branch Information:")
        print("=" * 50)
        
        # Get branch info
        result = subprocess.run(['git', 'branch'], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        
        return True
    except Exception as e:
        print(f"❌ Error showing final status: {e}")
        return False

if __name__ == "__main__":
    print("🔧 Finalizing JARVIS Git Setup...")
    success = finalize_git_setup()
    
    if success:
        show_final_status()
        print("\n🎉 JARVIS Git setup is now complete!")
        print("\nTo upload to GitHub, run: upload_to_github.bat")
    else:
        print("\n❌ Error finalizing Git setup!")