import random
print("Жёлтый, синий, красный, зелёный, розовый")
colour = random.choice(["Жёлтый", "Синий", "Красный", "Зелёный", "Розовый"])
tryagain = True
while tryagain is True:
    your_colour = str(input("Угадайте, из вышеперечисленных цветов, "
                            "тот, который выбрала программа: "))
    if colour == your_colour.title():
        print("Отлично!")
        tryagain = False
    else:
        if colour == "Жёлтый":
            print("Неправильно, держи подсказку!\n ... тюльпаны — вестники "
                  "pазлуки, цвета запоздалой утpенней звезды!")
        elif colour == "Синий":
            print("Неправильно, держи подсказку!\n ... — ... иней лёг "
                  "на провода. В небе тёмно — ... ... звезда.")
        elif colour == "Красный":
            print("Неправильно, держи подсказку!\n Девушки бывают разные"
                  " - черные, белые, ...")
        elif colour == "Зелёный":
            print("Неправильно, держи подсказку!\n И снится нам не рокот "
                  "космодрома,не эта ледяная синева,а снится нам трава, "
                  "трава у дома, ... ... трава.")
        else:
            print("Неправильно, держи подсказку!\n ... розы Светке Соколовой,"
                  " Светке Соколовой, однокласснице моей.")
