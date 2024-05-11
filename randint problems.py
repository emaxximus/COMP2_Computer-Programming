#randomizer
from random import randint

rnum=randint(20,25)

gnum=eval(input("Type your guess number from 20 to 25: "))

if gnum<rnum:
    print("Too low, the correct answer is ", rnum)
elif gnum>rnum:
    print("Too high, the correct answer is ", rnum)
else:
    print("You got it!")
    
#guessing game
from random import randint

num=randint(1,5)

print("\nThis is a guessing game.")
gnum=eval(input("Type your guess number from 1 to 5: "))

if num==gnum:
    print("Congratulations! You got it!!")
else:
    print("Oops, you're wrong. The correct answer is ", num,".",sep="")
    
#positive number
from random import randint

num=randint(-5,5)
gnum=eval(input("\nType your guess number from -5 to 5: "))

print("\nThe random number is ",num)

if num>0:
    print("The number is positive.")

print("End of the program.")