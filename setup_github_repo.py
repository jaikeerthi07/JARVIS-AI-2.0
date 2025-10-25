#!/usr/bin/env python3
"""
Script to help set up JARVIS project for GitHub upload
"""

import os
import sys
import subprocess
import shutil

def check_git_installed():
    """Check if Git is installed"""
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Git is installed: {result.stdout.strip()}")
            return True
        else:
            print("❌ Git is not installed or not in PATH")
            return False
    except FileNotFoundError:
        print("❌ Git is not installed or not in PATH")
        return False

def setup_git_config():
    """Set up Git user configuration"""
    try:
        # Try to get existing config
        email_result = subprocess.run(['git', 'config', '--global', 'user.email'], 
                                    capture_output=True, text=True)
        name_result = subprocess.run(['git', 'config', '--global', 'user.name'], 
                                   capture_output=True, text=True)
        
        if email_result.returncode == 0 and name_result.returncode == 0:
            email = email_result.stdout.strip()
            name = name_result.stdout.strip()
            if email and name:
                print(f"✅ Git user already configured: {name} <{email}>")
                return True
        
        # Set default config
        default_email = "jarvis@example.com"
        default_name = "JARVIS Developer"
        
        subprocess.run(['git', 'config', '--global', 'user.email', default_email], 
                      capture_output=True)
        subprocess.run(['git', 'config', '--global', 'user.name', default_name], 
                      capture_output=True)
        
        print(f"✅ Git user configured: {default_name} <{default_email}>")
        return True
    except Exception as e:
        print(f"❌ Error setting up Git config: {e}")
        return False

def initialize_git_repo():
    """Initialize a Git repository in the JARVIS project directory"""
    project_path = r"c:\Users\Jaikeerthi\Music\jarvis"
    
    if not os.path.exists(project_path):
        print(f"❌ Project path does not exist: {project_path}")
        return False
    
    try:
        # Change to project directory
        os.chdir(project_path)
        print(f"📁 Working in directory: {project_path}")
        
        # Check if already a git repo
        if os.path.exists('.git'):
            print("✅ Git repository already initialized")
        else:
            # Initialize git repository
            result = subprocess.run(['git', 'init'], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Git repository initialized successfully")
            else:
                print(f"❌ Failed to initialize Git repository: {result.stderr}")
                return False
        
        return True
    except Exception as e:
        print(f"❌ Error changing directory or initializing repo: {e}")
        return False

def create_gitignore():
    """Create a .gitignore file for the JARVIS project"""
    gitignore_content = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak
venv.bak

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# IDE files
.vscode/
.idea/
*.swp
*.swo
*~

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# JARVIS specific files
*.db
*.log
*.tmp
*.temp
secrets.json
api_config.py
cookies.json

# Audio files
*.mp3
*.wav
*.m4a

# Model files (large files)
*.pb
*.pbtxt
*.onnx
*.h5
*.pt
*.pth

# Training data
trainer/
samples/

# Generated files
generated_websites/
website_builder_cache/
"""
    
    try:
        with open('.gitignore', 'w') as f:
            f.write(gitignore_content)
        print("✅ .gitignore file created successfully")
        return True
    except Exception as e:
        print(f"❌ Error creating .gitignore file: {e}")
        return False

def create_readme():
    """Create a README.md file for the JARVIS project"""
    readme_content = """# JARVIS - Just A Rather Very Intelligent System

![JARVIS Iron Man Assistant](jarvis/www/jarvis_ironman.png)

JARVIS is an advanced voice-controlled personal assistant inspired by the Iron Man movies. It features face recognition, voice commands, web browsing, application control, and much more.

## Features

- Voice Recognition and Text-to-Speech
- Face Recognition and Authentication
- Web Search and Browsing
- Application Control
- Media Playback
- Email and Calendar Integration
- AI-Powered Chatbot
- Website Builder
- Math and Science Expert
- Emotion Detection
- Red Activation Mode (Special Feature)

## Prerequisites

- Python 3.8 or higher
- Windows OS (recommended)
- Camera for face recognition
- Microphone for voice commands

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/jarvis.git
   cd jarvis
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Install additional requirements:
   ```bash
   pip install -r requirements_advanced.txt
   ```

4. Set up API keys in `jarvis/engine/api_config.py`:
   - Groq API Key
   - SerpAPI Key
   - Google API credentials (optional)

## Usage

Run JARVIS using the batch script:
```bash
jarvis\\run_jarvis.bat
```

Or directly with Python:
```bash
cd jarvis
python run.py
```

## Voice Commands

- "Hello JARVIS" - Greeting
- "Open [application/website]" - Launch applications or websites
- "Play [song] on YouTube" - Play music videos
- "What is [query]?" - Ask questions
- "Activated JARVIS to reddot" - Activate red mode
- "JARVIS normal mode" - Deactivate red mode

## Project Structure

```
jarvis/
├── engine/                 # Core functionality
│   ├── auth/              # Face recognition authentication
│   ├── models/            # AI models
│   ├── features.py        # Feature implementations
│   ├── command.py         # Command processing
│   └── api_config.py      # API configuration
├── www/                   # Web interface
│   ├── index.html         # Main interface
│   ├── style.css          # Styling
│   └── assets/            # Images, audio, etc.
├── requirements.txt       # Python dependencies
└── run.py                 # Main entry point
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by JARVIS from Iron Man movies
- Uses various open-source libraries and APIs
"""
    
    try:
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print("✅ README.md file created successfully")
        return True
    except Exception as e:
        print(f"❌ Error creating README.md file: {e}")
        return False

def setup_github_repo():
    """Main function to set up the GitHub repository"""
    print("🚀 Setting up JARVIS project for GitHub upload...")
    
    # Check if Git is installed
    if not check_git_installed():
        print("Please install Git first: https://git-scm.com/downloads")
        return False
    
    # Set up Git configuration
    print("\n👤 Setting up Git configuration...")
    if not setup_git_config():
        print("⚠️  Warning: Could not set up Git configuration")
    
    # Initialize Git repository
    if not initialize_git_repo():
        return False
    
    # Create .gitignore file
    print("\n📝 Creating .gitignore file...")
    if not create_gitignore():
        return False
    
    # Create README.md file
    print("\n📝 Creating README.md file...")
    if not create_readme():
        return False
    
    # Add files to git
    print("\n➕ Adding files to Git...")
    try:
        subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
        print("✅ All files added to Git")
    except Exception as e:
        print(f"❌ Error adding files to Git: {e}")
        return False
    
    # Make initial commit
    print("\n💾 Making initial commit...")
    try:
        result = subprocess.run(['git', 'commit', '-m', 'Initial commit: JARVIS project setup'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Initial commit created successfully")
        else:
            print(f"⚠️  Commit message: {result.stderr}")
    except Exception as e:
        print(f"❌ Error making initial commit: {e}")
        return False
    
    print("\n🎉 GitHub repository setup complete!")
    print("\nNext steps to publish to GitHub:")
    print("1. Create a new repository on GitHub (https://github.com/new)")
    print("2. Copy the repository URL")
    print("3. Run: git remote add origin YOUR_REPOSITORY_URL")
    print("4. Run: git branch -M main")
    print("5. Run: git push -u origin main")
    
    return True

if __name__ == "__main__":
    success = setup_github_repo()
    if success:
        print("\n✅ JARVIS project is ready for GitHub upload!")
    else:
        print("\n❌ There were issues setting up the GitHub repository.")
        sys.exit(1)