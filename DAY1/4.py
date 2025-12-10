# ## >>>> LOOPS



# loops are used to repeat functions
# there are two types of loops
# 1>>WHILE loop - jab tak condition true hai tab tak vo kaam repeat hota rahega
#     a>> BREAK - loop ke andar jha pr pr hum break likh denge vhi pr hamara loop ruk jayega
#     b>> CONTINUE  - jha pr hamein kuch skip krwan ho us condition pr continue likh do
#         in english - countinues execution of loop with the next iteration
# 2>>FOR loop - sequence mai chalne ke liye for loop use krte
#        in english - loops are used for sequential traversal. for transversing list, tuple,strings etc. 

# print hello 5 times
# count = 1    #initialize krwa rhe hai - isko apn iterators kehte h 
# while (count <= 5) : #iska matlab hai jab tak hai tab tak run krta hi rhega -- isko apn iteration kehte h
#     print("hello")
#     count += 1   #isko lgane se hello 5 baar hi print hoga kyunki while ki condition mai 5 put kiya hai
# print(count) #isko likhne se kitni bar print hua ye show krega output mai
# # upar jo count likha hai usko iterators kehte hai aur loop mai run krne ko iteration kehte hai
# # count hi lena zarrori nhi hai kuch bhi le skte hai ,for ex:i ,j,etc 


# i = 1
# while i<=100:
#     print("hey")
#     i += 1
#     print("i")  #ye count krega agr apan ko count krna h to

# print number from 1 to 5
# i = 1 
# while i <= 5:
#     print(i)
#     i += 1

# i = 1
# while i <= 5:
#     print("i")
#     i += 1
# iske output mai 'i' 5 baar print ho jayega kyunki apn ne string store krayi hai
 
# print numbers from 5 to 1
# i = 5
# while i >= 1 :
#     print(i)
#     i -= 1
# print("loop ended")

# ## practice questions for while loop

# #1>>>print numbers from 1 to 100
# i = 1
# while i<=100 :
#     print(i)
#     i +=1

# #2>>> print numbers from 100 to 1
# i = 100
# while i>1:
#     print(i)
#     i -= 1

# #3>>> print multipication table of 6
# n= int(input("enter number"))
# i = n
# while i <= 10:
#     print(i)
#     i += n

# 4>>> print the following elements using loops
# #   [1,4,9,16,25,36,49,64,81,100] 
# i = 1 
# while i <= 10:
#     print(i**2)
#     i += 1

# 2nd method
# lst=[]
# i=1
# while i<=10:
#     lst.append(i**2)
#     i+=1
# i=0
# while i<len(lst):
#     print(lst[i])
#     i+=1


# 5>>> search for a number x in this tuple using loop
#         (1,4,9,16,25,36,49,64,81,100)


# 6>>> WAP to find the sum of first n natural numbers. (using while)
# n = int(input("Enter the range: " ))
# sum = 0
# i = 1
# while i<= n :
#     sum += i
#     i += 1
# print("total sum : ",sum)

# >>>>>BREAK<<<<<
# i = 1
# while i<=5:
#     print(i)
#     if( i== 3):
#         break
#     i +=1

# <<<<CONTINUE>>>>
# i = 0
# while i <= 5:
#     if (i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1

# print only odd numbers between 1 - 10
# i = 1
# while i <= 10:
#     if ( i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

# print only even numbers between 1 - 10
# i = 1
# while i <=10:
#     if(i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

# ## >>>>>>>>>>>FOR LOOOOOOPPP>>>>>>>>>>>
# nums = [1,2,3,4,5]
# for val in nums:
#     print(val)

# names = ["abhiral" ,"abhinav" ,"ayush" ,"rishi" ,"parth"]   
# for val in names:
#     print(val )

# tup =(23,4,54,53,69,6)
# for val in tup:
#     print(val)

# str = "pythin programming"
# for char in str:
#     print(char)

# ##practice questions for FOR LOOP
# # Q1> print the element of the following list using a loop
#         [1,4,9,16,25,36,49,64,81,100]
# nums = [1,4,9,16,25,49,64,81,100]
# for val in nums:
#     print(val)

# # Q2> search for the number x in this tupple
#       (1,4,9,16,25,36,49,64,81,100)

# nums =(1,4,9,16,25,36,49,64,81,100)
# x= 49

# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx",idx)
#         break
#     idx += 1


# Range()
# range functions returns a sequence of numbers ,starting from 0 by default,and increments by 1(by default),
# and increments by 1(by default) ,and stops before a specified number.

# for i in range(29):
#     print(i)

# range mai 3 type ki value hoti hai - (start?,stop,step?)
# isme question mark ka matlab hai vo value compulsory nhi h dena 


# ex dekhte hai
# for i in range(10):  #range(stop)
#     print (i)

# for i in range(2,10):  #range (start,stop)
#     print(i)


# for i in range(2,10,2):  #range(start,stop,step)
#     print(i)              #step ka matlab hai kitne se increase krega 

# ## PRACTICE (using for and range())
# Q!>>>> print number from 1 to 100
# for i in range(1,101):
#     print(i)


# Q2>>>> print number 100 to 1
# for i in range(100,0,-1):
# print(i) 

# Q3>>>> print a multipication table of number n 

# n = int(input("enter number"))
# for i in range (11):
#     print(n*i)

# PASS statement
# PASS is a null statement that does nothing
# also it is a placeholder for future code
# for ex :

# for i in range(5):
#     pass

# if i>5:
#     pass
#     print("dont do work")


# PRACTICE QUESTION 
# Q1>>>>---- WAP to find the sum of n numbers(using while)

# n = int(input("Enter Number"))
# sum = 0
# while i<=n:
#     print(sum)
#     sum += 1


# Q2>>>>---- WAP to fing find factorial
# n = 3
# fact = 1
# i = 1
# while i<= n:
#     fact*=i
#     i +=1
# print("factorial = ",fact)









range(5)

arr = [22,44,33,22]
print(arr)
arr.reverse()
print(arr)

# n = 5
# for i in range(n):
#     print(' ' * (n-i-1) + '*' * (2*i +1))

# for i in range (n - 2, -1, -1):
#     print (' ' * (n-i-1) +'*' *(2*i +1))

rows =5
for i in range(1, rows + 1):
    print("*"*i )