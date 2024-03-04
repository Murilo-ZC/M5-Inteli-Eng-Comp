from flask import Flask
from qreader import QReader
import cv2

# Create a QReader instance
qreader = QReader(
    model_size='l',
    min_confidence=0.5
)

app = Flask(__name__)

@app.route('/capture')
def hello_world():
    camera = cv2.VideoCapture(0)
    _, image = camera.read()
    cv2.imwrite("qrcode.png", image)
    camera.release()
    image = cv2.cvtColor(cv2.imread("qrcode.png"), cv2.COLOR_BGR2RGB)
    decoded_text = qreader.detect_and_decode(image=image)
    return {"dados": decoded_text}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)