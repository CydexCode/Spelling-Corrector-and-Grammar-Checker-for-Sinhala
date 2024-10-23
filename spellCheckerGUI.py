import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import re
import difflib

def preprocess_text(text):
    """
    Preprocess the given text by removing unwanted characters and normalizing it.
    This function will keep only Sinhala characters and spaces.
    """
    text = re.sub(r'[^\u0D80-\u0DFF\s]', '', text)
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
    with open(r'D:\sem7\EC9640-AI\group project\SpellAndGrammarChecker\Sinhala-Spell-and-Grammar-Checker\DictionaryCreation\sinhala_dictionary.txt', 'r', encoding='utf-8') as f:
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
            closest_matches = difflib.get_close_matches(word, dictionary, n=1)
            if closest_matches:
                corrected_words.append(closest_matches[0])
            else:
                corrected_words.append(word)
    return ' '.join(corrected_words)

def basic_grammar_check(text):
    """
    Perform a basic grammar check on the given text.
    This function checks for repeated words and punctuation issues.
    """
    grammar_issues = []
    words = tokenize(preprocess_text(text))
    
    for i in range(len(words) - 1):
        if words[i] == words[i + 1]:
            grammar_issues.append(f"Repeated word: '{words[i]}'")
    
    if not re.match(r'.*[.!?]$', text.strip()):
        grammar_issues.append("The text does not end with proper punctuation (., !, ?).")
    
    return grammar_issues

def auto_correct_grammar(text):
    """
    Automatically correct basic grammar mistakes in the input text.
    This function will correct repeated words and add punctuation if missing.
    """
    words = tokenize(preprocess_text(text))
    corrected_words = []
    
    for i in range(len(words)):
        if i == 0 or words[i] != words[i - 1]:
            corrected_words.append(words[i])
    
    corrected_text = ' '.join(corrected_words)
    
    if not re.match(r'.*[.!?]$', corrected_text.strip()):
        corrected_text += '.'
    
    return corrected_text

def run_spell_and_grammar_check():
    """
    Run the spell and grammar check on the input text and display the results in the same window.
    """
    input_text = text_area.get("1.0", tk.END)
    dictionary = load_dictionary()
    
    misspelled_words = spell_check(input_text, dictionary)
    grammar_issues = basic_grammar_check(input_text)
    
    result_area.delete("1.0", tk.END)
    
    if not misspelled_words:
        result_area.insert(tk.END, "No spelling errors found!\n", "green")
    else:
        result_area.insert(tk.END, "Misspelled words:\n", "red")
        result_area.insert(tk.END, ", ".join(misspelled_words) + "\n")
    
    if not grammar_issues:
        result_area.insert(tk.END, "No grammar issues found!\n", "green")
    else:
        result_area.insert(tk.END, "Grammar issues:\n", "red")
        result_area.insert(tk.END, "\n".join(grammar_issues) + "\n")

def auto_correct_text():
    """
    Automatically correct misspelled words in the input text.
    """
    input_text = text_area.get("1.0", tk.END)
    dictionary = load_dictionary()
    corrected_text = auto_correct(input_text, dictionary)
    
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, corrected_text)

def auto_correct_grammar_text():
    """
    Automatically correct grammar mistakes in the input text.
    """
    input_text = text_area.get("1.0", tk.END)
    corrected_text = auto_correct_grammar(input_text)
    
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
root.geometry("700x700")
root.configure(bg="#f0f0f0")

# Main Frame
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Title label
title_label = tk.Label(main_frame, text="Sinhala Spell and Grammar Checker", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(main_frame, bg="#f0f0f0")
input_frame.pack(pady=5)

input_label = tk.Label(input_frame, text="Enter Sinhala text below:", font=("Arial", 12), bg="#f0f0f0")
input_label.grid(row=0, column=0, padx=5, pady=5)

text_area = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, width=60, height=10, font=("Arial", 12))
text_area.grid(row=1, column=0, padx=5, pady=5)

# Button Frame
button_frame = tk.Frame(main_frame, bg="#f0f0f0")
button_frame.pack(pady=10)

# Place "Check Spelling and Grammar" and "Reset" buttons on the same line
check_button = tk.Button(button_frame, text="Check Spelling and Grammar", command=run_spell_and_grammar_check, width=25, bg="#4CAF50", fg="white")
check_button.grid(row=0, column=0, padx=5, pady=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset_text, width=25, bg="#f44336", fg="white")
reset_button.grid(row=0, column=1, padx=5, pady=5)

# Auto-correct buttons below the first row of buttons
auto_correct_button = tk.Button(button_frame, text="Auto Correct Spelling", command=auto_correct_text, width=18, bg="#2196F3", fg="white")
auto_correct_grammar_button = tk.Button(button_frame, text="Auto Correct Grammar", command=auto_correct_grammar_text, width=18, bg="#2196F3", fg="white")

auto_correct_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")
auto_correct_grammar_button.grid(row=1, column=1, padx=5, pady=5, sticky="e")

# Result Frame
result_frame = tk.Frame(main_frame, bg="#f0f0f0")
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, text="Results:", font=("Arial", 12), bg="#f0f0f0")
result_label.grid(row=0, column=0, padx=5, pady=5)

result_area = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, width=60, height=10, font=("Arial", 12))
result_area.grid(row=1, column=0, padx=5, pady=5)

result_area.tag_configure("red", foreground="red")
result_area.tag_configure("green", foreground="green")

# Tooltips
def create_tooltip(widget, text):
    tool_tip = tk.Toplevel(widget)
    tool_tip.withdraw()
    tool_tip.overrideredirect(True)
    label = tk.Label(tool_tip, text=text, background="#ffffe0", relief="solid", borderwidth=1, font=("Arial", 10))
    label.pack()

    def show_tooltip(event):
        tool_tip.deiconify()
        tool_tip.geometry(f"+{event.x_root+20}+{event.y_root+20}")

    def hide_tooltip(event):
        tool_tip.withdraw()

    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)

create_tooltip(check_button, "Checks for spelling and grammar issues in the text.")
create_tooltip(auto_correct_button, "Automatically corrects any spelling mistakes.")
create_tooltip(auto_correct_grammar_button, "Automatically fixes grammar issues.")
create_tooltip(reset_button, "Clears the input and result areas.")

# Start the Tkinter main loop
root.mainloop()