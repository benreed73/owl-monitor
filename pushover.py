import httplib
import urllib

def send_pushover(message,subject,api_key,user_key,device):
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	try :
		conn.request("POST", "/1/messages.json", urllib.urlencode({
		"token": api_key,
		"user": user_key,
		"message": message,
		"device": device,
		"title": subject
		}), { "Content-type": "application/x-www-form-urlencoded" })
		conn.getresponse()
	except :
		pass
	
