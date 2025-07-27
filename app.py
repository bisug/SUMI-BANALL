from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '@dear_sumi is alive!'

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))

threading.Thread(target=run).start()  
