# https://developers.google.com/edu/python/dict-files

## Can build up a dict by starting with the new empty dict {}
## and storing key/value pairs into the dict like this:
## dict[key] = value-for-that-key
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print dict ## {'a':, 'alpha', 'o': 'omega' 'g': 'gamma''}

print dict['a'] ## Simple lookup, returns 'alpha'
dict['a'] = 6   ## Put new key/value into dict
'a' in dict     ## True
## print dict['z']              ## Throws KeyError
if 'z' in dict: print dict['z'] ## Avoid KeyError
print dict.get('z')     ## None (instead of KeyError)

## By default, iterating over a dict iterates over its keys.
## Note that the keys are in a random order.
for key in dict: print key
## prints a g o

## Exactly the same as above
for key in dict.keys(): print key

## Get the .keys() list:
print dict.keys()   ## ['a', 'o', 'g']

## Likewise, there's a .values() list of values
print dict.values() ## ['alpha', 'omega', 'gamma']

## Common case -- loop over the keys in sorted order,
## accessing each key/value
for key in sorted(dict.keys()):
    print key, dict[key]

## .items() is the dict expressed as (key, value) tuples
print dict.items() ## [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

## This loop syntax accesses the whole dict by looping
## over the .items() tuple list, accessing one (key, value)
## pair on each iteration.
for k, v in dict.items(): print k, '>', v
## a > alpha o > omega g > gamma

## NOTE:
# There are "iter" variants of these methods called iterkey(), itervalues() and iteritems() which 
# avoid the cost of constructing the whole list -- a performance win if the data is huge.
# However, I generally prefer the plain keys() and values() methods with their sensible 
# names. In Python 3000 revision, the need for the iterkeys() variants is going away.

#####################
## DICT FORMATTING ##
#####################
hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'I want %(count)d copies of %(word)s' % hash # %d for int, %s for string
# 'I want 42 copies of garfield'

#########
## DEL ##
#########
var = 6
del var # var no more!

list = ['a', 'b', 'c', 'd']
del list[0]     ## Delete first elements
del list[-2:]   ## Delete last two elements
print list      ## ['b']

dict = {'a':1, 'b':2, 'c':3}
del dict['b']   ## Delete 'b' entry
print dict      ## {'a':1, 'c':3}

###########
## FILES ##
###########
f = open('name', 'r')   # Opens the file into the variable f, ready for reading operations.
f.close()               # Close the file when finished.
# Use 'r' for reading
# Use 'w' for writing
# Use 'a' for append
# The special mode 'rU' is the "Universal" option for text files where it's smart about
# converting different line-endings so they always come through as a simple '\n'

# The for-loop technique is a simple and efficient way to look at all the lines in a text file:
# Echo the contents of a file
f = open('foo.txt', 'rU')
for line in f:      ## iterates over the lines of the file
    print line,     ## trailing, so print does not add an end-of-line char
                    ## since 'line' already includes the end-of line.
f.close()

# For writing the f.write(string) is the easiest way to wirte data to an open output file

###################
## FILES UNICODE ##
###################
# The "codecs" module provides support for reading a unicode file.
import codecs
f = codecs.open('foo.txt', rU, 'utf-8')
for line in f:
    # here line is a *unicode* string
    

######################################
## EXERCISE INCREMENTAL DEVELOPMENT ##
######################################
# Building a Python program, don't write the whole thing in one step. Instead 
# identify just a first milestone, e.g. "well the first step is to extract the 
# list of words." Write the code to get to that milestone, and just print your 
# data structures at that point, and then you can do a sys.exit(0) so the program
# does not run ahead into its not-done parts. Once the milestone code is working,
# you can work on code for the next milestone. Being able to look at the printout
# of your variables at one state can help you think about how you need to 
# transform those variables to get to the next state. Python is very quick with
# this pattern, allowing you to make a little change and run the program to see 
# how it works. Take advantage of that quick turnaround to build your program in
# little steps.


