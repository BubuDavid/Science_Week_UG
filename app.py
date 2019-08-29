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
from members_info import Member, Collect_Members
from unidecode import unidecode
from dbmongo import MONGO_URI
from dbmongo import db_connect
from dbmongo import db_insert_user
from dbmongo import db_find_all
from dbmongo import db_delete_one
from form import LoginForm, New_Member, Code_Verification_Form
from Verification_Code_Twilio import send_SMS, code_generator

#Set an app
app = Flask(__name__, template_folder = "templates")
#Set users dbconnector
users = db_connect(MONGO_URI, 'mi_app', 'users')
tempdb = db_connect(MONGO_URI, 'test_database', 'posts')
member = {}

test_profile = Member(phone="", 
              social="https://www.facebook.com/DavidWeroBubu", 
              name="David Pedroza", 
              description="Estudiante de física 💧 | Amante de la ciencia y la tecnología 🤖 | Divulgador científico 👨🏻‍🔬 | Obsesivo por los concursos y olimpiadas 🥇 | En búsqueda exhaustiva por conocimiento de todo tipo 🧐 | Jugador nada profesional de voleibol 🏐".decode('utf8'), 
              photo_link="https://scontent.fbjx1-1.fna.fbcdn.net/v/t1.0-9/36511070_1727456190663968_8061036432086532096_n.jpg?_nc_cat=109&_nc_oc=AQlmkWJAgd4gZSTfNYTPsU6rkkc3tR_E4Rv4LuCWf_YGTFAaYx--Q2YeTnupuToeAehQuEcx9DzwQ68MMKB9cLV4&_nc_ht=scontent.fbjx1-1.fna&oh=dcd11e166fcda7cc0fe530567d79e93e&oe=5E084BD0", 
              pos="Coordinator"

             		)

#Index section
#Jumbotron, navbar, buttons, footer-contacts.
@app.route('/')  
def index():
	error = False
	fl_members = db_find_all(users)

	return render_template('index.html', members = fl_members)

@app.route('/verification_code/<string:vc>/<int:error>', methods=['GET', 'POST'])
def verification_code(vc, error):
	form2 = Code_Verification_Form(request.form)
	print(vc)
	
	if request.method == 'POST':
		while form2.code.data != vc:
			return redirect(f'/verification_code/{vc}/1')
		#Put member in db.
		new_member = db_find_all(tempdb)

		for item in new_member:
			query = {
				"Name": item['Name'],
				"Description": item['Description'],
				"Position": item['Position'],
				"Social": item['Social'],
				"Phone_number": item['Phone_number'],
				"Photo_link": item['Photo_link']
			}
		db_delete_one(tempdb, query)
		db_insert_user(users, query)
			
		return redirect('/sign-up/1')

	return render_template("verification.html", error=error)


#Sign_up section
#Form, footer-contacts, navbar, buttons.
@app.route('/sign-up/<int:flag>', methods = ["GET", "POST"])
def sign_up(flag):
	vc = False
	repeat=False
	form = New_Member(request.form)
	new_name=""
	new_description=""
	new_position=""
	new_social=""
	new_phone_number=""
	new_photo_link=""
	condition=""

	if request.method == 'POST' and vc == False:
		repeat=False
		auxiliar = db_find_all(users, {"Phone_number": str(form.phone_number.data)})
		try:
			for item in auxiliar:
				print(item['Name'])
				#repeat=True
		finally:
			if repeat!=True:
				
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

					#Code_Verification_Section
					sid = os.environ.get('TWILIO_AUTH_SID')
					token = os.environ.get('TWILIO_AUTH_TOKEN')
					vc = code_generator(new_name)	
					print(vc)
					send_SMS(account_sid = sid, auth_token=token, phone_number=new_phone_number, message_content=vc)
					db_insert_user(tempdb, member)
					return redirect(f'/verification_code/{vc}/0')

	return render_template('sign_up.html', vc=vc, repeat=repeat, member=test_profile, flag=flag, name=new_name)

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