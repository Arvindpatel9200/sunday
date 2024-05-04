                                  #recursion is a fuction which calles  itself
                           # it is  directelly use a mathmeticaal formula  as a fuction .
'''
def facto(i):
    if i ==0 or i==1:
        return 1
    else:
        return i*facto(i-1)
print ("fectorial is ",facto(5))        #RECURSIV FUCTION 

'''


                #WRITE A PROGRAM TO FIN THE  MAXIMUM NUMBER IN BETWEEN 3 NUMBERS

def max(num1,num2,num3):
    if num1>num2:
        return num1
    else:
        if num2>num3:
            return num2
        else:
            return num3
M=max(23,34,324)
print ("Themaximum number is  :",str(M))
print ("Themaximum number is  :",M)
 