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