from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Itay, Good wishes Itay and quick recovery'

app.run(host='0.0.0.0', port=8081)