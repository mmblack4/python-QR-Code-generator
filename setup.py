import pyqrcode,png
qr=pyqrcode.create(input('Enter info:'))
qr.png('code.png',scale=10)