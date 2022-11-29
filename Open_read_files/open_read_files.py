from pprint import pprint
import operator
import os

print("Задание 3")


def get_info_and_writing_to_list(file_names):
    my_data_list = []
    for file in file_names:
        with open(file, encoding='utf-8') as f:
            lines = f.read().splitlines()
            my_data_list.append([file, len(lines)])
            my_data_list[len(my_data_list) - 1] += lines
    my_data_list.sort(key=len)
    return my_data_list


def writing_info_to_file(my_data, my_file):
    with open('result.txt', 'w', encoding='utf-8') as f:
        for file in my_data:
            for elem in file:
                f.write(f'{elem}\n')
    file_path = os.path.join(os.getcwd(), my_file)
    return file_path


print(writing_info_to_file(get_info_and_writing_to_list(['1.txt', '2.txt', '3.txt']), 'result.txt'))
print("\nВсе решение в файле result")
