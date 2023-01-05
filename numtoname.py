from num2words import num2words

number = int(input())
print("what language do you want?")
print(" span: 1")
print(" eng: 2")
print(" fran: 3")
print(" german: 4")
langind = int(input(""))
def Langindtolang(langint):
    if langint == 1:
        return "es"
    if langint == 2:
        return "en"
    if langint == 3:
        return "fr"
    if langint == 4:
        return "de"
name = num2words(number, lang = Langindtolang(langind))
print(name)