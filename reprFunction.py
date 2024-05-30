# s= """w'o"w"""
# repr(s)
# str(s)
# eval(str(s))==s
# eval(repr(s))==s

import datetime
today=datetime.datetime.now()
print(str(today))
print(repr(today))