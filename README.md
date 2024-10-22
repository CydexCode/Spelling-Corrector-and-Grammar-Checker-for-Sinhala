# Sinhala Spell and Grammar Checker

This project is a **Sinhala Spell and Grammar Checker** that helps users write error-free Sinhala text. It provides functionalities for detecting and correcting common spelling and grammatical errors in Sinhala, using a custom-built dictionary and basic grammar-checking rules. The tool is built with Python and features an interactive graphical user interface (GUI).

## Features

- **Spell Checking**
  - Identifies misspelled Sinhala words based on a custom dictionary.
  - Highlights misspelled words in the results section.

- **Grammar Checking**
  - Detects common grammar issues, such as repeated words and missing punctuation.
  - Suggests corrections to improve text readability and quality.

![Screenshot 2024-10-22 124230](https://github.com/user-attachments/assets/5c9cfef2-7fa1-491d-b170-45748b498611)

- **Auto-Correction**
  - Automatically corrects spelling mistakes by finding the closest match from the dictionary.
  - Corrects basic grammar mistakes, such as repeated words and adding missing punctuation.
    
![Screenshot 2024-10-22 124247](https://github.com/user-attachments/assets/9f73ecef-e6d7-4d7c-a0fd-ea145dcb4f41)


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
