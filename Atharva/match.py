import re
import spacy
import nltk


nltk.download('punkt')


try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    from spacy.cli import download
    download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')


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
            # Filter out sentences that do not match the context of the product keyword
            relevant_sentences = [sent for sent in sentences if product_keyword.lower() in sent.lower()]
            section_text = ' '.join(relevant_sentences)
            extracted_sections[f"{product_keyword} - Section {i+1}"] = section_text
    return extracted_sections

# Function to format extracted sections into bullet points with hierarchy
def format_sections(sections):
    formatted_output = ""
    for title, content in sections.items():
        formatted_output += f"\n{title}:\n"
        # Split content into points using regex for more comprehensive splitting
        points = re.split(r'(?<=\.\s)(?=[A-Z0-9])', content)
        for point in points:
            if point.strip():  # Check to ensure no empty points are added
                formatted_output += f"- {point.strip()}\n"
                # Check for sub-points (e.g., a, b, c or i, ii, iii)
                sub_points = re.split(r'(?<=\)\s)(?=[a-zA-Z])', point.strip())
                if len(sub_points) > 1:
                    for sub_point in sub_points[1:]:
                        formatted_output += f"  - {sub_point.strip()}\n"
    return formatted_output

# File path to the regulations text file
file_path = 'Regulation.txt'

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
