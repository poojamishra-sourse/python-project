import qrcode as qr  #qr code ka module import kiya hai
img= qr.make("hello, this is pooja mishra ")  #QR code banaya hai
img.save("my_qr_code.png")  #QR code ko image file me save kiya hai
print("QR code generated and saved as my_qr_code.png")