#!/usr/bin/python3

# Import modules for CGI handling 
import cgi, cgitb
import datetime
import re

#Fail Checker
cgitb.enable()
formData = cgi.FieldStorage()
#Obtain radio button values
rb=formData.getvalue('typ')
rb=str(rb)
#Obtain year value
ye = formData.getvalue('year')
#Values for naming
st="1 21 31"
nd="2 22"
rd="3 23"
if(ye.isdigit()):
	#convert string to integer so it can be processed by algorithm
	ye=int(ye)
	def Easter(y):
		a = y % 19
		b = y // 100
		c = y % 100
		d = b // 4
		e = b % 4
		g = (8 * b + 13) // 25
		h = (19 * a + b - d - g + 15) % 30
		j = c // 4
		k = c % 4
		m = (a + 11 * h) // 319
		r = (2 * e + 2 * j - k - h + m + 32) % 7
		n = (h - m + r + 90) // 25
		p = (h - m + r + n + 19) % 32

		return datetime.date(year=y, month=n, day=p)


	#Print webpage
	print('Content-type:text/html\r\n\r\n')
	print('<html lang="en"><head>')
	print('<title>Success</title>')
	print('<meta charset="utf-8">')
	print('<link rel="stylesheet" href="..\style.css">')
	print('</head>')
	print('<body>')
	print('<div>')
	print('<header><h2>Easter on that year:</h2></header>')
	easter = Easter(ye)
	#Radio button type variations
	if(rb=="proper"):
		sc=str(easter.strftime("%d"))
		if(sc in st):
			date=easter.strftime("%dst of %B, %Y")
		elif(sc in nd):
			date=easter.strftime(" %dnd of %B, %Y")
		elif(sc in rd):
			date=easter.strftime("%drd of %B, %Y")
		else:
			date=easter.strftime("%dth of %B, %Y")
	elif(rb=="weekday"):
		sc=str(easter.strftime("%d"))
		if(sc in st):
			date=easter.strftime("%A, %dst of %B, %Y")
		elif(sc in nd):
			date=easter.strftime("%A, %dnd of %B, %Y")
		elif(sc in rd):
			date=easter.strftime("%A, %drd of %B, %Y")
		else:
			date=easter.strftime("%A, %dth of %B, %Y")
	else:
				date = easter.strftime("%d/%m/%Y")
	#Continue printing web page
	print('<p>'+date+'</p>')
	print('<footer>Algorithm provided by CM1103 Problem Solving with Python, Stuart Allen.</footer>')
	print('</div>')
	print('</body></html>')
else:
	#in case of gibberish/words/punctuation in the input field
	print('Content-type:text/html\r\n\r\n')
	print('<html lang="en"><head>')
	print('<title>Civilized Error Message</title>')
	print('<meta charset="utf-8">')
	print('<link rel="stylesheet" href="..\style.css">')
	print('</head>')
	print('<body>')
	print('<div>')
	print('<header><h2>Oops!</h2></header>')
	print('<p>It would appear that you have tried to break the code, well, you failed. I anticipated that, so here we are, with a civilized error message, with neat CSS formatting. Now if you still want to find out what the easter date of a given year is, go back and enter an actual number.</p>')
	print('<form action="..\Exercise2.html"><input type="submit" value="Back to Trying" /></form>')
	print('<footer>Easter Algorithm provided by CM1103 Problem Solving with Python, Stuart Allen.</footer>')
	print('</div>')
	print('</body></html>')
rb=0
yr=0