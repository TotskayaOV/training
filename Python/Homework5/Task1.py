# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_str = 'Мотя самозабвенно собирал вещи с Аней Абвегедейкой, чтобы уехать в незабвенный Зимбабве "Хараре"'

st_sign = [',', '!', '.', '?']
new_str = ' '.join( map( lambda s: s if "абв" not in s.lower() else s[-1] if s[-1] in st_sign else "", my_str.split() ) )
for c in st_sign:
    new_str = new_str.replace(' ' + c, c).replace('  ', ' ')

print(new_str)