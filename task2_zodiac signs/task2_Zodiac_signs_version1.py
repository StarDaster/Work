month = input("Введите месяц: ").lower()
number = int(input("Введите число: "))

if month == ("май").lower():
    zodiac = "телец" if 1 <= number <= 21 else "близнецы"

elif month == ("июнь").lower():
    zodiac = "близнецы" if 1 <= number <= 21 else "рак"

elif month == ("июль").lower():
    zodiac = "рак" if 1 <= number <= 22 else "лев"

elif month == ("август").lower():
    zodiac = "лев" if 1 <= number <= 21 else "дева"

elif month == ("сентябрь").lower():
    zodiac = "дева" if 1 <= number <= 23 else "весы"

elif month == ("октябрь").lower():
    zodiac = "весы" if 1 <= number <= 23 else "скорпион"

elif month == ("ноябрь").lower():
    zodiac = "скорпион" if 1 <= number <= 22 else "стрелец"

elif month == ("декабрь").lower():
    zodiac = "стрелец" if 1 <= number <= 22 else "козерог"

elif month == ("январь").lower():
    zodiac = "козерог" if 1 <= number <= 20 else "водолей"

elif month == ("февраль").lower():
    zodiac = "водолей" if 1 <= number <= 19 else "рыбы"

elif month == ("март").lower():
    zodiac = "рыбы" if 1 <= number <= 20 else "овен"

elif month == ("апрель").lower():
    zodiac = "овен" if 1 <= number <= 20 else "телец"

print("Вывод:")
print((zodiac).capitalize())
