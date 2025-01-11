# app/text_formatter.py

def format_extracted_text(text):
    """
    Formats the extracted text by separating lines and paragraphs correctly.
    
    Args:
        text (str): The raw text extracted from the PDF.
    
    Returns:
        str: The formatted text with proper line and paragraph separation.
    """
    # Split the text into lines
    lines = text.splitlines()
    
    # Remove empty lines and strip whitespace
    lines = [line.strip() for line in lines if line.strip()]
    
    # Join the lines with proper paragraph separation
    formatted_text = "\n\n".join(lines)
    
    return formatted_text
