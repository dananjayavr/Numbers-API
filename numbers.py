import urllib2

# Numbers API - Function calls wrapped in Python functions.

# Query Options:

# fragment: Mix output with user created strings
# notfound (default): Return custom 404 style message. 
# Ex: http://numbersapi.com/75865944?default=Not%20Cool!

# notfound (floor or ceil): round the number accordingly.
# Ex: http://numbersapi.com/35353?notfound=floor
# Ex: http://numbersapi.com/353530?notfound=ceil?fragment'

# Use max,min to limit random queries
# Ex: http://numbersapi.com/random?min=10&max=20'

# supply json to get a JSON output: (Process JSON accordingly)
# Ex: http://numbersapi.com/random?json'



def number_trivia(n,fragment=False):
	'''Get some trivia on a number n.
	'''
	if fragment == True:
		return urllib2.urlopen('http://numbersapi.com/%d/trivia?fragment' % n).read()
	else:
		return urllib2.urlopen('http://numbersapi.com/%d/trivia' % n).read()



def number_math(n,fragment=False):
	if fragment == True:
		return urllib2.urlopen('http://numbersapi.com/%d/math?fragment' % n).read()
	else:
		return urllib2.urlopen('http://numbersapi.com/%d/math' % n).read()



def number_date(month,date,fragment=False):
	if fragment == True:
		return urllib2.urlopen('http://numbersapi.com/%d/%d/date?fragment' % (month,date)).read()
	else:
		return urllib2.urlopen('http://numbersapi.com/%d/%d/date' % (month,date)).read()



def random_trivia(fragment=False):
	if fragment == True:
		return urllib2.urlopen('http://numbersapi.com/random/trivia?fragment').read()
	else:
		return urllib2.urlopen('http://numbersapi.com/random/trivia').read()



def random_math(fragment=False):
	if fragment == True:
		return urllib2.urlopen('http://numbersapi.com/random/math?fragment').read()
	else:
		return urllib2.urlopen('http://numbersapi.com/random/math').read()


def random_date(fragment=False):
	if fragment == True:
		return urllib2.urlopen('http://numbersapi.com/random/date?fragment').read()
	else:
		return urllib2.urlopen('http://numbersapi.com/random/date').read()

