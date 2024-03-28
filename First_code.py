# Class_Ex1:
# Write python program that converts seconds to
# (x Hour, x min, x seconds)
# ----------------------------------------------------------------

#S=int(input('Please enter seconds:'))
#if S>=3600:
 #   H=S//3600
  #  M=((S%3600)//60)
   # Sec=((S%3600)%60)
    #print('Hours:',H,'Minutes:',M,'Seconds:',Sec)
#else:
 #   print('Hours:', '0', 'Minutes:', S//60, 'Seconds:', S%60)
#exit()
#-----------------------------------------------------------------
#write a program to print all the even numbers from 1 to 100
#for i in range(1,100):
 #if i%2==0:
  # print(i,end=",")
#-----------------------------------------------------------
#write a program to find the factrial of the given number
#j=int(input("please enter your number :"))
#factorial=1
#if j<0:
 #   print("it cannot be calculated")
#elif j==0:
 #   print("the factorial of zero is one")
#else:
 #   while j>0:
  #   factorial=factorial*j
   #  j=j-1

#print("the factrial of your number is ",factorial)
#---------------------------------------------------------
#Write a program that calculates the sum of the digits of a given number
#T=int(input("Enter the number"))
#n1=T%10
#n10=(T//10)%10
#n100=(T//100)

#print(" sum of your digits is: ", n1+n10+n100)
#-----------------------------------------------------------
#Write a program that calculates the sum of the first N natural numbers, where N is a positive integer provided by the user.
#k=int(input("please enter your number: "))

#base=0

#if k<0:
 #   print("sorry, I cannot process negative number")
#elif k==0:
 #   print("sorry, I cannot process zero")
#else:
  #  while k>0:
   #     base=base+k
    #    k=k-1
#print("the sum of your first N natural numbers is :", base)
#-------------------------------------------------------------
 #Write a Python program that requests five integer values from the user. It then prints the maximum
#and minimum values entered. If the user enters the values 3, 2, 5, 0, and 1, the program would
#indicate that 5 is the maximum and 0 is the minimum. Your program should handle ties properly;
#for example, if the user enters 2, 4 2, 3 and 3, the program should report 2 as the minimum and 4 as
#maximum
#----------------------------------------------------------------------------------------------------
#a=int(input("please enter your first number"))
#b=int(input("please enter your second number"))
#c=int(input("please enter your third number"))
#d=int(input("please enter your fourth number"))
#e=int(input("please enter your fifth number"))

#print( "maximum is:", max(a,b,c,d,e), "and minimum is:", min(a,b,c,d,e))

#-------------------------------------------------------------------------------
#Sum of even numbers:
#-------------------------------------------------------------------------------
#sum=0
#for i in range(0,101,2):
#    sum=sum+i
#print(sum)
#------------------------------------------------------------------------------
 #Write a python program to print all the different arrangements of the
# letters A, B, C and D. Each string printed is a permutation of ABCD.
#------------------------------------------------------------------------------------
#for i in ["A","B","C","D"]:
 #   for j in  ["A","B","C","D"]:
 #      if i!=j:
  #        for k in ["A","B","C","D"]:
   #           if i!=k and j!=k:
    #             for z in ["A","B","C","D"]:
     #               if i!=z and j!=z and k!=z:
      #                  print(i+j+k+z, end="/")
#-------------------------------------------------------------------------
# Write a python program to print all the different arrangements of the
# letters A, B, and C. Each string printed is a permutation of ABC.
#---------------------------------------------------------------------------
#for i in ["A","B","C"]:
#   for j in  ["A","B","C"]:
#      if i!=j:
#          for k in ["A","B","C"]:
#              if k!=i and k!=j:
#                  print(i+j+k, end="/")
#--------------------------------------------------------------------------
# Write python program to print prime numbers up to a specified values.
#--------------------------------------------------------------------------\
 #Write a Python function called calculate_grade that takes in a
#list of student scores as input. Each score is an integer between 0 and 100.
#Your function should calculate the average score and then return
#the corresponding letter grade based on the following grading scale
#-------------------------------------------------------------------------------
#def calculator():
#    sum = 0
#    grade_list = []

#    for i in range(0,n):
#     grade=int(input("please enter the grade"))
#     if grade>100:
#      print("please enter numbers below 100")
#     else:
#      grade_list.append(grade)

#    for i in grade_list:
#      sum=sum+i

#    average=sum/n

#    if average>=90 and average<=100:
#          print("average is",average,"the grade scale is A")
#    if average >= 80 and average<=89:
#          print("average is",average,"the grade scale is B")
#    if average >= 70 and average<=79 :
#          print("average is", average," the grade scale is C")
#    else:
#          print("average is", average, "the grade scale is F")


#n = int(input("please enter the number of grades that you would like to enter"))
#calculator()
#----------------------------------------------------------------------------
#Word_frequency
#-----------------------------------------------------------------------------
#def wordcounter(Text):

#    list=["a","an", "and","the"]
#    filtered_text=[]
#    Text=str.lower(Text)
#    words=str.split(Text)

#    for i in words:
#      if i not in list:
#       filtered_text.append(i)

 #   Text = " ".join(filtered_text)
#    print(Text)

 #   Wordcount={}

#    for i in filtered_text:
#        if i in Wordcount:
#            Wordcount[i]+=1
#        else:
#            Wordcount[i]=1
#    print(Wordcount)

#Text = str(input("Enter your sentence"))
#wordcounter(Text)
#----------------------------------------------------------------------------------
## Suppose we wish to draw a triangular tree, and its height is provided
# by the user.
#---------------------------------------------------------------------------
#Height=int(input("Enter the height of the tree"))
#j=0
#sign="*"
#while j<Height:
#    spaces = ' ' * (Height - j - 1)
#    stars = sign * (2 * j + 1)
#    print(spaces + stars)
#    j += 1
#---------------------------------------------------------------------------
#Write a program that simulates the rolling of a die.
# ----------------------------------------------------------------
#import random
#print(" this is a die rolling program")
#while True:
#    input("welcome to the game, please enter to roll the die")
#    number= random.randint(1,6)
#    print(" your number is: "," ", number)
#    rolling= input("enter yes if you wanna roll again, other wise enter no    ")
#    if rolling== "yes":
#       number= random.randint(1,6)
#       print(" your number is: ", " ", number)
#    else:
#         break

import random
#def roll_dice():
#    print(" this is a die rolling program")
#    while True:
#        input("welcome to the game, please enter to roll the die")
#        number = random.randint(1, 6)
#        print(" your number is: ", " ", number)
#        rolling = input("enter yes if you wanna roll again, other wise enter no    ")
#        if rolling == "yes":
#            number = random.randint(1, 6)
#            print(" your number is: ", " ", number)
#        else:
#            break

#----------------------------------------------------------------------------------------------
#input("enter if you wanna roll")
#roll_dice()

#Class_Ex3:
# Randomly Permuting a List
# ----------------------------------------------------------------
#import random
#c=[50,4,2,10,5]
#n=len(c)
#for i in range(0,n-1):
#      p= random.randrange(i,n)
#      c[i],c[p]=c[p],c[i]

#print(c)









# =================================================================
# Class_Ex4:
# Write a program to convert a tuple to a string.
# ----------------------------------------------------------------
import random

Arbitrary_tuple = input("please enter an arbitrary tuple")

if type(Arbitrary_tuple)==tuple:
  for element in eval(Arbitrary_tuple):
       element=str(element)
     print(element,end=" ")

print(type(element))




# =================================================================
# Class_Ex5:
# Write a program to get the 3th element and 3th element from last of a tuple.
# ----------------------------------------------------------------


# =================================================================
# Class_Ex6:
# Write a program to check if an element exists in a tuple or not.
# ----------------------------------------------------------------


# =================================================================
# Class_Ex7:
# Write a  program to check a list is empty or not.
# ----------------------------------------------------------------
#def list_checker():
# while True:
#     numbers=input("please enter your list numbers")
#     list1=[]
#     for i in numbers.split():
#          i = i.strip()
#          list1.append(i)
#     if not list1:
#      print("your list is empty")
#     else:
#      print(list1)
#      print(len(list1))

#input("welcome to the program, please press enter to continue")
#list_checker()

# =================================================================
# Class_Ex8:
# Write a program to generate a 4*5*3 3D array that each element is O.
# ----------------------------------------------------------------
#----------------------

























#name="Amirali Bozorgnia"
#print(len(name))
#print(name.split("Amirali Bozorgnia"))
#print(name.find("a"))
#print(name.upper())
#print(name.replace("Amirali Bozorgnia", "Hossein Tabary"))
#print(name)

#import math
#k=3.569
#print(round(k,2))
#print(round(k,3))
#print(round(k,1))
#print(math.log10(k))
#print(math.floor(k))
#print(math.ceil(k))
#print(math.sin(k))
#print(math.sqrt(k))
#print(pow(k,2))

#name="Amirali Bozorgnia"
#First_name=name[0:7]
#last_name=name[8:]
#print(First_name+" "+last_name)


#print(name[0:7:2])

