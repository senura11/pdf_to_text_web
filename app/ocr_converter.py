import pytesseract
from pdf2image import convert_from_path

def pdf_to_text_ocr(pdf_path, output_txt_path):
    images = convert_from_path(pdf_path)
    text = ""

    for image in images:
        text += pytesseract.image_to_string(image, lang='sin')

    with open(output_txt_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)
