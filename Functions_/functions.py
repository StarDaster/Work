# Список. Каталог документов
documents = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    "name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}]
# Словарь. Перечень полок, на которых находятся документы
directories = {"1": ["2207 876234", "11-2"], "2": ["10006"], "3": []}

print("\nРабота с архивом!")


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
def people_document(arg_number):
    for doc_number in documents:
        if doc_number["number"] == arg_number:
            print("Владелец документа: ", doc_number["name"])
            break
    else:
        print("Внимание! Такого документа - нет в архиве.")


# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
def list_documents():
    for document in documents:
        print(' {} "{}" "{}" '.format(document["type"], document["number"],
                                      document["name"]))


# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
def shelf_number(arg_number):
    shelf_break = False
    for shelf_directory in directories.items():
        for doc_number in shelf_directory[1]:
            if doc_number == arg_number:
                print("Данный документ находится на полке - ", shelf_directory[0])
                shelf_break = True
                break
        if shelf_break == True:
            break
    else:
        print("Внимание! Документа нет на полке.")


# a – add – команда, которая добавит новый документ в каталог и в перечень полок,
# спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
def add_new_document(agr_type, arg_number, arg_name, arg_dir_number):
    if int(arg_dir_number) == 1 or int(arg_dir_number) == 2 or int(
            arg_dir_number) == 3:
        documents.append({
            "type": agr_type,
            "number": arg_number,
            "name": arg_name
        })
        directories[arg_dir_number].append(arg_number)
        print("\n Ваш документ добавлен в Архив!")
    else:
        print("\n Внимание! Такой полки не существует.")


# Вывести имена всех владельцев документов.
# С помощью исключения KeyError проверить, есть ли поле "name" и "number".
def print_name(arg_key):
    for document in documents:
        try:
            if arg_key == "name" and document[arg_key]:
                print(' {} - "{}" '.format(document[arg_key], document["number"]))
            elif arg_key == "number" and document[arg_key]:
                print(' {} - "{}" '.format(document['name'], document[arg_key]))
            else:
                print("{}".format(document[arg_key]))
        except KeyError:
            print("Внимание!!! Введенный Ключ не найден.")


# Печать архива
def print_document_from_archive():
    print("\nКаталог документов.")
    for document in documents:
        print(' {0} "{1}" "{2}" '.format(document["type"], document["number"],
                                         document["name"]))

    print("\nПеречень полок, на которых находятся документы.")
    for num_shelf, doc_num in directories.items():
        print("Полка №", num_shelf, doc_num)


# Основное меню для запуска команд
def main_menu():
    while True:
        command = input("\n \
    Выберете одну из команд: p, l, s, a, \n \
    Для выхода наберите: exit или e или quit или q \n \
    Для вызова справки наберите: help или h или ? \n \
    Введите команду: ")
        if command == "p":
            people_document(input("\nВведите номер документа:"))
        elif command == "l":
            list_documents()
        elif command == "s":
            shelf_number(input("\nВведите номер документа:"))
        elif command == "a":
            add_new_document(
                input("\nВведите тип документа (passport,invoice,insurance...):"),
                input("Введите номер документа: "), input("Введите имя: "),
                input("Введите номер полки (1, 2, 3): "))
            print_document_from_archive()
        elif command == "exit" or command == "e":
            print("Good luck see latter:)")
            break
        elif command == "quit" or command == "q":
            print("Good luck see latter:)")
            break
        elif command == "help" or command == "h":
            print("\n \
    p – команда, которая по номеру документа выведет имя, владельца;\n \
    l – команда, которая выведет список всех документов;\n \
    s – команда, которая по номеру документа выведет номер полки, на которой он находится;\n \
    a – команда, которая добавит новый документ в архив;\n \
")
        elif command == 'help' or command == "?":
            print("\n \
    p – команда, которая по номеру документа выведет имя, владельца;\n \
    l – команда, которая выведет список всех документов;\n \
    s – команда, которая по номеру документа выведет номер полки, на которой он находится;\n \
    a – команда, которая добавит новый документ в архив;\n \
")
        else:
            print("Такой команды нет, только те команды, которые есть в списке.")


main_menu()
