# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные ('aaaaabbbcccc') и выходные данные хранятся в отдельных текстовых файлах.

def compressed_fail(path_1, path_2):    # архивирование
    data = open(path_1, 'r')            # чтение данных из файла
    for line in data:
        num_row = list(line)
    data.close()

    compressed_string = ''
    count = 1
    for i in range(len(num_row)-1):
        if num_row[i] == num_row[i+1]:  # считаем количество повторяющихся элементов
            count += 1
        else:                           # если i-тый элемент не совпадает с посчитанными записываем в строку count и предыдущий элемент
            compressed_string = compressed_string + str(count) +  num_row[i-1]
            count = 1
    compressed_string = compressed_string + str(count) +  num_row[-1]   # т.к. мы выпали из цикла до внесения последнего элемента, добавляем его вручную

    with open(path_2, 'w', encoding = 'UTF-8') as f:    # записываем результат в заданный файл (path_2)
        f.write(compressed_string)


def decompressed_fail(path_1, path_2):  # распаковка

    data = open(path_1, 'r')            # чтение из файла
    for line in data:
        num_row = list(line)
    data.close()
    
    decompressed_string = ''
    for i in range(0, len(num_row), 2):
        decompressed_string = decompressed_string + (int(num_row[i]) * num_row[i+1])
    with open(path_2, 'w', encoding = 'UTF-8') as f:    # записываем результат в заданный файл (path_2)
        f.write(decompressed_string)
    

def main():
    compressed_fail('Homework5/input_file.txt', 'Homework5/output_file.txt')
    decompressed_fail('Homework5/output_file.txt', 'Homework5/input_file.txt')

if __name__ == "__main__":     # точка входа
    main()