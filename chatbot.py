import re
import random
import os
import nltk

# Explicitly tell NLTK to look for data in the local project folder (for Render)
nltk.data.path.append(os.path.abspath('./nltk_data'))

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [stemmer.stem(t) for t in tokens]
    return ' '.join(tokens)

rules = [
    {
        "patterns": [r"hello|hi|hey|good morning"],
        "responses": ["Hello! How can I help you today?",
                      "Hey there! What can I help you with?"]
    },
    {
        "patterns": [r"what is (ai|artificial intelligence)|explain ai"],
        "responses": ["AI is the simulation of human intelligence in machines. "
                      "It includes areas like machine learning, NLP, and robotics."]
    },
    {
        "patterns": [r"what is nlp|natural language processing"],
        "responses": ["NLP stands for Natural Language Processing. It is a branch of AI "
                      "that helps computers understand and process human language."]
    },
    {
        "patterns": [r"what is nltk|natural language toolkit"],
        "responses": ["NLTK is a Python library used for NLP tasks like tokenization, "
                      "stemming, and stopword removal."]
    },
    {
        "patterns": [r"study|study tips|how to study"],
        "responses": ["Try the Pomodoro technique — 25 minutes of focused study, "
                      "then a 5 minute break. Also practice active recall!"]
    },
    {
        "patterns": [r"exam|test|revision|prepare"],
        "responses": ["Start revision early, review past questions, sleep well "
                      "the night before, and eat before the exam!"]
    },
    {
        "patterns": [r"assignment|project|deadline|submission"],
        "responses": ["Break your assignment into smaller tasks with mini deadlines. "
                      "Start early and test your code frequently."]
    },
    {
        "patterns": [r"python|programming|coding|how to code"],
        "responses": ["Python is one of the best languages for beginners. "
                      "Practice on replit.com or w3schools.com to get started!"]
    },
    {
        "patterns": [r"machine learning|ml"],
        "responses": ["Machine Learning is a type of AI where systems learn from data "
                      "without being explicitly programmed. Examples include spam filters "
                      "and Netflix recommendations."]
    },
    {
        "patterns": [r"who are you|your name|what are you"],
        "responses": ["I am EduBot, a Rule-Based AI Chatbot built for CSC 309. "
                      "I use pattern matching to answer school-related questions!"]
    },
    {
        "patterns": [r"thank|thanks|thank you"],
        "responses": ["You're welcome! Good luck with your studies!",
                      "Anytime! Feel free to ask more questions."]
    },
    {
        "patterns": [r"bye|goodbye|exit|quit"],
        "responses": ["Goodbye! Good luck with your exams!"]
    },
]

def get_response(user_input):
    for rule in rules:
        for pattern in rule["patterns"]:
            if re.search(pattern, user_input, re.IGNORECASE):
                return random.choice(rule["responses"])
    return "I'm not sure about that. Try asking about AI, NLP, study tips, or exams!"
