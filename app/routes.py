from flask import Blueprint, request, jsonify, render_template
from .barcode_utils import detect_barcodes

bp = Blueprint('main', __name__)
counts = {}

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/scan', methods=['POST'])
def scan():
    file = request.files['image']
    barcodes = detect_barcodes(file)

    for barcode in barcodes:
        if barcode not in counts:
            counts[barcode] = 0
        counts[barcode] += 1

    return jsonify({'counts': counts})
