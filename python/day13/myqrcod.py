import qrcode

img = qrcode.make('Hello World!')
img.save('helloworld_qrcode.png')