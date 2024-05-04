                  #prob..01

'''num1=int(input("enter first number 1 :"))      
num2=int(input("enter first number 2:"))
num3=int(input("enter first number 3:"))
num4=int(input("enter first number 4:"))
print(num1,num2,num3,num4)
if(num1>num4):
    f1=num1
else:
    f1=num4
if(num2>num3):
    f2=num2
else:
    f2=num3
if(f1>f2):
    print(str(f1)+"is greatest")
else:
    print(str(f2)+" is greatest") '''

                            #prob..no  02
'''  
num1=int(input("enter first marks 1 :"))      
num2=int(input("enter first marks 2:"))
num3=int(input("enter first marks 3:"))
finalno=(num1+num2+num3)/3
if (finalno>40 and num1>33 and num2>33 and num3>33):
    print("congrgratulations you are passed ")
else:
    print("oh sorry  you are failed ")  
print("\nbecouse your total peresent is:-->",finalno,
      "\nand first  subject marks is:-->",num1,
      "\nand second subject marks is:-->",num2,
      "\nthird  subject marks is:-->",num3)
'''
                         #prob..no.. 03
'''text=input("Enter the text\n")

if("make a lot of money " in text ):
    spam =True
elif("buy now" in  text):
    spam =True
elif("click this" in  text):
    spam =True
elif("suscribe this " in  text):   
    spam =True
else:
    spam =False    

if(spam):
    print("this text is spam")
else:
   print("this text is not spam")    

'''
                    #prob..no..04
'''username=input("enter the username::-->")
lenth=(len(username))
print(lenth)
if (lenth>10):
    print("username is greater then 10,and the user name is :-->",username)
else:
    print("username is Less then 10,and the user name is :-->",username)    

'''
                   #prob..no ...05
'''
lis =[3,"avi","aroma",'true',"maya","mahi","livetogather"]
name=input("Enter the name you want to check\n::-->")

if name in lis:
    peresent=True
else:
    peresent=False
if(peresent):
    print("name is  preasent in the list\n::--> ",name)   
else:
    print("name is not preasent in the list\n::--> ",name)           '''
             
             #prob... no..06

marks= int(input("enter your marks\n"))
if(marks>=90):
    grade="exll"
elif  marks>=80:
    grade="A+"
elif marks>=60:
    grade="A"
elif marks>=50:
    grade="B"
elif marks >=33:
    grade="c"
else:
    grade="fail"
print("your grade is :"+grade)                        

                                 #prob...no 07
