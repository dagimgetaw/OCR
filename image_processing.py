import cv2
import numpy as np
import pytesseract

# OCR for standard images
def ocr_image(image_data: bytes) -> str:
    img = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return pytesseract.image_to_string(adaptive, config="--psm 3")

# Extract tables from images
def extract_table_from_img(image_data: bytes):
    img = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_GRAYSCALE)
    _, binary_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)

    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 40))

    horizontal_lines = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    vertical_lines = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
    grid_img = cv2.addWeighted(horizontal_lines, 0.5, vertical_lines, 0.5, 0.0)

    contours, _ = cv2.findContours(grid_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    table_data = [pytesseract.image_to_string(img[y:y+h, x:x+w], config='--psm 7').strip() for x, y, w, h in [cv2.boundingRect(c) for c in contours]]

    return table_data or "No tables found in image"
