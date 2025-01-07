import fitz  # PyMuPDF

def pdf_to_text(pdf_path, output_txt_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()

    with open(output_txt_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)
