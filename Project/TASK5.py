#use the request libray
import requests
#for task8 Test Case
class TASK5:
    #to modify the headers user-agent
 headers = {
     "User-Agent":"Mobile"
 }
 #the webserver ip url spicyx
 url = "http://192.168.126.148/spicyx/"
    #client request url,headers
 r = requests.get(url,headers=headers)
    #display the whole html content of the webpage
 print(r.text)
 #display the status response code
 print("Status code:")
 print("\t *", r.status_code)
 #get just the url headers
 h = requests.head(url)
 print("Header:")
 print("**********")
 #to print out url headers content line by line
 for x in h.headers:
     print("\t ", x, ":", h.headers[x])
 for x in headers:
     print("\t ", x, ":", headers[x])
 print("**********")


