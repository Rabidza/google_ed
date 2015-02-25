colors = ['red', 'blue', 'green']
print colors[0]      ## red
print colors[2]      ## green
print len(colors)   ## 3

### IMPORTANT ###
b = colors ## Does not copy the list, this makes a and b point to the same list in memory!

#########
## for ##
#########
# for var in list 
# looks at each element in a list

### IMPORTANT ###
# Do not add or remove from the list during iteration

squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print sum   ## 30

########
## in ##
########
# value in collection
# tests if the value is in the collection and returns True/False

list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print 'yay'
# NH - using the word 'list' as a variable name is bad style!

###########
## range ##
###########
## print the numbers from 0 through 99
for i in range(100):
    print i
# Note there is a variant called xrange() which avoids the cost of building the whole list for performance sensitive cases

################
## while loop ##
################
# break and continue statements work as in C++ and Java
## Access every 3rd element in a list
a = 'while loop'
i = 0
while i < len(a):
    print a[i]
    i += 3

## Common list methods
# list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
# list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
# list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
# list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
# list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
# list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
# list.reverse() -- reverses the list in place (does not return it)
# list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).

list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print list  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print list.index('curly')    ## 2
list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print list  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
