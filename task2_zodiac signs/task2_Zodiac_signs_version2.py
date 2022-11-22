month = input("Введите месяц: ").lower()
number = int(input("Введите число: "))

if (month == "март" and 21 <= number <= 31) or (month == "апрель" and 1 <= number <= 20):
    zodiac = ("овен")

elif (month == "апрель" and 21 <= number <= 30) or (month == "май" and 1 <= number <= 21):
    zodiac = ("телец")

elif (month == "май" and 22 <= number <= 31) or (month == "июнь" and 1 <= number <= 21):
    zodiac = ("близнецы")

elif (month == "июнь" and 22 <= number <= 30) or (month == "июль" and 1 <= number <= 22):
    zodiac = ("рак")

elif (month == "июль" and 23 <= number <= 31) or (month == "август" and 1 <= number <= 21):
    zodiac = ("лев")

elif (month == "август" and 22 <= number <= 31) or (month == "сентябрь" and 1 <= number <= 23):
    zodiac = ("дева")

elif (month == "сентябрь" and 23 <= number <= 30) or (month == "октябрь" and 1 <= number <= 23):
    zodiac = ("весы")

elif (month == "октябрь" and 24 <= number <= 31) or (month == "ноябрь" and 1 <= number <= 22):
    zodiac = ("скорпион")

elif (month == "ноябрь" and 23 <= number <= 30) or (month == "декабрь" and 1 <= number <= 22):
    zodiac = ("стрелец")

elif (month == "декабрь" and 23 <= number <= 31) or (month == "январь" and 1 <= number <= 20):
    zodiac = ("козерог")

elif (month == "январь" and 21 <= number <= 31) or (month == "февраль" and 1 <= number <= 19):
    zodiac = ("водолей")

elif (month == "февраль" and 20 <= number <= 28) or (month == "март" and 1 <= number <= 20):
    zodiac = ("рыбы")

print("Вывод:")
print((zodiac).capitalize())
