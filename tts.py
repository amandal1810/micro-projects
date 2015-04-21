#type in a text as input and hear it in voice! A small Text-to-Speech Convereter using the Yahoo TTS API. Voice will play in your default media player.
import urllib2, urllib
import os
baseurl = "http://tts-api.com/tts.mp3?"
print "enter text to convert to speech : "
text = raw_input()
api_url = baseurl + urllib.urlencode({'q':text})
result = urllib2.urlopen(api_url).read()
f = open('tts.mp3', 'wb')
f.write(result)
f.close()
os.system("start tts.mp3")
