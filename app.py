from flask import Flask

# Using __name__ we give a unique name to our Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hola'


app.run(port=5000)
