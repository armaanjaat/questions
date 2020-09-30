 #Nighthawk Programming
#calculate how many days you have passed till birth

import datetime

today=datetime.date.today()
print("Today is ",today)    #Today's date extracted


a=int(input("Enter Your B'Day Date(1-31) "))
b=int(input("Enter Your B'Day Month Number(0-12) "))
c=int(input("Enter Your B'Day Year "))

birthday=datetime.date(c,b,a)
print("Your Birthday is ",birthday)  #Birthday Extracted

#birthday=datetime.date(2003,7,7)
#print("Your Birthday is ",birthday)

days_on_earth=(today-birthday).days
print("You have completed ",days_on_earth,"Days on Earth")
input("Press enter to exit")



