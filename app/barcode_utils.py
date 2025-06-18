from PIL import Image
import cv2
import numpy as np
from pyzxing import BarCodeReader

reader = BarCodeReader()

def detect_barcodes(file_storage):
    # Converte para RGB e depois para numpy
    image = Image.open(file_storage.stream).convert('RGB')
    np_img = np.array(image)
    _, buffer = cv2.imencode('.jpg', cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR))

    # Salva temporariamente como arquivo JPG
    temp_path = "temp_scan.jpg"
    with open(temp_path, "wb") as f:
        f.write(buffer)

    # Usa pyzxing para decodificar códigos
    result = reader.decode(temp_path)
    codes = []

    for r in result:
        if r.get("format", "").startswith("EAN"):
            codes.append(r["raw"])

    return codes
