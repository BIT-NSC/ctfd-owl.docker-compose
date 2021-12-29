# encoding:utf-8
from flask import Flask,request,render_template_string 
import urllib.request,urllib.parse 
app = Flask(__name__) 
@app.route("/") 
def hello(): 
	return "hello world!" 
if __name__ == '__main__': 
	app.run(debug=False, host='0.0.0.0', port=8000)