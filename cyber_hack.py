import httplib, urllib, time
a = str(int(time.time()))
params = urllib.urlencode({'mode': '193', 'username': '701163015','a': a, 'producttype' : '0' })
headers = {
	"Host":"172.31.1.6:8090",
	"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0",
	"Accept":"image/png,image/*;q=0.8,*/*;q=0.5",
	"Accept-Language":"en-US,en;q=0.5",
	"Accept-Encoding":"gzip, deflate",
	"Referer":"https://172.31.1.6:8090/httpclient.html",
	"Content-Length":"57"
	}
conn = httplib.HTTPSConnection("172.31.1.6",8090)
conn.request("POST", "logout.xml", params, headers)
conn2 = httplib.HTTPConnection("172.31.49.91",8084)
conn2.request("GET","Lab_project/login.jsp")
res = conn2.getresponse()
print response.status, response.reason
#response = conn.getresponse()
