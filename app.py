from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=('POST',))
def listen():
    data = request.json
    print(data)
    return 'Hello, world!'
