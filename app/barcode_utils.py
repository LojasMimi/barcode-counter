from pyzbar.pyzbar import decode
from PIL import Image

def detect_barcodes(file_storage):
    image = Image.open(file_storage.stream)
    barcodes = decode(image)
    return [barcode.data.decode('utf-8') for barcode in barcodes if barcode.type.startswith('EAN')]
