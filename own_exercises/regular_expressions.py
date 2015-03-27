import re
match = r3.search(pattern, text)

# example each line represents i/o in python interpreter
match = re.search('iig', 'called piiig')
match
<_sre.SRE_Match object at 0x7fcfffd54308>
match.group()
'iig'

match = re.search('iig', 'called piiig')
match
# blank -- match is NULL
match.group()
# will produce an error because match is not an object 

#use an if match: to get around the error
def Find(pat, text):
    match = re.search(pat, text)
    if match:
        print match.group()
    else:
        print 'not found'

#i/o example
Find('ig', 'called piiig')
ig
Find('igs', 'called piiig')
not found

# Normal characters match each other
# . (dot) any char except new line \n
# \w word characters [abcd..., 1234]
# \d digit
# \s whitespace \S non-whitepsace
# + 1 or more ## finds 1 or more of the chars ### Find(r':w+', 'blah blah :kitten blabh blah') ==> :kitten
# *0 or more ## finds 0 or more

# REMEMBER it will only find the 1st instance of the match

# using r to make the string equal to raw text (no processing happens in string)
# which means special characters aren't handled in a special way.
Find(r'c.l', 'c.lled piiig much better: xyzgs')
c.l

# Finding an email address: brackets [] finds a group
Find(r'[\w.]+@[\w.]+', 'blah nick.p@gmail.com yatta @')
nick.p@gmail.com

# finding a username and domain name seperately -- parentheses () around the parts you care about
m = re.search(r'([\w.]+)@([\w.]+)', 'blah nick.p@gmail.com yatta @')
m.group()
'nick.p@gmail.com'
m.group(1)
'nick.p'
m.group(2)
'gmail.com'

# find all matches
re.findall(r'[\w.]+@[\w.]+', 'blah nick.p@gmail.com yatta foo@bar')
['nick.p@gmail.com', 'foo@bar']

re.findall(r'([\w.]+)@([\w.]+)', 'blah nick.p@gmail.com yatta foo@bar')
[('nick.p', 'gmail.com'), ('foo', 'bar')]

# run: dir(re) -- this gives a list of flags which can be used just add it as a third argument
re.findall(r'([\w.]+)@([\w.]+)', 'blah nick.p@gmail.com yatta foo@bar', IGNORECASE)