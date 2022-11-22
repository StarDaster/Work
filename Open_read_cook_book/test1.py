"""
file_object = open("open_read_cook_book — копия.txt", "r", encoding="utf-8")
# Шаг 2 - Выполнить работу (пока читаем файл)
data = file_object.read()
print(data)
# Шаг 3 - Закрыть файл
file_object.close()"""

a = 6104
b = 0
c = "//"
c = str(c)
if (a / b) or (b / a) or (b / b):
    print("На ноль делить нельзя!")
if (a + a) or (a * a) or (a / a) or (a - a):
    print(a)
if (a / c):
    print("Неверная операция")
