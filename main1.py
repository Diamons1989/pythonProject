import re


text = input("Введіть слово або речення: ")
if re.findall(r"^[A-Z]+\D.\w*", text):
    print(text, "валідне")
else:
    print(text, "не валідне")
