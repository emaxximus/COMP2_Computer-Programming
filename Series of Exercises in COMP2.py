#Exercise 1 THE NUMBER IS HIGHER
num=eval ( input ( "Type a number: "))
if num>0:
    print("The number is positive.")
print("End of the program.")

#Exercise 2 RANDOM NUMBER, POSITIVE OR NEGATIVE
from random import randint
num=randint(-5,5)
print("\nThe random number is ", num)
if num>0:
    print("The number is positive.")
print("End of the program.")

#Exercise 3 THE NUMBER IS LOWER
#Ask the user a number and identify if it is lower than 200
num = eval ( input ( "\nType a number: "))
if num<200:
    print("The number is lower than 200.")
print("End of the program.")

#Exercise 4 
num=eval(input("\nEnter the luggage weigh: "))
if num>50:
    print("There is a $25 charge for the luggage that heavy.")
print("Thank you!")

#Exercise 5 GUESSING GAME
from random import randint
num=randint(1,5)
print("\nThis is a guessing game.")
gnum=eval(input("Guess the number form 1 to 5: "))
if num==gnum:
    print("You guess it right.")
else:
    print("The correct number is ", num, ".", sep="")
    
#Exercise 6 ODD OR EVEN
num=eval(input("\nType a number: "))
if num%2==0:
    print("The number is even.")
print("The number is odd.")

#Exercise 7 DISCOUNT
amnt=eval(input("\nEnter the amount: "))
if amnt<1000:
    discount=amnt*0.05
    print("Your discounted amount is ", discount, ".", sep="")
else:
    discount=amnt*0.10
    print("Your discounted amount is ", discount, ".", sep="")    
print("Net payable: ", amnt-discount)

#Exercise 8 ELECTION ELLIGIBILITY
age=eval(input("\nEnter your age: "))
if age>=18:
    print("The applicant is elligible to vote for the elections.")
else:
    print("The applicant is not elligible to vote for the elections.")

#Exercise 9 QUIZ
score=0
print("\nUse CAPITAL LETTERS ONLY!")

q1=input("What is the capital of Japan? ")
if q1=="TOKYO":
    print("Your answer is correct!")
    score=score+1
else:
    print("Ooops! Your answer is wrong.")
    print("The correct answer is TOKYO.")
    
q2=input("What is the capital of Philippines? ")
if q2=="MANILA":
    print("Your answer is correct!")
    score+=1
else:
    print("Ooops! Your answer is wrong.")
    print("The correct answer is MANILA.")
    
q3=input("What is the capital of South Korea? ")
if q3=="SEOUL":
    print("Your answer is correct!")
    score+=1
else:
    print("Ooops! Your answer is wrong.")
    print("The correct answer is SEOUL.")

print("Your final score is ", score, ".", sep="")
