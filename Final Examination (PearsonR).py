from math import sqrt
name=str(input("NAME: "))

print("\nHello, ",name,"! \nKindly follow the direction given below.",sep="")
print("Direction: Give the following data according to its pair of variable.")
print('\nPEARSON CORRELATION COEFFICIENT')
print("Give the values of x and y.")
n=eval(input("Sample size: "))
i=0
Sx=0    
Sy=0     
Sxsq=0     
Sysq=0    
Sxy=0 
pr=0

for i in range(n):
    x=eval(input("Type the x: "))
    y=eval(input("Type the y: "))
    
#Solution
#Σx and Σy
    Sx=Sx+x 
    Sy=Sy+y            
#Σx^2 and Σy^2           
    x2=x*x
    Sxsq+=x2 
    y2=y*y 
    Sysq+=y2  
#Σxy           
    xy=x*y  
    Sxy+=xy 
    
print("\nn:    ", n)
print("Σx:   ", Sx)
print("Σy:   ", Sy)
print("Σx^2: ", Sxsq)
print("Σy^2: ", Sysq) 
print("Σxy:  ", Sxy)

#Pearson R
try:
    r=(n*Sxy)-(Sx*Sy)
    r1=(n*Sxsq)-(Sx**2) 
    r2=(n*Sysq)-(Sy**2)
    r3=sqrt(r1*r2)
    p=r/r3
    pr=round(p,3)
    print("\nPEARSON R = ",pr)
    
#Significant relationship between x and y
    if pr>=0.000 and pr<=0.204 or pr<=-0.000 and pr>=-0.204:
        print("Finding: No Relationship.")
    elif pr>=0.205 and pr<=0.404 or pr<=-0.205 and pr>=-0.404:
        print("Finding: Low Relationship.") 
    elif pr>=0.405 and pr<=0.604 or pr<=-0.405 and pr>=-0.604:
        print("Finding: Moderate Relationship.")
    elif pr>=0.605 and pr<=0.894 or pr<=-0.605 and pr>=-0.894:
        print("Finding: High Relationship.")    
    elif pr>=0.895 and pr<=0.999 or pr<=-0.895 and pr>=-0.999:
        print("Finding: Very High Relationship.")   
    elif pr==1 or pr==-1: 
        print("Finding: Perfect Relationship.")
    else:
        print("Invalid Result.")    

#Coefficient of Determination
    cd=(pr**2)*100
    print("COEFFICIENT OF DETERMINATION: ",round(cd,2),"%",sep="")
    con=str(input("Do you want to run the program again [Y/N]? "))
    while con=="Y" or con=="y":
        from math import sqrt
        print("\nDirection: Give the following data according to its pair of variable.")
        print('\nPEARSON CORRELATION COEFFICIENT')
        print("Give the values of x and y.")
        n=eval(input("Sample size: "))
        i=0
        Sx=0    
        Sy=0     
        Sxsq=0     
        Sysq=0    
        Sxy=0 
        pr=0

        for i in range(n):
            x=eval(input("Type the x: "))
            y=eval(input("Type the y: "))
            
        #Solution
        #Σx and Σy
            Sx=Sx+x
            Sy=Sy+y            
        #Σx^2 and Σy^2           
            x2=x*x
            Sxsq+=x2 
            y2=y*y 
            Sysq+=y2  
        #Σxy           
            xy=x*y  
            Sxy+=xy 
            
        print("\nn:    ", n)
        print("Σx:   ", Sx)
        print("Σy:   ", Sy)
        print("Σx^2: ", Sxsq)
        print("Σy^2: ", Sysq) 
        print("Σxy:  ", Sxy)

        #Pearson R
        try:
            r=(n*Sxy)-(Sx*Sy)
            r1=(n*Sxsq)-(Sx**2) 
            r2=(n*Sysq)-(Sy**2)
            r3=sqrt(r1*r2)
            p=r/r3
            pr=round(p,3)
            print("\nPEARSON R = ",pr)
            
        #Significant relationship between x and y
            if pr>=0.000 and pr<=0.204 or pr<=-0.000 and pr>=-0.204:
                print("Finding: No Relationship.")
            elif pr>=0.205 and pr<=0.404 or pr<=-0.205 and pr>=-0.404:
                print("Finding: Low Relationship.") 
            elif pr>=0.405 and pr<=0.604 or pr<=-0.405 and pr>=-0.604:
                print("Finding: Moderate Relationship.")
            elif pr>=0.605 and pr<=0.894 or pr<=-0.605 and pr>=-0.894:
                print("Finding: High Relationship.")    
            elif pr>=0.895 and pr<=0.999 or pr<=-0.895 and pr>=-0.999:
                print("Finding: Very High Relationship.")   
            elif pr==1 or pr==-1: 
                print("Finding: Perfect Relationship.")
            else:
                print("Invalid Result.")        

        #Coefficient of Determination 
            cd=(pr**2)*100
            print("COEFFICIENT OF DETERMINATION: ",round(cd,2),"%",sep="")
            con=str(input("Do you want to run the program again [Y/N]? ")) 
            
        except ZeroDivisionError:  
            print("\nThe coefficient of determination is NaN.")
            print("Explanation: This is a strong negative correlation, which means that")
            print("high X variable scores go with low Y variable scores (and vice versa).")
            con=str(input("Do you want to run the program again [Y/N]? "))
    else:
        print("Thank you for using this program. :)")

except ZeroDivisionError:  
    print("\nThe coefficient of determination is NaN.")
    print("Explanation: This is a strong negative correlation, which means that")
    print("high X variable scores go with low Y variable scores (and vice versa).")
    con=str(input("Do you want to run the program again [Y/N]? "))    
    while con=="Y" or con=="y":
        from math import sqrt
        print("\nDirection: Give the following data according to its pair of variable.")
        print('\nPEARSON CORRELATION COEFFICIENT')
        print("Give the values of x and y.")
        n=eval(input("Sample size: "))
        i=0
        Sx=0    
        Sy=0     
        Sxsq=0     
        Sysq=0    
        Sxy=0 
        pr=0

        for i in range(n):
            x=eval(input("Type the x: "))
            y=eval(input("Type the y: "))
            
        #Solution
        #Σx and Σy
            Sx=Sx+x 
            Sy=Sy+y            
        #Σx^2 and Σy^2           
            x2=x*x
            Sxsq+=x2 
            y2=y*y 
            Sysq+=y2  
        #Σxy           
            xy=x*y  
            Sxy+=xy 
            
        print("\nn:    ", n)
        print("Σx:   ", Sx)
        print("Σy:   ", Sy)
        print("Σx^2: ", Sxsq)
        print("Σy^2: ", Sysq) 
        print("Σxy:  ", Sxy)

        #Pearson R
        try:
            r=(n*Sxy)-(Sx*Sy)
            r1=(n*Sxsq)-(Sx**2) 
            r2=(n*Sysq)-(Sy**2)
            r3=sqrt(r1*r2)
            p=r/r3
            pr=round(p,3)
            print("\nPEARSON R = ",pr)
            
        #Significant relationship between x and y
            if pr>=0.000 and pr<=0.204 or pr<=-0.000 and pr>=-0.204:
                print("Finding: No Relationship.")
            elif pr>=0.205 and pr<=0.404 or pr<=-0.205 and pr>=-0.404:
                print("Finding: Low Relationship.") 
            elif pr>=0.405 and pr<=0.604 or pr<=-0.405 and pr>=-0.604:
                print("Finding: Moderate Relationship.")
            elif pr>=0.605 and pr<=0.894 or pr<=-0.605 and pr>=-0.894:
                print("Finding: High Relationship.")    
            elif pr>=0.895 and pr<=0.999 or pr<=-0.895 and pr>=-0.999:
                print("Finding: Very High Relationship.")   
            elif pr==1 or pr==-1: 
                print("Finding: Perfect Relationship.")
            else:
                print("Invalid Result.")        

        #Coefficient of Determination 
            cd=(pr**2)*100
            print("COEFFICIENT OF DETERMINATION: ",round(cd,2),"%",sep="")
            con=str(input("Do you want to run the program again [Y/N]? ")) 

            
        except ZeroDivisionError:
            print("\nThe coefficient of determination is NaN.")
            print("Explanation: This is a strong negative correlation, which means that")
            print("high X variable scores go with low Y variable scores (and vice versa).")
            con=str(input("Do you want to run the program again [Y/N]? ")) 
    else:
        print("Thank you for using this program. :)")
        