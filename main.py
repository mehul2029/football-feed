import bs4
import urllib.request
import subprocess
import time
import sys

#Popup a notification on ubuntu desktop
def sendmessage(message):
	length = len(message)
	for i in range(length//124+1):
		subprocess.Popen(['notify-send',message[(i*124) : (i+1)*124]])
	return

#Request and parse the given webpage for commentary 
def get_the_feed():
	url = urllib.request.urlopen(str(sys.argv[1]))
	readHtml = url.read();
	url.close();
	soup = bs4.BeautifulSoup(readHtml,'html.parser')
	post = soup.body.find(class_ = "post").text
	return post 

#Main function 
previous = ""
while True:
	latest = get_the_feed()
	if latest != previous :
		previous = latest
		sendmessage(latest) 
	time.sleep(5)