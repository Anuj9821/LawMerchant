import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

def convert_pdf_to_images(pdf_path):
    
    return convert_from_path(pdf_path, dpi=300)

def extract_text_from_images(image_paths):
    extracted_text = []
    for image_path in image_paths:
        
        text = pytesseract.image_to_string(Image.open(image_path))
        extracted_text.append(text)
    return extracted_text

def main(pdf_path):

    images = convert_pdf_to_images(pdf_path)
    
    
    output_dir = 'eximg'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    
    image_paths = []
    for i, page in enumerate(images):
        image_path = os.path.join(output_dir, f'page_{i}.png')
        page.save(image_path, 'PNG')
        image_paths.append(image_path)
    
   
    extracted_text = extract_text_from_images(image_paths)
    
   
    with open('atharvaexe.txt', 'w', encoding='utf-8') as file:
        for i, text in enumerate(extracted_text):
            file.write(f"Text from page {i + 1}:\n{text}\n{'='*80}\n")
    
    # Cleanup image files
    for image_path in image_paths:
        os.remove(image_path)

if __name__ == '__main__':
    pdf_path = 'D:\\Projects\\TIMEPASS\\img to text\\Direction.pdf' 
    main(pdf_path)
