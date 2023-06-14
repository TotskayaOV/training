# Напишите программу, удаляющую из текста все слова, содержащие "абв".

my_str = 'АБВ, ылоажы фыыдлх абв? Зщышф вабвв ффлжв абВ'
st_sign = [',', '!', '.', '?']

for c in st_sign:
    my_str = my_str.replace(c, ' ' + c + ' ')

new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))

for c in st_sign:
    new_str = new_str.replace(' ' + c, c)


print(new_str)