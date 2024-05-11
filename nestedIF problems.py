#Technician
print("\nHelp! My computer doesn't work.")
choice=input("Does the computer make any sounds (fans, etc.) [Y/N]? ")
if choice=="N" or choice=="n":
    choice1=input("Is it plugged in? (y/n): ")
    if choice1=="N" or choice1=="n":
        print("Plug it in. If the problem persists, \n please run this probram again.")
    else:
        choice2=input("Is the switch in the \"on\" position? (y/n): ")
        if choice2=="N" or choice2=="n":
            print("Turn it on. If the problem persists, \n please run this program again.")
        else:
            choice3=input("Does the computer have a fuse? (y/n): ")
            if choice3=="N" or choice3=="n":
                choice4=input("Is the outlet OK? (y/n): ")
                if choice4=="N" or choice4=="n":
                    print("Check the outlet's circuit breaker or fuse. Move to a new outlet, if necessary. If the problem persists, please run this program again.")
                else:
                    print("Please consult a service technician.")
            else:
                print("Check the fuse. Replace if necessary. If the problem persists, then please run this program again.")
else:
    print("Please consult a service technician.")
    
#A year is a leap year if it is divisible by 4, 
#except that years divisible by 100 are not leap years
#unless they are also divisible by 400. 
#Write a program that asks the user for a year and prints
#out whether it is a leap year or not.

year=eval(input("Type a year: "))

if year%4==0:
    if year%400:
        if year%100==0:
            print(year, " is not a leap year.")
        else:
            print(year, " is a leap year.")
    else:
        print(year, " is a leap year.")   
else:
    print(year, " is not a leap year.")
    