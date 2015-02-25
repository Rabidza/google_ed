# This will not run varaibles are undefined!
# Example of if statements

if speed >= 80:
    print 'License and registration please'
    if mood == 'terrible' or speed >= 100:
        print 'You have the right to remain silent.'
    elif mood == 'bad' or speed >= 90:
        print "I'm going to have to write you a ticket."
        write_ticket()
    else:
        print "Let's try to keep it under 80 ok?"

# The if statement can be a one-liner if it is short:
if speed >= 80: print 'You are so busted'
else: print 'Have a nice day'