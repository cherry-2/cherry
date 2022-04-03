# Python program to add two numbers

# a = 2
# b= 3.5
# print(type(b))
# print (a+b)
# print (b-a)
# print(b/a)
# print (b*a)
# print (b**a)
# print (b//a)

# Maximum of two numbers in Python


'''def mymax (lista):
    max = lista[0]
    for x in lista:
        if x>max:
            max =x
    return max
lista= [1,2,3,4,5,8,7,6]

print ("max number is:", mymax(lista))'''


# Python Program for factorial of a number
# fibanacci sequence


'''def factorial(n):
    if n==1:
        return 1
    elif n==0:
        return 1
    else:
        return (n * factorial(n - 1))


num = 5
print("factorial of num is:", factorial(num))


def factorial2(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1) # lambda function

num1=5
print("factorial of num is:", factorial2(5))'''

#Python Program for simple interest

'''def simple_interest(p,t,r):
    print ("principle amount is:", p)
    print ("time period is:", t)
    print("rate of interest is: ", r)

    si = (p*t*r)/100
    print ("Simple Interest is:",si)
    return si


simple_interest(10000,5,5)'''
# Python Program for compound interest


'''def compound_interest(p,r,t):
    A = p*((1+r/100)**t)
    CI = A-p
    print("compound Interest is:", CI)
    return CI
compound_interest(10000,10.25,5)'''

# Python Program to check Armstrong Number

'''def power(x,y):
    if y==0:
        return 1
    if y%2==0:
        return power(x,y//2)* power(x,y//2)
    return x*power(x,y//2)*power(x,y//2)

def order(x):
    n=0
    while x != 0:
        n=+1
        x=x//10
    return n

def armstrong_number(x):
    n= order(x)
    temp=x
    sum1=0
    while temp != 0:
        r=temp%10
        sum1 = sum1 + power(r, n)
        temp = temp // 10

        # If condition satisfies
    return (sum1 == x)
x=153
print(armstrong_number(x))'''
# python Program for Program to find area of a circle


'''def area_of_circle(r):
    print(3.14*r*r)

area_of_circle(5)'''
# Python program to print all Prime numbers in an Interval

'''def prime_numbers(x,y):
    prime_list =[]
    for i in range (x,y):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j==0:
                    break
            else:
                prime_list.append (i)
    return prime_list


lst = prime_numbers(1,24)
if len(lst)==0:
    print ("no prime numbers")
else:
    print("prime numbers list is ",lst)'''

# Python program to check whether a number is Prime or not

def prime_or_not(x):
    if x>1:
        for i in range(2,int(x/2)+1):
            if x%i==0:
                print("given number is not prime")
                break

            else:
                print("given number is  prime")
    else:
        print("number is not prime")
prime_or_not(122)

