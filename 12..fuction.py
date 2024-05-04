                                   #function 
               # fuction is  a grouph of statement performing a specific task .
    # a function can be reused by thr programmer in a given programm any number of times..
'''
def persent(marks):
    p=(marks[0]+marks[1]+marks[2]+marks[3]+marks[4]+marks[5])/600*100         #reused the code in multiple time 
    return p

Avi_marks=[29,44,55,43,29,99]
peresent1=persent(Avi_marks)

pihu_marks=[32,36,53,67,54,47]
peresent2=persent(pihu_marks)

shivu_marks=[54,24,35,46,76,56]
peresent3=persent(shivu_marks)


print(peresent1 ,peresent2,peresent3)'''


                    #fuction with argument
'''
def first(name):
    print("Hii",name)
  
def sum(num1,num2,num3,num4,num5,num6):           # we are give multiple argument 
    s=(num1+num2+num3+num4+num5+num6)  
    print(s)

first("avi")
sum(23,3,45,5,65,67)'''


                                #fuction with defult parameter  value 

def name_info(first_name="Jay",middle_name="Shri",last_name="Ram"):
    print(first_name,middle_name,last_name)  

name_info("ARVIND",'KUMAR','PATEL')
name_info()                         #Default parameters are used when we do not give input.