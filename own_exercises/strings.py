## https://developers.google.com/edu/python/strings

#################
## Concatenate ##
#################
s = 'hi'
print s[1]          ## i
print len(s)        ## 2
print s + ' there'  ## hi there

pi = 3.14
## text = 'The value of pi is ' + pi    ## NO, does not work
text = 'The value of pie is ' + str(pi) ## yes

raw = r'this\t\n and that'
print raw ## this\t\n and that

multi = """It was the best of times.
It was the worst of times."""
print multi

###########################
## Common string methods ##
###########################

## https://docs.python.org/2/library/stdtypes.html#string-methods

# s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
# s.strip() -- returns a string with whitespace removed from the start and end
# s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
# s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
# s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
# s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
# s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
# s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

s = "Hello"
s[1:4]      ## is 'ell' -- chars starting at index 1 and extending up to but not including index 4
s[1:]       ## is 'ello' -- omitting either index defaults to the start or end of the string
s[:]        ## is 'Hello' -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
s[1:100]    ## is 'ello' -- an index that is too big is truncated down to the string length

##############
## String % ##
##############
# % operator
text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff','blow down')
print text

# add parens to make the long-line work:
text = ("%d little pigs come out or I'll %s and %s and %s" % 
    (3, 'huff', 'puff', 'blow down'))

# i18n Strings (Unicode)
ustring = u'A unicode \u018e string \xf1'
print ustring # u'A unicode \u018e string \xf1'

## (ustring from above contains a unicode string)
s = ustring.encode('utf-8')
print s ## 'A unicode \xc6\x8e string \xc3\xb1'  ## bytes of utf-8 encoding
t = unicode(s, 'utf-8')     ## Convert bytes back to a unicode string
print t == ustring        ## True ## It's the same as the original, yay!