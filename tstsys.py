import sys
import urllib.request
print(sys.platform)
page = urllib.request.urlopen('http://hesam80.pergig.ir')
print(page)
for line in page :
	print(line)
	
