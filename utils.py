# utils.py

from fpdf import FPDF
import os

def generate_pdf(pdf_name, text_content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=text_content, border=0, align='L')
    pdf.output(pdf_name)

if __name__ == "__main__":
    pdf_name = "example.pdf"
    text_content = "This is the content of my PDF.\nYou can add more text here."
    generate_pdf(pdf_name, text_content)

