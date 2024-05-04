                               # prob  ..no .. 01
'''
def great(num1,num2,num3):
    if num1>num2:
       return(num1)
    else:
        if num2>num3:
            return (num2)
        else:
            return  (num3)
  
maxim=great(23,423,90)
print (maxim)'''

      


'''
def maximum (num1, num2, num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else:    
        if (num2>num3):
            return num2
        else:
            
            return num3
m=maximum(69,89,79)
print("the  maximum number is :-->" + str (m))            
'''

                                             #prob.. no.. 02
'''
def temprature (temp):
    t=temp*(9/5)+32
    print (t)

temprature(37) '''


                         #prob... no ... 03

                           #s=n*(n-1)
def sum(i):
    if i==0 or i==1:
        return 1
    else:
        s=i*sum(i-1)
        print (s)
sum(23)







