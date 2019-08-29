# -*- coding: utf-8 -*-
# ===============================================================
# Author: David Pedroza Segoviano
# Email: david.pedroza.segoviano@gmail.com
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by David Pedroza (Bubu), for
# his workshop in Forum Tecnológico con PUPAS at León, Gto.
# Any explicit usage of this script or its
# contents is granted according to the license provided and
# its conditions.
# ===============================================================


"""
<-------- IDEAS ------------>
- It's a web page. :D
- Register some alums.
- SMS with a verification code.
<-------- Requirements ------------>
- Python. :D
- Flask. :D 
- Twilio
- Maybe a Data Base
<-------- Have to... ------------>
- Have to be responsive. :D  
- Useful.
- Functional.
"""

#Import libraries.
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__, template_folder = "templates")

@app.route('/')  
def index():
	redirect('/redirect')

	return redirect('/redirect')

@app.route('/redirect')
def redirecte():
	return "holly shit!"

#Page Not Found section
@app.errorhandler(404)
def error404(e):
	return render_template('404.html'), 404

#Run the app
if __name__ == '__main__': 
	app.run(debug = True, port = 5000)