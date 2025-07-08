import qrcode as qc

# easy and quick way
img = qc.make('www.youtube.com')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")


class QrCodeCreator:

    def __init__(self, boxSize, borderSize):
        self.qr = qc.QRCode(version=1, error_correction= qc.constants.ERROR_CORRECT_L, box_size=boxSize, border=borderSize) # version == Größe der Matrix

    def setQrContent(self,content, fileName, bgColor, fgColor):

      try:  
        self.qr.add_data(content)
        self.qr.make(fit=True) # Der Algorithmus sucht die kleinste mögliche QR-Code-Version, die ausreichend Kapazität für deine Daten (plus Fehlerkorrektur) hat.

        img = self.qr.make_image(fill_color=fgColor, back_color=bgColor)
        img.save(fileName)
      except Exception as e:
         print(f'Fehler bei der Generierung/Speicherung des QR Codes ! \n {e}')  


if __name__ == '__main__':
    qrInstance = QrCodeCreator(10,1)
    qrInstance.setQrContent("www.facebook.com", 'fb_qrcode.png', 'White', 'black')