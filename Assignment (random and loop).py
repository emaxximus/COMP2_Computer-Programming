#Assignment:
#Write a program that will display ten items of 
#2 random numbers multiplying by each other. 
#The user will answer the ten items quiz and show the score after. 
#Use for loop in this program.

#Emman Doria
score=0
for i in range(10):
    from random import randint
    rnum1=randint(1,10)
    rnum2=randint(1,10)
    print("\nMultiply ", rnum1, " and ", rnum2, ":",sep="")
    ans=eval(input("Answer: "))
    if ans==rnum1*rnum2:
        print("Correct!")
        score=score+1
    else:
        print("Wrong!")
        
print("\nYour final score is ", score, "/10.", sep="")
