import qrcode

from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20, border=10,)

qr.add_data("https://www.youtube.com/watch?v=G4mNV5DL1z0")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("kavya_all_india_women_hackathon.png")