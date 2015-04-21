#a small piece of code that simply fills up your parent directory with loads of kitten photos
from urllib2 import urlopen
for i in xrange(100,1000,50):
    kittens = urlopen('http://placekitten.com/g/'+str(i)+'/'+str(i+50))
    print kittens
    f = open('kittens'+str(i)+'.jpg', 'wb')
    f.write(kittens.read())
    f.close()
