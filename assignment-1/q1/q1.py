Users={}
Acquaintances={}
Messages={}
msgcounter=111


def add_friend(user_id,friend_id):
	try: 
		Acquaintances[user_id].append(friend_id)
		return True
	except:
		return False

def add_friends(user_id,friend_ids):
	try:
		Acquaintances[user_id].extend(friend_ids)
		return True
	except: 
		return False

def remove_user(user_id):
	try:
		d=User.pop(user_id)
		return True
	except:
		return False


def get_friends(user_id):
	try:
		return tuple(Acquantances[user_id])
	except:
		return None

def get_friends_of_friends(user_id):
	ret=[]
	try:
		for i in Acquaintances[user_id]:
#			print i
#	ret.extend(Acquaintances[i])
			for j in Acquaintances[i]:
				ret.append(j)
#			print ret
#			print "i",i
		
		for i in Acquaintances[user_id][:]:
			if i  in ret[:]:
				ret.remove(i)

		if user_id in ret[:]:
			ret.remove(user_id)
		return tuple(ret)
	except:
		return None


	
from time import strftime,gmtime
def send_message(sender_id,reciever_id,msg):
	try:
		date=strftime("%d-%m-%Y",gmtime())
		time=strftime("%H:%M:%S",gmtime())
		newmsg=(sender_id,msgcounter,msg,date,time)
		msgcounter=msgcounter+1
		Messages[reciever_id].append(newmsg)
		return True

	except:

		return False
		
def send_group_message(sender_id,recievers,msg):
	
		for i in range(len(recievers)):
			
			try:
				date=strftime("%d-%m-%Y",gmtime())
			 	time=strftime("%H:%M:%S",gmtime())
				newmsg=(sender_id,msgcounter,msg,date,time)
			 	msgcounter=msgcounter+1
			 	Messages[recievers[i]].append(newmsg)
			

			except: 
				return False

		return True

def get_messages_from_friend(rec,frn):
	try:
		ret=[]
		for i in range(len(Messages[rec])):
			if Messages[rec][i][0]==frn:
				ret.append(Messages[rec][i])
			
		return tuple(ret)

	except:
		return False


def get_messages_from_all_friends(rec):
	try:
		return tuple(Messages[rec])
	except:
		return False

def get_birth_day_messages(rec):
	try:
		ret=[]
		for i in range(len(Messages[rec])):
			if Messages[rec][i][2][0]==Users[rec][2][0] and Messages[rec][i][2][1]==Users[rec][2][1] and Messages[rec][i][2][4]==Users[rec][2][2] and Messages[rec][i][2][3]==Users[rec][2][3]:
				ret.append(Messages[rec][i])
		return tuple(ret)

	except:
		return False
def delete_message(usr,msg):
	try:
		for i in range(len(Messages[usr])):
			if Messages[usr][i][1]==msg:
				del Messages[usr][i]
		return True

	except:
		return False
def delete_messages(uid,msgs):
	dcount=0
	for i in range(len(msgs)):
		try:
			delete_message(uid,msgs[i])
			dcount=dcount+1

		except:
			pass
	return dcount
def delete_all_messages(user_id):
	try:
		del Messages[user_id][:]
		return True
	except:
		return False

def delete_messaged_from_friend(rec,frn):
	  try:
	  	for i in range(len(Messages[rec])):
	  		if Messages[rec][i][0]==frn:
				del Messages[rec][i]
		return True
          except:
	  	return False

