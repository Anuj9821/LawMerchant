import os
import re
import spacy
import nltk

# Download necessary NLTK data
nltk.download('punkt')

# Load SpaCy model
try:
    nlp = spacy.load('en_core_web_lg')
except OSError:
    from spacy.cli import download
    download('en_core_web_lg')
    nlp = spacy.load('en_core_web_lg')

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_product_sections(text, product_keyword):
    extracted_sections = []
    pattern = re.compile(
        rf'(?i)(^.*?{re.escape(product_keyword)}.*?)(?=\n[A-Z][^a-z]|\n[0-9]+\.\s|\Z)',
        re.DOTALL | re.MULTILINE
    )
    matches = pattern.findall(text)
    
    if matches:
        for i, match in enumerate(matches):
            match = match.strip()
            doc = nlp(match)
            sentences = [sent.text for sent in doc.sents]
            relevant_sentences = []
            for sent in sentences:
                if product_keyword.lower() in sent.lower():
                    relevant_sentences.append(sent)
                elif relevant_sentences and re.match(r'^[a-zA-Z0-9]\.', sent.strip()):
                    relevant_sentences.append(sent)
            section_text = ' '.join(relevant_sentences)
            extracted_sections.append(section_text)

    return extracted_sections

def process_all_files(base_dir, product_name):
    result = {
        "product": product_name,
        "categories": {}
    }

    for category in os.listdir(base_dir):
        category_path = os.path.join(base_dir, category)
        if os.path.isdir(category_path):
            file_path = os.path.join(category_path, 'regulations.txt')
            if os.path.isfile(file_path):
                regulations_text = read_file(file_path)
                sections = extract_product_sections(regulations_text, product_name)
                if sections:
                    result["categories"][category] = sections

    return result

# Directory path to the categories
base_dir = 'categories'

# User input for the product name
product_name = input("Enter the product name: ").strip()

# Process all files and get the result
result = process_all_files(base_dir, product_name)
print(result)
