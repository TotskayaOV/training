from random import randint as RI

string = '1 2 3 4 5 6 7 8 12 23 43'
string = list(map(int, string.split()))
# map - применяет функцию ко всем элементам 
# string = string.split()
# for i in range(len(string)):
#     string[i] = int(string[i])
string = list(filter(lambda x: x%2 == 0, string))
# filter - пропускат все через себя и если элемент удовлетворяет условию, то пропускает его
# если в фильтр передается ссылка на функцию, а не лямбда, то () не пишутся, т.к. фильтр проходит по всем элементам "string"
# def odd (x):
#     if x%2 ==0:
#         return x
string = list(map(lambda x: x**2, string))
# def cube(x):
#     return x**2
my_list = [RI(0, 10) for i in range(10) if i%2 == 0]
# my_list = []
# for i in range(10):
#   i = RI(0,10)
#   if i % 2 == 0:
#       my_list.append(i)
print(string)
 
string = '1 2 3 4 5 6 7'
alfabet = 'a b c d e f g'
signs = '! @ # $ %'
string = string.split()
alfabet = alfabet.split()
signs = signs.split()
for i, item in enumerate(string):
# for i, item in enumerate(string, 1): - нумерация начнется с 1
# for i in range(len(string)):
# for item in string:
    print(f'Индекс = {i}, элемент = {item}')
new_list = list(zip(string, alfabet, signs))
# zip работает на длинную минимального списка
print(new_list)

# lambda - возвращаемая, анонимная функция у которой нет имени + она однострочная
# можно использовать в словаре, например
calc = {'Сложение': lambda x, y: x + y} # сложение  - это ключ, лябда значение
print(calc.get('Сложение')(4, 5))