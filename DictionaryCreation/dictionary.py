import re
import os

# Path to the Sinhala dataset
dataset_path = 'D:\sem7\EC9640-AI\group project\SpellAndGrammarChecker\Sinhala-Spell-and-Grammar-Checker\DictionaryCreation\sinhala_text_file'  

# Function to extract Sinhala words
def extract_sinhala_words(text):
    # Regular expression to match Sinhala words (Use unicodes)
    sinhala_words = re.findall(r'[\u0D80-\u0DFF]+', text)
    return sinhala_words

# Dictionary to store unique Sinhala words
sinhala_word_set = set()

# Process each text file in the dataset folder
for root, dirs, file_list in os.walk(dataset_path):
    for file_name in file_list:
        if file_name.endswith('.txt'):  # Only process .txt files
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                # Extract Sinhala words
                words = extract_sinhala_words(text)
                sinhala_word_set.update(words)

# Write the unique Sinhala words to a new text file (sinhala_dictionary.txt)
dictionary_path = 'DictionaryCreation/sinhala_dictionary.txt'
with open(dictionary_path, 'w', encoding='utf-8') as dict_file:
    for word in sorted(sinhala_word_set):
        dict_file.write(word + '\n')

print(f"Dictionary created with {len(sinhala_word_set)} unique Sinhala words.")
print(f"Dictionary saved at {dictionary_path}")