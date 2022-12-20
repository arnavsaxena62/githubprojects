numberofDigits = int(input())
def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-2)+ fibonacci(i-1)

for j in range(numberofDigits):
    print(fibonacci(j))
    j+1