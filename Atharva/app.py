import sqlite3
import spacy

# Load the large English language model
nlp = spacy.load('en_core_web_lg')
nlp.max_length = 2000000  # Increase the maximum length limit

def extract_proper_nouns(text):
    # Process the text with spaCy
    doc = nlp(text)
    
    # Extract proper nouns (PROPN)
    proper_nouns = [token.text for token in doc if token.pos_ == "PROPN"]
    
    return proper_nouns

def read_sql_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query to select text content from the pdf_texts table
    cursor.execute("SELECT text_content FROM pdf_texts")
    rows = cursor.fetchall()
    
    text = " ".join([row[0] for row in rows])  # Assuming the text content is in the first column
    conn.close()
    return text

def write_text_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"{item}\n")

def process_text_in_chunks(text, chunk_size=1000000):
    # Split the text into chunks of specified size
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    
    proper_nouns = []
    for chunk in chunks:
        proper_nouns.extend(extract_proper_nouns(chunk))
    
    return proper_nouns

if __name__ == "__main__":
    # Path to the input SQLite database file
    input_db_path = "fssai_pdfs.db"
    
    # Path to the output file
    output_file_path = "output_proper_nouns.txt"
    
    # Read the text from the SQLite database
    text_content = read_sql_database(input_db_path)
    
    # Process the text in chunks and extract proper nouns
    proper_nouns = process_text_in_chunks(text_content)
    
    # Write the proper nouns to the output file
    write_text_file(output_file_path, proper_nouns)
    
    print("Proper nouns extracted and written to the output file.")
