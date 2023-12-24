# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from Home_modul import number_to_file, write_names_to_file, combining_func, func_new_files, sorted_func, rename_files



if __name__ == '__main__':
    number_to_file('text_seminar.txt', 8)
    write_names_to_file('name_seminar.txt', 10)
    combining_func()
    func_new_files(('.txt', '.bmp', '.jpg', '.mp3'), 'bin', 20)
    sorted_func('bin')
    rename_files(3, '.txt', [1, 3], 'check', 'bin\documents')
