import pytesseract
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from image_processing import ocr_image, extract_table_from_img
from pdf_processing import ocr_pdf, extract_table_from_pdf

# Set tesseract executable path for Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("index.html")

@app.post("/ocr-image/")
async def ocr_image_upload(file: UploadFile = File(...)):
    image_data = await file.read()
    extracted_text = ocr_image(image_data)
    tables = extract_table_from_img(image_data)
    return JSONResponse(content={"text": extracted_text, "tables": tables})

@app.post("/ocr-pdf/")
async def ocr_pdf_upload(file: UploadFile = File(...)):
    pdf_data = await file.read()
    tables = extract_table_from_pdf(pdf_data)
    extracted_text = ocr_pdf(pdf_data)
    return JSONResponse(content={"text": extracted_text, "tables": tables})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
