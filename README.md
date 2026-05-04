# EduBot 🎓

EduBot is a Rule-Based AI Chatbot built for the CSC 309 Mini Project. It uses pattern matching techniques inspired by Python's NLTK (Natural Language Toolkit) to answer school-related questions, provide study tips, and explain fundamental computer science concepts.

## Features
- **Pattern Matching:** Uses predefined rules and regular expressions to understand and respond to user queries.
- **NLTK Concepts:** Demonstrates the logic behind tokenization, stopword removal, and stemming.
- **Modern UI:** A sleek, responsive, dark-themed chat interface with micro-animations.
- **Quick Suggestions:** Built-in suggestion chips to help users get started immediately.

## Technology Stack
- **Backend:** Python, Flask, NLTK (Natural Language Toolkit)
- **Frontend:** Vanilla HTML, CSS, JavaScript

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hillary3000-web/EduBot.git
   cd EduBot
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install flask nltk SpeechRecognition pyttsx3
   ```

3. **Download required NLTK data:**
   Open a Python shell and run:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

4. **Run the application:**
   Start the Flask server:
   ```bash
   python app.py
   ```

5. **Access the chatbot:**
   Open your browser and navigate to: `http://127.0.0.1:5000`

## Project Structure
- `app.py`: The main Flask server script handling routing and API endpoints.
- `chatbot.py`: The core rule-based matching engine containing all patterns and responses.
- `templates/index.html`: The front-end user interface.
