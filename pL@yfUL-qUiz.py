
print("\n\t\t\tSobrang Random Quiz!")
print("\t\t uSE CaPITal l3TTeR$ 0N7Y!")
print("\nStart!")

score=0
wrong=0

q1=input("What body part of Shakira doesn't lie? ")
if q1=="HIPS":
    print("You got it right!")
    score=score+1
else:
    print("Ooops! Your answer is wrong.")
    print("Shakira's HIPS don't lie.")
    wrong=score+1
    
q2=input("Who you gonna call? ")
if q2=="GHOSTBUSTERS":
    print("You got it right!")
    score+=1
else:
    print("Ooops! Your answer is wrong.")
    print("The correct answer is GHOSTBUSTERS!!!")
    wrong+=1
      
q3=input("COCA-COLA or PEPSI: Who made it first to the space? ")
if q3=="COCA-COLA":
    print("You got it right!")
    score+=1
else:
    print("Ooops! Your answer is wrong.")
    print("Coca-cola and Pepsi were the only drinks in space that year but COCA-COLA was the first drink the astronaut drank in space shortly after the astronauts also took a gulp of the Pepsi drink.")
    wrong+=1

print("\nFill in the blanks: ") 
q4=input("BOOM TARAT TARAT! BOOM TARAT TARAT! TARARAT TARARAT ____ ____ ____. ")
if q4=="BOOM BOOM BOOM":
    print("You got it right!")
    score+=1
else:
    print("Ooops! Your answer is wrong.")
    print("The correct answer is BOOM BOOM BOOM.")
    wrong+=1

q5=input("What kind of music are balloons scared of? ")
if q5=="POP MUSIC":
    print("You got it right!")
    score+=1
else:
    print("Ooops! Your answer is wrong.")
    print("The correct answer is POP! MUSIC.")
    wrong+=1 
    
print("\nYou got", score, "correct answers.")
print("You got", wrong, "wrong answers.")
print("Your final score is ", score, "/5.", sep="")





