@echo off
echo ========================================
echo JARVIS GitHub Upload Helper
echo ========================================

echo.
echo This script will help you upload your JARVIS project to GitHub.
echo Please follow the instructions below:
echo.

echo 1. First, create a new repository on GitHub:
echo    - Go to https://github.com/new
echo    - Sign in to your GitHub account
echo    - Enter a repository name (e.g., "jarvis")
echo    - Choose if it should be Public or Private
echo    - DO NOT initialize with a README
echo    - Click "Create repository"
echo.

pause

echo.
echo 2. Copy the HTTPS or SSH URL of your new repository
echo    It should look like: https://github.com/yourusername/repositoryname.git
echo    or: git@github.com:yourusername/repositoryname.git
echo.

set /p repo_url="Enter your repository URL: "

if "%repo_url%"=="" (
    echo Error: No repository URL provided
    pause
    exit /b 1
)

echo.
echo 3. Setting up remote repository...
cd /d "c:\Users\Jaikeerthi\Music\jarvis"
git remote add origin %repo_url%
if %errorlevel% neq 0 (
    echo Warning: Remote might already be set. Continuing...
)

echo.
echo 4. Setting main branch...
git branch -M main
if %errorlevel% neq 0 (
    echo Warning: Could not set main branch. Continuing...
)

echo.
echo 5. Pushing to GitHub...
echo This may take a few minutes depending on your internet connection...
git push -u origin main

if %errorlevel% neq 0 (
    echo.
    echo Error: Failed to push to GitHub
    echo Please check your internet connection and repository URL
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! Your JARVIS project has been uploaded to GitHub!
echo ========================================
echo.
echo You can now access your repository at: %repo_url%
echo.
echo To update your repository in the future:
echo   cd c:\Users\Jaikeerthi\Music\jarvis
echo   git add .
echo   git commit -m "Your commit message"
echo   git push
echo.
pause