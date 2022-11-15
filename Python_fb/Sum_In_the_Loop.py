"""to add up a value we encounter in a loop we introduce a sum variable that starts at '0' and 
we add the value to the 'sum' each time through the loop"""

zoro = 0
print('Before', zoro)
for things in [9 ,41, 12, 3, 74, 15]:
    zoro = zoro + things
    print (zoro, things)
print('After ', zoro)
