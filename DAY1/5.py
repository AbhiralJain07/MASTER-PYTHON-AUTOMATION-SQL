###   >>>    function and recursion

#functions - group of statements that performs specific task

## functions redundancy ko reduce krta h aur reusablity ko increase krta hai

#1st method
def calc_sum(a,b):   ##ye function define kr rhe hai apan isme jop a,b likha h unko parameters kehte hai
    sum = a+b
    print(sum)
    return sum
calc_sum(5,10)      #ye function recall kkr rhe h apn aur 5 or 10 hai vo argments hai
calc_sum(12,18)
calc_sum(32,18)

#2nd method
def calc_sum(a,b):   #def calc_sum(a,b):
    return a + b          #return a+b      isko kehte h function define krna
                                            #isme bracket mai jo (a,b) likha hai usko parameters kehte hai
sum = calc_sum(1,2)  #calc_sum(1,2) >>> isko kehte hai function recall
print(sum)            #(1,2) >>> isko kehte hai arguments 

def print_hello():
    print("hello")

print_hello()


#Q1>>> average of 3 numbers
#1st method
def calc_average(a,b,c):
    average = (a+b+c)/3
    print(average)
    return average
calc_average(1,2,3)

# #2nd method
def calc_average(a,b,c):
    return (a+b+c)/3

average = calc_average(1,2,3)
print(average) 

#two types of function in python
# 1> built-in function - jo already defined hote hai ,ex: print() , len() , type() , range()
# 2>user defined function  - jo hum python mai likhte hai

#multipication of two numbers

#method1
def calc_pdt(a,b):
    pdt = a*b
    print(pdt)
    return pdt
calc_pdt(2,3)
                                                             
#method 2
def calc_pdt(a=2 ,b =3):
    print(a*b)
    return(a*b)
calc_pdt()







# ------------->>>>>>>>>>>>>>>>practicce ques<<<<<<<<<<<<<<_-----------------------



#q1>> WAF to print the length of the list.
names = ["abhiral","rishi" ,"ayush" ,"parth"]
def print_len(names):
    print(len(names))
    return(names)

print_len(names)


#q2>> WAF to print the elements of a list in a single line
names = ["abhiral","rishi" ,"ayush" ,"parth"]
def print_list(names):
    print(names)
    return(names)
print_list(names)


#Q3>>>> WAF to find factorial of n .(n is the parameter)

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= 1
        print(fact)

calc_fact(5)



#Q4>>>> WAF to convert USD to INR


def convertor(usd_value):
    inr_val = usd_value *83
    print(usd_value, "USD = " , inr_val , "INR")


convertor(2)

