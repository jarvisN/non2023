from pyzbar.pyzbar import decode
from PIL import Image

class QRDecoder:
    def __init__(self, image_path):
        self.image_path = image_path

    def decode_qr(self):
        # Open the image
        img = Image.open(self.image_path)

        # Decode the QR code
        decoded_objects = decode(img)

        # Create a list to store decoded data
        decoded_data = []

        for obj in decoded_objects:
            # Add decoded data to the list
            decoded_data.append(obj.data.decode('utf-8'))

        # Return the list of decoded data
        return decoded_data
