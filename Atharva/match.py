import re
import spacy
import nltk

# Ensure you have the required nltk data files
nltk.download('punkt')

# Ensure the SpaCy model is downloaded
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
    # Improved regex pattern to match sections starting with the product keyword and ending before the next uppercase heading or numbered section
    pattern = re.compile(
        rf'(?i)(^.*?{re.escape(product_keyword)}.*?)(?=\n[A-Z][^a-z]|\n[0-9]+\.\s|\Z)',
        re.DOTALL | re.MULTILINE
    )
    matches = pattern.findall(text)
    
    if matches:
        for i, match in enumerate(matches):
            # Clean up the match by removing extra spaces and newlines
            match = match.strip()
            # Use SpaCy to process the text and extract sentences
            doc = nlp(match)
            sentences = [sent.text for sent in doc.sents]
            # Join the sentences back to form the section text
            section_text = ' '.join(sentences)
            extracted_sections[f"{product_keyword} - Section {i+1}"] = section_text
    return extracted_sections

def format_sections(sections):
    formatted_output = ""
    for title, content in sections.items():
        formatted_output += f"\n{title}:\n"
        # Split content into points using regex for more comprehensive splitting
        points = re.split(r'(\d+\.\s|[a-zA-Z]\.\s)', content)
        formatted_content = ""
        i = 0
        while i < len(points):
            if points[i].strip() and re.match(r'\d+\.\s|[a-zA-Z]\.\s', points[i]):
                formatted_content += f"- {points[i].strip()} {points[i + 1].strip()}\n"
                i += 2
            else:
                formatted_content += f"- {points[i].strip()}\n"
                i += 1
        formatted_output += formatted_content
    return formatted_output

file_path = 'Compendium_Food_Fortification_Regulations_05_06_2022.txt'
# Read the regulations text from the file
regulations_text = read_file(file_path)

# User input for the product name
product_name = input("Enter the product name: ").strip()

# Extract product sections
product_sections = extract_product_sections(regulations_text, product_name)

# Format and display extracted sections
if product_sections:
    formatted_output = format_sections(product_sections)
    print(formatted_output)
else:
    print(f"No sections found for the product name: {product_name}")
