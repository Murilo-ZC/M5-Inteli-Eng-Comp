from qreader import QReader
import cv2

# Create a QReader instance
qreader = QReader()

# Vamos pegar a webcam do nosso PC
camera = cv2.VideoCapture(0)

#Captura uma imagem da webcam
_, image = camera.read()

# Salva a imagem em disco
cv2.imwrite("qrcode.png", image)

# Libera a Webcam
camera.release()

# Get the image that contains the QR code
image = cv2.cvtColor(cv2.imread("qrcode.png"), cv2.COLOR_BGR2RGB)

# Use the detect_and_decode function to get the decoded QR data
decoded_text = qreader.detect_and_decode(image=image)
print(decoded_text)