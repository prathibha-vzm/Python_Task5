from functools import reduce
import re
import datetime


'''QUESTION 1: List of Dictionaries, each representing name and age Keys, 
use Lambda function to filter out people under 18 and map the remaining peoples in a new list'''
print("Question 1")

#List of Dictionaries
list_dict=[{"name":"Ambi",'age':20},
           {"name":"Banu",'age':10},
           {"name":"Dann",'age':12},
           {"name":"Ivan",'age':16},
           {"name":"Janu",'age':27}]

#using Lambda function to filter out people under 18 and map the remaining peoples in a new list
remaining_people=(list(map(lambda name:name["name"],filter(lambda above:above['age']>18,list_dict))))

#output
print("People Above 18 are: ",remaining_people)

'''QUESTION 2: Given a list of numbers, use the reduce function and a lambda expression 
to calculate the product of all the numbers in the list'''
print("\nQuestion 2")

#list of numbers
list_numbers=[10,34,9,55]

#using the reduce function and a lambda expression to calculate the product of all the numbers in the list
product_numbers=reduce(lambda a,b:a*b,list_numbers)

#Output
print(list_numbers)
print("Thr product of a list of numbers: ",product_numbers)

'''QUESTION 3: Write a list comprehension that creates a new list of squares of even numbers from a given list,
Using lambda function to check for even numbers'''
print("\nQuestion 3")

#A number list
alist=[12,34,57,7]

print(alist)
print("Square of even numbers")

#List = [expression(i) for i in another_list if filter(i)]
# Using list comprehension and Lambda to check and square even numbers
even_list=[eve**2 for eve in alist if(lambda eve:eve%2==0)(eve)]

#output
print(even_list)


'''QUESTION 4 :Write a lambda function to check if a given string is a number'''
print("\nQuestion 4")

#getting input
var="@ustron1ut"

print(var)

#Using filter with lambda and regex to find the numbers in a string
filter_var=filter(lambda char:re.findall("[0-9]",char),var)

#converting the function to list
flist=list(filter_var)

#to check if there is a number in the list
if flist:
    print("Yes there is number in the string",flist)
else:
    print("No numbers")

'''Question 5: Use lambda function to extract date month and year from datetime object'''
print("\nQuestion 5")

D=datetime.datetime.now()
#storing the date
date=D.date()
#Using lambda and strftime method to extract date, month and year
date_lambda=lambda dmy:date.strftime("%d-%m-%y")

#passing date as an input
print("current date",date_lambda(date))

#Question 5:
print("\nQuestion 5")
#Use lambda function to extract date month and year from datetime object
D=datetime.datetime.now()

#Here used lambda to exract day, month and year in separate
da_lambda=lambda da:da.day #returns date
month_lambda=lambda dm:dm.month #returns month
year_lambda=lambda dy:dy.year #returns year

#passing current date and printing
print("Current date:",da_lambda(D))
print("Current month:",month_lambda(D))
print("Current Year",year_lambda(D))

'''Question 6:Create a lambda function to generate fibonacci series upto n terms'''

print("\nQuestion 6")
print("Enter your input")
#getting input as integer
fib_input=int(input())
#defining values to the var
t1=0
t2=1
print("The fibonacci series")
#using lambda and tuple to return values
fib_lambda= lambda a,b:(b,a+b)
#for loop to run upto n
for n in range(fib_input):
        t1,t2=fib_lambda(t1,t2) #return the value
        print(t1,end=" ")