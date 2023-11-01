from PIL import Image
import pytesseract

image_path = r"ImageandText\screenshot_20231101.png"

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open(image_path), lang="kor")

print(text)