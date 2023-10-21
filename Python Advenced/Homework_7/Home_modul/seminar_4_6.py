import os
import random as rnd
import string


def inner_func(extension: str, dir: str = '', min_size: int = 6, max_size: int = 30,
               min_count: int = 256, max_count: int = 4096, file_count: int = 42):
    letters = string.ascii_lowercase

    if dir:
        if not os.path.isdir(dir):
            os.mkdir(dir)

    for _ in range(file_count):
        name_size = rnd.randint(min_size, max_size)
        name = rnd.choices(letters, k=name_size)
        name = ''.join(name)

        if os.path.isfile(os.path.join(dir, name + extension)):
            x = 1
            while os.path.isfile(os.path.join(dir, name + f'_{x}' + extension)):
                x += 1
            file_name = name + f'_{x}' + extension
        else:
            file_name = ''.join(name) + extension

        rnd_size = rnd.randint(min_count, max_count)
        data = rnd.randbytes(rnd_size)

        with open(os.path.join(dir, file_name), 'wb') as file:
            file.write(data)


def func_new_files(extensions: tuple[str], dir: str = '', file_count: int = 1):
    for _ in range(file_count):
        extension = rnd.choice(extensions)
        inner_func(extension, dir=dir, file_count=file_count)


if __name__ == '__main__':
    func_new_files(('.txt', '.bmp', '.jpg', '.mp3'), 'bin2', 20)
