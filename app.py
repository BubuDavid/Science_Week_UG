"""
<-------- IDEAS ------------>
- It's a web page.
- Register some alums.
- SMS with a verification code.
<-------- Requirements ------------>
- Python.
- Flask.
- Twilio
- Maybe a Data Base
<-------- Have to... ------------>
- Have to be responsive. 
- Useful.
- Functional.
"""

#Import libraries.
from flask import Flask, render_template

#Set an app
app = Flask(__name__, template_folder = "templates")

#Index section
#Jumbotron, navbar, buttons, footer-contacts.
@app.route('/')
def index():
	return render_template('base.html')

#Sign_up section
#Form, footer-contacts, navbar, buttons.
@app.route('/Sign_up', methods = ["GET", "POST"])
def sign_up():
	return "<h1> Here should be a form for a new member </h1>"

#Login section
#Form, footer-contacts, navbar, buttons.
@app.route('/Login', methods = ["GET", "POST"])
def login():
	return "<h1> Here should be a form for a old member </h1>"

#Run the app
if __name__ == '__main__': 
	app.run(debug = True, port = 5000)