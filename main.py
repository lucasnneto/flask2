from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Vai ter planeja conta PYTHON</p>"

app.run(host='0.0.0.0',port=os.getenv('PORT'))