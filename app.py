from flask import Flask
import logging
import random
import time

app = Flask(__name__)

# Loglarni sozlash (Loki uchun)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

@app.route('/')
def hello():
    logging.info("Main page accessed")
    return "Agriculture Platform - Devops Project Running!"

@app.route('/update')
def update():
    # CPU va Memory yuklamasini simulyatsiya qilish uchun log
    status_code = random.choice([200, 200, 200, 404, 500])
    logging.info(f"GET /update HTTP/1.1 {status_code}")
    if status_code == 500:
        logging.error("Internal Server Error occurred during update")
    return f"Update status: {status_code}", status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)