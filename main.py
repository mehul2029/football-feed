import bs4
import urllib.request
import subprocess
import time
import sys

def sendmessage(message):
	subprocess.Popen(['notify-send',message])
	return

def get_the_feed():
	url = urllib.request.urlopen(str(sys.argv[1]))
	readHtml = url.read();
	url.close();
	soup = bs4.BeautifulSoup(readHtml,'html.parser')
	post = soup.body.find(class_ = "post").text
	return post 

previous = ""
while True:
	latest = get_the_feed()
	if latest != previous :
		previous = latest
		sendmessage(latest) 
	time.sleep(5)