import cv2
from pytesseract import pytesseract

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("seoultech.jpg")

words_in_image = pytesseract.image_to_string(img)

print(words_in_image)