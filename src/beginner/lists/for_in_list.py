mylist = [10, 20, 3, 4, 50, 60, 49, 12]

print('List members :')
for x in mylist:
    print(x)

print()
print('Index counter:')
for i in range(len(mylist)):
    print(i)

print()
print('Sort list and then print using index')

mylist.sort()
for i in range(len(mylist)):
    print(f'{i}- {mylist[i]}')

print('\nReverse sort the list')
mylist.sort(reverse=True)
print(mylist)
