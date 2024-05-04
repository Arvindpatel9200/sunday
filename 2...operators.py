#operators


#Arithmetic operators-->  +,-,*,/
avi='arvind'
mahi='patel'
a=123344
b=32.432
c=0.8333
d=232232
print(avi+mahi)  #string+string=str  
print(a+d)       #integer+integer=int
print(b+c)       #float+=float=float
print(a+b)       #int+float=float

#print(avi-mahi)  #string-string=NOt work  
print(a-d)       #integer-integer=int
print(b-c)       #float-float=float
print(a-b)       #int-float=float

#print(avi*mahi)  #string*string=Not work
print(a*d)       #integer*integer=int
print(b*c)       #float*float=float
print(a*b)       #int*float=float

#print(avi/mahi)  #string/string=Not work
print(a/d)       #integer/integer=int
print(b/c)       #float/float=float
print(a/b)       #int/float=float

#assignment operators--> =,+=,-=,
z=21
z+=10  #add
z-=10  #substract
z*=10  #into
z/=10   #divition 
print(z)

# comprision oprators-->==,>=,<,!=.     --> return boooleans<--
p=(232>2222)
print(p)
q=(2323==2323)
print(q)
r=(233!=0)
print(r)

#logical  OPERATORS-->AND OR NOT
bool1=True
bool2=False

print("the value of bool1 and bool2 is",(bool1 and bool2))
print("the value of bool1 and bool2 is",(bool1 or bool2))
print("the value of bool1 and bool2 is",(not bool2))
print("the value of bool1 and bool2 is",(not bool1 ))
