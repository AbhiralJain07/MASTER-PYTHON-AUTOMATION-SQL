## >>>> strings and conditional statements

str1 = "this is string . \n we are creating in python"
print(str1)

name1 = "abhiral"
name2 = "jain"
finalname = name1 + name2
print(finalname)
print(len(finalname))
# length jab calculate krte h tab space bhi calculate hota hai

str = "abhiral jain"
ch = str[3]
print(ch)
# OR
str = "abhiral jain"
print(str[6])
# isme str ko 0 se calculate krte hai jaise a pe 0 ,b pe 1 aise aage


# SLICING - mtlab beech se utna hi nikalna jitna apn chahte hai
str = "abhiral jain"
print(str[5:12])
print(str[0:12])

# -ve index slicing
str = "apple"
print(str[-4:-2])
print(str[-5:-1])


# STRING FUNCTION
str = "i am a coder"
print(str.endswith("re"))
print(str.capitalize())
#print(str.replace("i am a coder","my name is abhiral jain"))
print(str.find("a")) #jab bhi koi letter ya word find krna hota hai tab ye kaam krte hau
print(str.count("a"))

light = "blue"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
else:
    print("look")

print("end of code") #ye likhna hmari marzi hai


num = 5
if("num >= 2"):
    print("greater than 2")
elif("num > 3 "):
    print("greater than 2")

age = 24 
if(age >= 18):
    print("can vote")
else:
    print("can't vote")


marks = int(input("Enter marks : "))
if(marks >= 90):
    grade = "A"
elif(marks>=80 and marks<90):
    grade = "B"
elif(marks>=70 and marks<80):
    grade = "C"
elif(marks>=60 and marks<70):
    grade = "D"
elif(marks>=40 and marks<60):
    grade = "E"
else:
    grade = "fail"
print("grade of student ->" , grade)

#     NESTING = ek statement ke andr dusri statement likhna

age = int(input("enter age : "))

if(age>= 18):
    if(age>=80):
        print("can drive")
    else:
        print("can drive")
else:
    print("cannot drive")


age = 95

if(age>= 18):
    if(age>=80):
        print("can drive")
    else:
        print("can drive")
else:
    print("cannot drive")

num = int(input("enter number : "))
rem = num % 2
if(rem == 0):
    print("even number")
else:
    print("odd number")

# comparison between three numbers

a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))

if(a>=b and a>=c):
    print("first number is greatest :",a)
elif(b>=c):
    print("second number is greatest:",b)
else:
    print("third number is grreatest:",c)

# to find number is remainder of 7 or not

x = int(input("enter your number:"))
if(x%7 == 0 ):
    print("multipier of 7")
else:
    print("not a multipier of 7")