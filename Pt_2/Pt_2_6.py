distance = float(input("Сколько километров хотите проехать на автомобиле: "))
consumption = float(input("Сколько литров топлива"
                          " расходует автомобиль на 100 километров: "))
quantity = float(input("Сколько литров топлива в вашем баке: "))
if 100 * quantity / consumption < distance:
    print("Вам не хватит топлива чтобы проехать данную дистанцию")
else:
    print("Вы проедите данную дистанцию")


