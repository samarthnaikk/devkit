import sys
from pdf2docx import Converter

def run(args):
    if len(args) != 2:
        print("Usage: devkit convert <input_file> <output_file>")
        sys.exit(1)
    
    input_file, output_file = args

    if input_file.endswith(".pdf") and output_file.endswith(".docx"):
        convert_pdf_to_docx(input_file, output_file)
    else:
        print("Unsupported conversion type.")

def convert_pdf_to_docx(pdf_file, docx_file):
    try:
        cv = Converter(pdf_file)
        cv.convert(docx_file)
        cv.close()
        print(f"Converted {pdf_file} to {docx_file}")
    except Exception as e:
        print(f"Conversion failed: {e}")
