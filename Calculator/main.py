import Addition
import Division
import Modulus
import Multiplication
import Percentage
import Substraction


while(True):
    
    print(""""**************   Please Choose According to your work   ******************\n
      Press : 1 for Addition
      Press : 2 for Substraction
      Press : 3 for Multiplication
      Press : 4 for Division
      Press : 5 for Percentage
      Press : 6 for Modulus\n
*****************************************************************************
      """)


    
    num = int(input("Choose Your Operation : "))
    
    if num == 1 :
        a = int(input("Enter First number : "))
        b = int(input("Enter Second number : "))
        Addition.add(a,b)
    elif num == 2 :
        a = int(input("Enter a number : "))
        b = int(input("Enter substract number by : "))
        Substraction.subs(a,b)
    elif num == 3 :
        a = int(input("Enter First number : "))
        b = int(input("Enter Second number : "))
        Multiplication.mul(a,b)
    elif num == 4 :
        a = int(input("Enter Divisor number : "))
        b = int(input("Enter Divider number : "))
        Division.divi(a,b)
    elif num == 5 :
        a = int(input("Enter a number : "))
        b = int(input("Enter percentage of : "))
        Percentage.perc(a,b)
    elif num == 6 :
        a = int(input("Enter First number : "))
        b = int(input("Enter Modulur number By : "))
        Modulus.modu(a,b)
    else:
        num > 6
        exit()

        
    
    
