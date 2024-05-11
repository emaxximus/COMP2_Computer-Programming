#while LOOP
items=eval(input("How many numbers you want to add? "))
i=1
ans=0
for i in range(items):
    num=eval(input("Type a number: "))
    ans=ans+num
print("\nSum of all the numbers is ", ans)

choice=input("Do you want to run the program again? [Y/N]")
while choice=="Y" or choice=="y":
    items=eval(input("How many numbers you want to add? "))
    i=1
    ans=0
    for i in range(items):
        num=eval(input("Type a number: "))
        ans=ans+num
    print("\nSum of all the numbers is ", ans)

#guessing game
print("\nThis is a guessing game.")
from random import randint
num=randint(1,5)
gnum=0

while num!=gnum:
    gnum=eval(input("Type your guess number from 1 to 5: "))

print("Congratulations! You got it!!")

#double loop
print("\nThis is a guessing game.")
from random import randint
num=randint(1,5)
gnum=0

while num!=gnum:
    gnum=eval(input("Type your guess number from 1 to 5: "))

print("FINALLY! You got it!!")

choice=input("Do you want to run the program again? [Y/N]: ")
while choice=="Y" or choice=="y":
    print("\nThis is a guessing game.")
    from random import randint
    num=randint(1,5)
    gnum=0
   
    while num!=gnum:
        gnum=eval(input("Type your guess number from 1 to 5: "))

    print("FINALLY! You got it!!")
    choice=input("Do you want to run the program again? [Y/N]: ")
    

