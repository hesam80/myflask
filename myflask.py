
#Import dependencies
from flask import Flask
from factoriel import factoriel


#Create instance of Flask App
app = Flask(__name__)

#Define Route
@app.route("/")

#Content

def home():
    return("hello world ")




#Running and Controlling the script
if (__name__ =="__main__"):
    app.run(debug=True)