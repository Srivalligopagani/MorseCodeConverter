# PROJECT TITLE: MORSE CODE CONVERTER

A Python-based application that converts English text to Morse code and Morse code back to English.
It demonstrates the power of string manipulation, data mapping, and logic control flow, making it a great beginner project in Python.

# Core User Features 🔠

Text to Morse Conversion:
Convert any English sentence into Morse code with dots (.) and dashes (-) following international Morse standards.

Morse to Text Conversion:
Decode Morse code back into human-readable English text instantly.

Error Handling:
Automatically detects invalid Morse sequences or unsupported characters and notifies the user.

Extensible Design:
Easily expandable to include sound playback or a web-based GUI interface.

# Project Structure
MORSE CODE CONVERTER/
│
|---src/                 # Core logic files
|   |---morse_logic.py   # Conversion logic for text ↔ Morse
|   |__morse_dict.py     # Character-to-Morse dictionary
|
|---api/                 # Backend API (Optional Flask version)
|   |__app.py            # Flask endpoints for conversions
|
|---frontend/            # Frontend interface (optional)
|   |__app.py            # Streamlit or HTML interface
|
|___requirements.txt     # Python dependencies
|
|___README.md            # Project documentation
|
|____.env                # Environment variables (if any)

# Quick Start
Prerequisites

Python 3.8 or higher

Git (for cloning the project)

1. Clone or Download the Project

Option 1: Clone with Git

git clone <repository-url>


Option 2: Download and extract the ZIP file

2. Install Dependencies
pip install -r requirements.txt

3. Run the Application
Command-Line Version
python src/morse_logic.py


You’ll be prompted to enter text or Morse code, and the output will appear immediately.

Streamlit Frontend (Optional)
streamlit run frontend/app.py


The app will open in your browser at http://localhost:8501

Flask Backend (Optional)
cd api
python app.py

# How to Use

Run the program.

Choose a conversion mode:

Type English text to get Morse code output.

Type Morse code (using . and - separated by spaces) to get English translation.

View results directly in the console or UI.

Example:

Input (Text → Morse): HELLO WORLD
Output: .... . .-.. .-.. --- / .-- --- .-. .-.. -..

Input (Morse → Text): .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Output: HELLO WORLD

Technical Details
Technologies Used

Language: Python 3.8+

Frontend: Streamlit (Optional)

Backend: Flask (Optional REST API)

Data Structure: Python Dictionary

# Key Components

src/morse_dict.py

Contains mappings between characters and Morse code.

Used for both encoding and decoding.

src/morse_logic.py

Core logic for text-to-Morse and Morse-to-text conversion.

Includes validation and formatting.

api/app.py (optional)

Flask API providing /encode and /decode endpoints.

frontend/app.py (optional)

Streamlit web interface for user-friendly interaction.

Future Enhancements

Ideas for extending this project:

Audio Playback: Play Morse sounds (dots and dashes).

User Authentication: Save favorite phrases or messages.

File Conversion: Encode/decode text files.

Morse Trainer Mode: Help users learn Morse code interactively.

Support

For queries, improvements, or contributions, feel free to open an issue or pull request on the project repository.

