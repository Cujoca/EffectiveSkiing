import urllib2

contents = urllib2.urlopen("http://www.effectiveskiing.com").read()

print(str(contents))

