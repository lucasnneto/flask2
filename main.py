from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run(port=os.getenv('PORT'))