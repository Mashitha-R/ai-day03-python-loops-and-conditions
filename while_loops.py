""" WHILE LOOPS"""

a=1
while a<=30:
    a=a+1
    print(a)


#separate each digit of a number and print it on the new line
a=256
while a>0:
    print(a%10)
    a=a//10





b=int(input("tell your number :"))
while b>0:
    print(b%10)
    b=b//10


#ACCEPT A NUMBER AND ORINT IN REVERSE
a=int(input("enter your number"))
rev=0
while a>0:
    rev=rev*10+a%10
    a=a//10
print(rev)



#accept a number and check if its pallindromic number
a=int(input("enter your number"))
copy=a   #we use a copy to store a value
rev=0
while a>0:
    rev=rev*10+a%10
    a=a//10         #becz here a value ==0,so we use copy
if copy==rev:
    print("its a pallindrome")
else:
    print("its not a pallindrome")


