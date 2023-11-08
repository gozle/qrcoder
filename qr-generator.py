import qrcode 
from PIL import Image 
 

texts = ["Salam kitaphana","https://gozle.com/tm"]


import os 
if not os.path.exists("qr_codes"): 
    os.makedirs("qr_codes") 
 

for i, text in enumerate(texts): 
    qr = qrcode.QRCode(version=1, box_size=10, border=5) 
    qr.add_data(text) 
    qr.make(fit=True) 
    qr_img = qr.make_image(fill_color="black", back_color="white") 
    qr_img.save(f"qr_codes/qr_code_{i+1}.png") 

photo = Image.open("photo.png") 
 
for i, text in enumerate(texts): 
    qr_code = Image.open(f"qr_codes/qr_code_{i+1}.png") 
    qr_code_resized = qr_code.resize((490, 490)) 
    photo.paste(qr_code_resized, (260, 730)) 

    photo.save(f"photo_with_qr_code_{i}.png")