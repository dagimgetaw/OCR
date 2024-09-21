# FastAPI OCR Application

This project is a FastAPI application that provides OCR (Optical Character Recognition) capabilities for both images and PDFs. It uses Tesseract OCR to extract text and can handle tables in images and PDFs.

## Usage

This application features a user interface that allows you to upload images or PDF files and receive the extracted text in JSON format.

### 1. main.py

This file contains the FastAPI application and defines the routes for handling image and PDF uploads.

### Routes

- **/ocr-image/**

  - **Method:** POST
  - **Description:** Accepts an image file and returns the extracted text and tables.
  - **Request Body:** Image file (form-data).
  - **Response:** JSON containing the extracted text and tables.

- **/ocr-pdf/**
  - **Method:** POST
  - **Description:** Accepts a PDF file and returns the extracted text and tables.
  - **Request Body:** PDF file (form-data).
  - **Response:** JSON containing the extracted text and tables.

---

### 2. image_processing.py

This module provides functions for OCR and table extraction from images.

### Functions

- **`ocr_image(image_data: bytes) -> str`**

  - Takes image data as input and returns the extracted text as a string.

- **`extract_table_from_img(image_data: bytes) -> list`**
  - Takes image data as input and returns a list of extracted table data.

---

### 3. pdf_processing.py

This module provides functions for OCR and table extraction from PDF files.

### Functions

- **`ocr_pdf(pdf_data: bytes) -> str`**

  - Takes PDF data as input and returns the extracted text as a string.

- **`extract_table_from_pdf(pdf_data: bytes) -> list`**
  - Takes PDF data as input and returns a list of extracted table data.

## Features

- **OCR for Images**: Extract text from standard images and images containing tables.
- **OCR for PDFs**: Extract text and tables from PDF files.
- **UI Design**: Separate files for handling image and PDF processing.

## Directory Structure

```bash
OCR/
├── main.py
├── image_processing.py
├── pdf_processing.py
└── index.html
└── asset/
    ├── img.png
    ├── lorem.pdf
    ├── table_img.jpg
    ├── table_pdf.pdf
└── static/
    └── style.css
└── README. md
```

## Installation Guide

Follow these steps to set up the FastAPI OCR application:

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.7 or higher**
- **Tesseract OCR** (Make sure to note the installation path)

### Steps to Install

1.  **Clone the Repository**:
    Open your terminal and run the following command to clone the repository

    ```bash
    git clone https://github.com/dagimgetaw/OCR.git
    cd OCR

    ```

2.  **Set Up a Virtual Environment (Optional but Recommended)**:
    Create a virtual environment to manage dependencies

        ```bash
        python -m venv venv

.
Activate the virtual environment:

- For Windows:` venv\Scripts\activate`
- For macOS/Linux:` source venv/bin/activate`

3. **Install Requirements**:
   Install the necessary dependencies using pip

   ```bash
    pip install -r requirements.txt

   ```

4. **Tesseract Installation**:
   Make sure Tesseract OCR is installed on your system. You can download it from:
   [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

After installation, set the `tesseract_cmd` path in your code:
python

#### For Windows

` pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`

#### For macOS

`pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
`

#### Linux

`pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'`

3. **Run the Application**: Start the FastAPI application using the following command **Inside the directory**:
   `uvicorn main:app --host 0.0.0.0 --port 8000`

4. **Access the Application**: Access the application at http://localhost:8000.

## Requirements

Make sure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- Tesseract OCR (included in the Dockerfile)
- FastAPI
- OpenCV
- pdfplumber
- pdf2image

## License

This project is licensed under the MIT License. See the LICENSE file for details.
