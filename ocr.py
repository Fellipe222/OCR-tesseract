from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = os.getcwd() + r'\images'



for filename in os.listdir(image_path):
    f = os.path.join(image_path, filename)
    # checking if it is a file
    if os.path.isfile(f):
        # sometimes, the unicode ♀ or "\n\x0c" appears at the end of the readings, to solve this, the param config was added in the method
        ocr = pytesseract.image_to_string(Image.open(f), config='-c page_separator=""')

        print(f'image: {filename} || text: {ocr}')        
        