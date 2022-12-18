from flask import Flask,jsonify
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({'msg':"Deu certo"})

app.run(host='0.0.0.0',port=os.getenv('PORT'))