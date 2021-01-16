def checkBase(userid):
	uid = str(userid)
	opener = open("base.txt","r").read().split("\n")
	if uid in opener:
		return True
	else:
		return False

def newUser(userid,time_now,log,admin):
	try:
		uid = str(userid)
		opener = open("base.txt","a")
		opener.write("\n"+uid)
		opener.close()
		opener = open("profiles/"+uid+".txt","w")
		opener.write(str(time_now))
		if log == "y" or log == "Y":
			print("|Добавлен новый айди: "+uid)
	except Exception as E:
		print(E)

def er(ids, argv): # error log for admins ids - admin id, argv - 1 value
	import requests
	params = {'chat_id': ids, 'text': f'{argv}'}
	resp = requests.post(f'https://api.telegram.org/bot1497960082:AAHQyL48zNZh0YDcTnUhhEVcnZPNkYm6e/sendMessage', params)