from flask import Flask
from qreader import QReader
import cv2
import time

# Create a QReader instance
qreader = QReader(
    model_size='l',
    min_confidence=0.5
)

qreader_2 = QReader(
    model_size='n',
    min_confidence=0.5
)
app = Flask(__name__)

@app.route('/capture')
def hello_world():
    tempo = time.time()
    camera = cv2.VideoCapture(0)
    _, image = camera.read()
    cv2.imwrite("qrcode.png", image)
    camera.release()
    image = cv2.cvtColor(cv2.imread("qrcode.png"), cv2.COLOR_BGR2RGB)
    decoded_text = qreader.detect_and_decode(image=image)
    return {"dados": decoded_text, "tempo": time.time() - tempo}

@app.route('/fast-capture')
def hello_world2():
    tempo = time.time()
    camera = cv2.VideoCapture(0)
    _, image = camera.read()
    cv2.imwrite("qrcode.png", image)
    camera.release()
    image = cv2.cvtColor(cv2.imread("qrcode.png"), cv2.COLOR_BGR2RGB)
    decoded_text = qreader_2.detect_and_decode(image=image)
    return {"dados": decoded_text, "tempo": time.time() - tempo}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)