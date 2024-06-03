import scrapy
from scrapy.crawler import CrawlerProcess
import fitz  # PyMuPDF
import os
import mysql.connector

class FssaiPdfSpider(scrapy.Spider):
    name = 'fssai_pdf_spider'
    start_urls = ['https://fssai.gov.in/cms/food-safety-and-standards-regulations.php']

    # Define the directory where PDFs will be saved
    pdf_dir = 'downloaded_pdfs'
    
    # Create the directory if it doesn't exist
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    def parse(self, response):
        pdf_links = response.css('a::attr(href)').re(r'.*\.pdf$')
        for link in pdf_links:
            yield response.follow(link, self.save_pdf)

    def save_pdf(self, response):
        # Save PDF files to the specified directory
        path = os.path.join(self.pdf_dir, response.url.split('/')[-1])
        self.logger.info(f'Saving PDF {path}')
        with open(path, 'wb') as f:
            f.write(response.body)

def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def main():
    # Step 1: Run Scrapy spider to download PDFs
    process = CrawlerProcess(settings={
        "FEEDS": {
            "items.json": {"format": "json"},
        },
    })
    process.crawl(FssaiPdfSpider)
    process.start()

    # Step 2: Convert PDFs to text
    pdf_directory = 'downloaded_pdfs'  # Directory where PDFs are stored
    text_data = {}

    for pdf_file in os.listdir(pdf_directory):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_directory, pdf_file)
            text = pdf_to_text(pdf_path)
            text_data[pdf_file] = text

    # Step 3: Store text data in MySQL database
    conn = mysql.connector.connect(
        host='localhost',  # Replace with your MySQL host
        user='username',  # Replace with your MySQL user
        password='password',  # Replace with your MySQL password
        database='pdf_database'  # Database name created earlier
    )
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pdf_texts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            file_name VARCHAR(255) NOT NULL,
            text_content LONGTEXT NOT NULL
        )
    ''')

    for file_name, text_content in text_data.items():
        cursor.execute('''
            INSERT INTO pdf_texts (file_name, text_content)
            VALUES (%s, %s)
        ''', (file_name, text_content))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
