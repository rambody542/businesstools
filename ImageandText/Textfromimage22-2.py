import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
lauguages = pytesseract.get_languages(config='')
print(lauguages)