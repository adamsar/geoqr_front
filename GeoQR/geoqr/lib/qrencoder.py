"""
Utilities for making a new QR code
"""

import os
import os.path
import qrcode

def dir_down(path, levels):
    if levels == 0:
        return path
    return dir_down(os.path.dirname(path), levels - 1)
BASE = dir_down(__file__, 2)
ENDPOINT = os.path.join(BASE, "static/qrimgs")

def write_out(img):
    """
    Writes a qr image to the qr folder
    """
    candidate_base = "qr_%s.png"
    def check_candidate(count):
        candidate = os.path.join(ENDPOINT, candidate_base % str(count))
        if os.path.exists(candidate):
            return check_candidate(count+1)
        else:
            img.save(candidate)
            return candidate
    return check_candidate(0)
    

def generate_from_code(code):
    """
    Generates a fully qualified image file from
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10
    )
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image()
    return write_out(img).replace(BASE, "")
