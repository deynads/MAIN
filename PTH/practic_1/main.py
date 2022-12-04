# i = 0
# while i<3:
#     with open("text.txt", "a") as file:
#         i += 1
#         line = input("Введите Имя: ")
#         file.write(str(i)+". " +line)
#         line = input("Введите Фамилию: ")
#         file.write(" "+ line + " ")
#         age = input("Введите ваш возраст: ")
#         try:
#             age_int = int(age)
#             print("Ваш возраст: ",str(age_int))
#             file.write(" "+ str(age_int) + "\n")
#         except Exception as e:
#             print("Формат данных возраста не верный")
        

from encodings.utf_8 import encode

i = 0
while i<3:
    i += 1
    fname :str = input("Введите Имя: ")
    lname :str = input("Введите Фамилию: ")
    age :str = input("Введите ваш возраст: ")
    try:
            age_int = int(age)
            print("Ваш возраст: ",str(age_int))
            with open("practic_1/text.txt", "a", encoding="utf-8") as file:
                file.write(str(i) + ". " + fname + " " + lname + " " + age + "\n")

    except ValueError as e:
        print("Формат данных возраста не верный")

    
        
        
