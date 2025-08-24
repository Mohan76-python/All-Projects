# main.py
import argparse
from barcode_utils import generate_barcode_image, embed_barcode_in_pdf

def main():
    parser = argparse.ArgumentParser(description="Generate barcode and embed in PDF.")
    parser.add_argument("--data", required=True, help="Data to encode in barcode")
    parser.add_argument("--image", default="barcode.png", help="Output image filename")
    parser.add_argument("--pdf", default="barcode_receipt.pdf", help="Output PDF filename")
    args = parser.parse_args()

    image_path= generate_barcode_image(args.data, image_name=args.image)
    pdf_path = embed_barcode_in_pdf(args.data, image_path, pdf_name=args.pdf)

    print(f"✅ Barcode saved as {image_path}")
    print(f"✅ PDF saved as {pdf_path}")

if __name__ == "__main__":
    main()
