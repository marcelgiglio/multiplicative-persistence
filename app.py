
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

def notCrescentOrder(n):
    return "".join(sorted(str(n))) != str(n)

def HaveForbiddenPair(n):
    forbidenPairs = [('2','2'), ('2','3'), ('2','4'), ('3','3')]
    ans = False
    n = str(n)
    for pair in forbidenPairs:
        if (pair[0] in n and pair[1] in n.replace(pair[0],'',1)):
                ans = True
    return ans

def validNumber(n):
    ans = True
    if (notCrescentOrder(n) or HaveForbiddenPair(n)):
        ans = False
    return ans

max = 0
bestNumbers = []
for i in range(1000000):
    if (validNumber(i)):
        result = recursiveCalc(i)
        if(result[1] > max):
            max = result[1]
            printNumber(i, result[0])
            bestNumbers.append(i)
print (bestNumbers)
