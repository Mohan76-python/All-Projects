from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def generate_pdf_receipt(bill, items, output_dir="receipts"):
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, f"receipt_{bill['bill_id']}.pdf")

    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    y = height - 50  # Start from top

    # Header
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, f"Bill ID: {bill['bill_id']}")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Customer: {bill['customer_name']}")
    y -= 20
    c.drawString(50, y, f"Date: {bill['bill_date']}")
    y -= 20
    c.drawString(50, y, f"Payment Mode: {bill['payment_mode']}")
    y -= 20
    c.drawString(50, y, f"Remarks: {bill['remarks']}")
    y -= 30

    # Items
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Items:")
    y -= 20
    c.setFont("Helvetica", 11)
    for i, item in enumerate(items, start=1):
        line = f"{i}. {item['item_name']} x{item['quantity']} ₹{item['price_per_unit']} → ₹{item['total_price']}"
        c.drawString(50, y, line)
        y -= 20
        if y < 100:  # Prevent overflow
            c.showPage()
            y = height - 50

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Total Amount: ₹{bill['total_amount']}")

    c.save()
    return pdf_path
pdf.set_font("Helvetica", 'B', 16)
pdf.cell(0, 10, "🍽️ Mohan's Bistro", ln=True, align='C')

pdf.set_font("Helvetica", '', 12)
pdf.cell(0, 10, "Receipt", ln=True, align='C')
pdf.ln(10)
pdf.image("assets/logo.png", x=10, y=8, w=30)
import subprocess
subprocess.Popen(['start', pdf_path], shell=True)
