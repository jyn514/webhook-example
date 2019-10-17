from flask import Flask

app = Flask(__name__)

@app.route('/', methods=('POST',))
def listen():
    data = app.get_json()
    print(data)
    return 'Hello, world!'

