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

a=int(input("please enter your first number"))
b=int(input("please enter your second number"))
c=int(input("please enter your third number"))
d=int(input("please enter your fourth number"))
e=int(input("please enter your fifth number"))

print( "maximum is:", max(a,b,c,d,e), "and minimum is:", min(a,b,c,d,e))

#-------------------------------------------------------------------------------




name="Amirali Bozorgnia"
#print(len(name))
print(name.split("Amirali Bozorgnia"))
print(name.find("a"))
print(name.upper())
print(name.replace("Amirali Bozorgnia", "Hossein Tabary"))
print(name)

import math
k=3.569
print(round(k,2))
print(round(k,3))
print(round(k,1))
print(math.log10(k))
print(math.floor(k))
print(math.ceil(k))
print(math.sin(k))
print(math.sqrt(k))
print(pow(k,2))

name="Amirali Bozorgnia"
First_name=name[0:7]
last_name=name[8:]
print(First_name+" "+last_name)


print(name[0:7:2])

