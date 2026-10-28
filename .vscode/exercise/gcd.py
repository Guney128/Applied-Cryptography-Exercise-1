def greatestCommonDivider(firstNumber, secondNumber):
    currentGcd = 1
    indexFirstNumber = 0
    indexSecondNumber = 0
    for firstPrimeFactor in firstNumber:
        indexSecondNumber = 0
        for secondPrimeFactor in secondNumber:
            if firstNumber[indexFirstNumber] == secondNumber[indexSecondNumber]:
                currentGcd = firstPrimeFactor * currentGcd
                firstNumber[indexFirstNumber] = 1
                secondNumber[indexSecondNumber] = 1
            indexSecondNumber = indexSecondNumber + 1
        indexFirstNumber = indexFirstNumber + 1
    return currentGcd
