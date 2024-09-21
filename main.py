import pytesseract
from fastapi import FastAPI, File, UploadFile
from pdf2image import convert_from_bytes
from fastapi.responses import JSONResponse
import cv2
import numpy as np
from io import BytesIO


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = FastAPI()

# OCR function for images
def ocr_image(image_data: bytes) -> str:
    np_img = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    text = pytesseract.image_to_string(img)
    return text

# OCR function for PDFs
def ocr_pdf(pdf_data: bytes) -> str:
    images = convert_from_bytes(pdf_data)
    extracted_text = ""
    for image in images:
        text = pytesseract.image_to_string(image)
        extracted_text += text + "\n"
    return extracted_text

# Route for image OCR
@app.post("/ocr-image/")
async def ocr_image_upload(file: UploadFile = File(...)):
    image_data = await file.read()
    extracted_text = ocr_image(image_data)
    return JSONResponse(content={"text": extracted_text})

# Route for PDF OCR
@app.post("/ocr-pdf/")
async def ocr_pdf_upload(file: UploadFile = File(...)):
    pdf_data = await file.read()
    extracted_text = ocr_pdf(pdf_data)
    return JSONResponse(content={"text": extracted_text})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
