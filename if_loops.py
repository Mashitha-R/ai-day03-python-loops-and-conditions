""" LOOPS IN PYTHON """


# 'for' loops

#range function 
# range(start,stop,step)
a=range(1,20,1)
for i in a:
    print(i)

#second method
for i in range(1,20,1): #or range(20) where start=0 and step=1 is default
    print(i)

#reverse order
for i in range(16,0,-1):
    print(i)

for i in range(-3,-16,-1):  #to go backward -1 is used
    print(i)



#lets print a table of 5
for i in range(5,51,5):
    print(i)

n=int(input("WHICH TABLE YOU WANT? "))
for i in range(n,(n*10)+1,n):
    print(i)

#loops for strings
a="MASHITHA"
for i in range(8):
    print(a[i])

b="MASHITHA IS LEARNING PYTHON"
for i in range(len(b)):
    print(b[i])
 #or both can be used
b="MASHITHA IS LEARNING PYTHON"
for i in b:
    print(i)



""" 'break' 'continuous' 'else' statement """
for i in range(1,21):
    if i==15:
        break
    else:
        print(i)
#or 
for i in range(1,21):
    if i==15:
        print("break statement is executed")
        break
    print(i)
else:
    print("break statement is not executed")


for i in range(1,21):
    if i==15:
        continue
        print(i)


#revision
""" Accept an integer and Print hello world n times"""
n=int(input("provide a number:"))
for i in range(n):
    print("hello world")




"""Print natural number upto n"""
n=int(input("provide a number:"))

for i in range(1,n+1,1):
    print(i)


"""Reverse for loop.Print n to 1"""
n=int(input("provide a number:"))
for i in range(n,0,-1):
    print(i)


""" Take a number as input and print its table"""
n=int(input("provide a number:"))
for i in range(n,n*11,n):
    print(i)

#or
n=int(input("provide a table number:"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")


""" SUM UPTO TO n terms"""
n=int(input("provide a number:"))
sum=0
for i in range(1,n+1):
    sum=sum + i
print(f"Your sum is {sum}")


"""factorials of a number """
n=int(input("provide a number:"))
f=1
for i in range(1,n+1):
    f=f*i
print(f"{n}!={f}")





"""print the sum of all even and odd numbers in a range separately"""
n=int(input("provide a number:"))
even=0
odd=0

for i in range(1,n+1):
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print(f"the sum of even and odd number are {even},{odd}")




""" PRINT ALL THE FACTORS OF A NUMBERS"""
n=int(input("provide a number:"))

for i in range(1,n+1):
    if n%i==0:
        print(i)


""" ACCEPT A NUMBER AND CHECK IF IT IS A PERFECT NUMBER OR NOT,
A NUMBER WHOSE SUM OF FACTORS IS EQUAL TO THE NUMBER ITSELF"""
n=int(input("Check a number:"))
sum=0
for i in range(1,n):  #n is becz we nodont want n to sum up to other factors
        if n%i==0:
            sum=sum+i
if sum==n:
    print(f"{sum} is a perfect number")
else:
    print(f"{sum} is not a perfect number")



""" CHECK IF IS A PRIME NUMBER OR NOT"""

n=int(input("Check a NUMBER IS PRIME number OR NOT:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+i
if count==2:
    print("its a prime number")
else:
    print("its not a prime number")




""" reverse a string without using in build functions"""


a="mashitha"
             #print(a[::-1])
              #or
b=""          #empty strng used becz to get straight reverse order
              #print(a(i)) gives vertical reverse
for i in range(len(a)-1,-1,-1):
        b=b+a[i]
print(b)



""" same reverse check pallindrome or not """

a="masam"
             #print(a[::-1])
              #or
b=""          #empty strng used becz to get straight reverse order
              #print(a(i)) gives vertical reverse
for i in range(len(a)-1,-1,-1):
        b=b+a[i]
if b==a:
    print("your string is pallindrome")
else:
    print("its not pallindrome")



""" count all letters ,digits, and special symbols from a given string """

m="P@#yn26at^&i5ve"
char=0
dig=0
spl=0
for i in m:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        char+=1
    else:
        spl+=1
print(f"your digits{dig}\nyour alphabrt{char}\nyour spcl{spl}")
    





    

  














