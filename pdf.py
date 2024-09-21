import sys
import PyPDF2

def pdf_to_text(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Initialize an empty string to store the extracted text
        extracted_text = ""
        
        # Iterate through each page and extract the text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text() + "\n"
    
    return extracted_text

# Example usage
file_path = 'coverletter.pdf'
text = pdf_to_text(file_path)

# Set default encoding to utf-8 and print the text
sys.stdout.reconfigure(encoding='utf-8')
print(text)
