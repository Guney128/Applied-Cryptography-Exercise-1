def factor(valueToFactorise):
    i = 2
    primeFactors = []

    while valueToFactorise != 1:
        if valueToFactorise % i > 0:
            i = i + 1
        else:
            valueToFactorise = valueToFactorise // i 
            primeFactors.append(i)   

    return primeFactors