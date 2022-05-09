import qrcode


data = input('Insert text or url to generate QR Code: ')

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color='blue', back_color='white')

export = input('Enter the output file name: ')
img.save(f'C:/Temp/{export}.jpg')
