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
    extracted_sections = {}
    # Improved regex pattern to match sections starting with the product keyword and including subpoints
    pattern = re.compile(
        rf'(?i)(^.*?{re.escape(product_keyword)}.*?)(?=\n[A-Z][^a-z]|\n[0-9]+\.\s|\Z)',
        re.DOTALL | re.MULTILINE
    )
    matches = pattern.findall(text)
    
    print(f"DEBUG: Found {len(matches)} matches for keyword '{product_keyword}'")

    if matches:
        for i, match in enumerate(matches):
            # Clean up the match by removing extra spaces and newlines
            match = match.strip()
            # Use SpaCy to process the text and extract sentences
            doc = nlp(match)
            sentences = [sent.text for sent in doc.sents]
            # Filter out sentences that do not match the context of the product keyword
            relevant_sentences = []
            for sent in sentences:
                if product_keyword.lower() in sent.lower():
                    relevant_sentences.append(sent)
                elif relevant_sentences and re.match(r'^[a-zA-Z0-9]\.', sent.strip()):
                    relevant_sentences.append(sent)
            
            section_text = ' '.join(relevant_sentences)
            extracted_sections[f"{product_keyword} - Section {i+1}"] = section_text
            print(f"DEBUG: Extracted section {i+1} with {len(relevant_sentences)} relevant sentences")

    return extracted_sections

# File path to the regulations text file
file_path = 'Compendium_Food_Fortification_Regulations_05_06_2022.txt'

# Read the regulations text from the file
regulations_text = read_file(file_path)

# User input for the product name
product_name = input("Enter the product name: ").strip()

# Extract product sections
product_sections = extract_product_sections(regulations_text, product_name)

if product_sections:
    for title, content in product_sections.items():
        print(title + ":\n" + content + "\n\n")
else:
    print(f"No sections found for the product name: {product_name}")
