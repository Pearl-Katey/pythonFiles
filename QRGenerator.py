import qrcode
import sys
# val = sys.argv()
qr_address = 'https://ouo.press/go/I9Wai78'
name_img = "naruto.jpg"


img = qrcode.make(qr_address)
img.save(name_img)
