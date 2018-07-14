import re
str = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
s = re.findall('@(\S+)', str)
print(s)

s = re.findall('\S+?@\S+', str)
print(s)

s = re.findall('\S+@\S+', str)
print(s)
str = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
s = re.findall('href=".+"', str)
print(s)
s = re.findall('href="(.+)"', str)
print(s)
s = re.findall('http://.*',str)
print(s)