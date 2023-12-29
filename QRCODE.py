# project 1
import qrcode as qr
img = qr.make("https://www.linkedin.com/in/swajal-kumar-jha-87115b197/")
img.save("LinkedIn Profile.png")
print("Code Executed")

# project 2
import qrcode as qr
from PIL import Image

qr = qr.QRCode(version = 1,
                   error_correction= qr.constants.ERROR_CORRECT_H,
                   box_size = 10, border = 4,)
qr.add_data("https://www.linkedin.com/in/swajal-kumar-jha-87115b197/")
qr.make(fit=True)
img = qr.make_image(fill_color = "White", back_color = "Blue" )
img.save("LinkedIn Profile 2.png")
print("Code Executed")
