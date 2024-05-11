#Highest Lowest
a=eval(input("Enter a number: "))
b=eval(input("Enter a number: "))
c=eval(input("Enter a number: "))

if (a>b) and (a>c):
    print("The highest number is ", a,".", sep="")
elif (b>a) and (b>c):
    print("The highest number is ", b,".", sep="")
else:
    print("The highest number is ", c,".", sep="")
if (a<b) and (a<c):
    print("The lowest number is ", a,".", sep="")
elif (b<a) and (b<c):
    print("The lowest number is ", b,".", sep="")
else:
    print("The lowest number is ", c, ".", sep="")

#Grade Description
print("\nEnter your grades in Math, Science, English, Filipino, and Arts.")    
grade_1=eval(input("Enter your grade in Math: "))
grade_2=eval(input("Enter your grade in Science: "))
grade_3=eval(input("Enter your grade in English: "))
grade_4=eval(input("Enter your grade in Filipino: "))
grade_5=eval(input("Enter your grade in Arts: "))

ave=(grade_1+grade_2+grade_3+grade_4+grade_5)/5

if ave<75:
    print("Your average is ", round(ave,2))
    print("FAILED")
elif ave>=75 and ave<=79:
    print("Your average is ", round(ave,2))
    print("PASSED")
elif ave>=80 and ave<=85:
    print("Your average is ", round(ave,2))
    print("FAIR")
elif ave>=86 and ave<=90:
    print("Your average is ", round(ave,2))
    print("GOOD")
elif ave>=91 and ave<=95:
    print("Your average is ", round(ave,2))
    print("VERY GOOD")
elif ave>=96 and ave<=100:
    print("Your average is ", round(ave,2))
    print("EXCELLENT")
else:
    print("Invalid Grade")
    
#Get the amount of purchase of the user. 
#Use the following guide to give the user a discount.
#0-1000			5%
#1001-4999		10%
#5000 above		15%
#Display the discounted amount and net payable.


purchase=eval(input("\nAmount Purchased: "))

if purchase>=0 and purchase<=1000:
    discount= purchase * .05
    print("Discounted amount: ", discount)
    print("You only need to pay ", purchase - discount)
    
elif purchase>1000 and purchase<=4999:
    discount=purchase * .10
    print("Discounted amount: ", discount)
    print("You only need to pay ", purchase - discount)

elif purchase>=5000 :
    discount=purchase * .15
    print("Discounted amount: ", discount)
    print("You only need to pay ", purchase - discount)
    
else:
    print("Invalid amount.")
    discount=0
    
#Identify your year level base on number of credits taken
crdts=eval(input("\nHow many credits have you taken? "))

if crdts <= 23:
    print("FRESHMAN")
elif crdts >= 24 and crdts <= 53:
    print("SOPHOMORE")
elif crdts >= 54 and crdts <= 83:
    print("JUNIOR")
else:
    print("SENIOR")
    
#Identifiny the temperature level
temp=eval(input("\nEnter a temperature in Celcius: "))

if temp < -273.15:
    print("The temperature is invalid because it is below absolute zero.")
elif temp == -273.15:
    print("The temperature is absolute zero.")
elif temp > -273.15 and temp < 0:
    print("The temperature is below freezing point.")
elif temp == 0:
    print("The temperature is at the freezing point.")
elif temp > 0 and temp < 100:
    print("The temperature is in the normal range.")
elif temp == 100:
    print("The temperature is at the boiling point.")
else:
    print("The temperature is above the boiling point.")
    