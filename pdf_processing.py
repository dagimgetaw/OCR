import pdfplumber
from io import BytesIO
from pdf2image import convert_from_bytes
import pytesseract
import numpy as np

# Extract tables from a PDF
def extract_table_from_pdf(pdf_data: bytes):
    with pdfplumber.open(BytesIO(pdf_data)) as pdf:
        tables = [table for page in pdf.pages for table in page.extract_tables() if table]
    return tables or "No tables found"

# OCR for PDFs
def ocr_pdf(pdf_data: bytes) -> str:
    extracted_text = ""
    try:
        with pdfplumber.open(BytesIO(pdf_data)) as pdf:
            for page in pdf.pages:
                extracted_text += (page.extract_text() or "") + "\n"
    except:
        images = convert_from_bytes(pdf_data)
        extracted_text = "\n".join(pytesseract.image_to_string(np.array(img.convert('L')), config="--psm 3") for img in images)
    return extracted_text.strip()
