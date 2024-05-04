# a=int(input("enter the first number-->"))
# b=int(input("enter the second  number -->"))
# c=a+b
# print("the sum value is :-->",c)


# a=int(input("enter a number-->"))
# if a%2==0:
#     print("this number is even ",a)
# else:
#     print("this number is odd ",a)


# a=int(input("enter a  first number-->"))
# b=int(input("enter a second number-->"))
# if a>b:
#     print("this number is great ",a)
# else:
#     print("this number is great  ",b)



#    # Write a Python program to check prime numbers.

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(2)) # True



# num = int(input("enter a number :"))
# if num > 1:
#     for i in range(2, (num//2)+1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")



# import math
# def factorial(num):
#     return math.factorial(num)

# num=int(input("enter a number :"))
# print("the fectorial is given number ",num,"is",factorial(num))



# n = float(input('Enter a number: '))

# n_sqrt = n ** 0.5
# print('The square root of {0} is {1}'.format(n ,n_sqrt))


def leafyear(year):
    if(year % 400==0 or year %100!=0 and year % 4==0):
        print ("this is the leap year ",year)
    else:
        print ("this year is not leap year ",year)
year=int(input("enter a year "))  
leafyear(year)