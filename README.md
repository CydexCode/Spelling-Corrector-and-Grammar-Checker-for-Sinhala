# Sinhala Spell and Grammar Checker

This project is a **Sinhala Spell and Grammar Checker** that helps users write error-free Sinhala text. It provides functionalities for detecting and correcting common spelling and grammatical errors in Sinhala, using a custom-built dictionary and basic grammar-checking rules. The tool is built with Python and features an interactive graphical user interface (GUI).

![Screenshot 2024-10-22 125508](https://github.com/user-attachments/assets/11898157-0c3e-415d-9553-0444ee2450f6)

## Features

- **Spell Checking**
  - Identifies misspelled Sinhala words based on a custom dictionary.
  - Highlights misspelled words in the results section.

- **Grammar Checking**
  - Detects common grammar issues, such as repeated words and missing punctuation.
  - Suggests corrections to improve text readability and quality.

![Screenshot 2024-10-22 125625](https://github.com/user-attachments/assets/b20258ff-b441-4ce9-b5dd-43f88c538a0b)

- **Auto-Correction**
  - Automatically corrects spelling mistakes by finding the closest match from the dictionary.
  - Corrects basic grammar mistakes, such as repeated words and adding missing punctuation.
    
![Screenshot 2024-10-22 125910](https://github.com/user-attachments/assets/b0580fde-b3b6-41be-bf40-4a35756aeafc)

## Technical Details

- **Programming Language:** Python
- **Libraries Used:** 
  - `tkinter` for the graphical user interface.
  - `re` for regular expression-based text processing.
  - `difflib` for finding close matches to misspelled words.

- **Graphical User Interface (GUI)**
  - Designed using `tkinter`, featuring sections for input, results, and action buttons.
  - Color-coded feedback for errors (red) and correct feedback (green).
  - Buttons for checking spelling and grammar, auto-correcting text, and resetting fields.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/sinhala-spell-and-grammar-checker.git
   cd sinhala-spell-and-grammar-checker
