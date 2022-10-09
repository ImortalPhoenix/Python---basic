astr = 'Hello Bob'
try:
    iscr = int(astr)    #here the code is wronge as aster is a string not a int it will give a trace back error 
except:                 #so to componset we did the except function
    istr = -1

print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)

