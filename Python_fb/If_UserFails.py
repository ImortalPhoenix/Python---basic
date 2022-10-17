#if user fails this code will run
# this will skip the above code and move dirctly downwards to the not a number
rawstr = input('Enter a number:')
try :
    ival = int(rawstr) 
except:
    ival = -1  

if ival > 0:
    print('Nice Work') 
else:
    print('Not a number') 
