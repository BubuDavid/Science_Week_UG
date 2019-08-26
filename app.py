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
from flask import Flask, render_template, url_for, request, session, redirect
from members_info import Member, Collect_Members
from unidecode import unidecode
from dbmongo import MONGO_URI
from dbmongo import db_connect
from dbmongo import db_insert_user
from dbmongo import db_find_all
from form import LoginForm
from form import New_Member


#Set an app
app = Flask(__name__, template_folder = "templates")
#Set users dbconnector
users = db_connect(MONGO_URI, 'mi_app', 'users')

test_profile = Member(phone="", 
              social="https://www.facebook.com/DavidWeroBubu", 
              name="David Pedroza", 
              description="Estudiante de física 💧 | Amante de la ciencia y la tecnología 🤖 | Divulgador científico 👨🏻‍🔬 | Obsesivo por los concursos y olimpiadas 🥇 | En búsqueda exhaustiva por conocimiento de todo tipo 🧐 | Jugador nada profesional de voleibol 🏐",#.decode('utf8'), 
              photo_link="https://scontent.fbjx1-1.fna.fbcdn.net/v/t1.0-9/36511070_1727456190663968_8061036432086532096_n.jpg?_nc_cat=109&_nc_oc=AQlmkWJAgd4gZSTfNYTPsU6rkkc3tR_E4Rv4LuCWf_YGTFAaYx--Q2YeTnupuToeAehQuEcx9DzwQ68MMKB9cLV4&_nc_ht=scontent.fbjx1-1.fna&oh=dcd11e166fcda7cc0fe530567d79e93e&oe=5E084BD0", 
              pos="Coordinator"

             		)

#Index section
#Jumbotron, navbar, buttons, footer-contacts.
@app.route('/')  
def index():
	session_active=False
	if 'username' in session:
		session_active = True
	fl_members = db_find_all(users)

	return render_template('index.html', session_active=session_active, members = fl_members)

#Sign_up section
#Form, footer-contacts, navbar, buttons.
@app.route('/sign-up', methods = ["GET", "POST"])
def sign_up():
	flag = False
	vc = False
	form = New_Member(request.form)
	new_name=None
	new_description=None
	new_position=None
	new_social=None
	new_phone_number=None
	new_photo_link=None
	condition=None

	if request.method == 'POST':
		new_name = form.name.data
		new_description = form.description.data #.decode('utf-8')
		new_position = form.position.data
		new_social = form.social.data
		new_phone_number = form.phone_number.data
		new_photo_link = form.photo_link.data
		condition=[new_social, new_position, new_description, new_name, new_photo_link, new_phone_number]
		if condition != ['','','','','','']:
			member = {
				"Name": new_name,
				"Description": new_description,
				"Position": new_position,
				"Social": new_social,
				"Phone_number": new_phone_number,
				"Photo_link": new_photo_link
			}
			db_insert_user(users, member)
			flag = True


	return render_template('sign_up.html', vc=vc, member=test_profile, flag=flag, name=new_name)

#Login section
#Form, footer-contacts, navbar, buttons.
@app.route('/login', methods = ["GET", "POST"])
def login():
	flag = False
	if request.method == 'POST':
		pass

	return render_template("login.html", flag=flag)

#Page Not Found section
@app.errorhandler(404)
def error404(e):
	return render_template('404.html'), 404

#Run the app
if __name__ == '__main__': 
	app.run(debug = True, port = 5000)