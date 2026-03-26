import barcode
from barcode.writer import ImageWriter
import os

OUTPUT_DIR = "output"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def generate_code128(data, filename):
    code = barcode.get(
        "code128",
        data,
        writer=ImageWriter()
    )
    path = os.path.join(OUTPUT_DIR, filename)
    return code.save(path)

def generate_ean13(data, filename):
    if len(data) != 12 or not data.isdigit():
        raise ValueError("EAN-13 requires exactly 12 digits")

    code = barcode.get(
        "ean13",
        data,
        writer=ImageWriter()
    )
    path = os.path.join(OUTPUT_DIR, filename)
    return code.save(path)