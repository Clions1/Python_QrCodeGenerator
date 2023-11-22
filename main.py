import pyqrcode

text=input("enter text generate qr code :  ")

qrcode=pyqrcode.create(text)

qrcode.svg('qrcode.svg',scale=10)