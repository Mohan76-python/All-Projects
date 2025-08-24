import os
import argparse
import logging
from datetime import datetime
from tqdm import tqdm
from PIL import Image
# CLI argument setup
parser = argparse.ArgumentParser(description="Resize images in a folder.")
parser.add_argument('--input', default='input_images', help='Input folder path')
parser.add_argument('--output', default='output_images', help='Output folder path')
parser.add_argument('--width', type=int, default=800, help='Target width')
parser.add_argument('--height', type=int, default=600, help='Target height')
parser.add_argument('--format', default='JPEG', choices=['JPEG', 'PNG', 'WEBP'], help='Output image format')
parser.add_argument('--quality', type=int, default=85, help='Output quality (for JPEG/WEBP)')
parser.add_argument('--dry-run', action='store_true', help='Preview actions without saving files')
parser.add_argument('--log', default='resize_log.txt', help='Log file name')
args = parser.parse_args()

# Setup logging
logging.basicConfig(filename=args.log, level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info("🔧 Image resizing started")

# Ensure output folder exists
os.makedirs(args.output, exist_ok=True)

# Supported extensions
valid_extensions = ('.png', '.jpg', '.jpeg', '.webp')

# List valid image files
image_files = [f for f in os.listdir(args.input) if f.lower().endswith(valid_extensions)]

# Check if any images found
if not image_files:
    msg = f"⚠️ No valid image files found in '{args.input}' folder."
    print(msg)
    logging.warning(msg)
else:
    for filename in tqdm(image_files, desc="Processing images", unit="file"):
        img_path = os.path.join(args.input, filename)
        try:
            with Image.open(img_path) as img:
                resized_img = img.resize((args.width, args.height))
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(args.output, f"{base_name}.{args.format.lower()}")

                if args.dry_run:
                    msg = f"🔍 Dry run: Would save '{output_path}' at {args.width}x{args.height} in {args.format} format"
                    print(msg)
                    logging.info(msg)
                else:
                    save_kwargs = {'format': args.format}
                    if args.format in ['JPEG', 'WEBP']:
                        save_kwargs['quality'] = args.quality
                    resized_img.save(output_path, **save_kwargs)
                    msg = f"✅ Saved: {output_path}"
                    print(msg)
                    logging.info(msg)
        except Exception as e:
            err_msg = f"❌ Error processing {filename}: {e}"
            print(err_msg)
            logging.error(err_msg)

logging.info("✅ Image resizing completed")
print("✅ Pillow is working!")