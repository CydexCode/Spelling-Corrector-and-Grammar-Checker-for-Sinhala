import tkinter as tk
from tkinter import scrolledtext, messagebox
import re
from collections import Counter

def preprocess_text(text):
    """
    Preprocess the given text by removing unwanted characters and normalizing it.
    This function will keep only Sinhala characters and spaces.
    """
    # Keep only Sinhala characters (Unicode range: U+0D80 to U+0DFF) and spaces
    text = re.sub(r'[^\u0D80-\u0DFF\s]', '', text)
    # Convert to lowercase and trim any extra spaces
    text = text.strip().lower()
    return text

def tokenize(text):
    """
    Tokenize the text by splitting it into individual words based on spaces.
    """
    # Split the text based on whitespace to get individual words
    return text.split()

def load_dictionary():
    """
    Load the Sinhala dictionary from a file and return it as a set.
    """
    # Load the dictionary from the file
    with open('D:\MY\sem 7\AI\Project\Sinhala Spell and Grammar Checker\DictionaryCreation\sinhala_dictionary.txt', 'r', encoding='utf-8') as f:
        return set(f.read().splitlines())

def spell_check(text, dictionary):
    """
    Check for misspelled words in the given text.
    """
    # Preprocess and tokenize the input text
    words = tokenize(preprocess_text(text))
    # Identify misspelled words
    misspelled = [word for word in words if word not in dictionary]
    return misspelled

def basic_grammar_check(text):
    """
    Perform a basic grammar check on the given text.
    This function can be extended to include more advanced grammar rules.
    """
    grammar_issues = []
    
    # Example rule: Detect repeated words
    words = tokenize(preprocess_text(text))
    for i in range(len(words) - 1):
        if words[i] == words[i + 1]:
            grammar_issues.append(f"Repeated word: '{words[i]}'")

    # Example rule: Check for potential subject-verb agreement issues
    # (Can be extended with specific Sinhala language rules)
    
    return grammar_issues

# GUI setup
def run_spell_and_grammar_check():
    """
    Run the spell and grammar check on the input text and display the results.
    """
    input_text = text_area.get("1.0", tk.END)
    dictionary = load_dictionary()
    
    # Perform spell checking
    misspelled_words = spell_check(input_text, dictionary)
    spell_check_results = "No spelling errors found!" if not misspelled_words else "Misspelled words:\n" + ", ".join(misspelled_words)
    
    # Perform grammar checking
    grammar_issues = basic_grammar_check(input_text)
    grammar_check_results = "No grammar issues found!" if not grammar_issues else "Grammar issues:\n" + "\n".join(grammar_issues)
    
    # Display results in a message box
    result_message = f"{spell_check_results}\n\n{grammar_check_results}"
    messagebox.showinfo("Spell and Grammar Check Results", result_message)

# Create the main window
root = tk.Tk()
root.title("Sinhala Spell and Grammar Checker")
root.geometry("700x500")

# Add a label for instructions
label = tk.Label(root, text="Enter Sinhala text below:", font=("Arial", 14))
label.grid(column=0, row=0, padx=10, pady=10)

# Add a text area for input
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=("Arial", 12))
text_area.grid(column=0, row=1, padx=10, pady=10)

# Add a button to run the spell and grammar check
check_button = tk.Button(root, text="Check Spelling and Grammar", command=run_spell_and_grammar_check)
check_button.grid(column=0, row=2, padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
