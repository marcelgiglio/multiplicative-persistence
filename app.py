def recursiveCalc(n, counter=0, steps=''):
    if n<10:
        steps += 'Total Steps: ' + str(counter) + '.'
        return steps, counter
    counter+=1
    result = calc(n)
    steps += str(result)+', '
    return recursiveCalc(result, counter, steps)

def calc(n):
    result = 1
    while (n>0):
        mod = n % 10
        result *= mod
        n -= mod
        n /= 10
    return result

def printNumber(n, steps):
    print (str(n) + ': ' + steps)

max = -1
bestNumbers = []
for i in range(1000000):
    result = recursiveCalc(i)
    if(result[1] > max):
        max = result[1]
        printNumber(i, result[0])
        bestNumbers.append(i)
print (bestNumbers)
