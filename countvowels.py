text = open('text.txt', "r")
string = text.read()
count = 0
for i in range(len(string)):
    if string[i] == "a":
        count = count+1
    if string[i] == "e":
        count = count+1
    if string[i] == "i":
        count = count+1
    if string[i] == "o":
        count = count+1
    if string[i] == "u":
        count = count+1

print(count)