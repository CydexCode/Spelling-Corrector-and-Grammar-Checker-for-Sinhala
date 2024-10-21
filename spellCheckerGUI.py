import tkinter as tk
from tkinter import scrolledtext, messagebox
import re
from collections import Counter
import difflib  # Import difflib for finding closest matches

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
    return text.split()

def load_dictionary():
    """
    Load the Sinhala dictionary from a file and return it as a set.
    """
    with open(r'D:/MY/sem 7/AI/Project/Sinhala Spell and Grammar Checker/DictionaryCreation/sinhala_dictionary.txt', 'r', encoding='utf-8') as f:
        return set(f.read().splitlines())

def spell_check(text, dictionary):
    """
    Check for misspelled words in the given text.
    """
    words = tokenize(preprocess_text(text))
    misspelled = [word for word in words if word not in dictionary]
    return misspelled

def auto_correct(text, dictionary):
    """
    Auto correct the misspelled words by replacing them with the closest match from the dictionary.
    """
    words = tokenize(preprocess_text(text))
    corrected_words = []
    for word in words:
        if word in dictionary:
            corrected_words.append(word)
        else:
            # Find the closest match to the misspelled word
            closest_matches = difflib.get_close_matches(word, dictionary, n=1)
            if closest_matches:
                corrected_words.append(closest_matches[0])  # Use the closest match
            else:
                corrected_words.append(word)  # Keep the original word if no match is found
    return ' '.join(corrected_words)

def basic_grammar_check(text):
    """
    Perform a basic grammar check on the given text.
    This function can be extended to include more advanced grammar rules.
    """
    grammar_issues = []
    words = tokenize(preprocess_text(text))
    for i in range(len(words) - 1):
        if words[i] == words[i + 1]:
            grammar_issues.append(f"Repeated word: '{words[i]}'")
    return grammar_issues

def run_spell_and_grammar_check():
    """
    Run the spell and grammar check on the input text and display the results in the same window.
    """
    input_text = text_area.get("1.0", tk.END)
    dictionary = load_dictionary()
    
    misspelled_words = spell_check(input_text, dictionary)
    spell_check_results = "No spelling errors found!" if not misspelled_words else "Misspelled words:\n" + ", ".join(misspelled_words)
    
    grammar_issues = basic_grammar_check(input_text)
    grammar_check_results = "No grammar issues found!" if not grammar_issues else "Grammar issues:\n" + "\n".join(grammar_issues)
    
    result_text = f"{spell_check_results}\n\n{grammar_check_results}"
    result_area.delete("1.0", tk.END)  # Clear the result area
    result_area.insert(tk.END, result_text)

def auto_correct_text():
    """
    Automatically correct misspelled words in the input text.
    """
    input_text = text_area.get("1.0", tk.END)
    dictionary = load_dictionary()
    corrected_text = auto_correct(input_text, dictionary)
    
    # Replace the content in the text area with the corrected text
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, corrected_text)

def reset_text():
    """
    Clear the input text area and the result area.
    """
    text_area.delete("1.0", tk.END)
    result_area.delete("1.0", tk.END)

# GUI setup
root = tk.Tk()
root.title("Sinhala Spell and Grammar Checker")
root.geometry("700x600")

# Add a label for instructions
label = tk.Label(root, text="Enter Sinhala text below:", font=("Arial", 14))
label.grid(column=0, row=0, padx=10, pady=10)

# Add a text area for input
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15, font=("Arial", 12))
text_area.grid(column=0, row=1, padx=10, pady=10)

# Add a button to run the spell and grammar check
check_button = tk.Button(root, text="Check Spelling and Grammar", command=run_spell_and_grammar_check)
check_button.grid(column=0, row=2, padx=10, pady=10)

# Add a button for auto-correction
auto_correct_button = tk.Button(root, text="Auto Correct", command=auto_correct_text)
auto_correct_button.grid(column=0, row=3, padx=10, pady=10)

# Add a button to reset the text
reset_button = tk.Button(root, text="Reset", command=reset_text)
reset_button.grid(column=0, row=4, padx=10, pady=10)

# Add a text area for displaying the results
result_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10, font=("Arial", 12))
result_area.grid(column=0, row=5, padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
