import qrcode as qr

generated_code = qr.make('Hologram')
generated_code.save('hologram.png')
