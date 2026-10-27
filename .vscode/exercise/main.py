from factor import *
from gcd import *

while True:
    print("Enter two integers: ")
    firstValueToFactorise = int(input())  
    secondValueToFactorise = int(input())
    if type(firstValueToFactorise) != int or firstValueToFactorise < 0 or type(secondValueToFactorise) != int or secondValueToFactorise < 0:
        print("Please enter a number bigger than 0")      
    else:
        break
            
print(factor(firstValueToFactorise))
print(factor(secondValueToFactorise))
print(greatestCommonDivider(factor(firstValueToFactorise), factor(secondValueToFactorise)))