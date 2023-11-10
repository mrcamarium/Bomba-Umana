import zlib, zipfile
from sys import argv

test = "0" * 10000

cmpstr = zlib.compress(test.encode('utf-8'))

to_cmp = test + str(cmpstr)
cmpstr = zlib.compress(to_cmp.encode('utf-8'))

zf = zipfile.ZipFile("test.zip" ,mode='w',compression=zipfile.ZIP_DEFLATED)

for  i in range(int(argv[1])):
	print(i)
	zf.writestr('a'+ str(i) +'.txt',test)