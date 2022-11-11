"""to count how many time we execute a loop we introduce a counter 
varialbe that starts at 0 and one to it each tie through the loop """

zoro = 0
print('Before', zoro)
for things in [9 ,41, 12, 3, 74, 15]:
    zoro = zoro + 1
    print (zoro, things)
print('After ', zoro)
