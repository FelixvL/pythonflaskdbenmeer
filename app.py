from flask import Flask
import felix
app = Flask(__name__)

@app.route("/felix/<eerstetest>")
def felixmethode(eerstetest):
    return felix.felixstart(eerstetest)


@app.route("/felix3/allefietsen")
def felixmethode2():
    return felix.toonAlleFietsen()

@app.route("/felix4/leescsv")
def felixmethode3():
    return felix.leesuitcsv()