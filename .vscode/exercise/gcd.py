def greatestCommonDivider(firstNumber, secondNumber):
    currentGcd = 0
    for firstPrimeFactor in firstNumber:
        for secondPrimeFactor in secondNumber:
            if firstPrimeFactor == secondPrimeFactor:
                currentGcd = firstPrimeFactor

    return currentGcd
