from factor import *


while True:
    print("Enter an integer: ")
    valueToFactorise = int(input())  
    if type(valueToFactorise) != int or valueToFactorise < 0:
        print("Please enter a number bigger than 0")      
    else:
        break
            
print(factor(valueToFactorise))