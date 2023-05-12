from flask import Flask
import felix
app = Flask(__name__)

@app.route("/felix/<eerstetest>")
def felixmethode(eerstetest):
    return felix.felixstart(eerstetest)