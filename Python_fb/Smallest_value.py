#smallest_so_far = 0 #this will not work  replace 0 = None
smallest = None
print('before', smallest)
for the_num in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = the_num
    elif the_num < smallest:
        smallest = the_num
    print(smallest, the_num)

print('After', smallest)