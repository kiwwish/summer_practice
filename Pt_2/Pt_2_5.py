import random
score = 0
win = 0
loss = 0
while score < 3:
    player = int(input("Введите 0, если хотите выбрать орла или 1,"
                       " если хотите выбрать решку: "))

    if player != 0 and player != 1:
        print("Вы ввели не то число.")
        break

    program = random.choice([0, 1])
    if player == program:
        win = win + 1
        score = 0
        print("Вы выиграли!")

    else:
        loss = loss + 1
        score = score + 1
        print("Вы проиграли!")

    print("Количество выиграшей составляет ", win, " раз(а), а проигрышей ,",
          loss, " раз(а)")
    print()
print("Игра окончена!")
