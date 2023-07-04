dictionary = {
    "КРИНЖ": "Что-то очень странное или стыдное",
    "РОФЛ": "шутка",
    "КРИПОВЫЙ": "страшный, пугающий",
    "АГРИТЬСЯ": "Злиться"
}
while True:
    word = input("Введите непонятное Вам слово: ").upper()
    if word in dictionary.keys():
        print(dictionary[word])
    else:
        print("Такого слова нет в словаре")
        answer = input("Хотите ли вы добавить это слово в словарь?").upper()
        if answer == "ДА":
            newword = input("Напишите значение этого слова")
            dictionary[word] = newword

        

