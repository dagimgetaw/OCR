import cv2
import numpy as np
import pytesseract

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read the image
img = cv2.imread("img.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

# Configuration for Tesseract OCR
config = "--psm 3"

# Perform OCR on the adaptive thresholded image
text = pytesseract.image_to_string(adaptive, config=config)

# Print the extracted text
print(text)

# Display the original and processed images
cv2.imshow("Original Image", img)
cv2.imshow("Adaptive Thresholding", adaptive)

# Wait for any key to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
