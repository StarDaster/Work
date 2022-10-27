boys = ["peter", "alex", "john", "arthur", "richard"]
girls = ["kate", "liza", "kira", "emiliya", "trisha"]
boys.sort()
girls.sort()
x = 0
if len(boys) == len(girls):
    print("Идеальные пары:")
    for boy, girl in zip(boys, girls):
        x += 1
        print(f"{x}.", boy.capitalize(), "и", girl.capitalize())
else:
    print("Не равное количество участников и кто-то может остаться без пары")
