# Generating QR Codes with Python

Question Summary
The user provided a Python script that generates QR codes and adds them to an image. They are requesting documentation for this script to include in a GitHub Readme.md file.

Answer
To generate QR codes and add them to an image using Python, you can use the qrcode library along with the PIL (Python Imaging Library) module. The provided script demonstrates this process.

First, make sure you have the necessary libraries installed. You can install them using pip:

  ```
pip install qrcode
pip install pillow
  ```

Next, import the required modules:

  ```
import qrcode
from PIL import Image
  ```
Define the text or URLs you want to encode as QR codes:
  ```
texts = ["Salam kitaphana", "https://gozle.com/tm"]
  ```

Create a directory to store the generated QR codes:

  ```
import os
if not os.path.exists("qr_codes"):
    os.makedirs("qr_codes")
  ```

Loop through each text and generate a QR code:

  ```
for i, text in enumerate(texts):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(f"qr_codes/qr_code_{i+1}.png")


Open the base image where you want to add the QR codes:
photo = Image.open("photo.png")
  ```

Loop through each text again and add the corresponding QR code to the image:

  ```
for i, text in enumerate(texts):
    qr_code = Image.open(f"qr_codes/qr_code_{i+1}.png")
    qr_code_resized = qr_code.resize((490, 490))
    photo.paste(qr_code_resized, (260, 730))
    photo.save(f"photo_with_qr_code_{i}.png")
  ```

This script generates QR codes for the provided texts and adds them to the "photo.png" image. The resulting images with the QR codes are saved as "photo_with_qr_code_0.png", "photo_with_qr_code_1.png", and so on.

You can customize the script further based on your specific requirements, such as changing the QR code size, position, or image format.

Make sure to include the necessary images and update the file paths accordingly when using this script.
