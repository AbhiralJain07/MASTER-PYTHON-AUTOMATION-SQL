## VARIABLES AND DATA TYPES :


print("hello world " )
name = "Abhiral"
age = 19
price = 45.55

print(type(name))
print(type(age))
print(type(price))
# #boolean value mai sirf True ya False hota hai 

age = 19
old = False
a = None
print(type(old))
print(type(a))

# # arithmetic operator
a = 2
b = 4
sum = a + b
print(sum)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder 
print(a**b) #a^b

# # relational operator
a = 40
b = 49

print( a == b)
print(a != b )
print( a >= b)
print(a > b)
print(a<=b)
print( a< b)
  
# assignment operator
num = 10
num += 10
print("num : " , num )

num = 10
num -= 10
print("num : " , num )

num = 10
num *= 10
print("num : ", num )

num = 10
num **= 5
print("num : " ,num)

# logical operators [not, and ,or]
#

#Expression Execution
A,B = 2,3
Txt = "@"
print(2*Txt*3)

A,B = ("JAI SHREE RAM\n" ,10000) 
Txt="@"
# print((A+Txt)*B)

A,B = 2,3
C = 4
print(A+B*C)

A,B = 10,5.0
C = A*B
print(C)

A,B = 1,2
C= A/B
print(C)

A,B = 12 ,-5
C = A//B, A/B
print(C)

A,B=-5,2
C=A%B
print(C)

A,B=5,2
C=A%B
print(C)

A,B=5,-2
C=A%B
print(C)

# #jab bhi denominator mai -ve sign hoga tabhi answer mai -ve aayega nhi to kisi bhi case mai answer -ve nhi aayega


# #INPUT IN PYTHON
name = input("name : ")
age = int(input("age = "))
print(type(age))
print(age+12)

print("name")
print("age")


print("My name is " , name , "and i am",age ,"years old")
print("my name is ", name , "and i am ", age , "years old")
 
a = 2
b = 3
print(a**b)

# #operator precedence
# #not>and>or


# #conditional statement - if-else-elif
vote = input("vote : ")
if(age>=18):
    print("vote")
elif(age<18):
    print("underage")

light = input("light : ")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light broken")

marks  = input("marks : ")
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >=70 and marks < 80):
    print("C")
else:
     print("FAIL")

#single line conditional statements
food = input("food = ")
eat = "yes" if food == "cake" else "no"
print (eat) 

food = input("food  = ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")
 
age = int(input("age =  "))
vote = ("yes" , "no") [age < 18]
#isme answer sahi nhi aa rha hai^^


sal = float(input("salary : "))
tax = sal * (0.1 , 0.2) [sal > 500000]
print(tax)

# Type Conversion
a , b = 1 , "2"
c = int(b)
print(a+c)

a = float("2") 
b = 4.25
sum = a+b
print(sum)

a = int("2")
b = 4.35
print(a +b)

name = input ("enter your name ")
age = input("enter your age")
print("welcome" , name , age  )

val = input("enter your value")
print(type(val) , val)

int("5")
val = float(input("enter same value : "))
print(type(val) , val)

name = input("enter name : ")
age = int(input("enter age : "))
marks = input("marks = ")
print("welcome" , name)
print("age = ",age)
print("marks = " , marks)

a = float(input("enter first  : "))
b = float(input("enter second  : "))

print("Avg = " , (a+b)/2)

print("end of code")


