class Member():

	#Attributes:
	def __init__(self, name, description, photo_link, pos, social):
		self.name = name
		self.description = description
		self.photo = photo_link
		self.pos = pos
		self.social = social

	#Methods
	def __str__(self):
		info = self.name + "\n"
		info += self.description + "\n"
		info += self.pos + "\n"
		#info += self.photo
		return info

class Collect_Members():

	#Attributes:
	def __init__(self, member_list):
		self.member_list = member_list


	#Special Methods
	def __str__(self):
		info = ""
		for person in self.member_list.values():
			info = info + person.name + "\n"
			info = info + person.description + "\n"
			info = info + person.pos + "\n\n"

		return info

	#Methods
	def add(self, new_member):
		self.member_list[new_member.name] = new_member

	def delete(self, bad_member):
		if bad_member in self.member_list:
			del self.member_list[bad_member]
		else:
			print("El mimebro no existe")

	def edit_profile(self, member_edit, new_photo_link="", new_name = "", new_description = "", new_pos="", new_social=""):
        
		if member_edit in self.member_list.values():
			print("No existe el miembro")
			return
			
		name_aux = self.member_list[member_edit].name
		description_aux = self.member_list[member_edit].description
		photo_link_aux = self.member_list[member_edit].photo
		pos_aux = self.member_list[member_edit].pos
		social_aux = self.member_list[member_edit].social

		if new_name != "":
			name_aux = new_name
		if new_description != "":
			description_aux = new_description
		if new_photo_link != "":
			description_aux = new_photo_link
		if new_pos != "":
			pos_aux = new_pos
		if new_social != "":
			social_aux = new_social

		new = Member(social = social_aux, name=name_aux, description=description_aux, photo_link=photo_link_aux, pos=pos_aux)

		self.add(new)
		self.delete(member_edit)  

"""

bubu = Member(name='Bubu', description = 'SCIENCE BITCH!', photo_link='https://scontent.fbjx1-1.fna.fbcdn.net/v/t1.0-9/36511070_1727456190663968_8061036432086532096_n.jpg?_nc_cat=109&_nc_eui2=AeHvY-uNbWwHxjD-26n79HpTAGZr9eVNCygPi8AYD9d3k85jeTQ56cU9tbi-yedItJkJV1XeSe9_hM8BEzNYeehH-cdDgI-D390HLAU0kXmh2w&_nc_oc=AQmwu9YOAK2aH4S3RcZ_bkYPbuFKQsJMyRPc7-pCqVQEghcaN5PelA4elRXcJEuvZbyB6YF4X4MsjDsoh4bYcg2E&_nc_ht=scontent.fbjx1-1.fna&oh=c3d04de6f331b03c00be1d3220bcc216&oe=5E084BD0', time=str(datetime.datetime.now()))
missa = Member(name='Missa', description="I'm joto", photo_link='https://scontent.fbjx1-1.fna.fbcdn.net/v/t1.0-9/59404925_2364695540478790_6760001489923473408_n.jpg?_nc_cat=100&_nc_eui2=AeHWHl1NiAWlnt-fkoCA1m8vdBOCYHRN-ZqHy3McAftCCEFMOCAGFPFogPKQuq1gzS5UEP0dPOKFmLkcFNq1zdLE_hC4cEjKS1RaVK0qjt8Bww&_nc_oc=AQke_4l-w2FcfZR2wkYXLv1K29Eiav01wChTdFN7RR9hA203FWybjqB9U7ueMoWqjkbsQ_9jzgeX1rjkmG1-G7gr&_nc_ht=scontent.fbjx1-1.fna&oh=0e312325e95491606b0433f02d3f4c95&oe=5E1297CE', time=str(datetime.datetime.now()))
rodo = Member(name="Rodolfo", description="Python Rocks!", photo_link="https://rodolfoferro.xyz/assets/images/profile.jpg", time=str(datetime.datetime.now()))
"""

"""
fl_members = Collect_Members({bubu.name: bubu, missa.name: missa})

fl_members.edit_profile(member_edit='Bubu', new_name="David Pedroza")

print(fl_members)

print("NOOOOOOOOOOOOOOOOOWWWWWWWWWWWWWWWW\n")

fl_members.add(rodo)
fl_members.delete('David Pedroza')

print(fl_members)
"""