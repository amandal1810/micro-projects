#asks for the name of a city/state/country and shows the weather forecast for that city/state/country in your web browser using the Yahoo Weather API
import urllib2, urllib, json
import os
baseurl = "https://query.yahooapis.com/v1/public/yql?"
#yql_query = "select wind from weather.forecast where woeid=2460286"
print "enter city name to obtain weather forecast : "
country = raw_input()
yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='"+country+"')"
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
result = urllib2.urlopen(yql_url).read()
data = json.loads(result)
to_html = data['query']['results']['channel']['item']['title']+"<br/></br>"+data['query']['results']['channel']['item']['description']
print to_html
f = open('weather_now.html', 'wb')
f.write(to_html)
f.close()
os.system("start weather_now.html")
