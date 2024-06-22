import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Function to check if a word is a food or vegetable
def is_food_or_vegetable(word):
    synsets = wordnet.synsets(word)
    for synset in synsets:
        if 'food' in synset.lexname() or 'vegetable' in synset.lexname():
            return True
    return False

# Input and output file paths
input_file = 'output_proper_nouns.txt'
output_file = 'extracted_foods_vegetables.txt'

# Set to store extracted words to avoid duplicates
extracted_words = set()

# Read the large text file and extract relevant words
with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        words = word_tokenize(line)
        tagged_words = pos_tag(words)
        for word, tag in tagged_words:
            if tag.startswith('NN') and is_food_or_vegetable(word.lower()):
                if word.lower() not in extracted_words:
                    extracted_words.add(word.lower())

# Write extracted words to output file
with open(output_file, 'w', encoding='utf-8') as output:
    for word in extracted_words:
        output.write(word + '\n')

print(f"Extraction complete. Extracted words saved in {output_file}")
