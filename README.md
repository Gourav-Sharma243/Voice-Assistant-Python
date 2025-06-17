# Gourav's AI Voice Assistant

This is a simple voice-activated AI assistant built in Python. It can perform various desktop tasks like opening websites, telling jokes, playing music, checking the time, sending emails, and setting reminders — all through voice commands.

## 🧠 Features

- Voice interaction using `speech_recognition` and `pyttsx3`
- Open websites like YouTube, Google, Stack Overflow, GitHub, LinkedIn, etc.
- Search Wikipedia and Google
- Play random music via YouTube Music
- Send emails using Gmail SMTP
- Tell jokes to lighten your mood
- Set reminders (text-based; WIP for time-based alerts)
- Weather search via Google
- Launch desktop applications like Notepad, Calculator, VS Code, and Outlook

## 🛠️ Technologies Used

- Python 3.12+
- `pyttsx3` for text-to-speech
- `speech_recognition` for voice input
- `smtplib` for sending emails
- `os`, `webbrowser`, `random`, `datetime` for system operations
- `wikipedia` Python package for fetching summaries
- `pyaudio` for accessing the microphone

## 📦 Installation

1. **Clone this repository** or download the Python file directly.
2. **Install dependencies**:

```bash
pip install pyttsx3 speechrecognition wikipedia pyaudio
