import urllib, json
import datetime, time
import threading
channel = "699545" # channel id
read_api = "7U43M7RE7WG4E7SL" # API key
check_interval = 5; # in seconds

next_call = time.time()
url = "http://api.thingspeak.com/channels/" + channel + "/feed.json?key=" + read_api
response = urllib.urlopen(url);
data = json.loads(response.read())
channeldata = data[u'channel']
channeldata = channeldata[u'last_entry_id']
cache = channeldata
print "Demo to retrieve Data from the ThingSpeak Channel"
print "CTRL+C to end"

def checkChannel():
	global next_call
	global cache
	global channel
	global read_api
	url = "http://api.thingspeak.com/channels/" + channel + "/feed.json?key=" + read_api
	response = urllib.urlopen(url);
	data = json.loads(response.read())
	channeldata = data[u'channel']
	channeldata = channeldata[u'last_entry_id']

	if cache != channeldata:
		print "CHANNEL UPDATE!"
		cache = channeldata

	next_call = next_call + check_interval
	threading.Timer( next_call - time.time(),checkChannel ).start()

checkChannel();
