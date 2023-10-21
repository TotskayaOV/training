import random as rnd

L_LIMIT = -1000
H_LIMIT = 1000


def number_to_file(filename: str, lines: int):
    file = open(filename, 'a', encoding='UTF-8')
    for _ in range(lines):
        a = rnd.randint(L_LIMIT, H_LIMIT)
        b = rnd.uniform(L_LIMIT, H_LIMIT)
        file.write(f'{a} | {b}\n')
    file.close()

if __name__ == '__main__':
    number_to_file('text_seminar.txt', 8)
