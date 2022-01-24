import qrcode

data = input('Enter the data to encode: ')

qr = qrcode.QRCode(version=5, box_size=10, border=4)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image()

img.save(input('Enter the path to save the generated QR Code: '))
