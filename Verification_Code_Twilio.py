from twilio.rest import Client
from random import randint

def send_SMS(account_sid, auth_token, phone_number, message_content):
	
	client = Client(account_sid, auth_token)
	
	message = client.messages.create(
		to = "+52" + phone_number,
		from_ = "",
		body = message_content
	)

def code_generator(name):
	random = str(randint(1000,10000))
	code = name.split()
	code = code[0]
	code += random
	code = code[::-1]
	print(code)
	return code


