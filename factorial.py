number = int(input(""))
i = 0
answer = 1
for i in range(number):
    if (i != number):
        answer = answer*(number-i)
    else:
        print(answer)
print(answer)




