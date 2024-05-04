a=[1,2,3,455,32,22,11]
b=[3,"avi",32,'true',344,"mahi","livetogather"]        #we can store value of different data type 
print(a[0:])                           #list indexing strat from [0] index to [-1]
print(b[0:])
a[-1]=355
b[2]="patel_sahab"                               #we can change value of list 
print(a)
print(b)
print(b[0:-1:2])                                    #list slicing
print(b[0: :2])

                                   #list method

a=[1,2,3,455,32,22,11]
b=[3,"avi",32,'true',344,"mahi","livetogather"]
print(a)                                                     #before sort: a=[1,2,3,455,32,22,11]
a.sort()                                                     #sort the list
#b.sort()                                                    #TypeError: not supported between instances of 'str' and 'int'
print(a)                                                     #after sort: a=[1,2,3,11,22,32,455]

a.reverse()                                                  #reverse the list 
print(a)                                                     #after the list 


a.append(23)                                                 #add a no end of the list
print(a)
a.sort()
print(a)

a.insert(6,24)                                               #add 24 at index 6
print(a)

a.pop(-1)                                                    #delete a element(455) at index -1
print(a)                                           
a.remove(32)
print(a)
