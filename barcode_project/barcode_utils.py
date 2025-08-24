# barcode_utils.py
import barcode
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def generate_barcode_image(data, output_dir="output", image_name="barcode.png"):
    BarcodeClass = barcode.get_barcode_class('code128')
    code = BarcodeClass(data, writer=ImageWriter())
    os.makedirs(output_dir, exist_ok=True)
    image_path = os.path.join(output_dir, image_name)
    code.save(image_path.replace(".png", ""))
    return image_path

def embed_barcode_in_pdf(data, image_path, output_dir="output", pdf_name="barcode_receipt.pdf"):
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, pdf_name)
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    c.drawString(100, height - 100, f"Barcode for: {data}")
    c.drawImage(image_path, 100, height - 300, width=200, height=100)
    c.save()
    return pdf_path
