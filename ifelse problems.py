#password & username
print("\tCreate a Username.")
username = input("Create your username:")
print("\tCreate a password.")
password = input("Enter your password: ")

print("\nWelcome to Emman.com")

x1=input("Please enter your username:")
if x1 == username:
    y1 = input("Please enter your password: ")
    if y1 == password:
        print("Logged in successfully as ", username, ".", sep="") 
    else:
        print ("Password incorrect!")
else:
    print ("Username incorrect!")
    
#converter
cm=eval(input("Enter a lenght in centimeters: "))
inches=cm/2.54
if cm < 0:
    print("The entry is invalid.")
else:
    print("There are ", round(inches,2), " inche/s in a ",  cm, " centimeter/s.", sep="")
print("Emmanuel Doria")

#election age
age=eval(input("Enter your age: "))

if age>=18:
    print("The applicant is elligible to vote for the elections.")
    
else:
    print("The applicant is not elligible to vote for the elections.")
    
#A Python Program to check if the 
#input number is even or odd.

num=eval(input("Type a number: "))

if num%2==0:
    print("The number is even.")
else:
    print("The number is odd.")
    
