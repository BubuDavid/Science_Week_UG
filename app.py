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
from members_info import Member, Collect_Members
import datetime

#Set an app
app = Flask(__name__, template_folder = "templates")

#Index section
#Jumbotron, navbar, buttons, footer-contacts.
@app.route('/')  
def index():

	bubu = Member(social="https://www.facebook.com/DavidWeroBubu", name="David Pedroza", description="Estudiante de física 💧 | Amante de la ciencia y la tecnología 🤖 | Divulgador científico 👨🏻‍🔬 | Obsesivo por los concursos y olimpiadas 🥇 | En búsqueda exhaustiva por conocimiento de todo tipo 🧐 | Jugador nada profesional de voleibol 🏐", photo_link="https://scontent.fbjx1-1.fna.fbcdn.net/v/t1.0-9/36511070_1727456190663968_8061036432086532096_n.jpg?_nc_cat=109&_nc_oc=AQlmkWJAgd4gZSTfNYTPsU6rkkc3tR_E4Rv4LuCWf_YGTFAaYx--Q2YeTnupuToeAehQuEcx9DzwQ68MMKB9cLV4&_nc_ht=scontent.fbjx1-1.fna&oh=dcd11e166fcda7cc0fe530567d79e93e&oe=5E084BD0", pos="Coordinator")
	fl_members = Collect_Members({bubu.name: bubu})
	missa = Member(social="https://www.facebook.com/Gabriel.Missael.Barco?epa=SEARCH_BOX", name="Missael Barco", description="Estudiante de Física 📈/ Entusiasta de C/C++ / Divulgador de ciencia 🍃 / Gusto por movimiento Maker / Me gusta inspirar a otros, y también me gustan los perros. 🐶", photo_link="https://futurelab.mx/images/members/missael.jpg", pos="Community Member")
	ferro = Member(social="https://www.facebook.com/ferro.11", name="Rodolfo Ferro", description="Computer-mathemagics! · Future Lab · Lab León · GitHub Campus Expert · CdeCMx · Python · Saris 💖", photo_link="https://rodolfoferro.xyz/assets/images/profile.jpg", pos="Co-Founder")
	fl_members.add(ferro)
	fl_members.add(missa)
	return render_template('index.html', members = fl_members.member_list.values())

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

#Page Not Found section
@app.errorhandler(404)
def error404(e):
	return render_template('404.html'), 404

#Run the app
if __name__ == '__main__': 
	app.run(debug = True, port = 5000)