# JARVIS-AI-2.0 - Just A Rather Very Intelligent System

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
   git clone https://github.com/jaikeerthi07/JARVIS-AI-2.0.git
   cd JARVIS-AI-2.0
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
jarvis\run_jarvis.bat
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