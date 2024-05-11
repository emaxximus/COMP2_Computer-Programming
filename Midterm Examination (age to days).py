print("\nName: Doria, Emmanuel C.")
print("Section: CAS-05-401P")
print("\n\t\t\tMIDTERM EXAMINATION")

print("Problem #3: Create a program the will convert \nthe age of the user to days. Use 365 days \nas the length of a year and exclude leap years.")
print("Positive integer inputs only be included. If the \nnumbers are negative, the program will show 'Invalid Age'.")
print("The program will stop when the user say so.")

for I in range (1):
    age=eval(input("Type your age: "))
if age>0:
    ans=age*365
    print("You are ", ans, "days old.")
else:
    print("Invalid age.")
   
choice=input("Would you like to convert an age to days again? [Y/N]: ")
while choice=="y" or choice=="Y":
    for I in range (1):
        age=eval(input("Type your age: "))
    if age>0:
        ans=age*365
        print("You are ", ans, "days old.")
    else:
        print("Invalid age.")
    choice=input("Would you like to convert an age to days again? [Y/N]: ")
