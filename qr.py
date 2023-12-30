
# pip install qrcode

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border=4,
)
qr.add_data("any link")

img =qr.make_image()
img.save("qrcode.png")
