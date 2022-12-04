
i = 0
while i<3:
    i += 1
    try:
        word :str = input("Введите слово, состоящее не менее, чем из 3 символов: ")
        if len(word) <= 3:
            print("Ваше слово состоит из ---" + str(len(word)) + "--- символов. Введите другое слово: ")
            continue
        if not word.isalpha():
            print("Ваше слово содержит числа или спецсимволы. Введите другое слово: ")
            continue
        with open("practic_2/words.txt", "a", encoding="utf-8") as file:
                file.write(str(i) + ". " + str(word) + "\n")
                print("Ваше слово - "+ str(word) + " было записано в файл") 

    except Exception as e:
         # print("Что-то пошло не так")
         print(e)