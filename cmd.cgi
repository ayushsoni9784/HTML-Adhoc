#!/usr/bin/python3


import    cgi
import    cgitb
import subprocess
#to show common error in web browser
cgitb.enable() 


print("Content-type:text/html")
print("")


webdata=cgi.FieldStorage() # this will collect all the data html code eith data
# now extracting value of x
data=webdata.getvalue("x")
#sending output of client via web server
print(data)


output=subprocess.getoutput(data)
print(output)
print("<pre>")
print(output)
print("<pre>")
