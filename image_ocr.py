# from PIL import Image

# try:
#     import pytesseract
# except ImportError:
#     pytesseract = None


# def extract_image_text(file):
#     if pytesseract is None:
#         return "OCR is disabled in this deployment environment."

#     image = Image.open(file)
#     return pytesseract.image_to_string(image)


from PIL import Image

try:
    import pytesseract
except ImportError:
    pytesseract = None

def extract_image_text(file):
    if pytesseract is None:
        return "OCR is disabled in this environment."

    image = Image.open(file)
    return pytesseract.image_to_string(image)
