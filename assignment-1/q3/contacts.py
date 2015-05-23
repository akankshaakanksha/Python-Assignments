
from phonenum import *

def create_contacts():
	return {}

def add_contacts(contacts, name, phone_num, phone_type,country_code=None):
    if contacts.has_key(name):
        phone_nums = contacts[name]
        phone_nums.append(Phonenum(phone_num, phone_type,country_code))
    else:
    	contacts[name] = [ Phonenum(phone_num, phone_type,country_code) ]
def update_contact_number(contacts,contact_name,old_number,new_number):
	try:
#Assuming a single contact for every contact name
		contacts[contact_name][0]=new_number
		return True
	except:
		return False
		
