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

class Member():

	#Attributes:
	def __init__(self, name, description, photo_link, pos, social, phone):
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
			info = info + person.pos + "\n"
			info += person.phone

		return info

	#Methods
	def add(self, new_member):
		self.member_list[new_member.name] = new_member

	def delete(self, bad_member):
		if bad_member in self.member_list:
			del self.member_list[bad_member]
		else:
			pass
			#print("El mimebro no existe")

	def edit_profile(self, member_edit, new_photo_link="", new_phone="", new_name = "", new_description = "", new_pos="", new_social=""):
        
		if member_edit in self.member_list.values():
			#print("No existe el miembro")
			return
			
		name_aux = self.member_list[member_edit].name
		description_aux = self.member_list[member_edit].description
		photo_link_aux = self.member_list[member_edit].photo
		pos_aux = self.member_list[member_edit].pos
		social_aux = self.member_list[member_edit].social
		phone_aux = self.member_list[member_edit].phone

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
		if new_phone != "":
			phone_aux = new_phone

		new = Member(phone=phone_aux, social = social_aux, name=name_aux, description=description_aux, photo_link=photo_link_aux, pos=pos_aux)

		self.add(new)
		self.delete(member_edit)  
