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
from flask import Flask, render_template
from members_info import Member, Collect_Members

#Set an app
app = Flask(__name__, template_folder = "templates")

#Set a global user, I'll use later.
bubu = Member(phone="", social="https://www.facebook.com/DavidWeroBubu", name="David Pedroza", description="Estudiante de física 💧 | Amante de la ciencia y la tecnología 🤖 | Divulgador científico 👨🏻‍🔬 | Obsesivo por los concursos y olimpiadas 🥇 | En búsqueda exhaustiva por conocimiento de todo tipo 🧐 | Jugador nada profesional de voleibol 🏐", photo_link="https://scontent.fbjx1-1.fna.fbcdn.net/v/t1.0-9/36511070_1727456190663968_8061036432086532096_n.jpg?_nc_cat=109&_nc_oc=AQlmkWJAgd4gZSTfNYTPsU6rkkc3tR_E4Rv4LuCWf_YGTFAaYx--Q2YeTnupuToeAehQuEcx9DzwQ68MMKB9cLV4&_nc_ht=scontent.fbjx1-1.fna&oh=dcd11e166fcda7cc0fe530567d79e93e&oe=5E084BD0", pos="Coordinator")

#Index section
#Jumbotron, navbar, buttons, footer-contacts.
@app.route('/')  
def index():

	fl_members = Collect_Members({bubu.name: bubu})
	missa = Member(phone="", social="https://www.facebook.com/Gabriel.Missael.Barco?epa=SEARCH_BOX", name="Missael Barco", description="Estudiante de Física 📈/ Entusiasta de C/C++ / Divulgador de ciencia 🍃 / Gusto por movimiento Maker / Me gusta inspirar a otros, y también me gustan los perros. 🐶", photo_link="https://futurelab.mx/images/members/missael.jpg", pos="Community Member")
	ferro = Member(phone="", social="https://www.facebook.com/ferro.11", name="Rodolfo Ferro", description="ƒ[💻] Computer-mathemagician | 👨🏻‍💻 Consultor tech en Lab León | 🚩 GitHub Campus Expert | ⚙️ Dev en CloudLinux | 🐍 Pythonista | 🧠 Inteligencia Artificial | ⚡️ Automatización", photo_link="https://rodolfoferro.xyz/assets/images/profile.jpg", pos="Co-Founder")
	fl_members.add(ferro)
	fl_members.add(missa)
	return render_template('index.html', members = fl_members.member_list.values())

#Sign_up section
#Form, footer-contacts, navbar, buttons.
@app.route('/sign-up', methods = ["GET", "POST"])
def sign_up():
	flag = False
	return render_template('sign_up.html', member=bubu, flag=flag)

#Login section
#Form, footer-contacts, navbar, buttons.
@app.route('/login', methods = ["GET", "POST"])
def login():
	flag = False
	return render_template("login.html", flag=flag)

#Page Not Found section
@app.errorhandler(404)
def error404(e):
	return render_template('404.html'), 404

#Run the app
if __name__ == '__main__': 
	app.run(debug = True, port = 5000)