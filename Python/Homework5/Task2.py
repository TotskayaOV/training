# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random
# Фразы, повторяющиеся больше 2 раз, уберем в функции.
def Bot_M(count, move):
    return(f'На столе {count} конфет. Я возьму {move}.')
    
def Player_M(count, name):
    return(f'На столе {count} конфет. {name.title()}, сколько ты возьмешь конфет?\nВведите количество: ')
    
def Bot_Win():
    return('Больше конфет не осталось! Я выиграл!')

def Rules_Game(x, y):
    return(f'На столе лежит {x} конфет. Можно взять от 1 до {y} конфет. Тот кто берет последнюю конфету, забирает их все.\n')

def Input_Error():
    print('Ошибка ввода. Запустите игру сначала.')

# Не смогла встроить защиту от дурака в цикл внутри цикла и вынесла ввод в функцию
def fool_proof(x, y, z):
    valid = False
    while valid == False:
        num = input(Player_M(x, y))
        try:
            num = int(num)
            if 0 < num <= z: valid = True                                               
            else:
                print(f"Некорректный ввод. Нужно ввести число цифрами от 1 до {z}.")
                continue
        except:
            print(f"Некорректный ввод. Нужно ввести число цифрами от 1 до {z}.")
            continue
    return num

# Сразу же вынесла такую же защиту на ввод данных для противника и сложности
def violation_terms(num):
    valid = False
    if num == 1:
        min_num = 0
        max_num = 1
        keyword_phrase = f'Ты будешь играть со мной или с другим игроком?\nЕсли будете играть с компьютером введите {min_num}, если с игроком - {max_num}: '
    else:
        min_num = 1
        max_num = 2
        keyword_phrase = f'Выбери уровень сложности: {min_num} - легкий, {max_num} - сложный: '        
    while valid == False:
        result = input(keyword_phrase)
        try:
            result = int(result)
            if (min_num - 1) < result < (max_num + 1): valid = True
            else:
                print(f"Некорректный ввод. Нужно ввести число {min_num} или {max_num}.")
                continue
        except:
            print(f"Некорректный ввод. Нужно ввести число {min_num} или {max_num}.")
            continue
    return result


candies = 252
max_step = 28
name_player = input('Привет! Как тебя зовут?\nВведите имя: ').lower()
opponent_player = violation_terms(1)
    

# Игра с другим игроком
if opponent_player == 1:
    name_player2 = input('Привет! Как зовут второго игрока?\nВведите имя: ').lower()
    print(Rules_Game(candies, max_step))
    
    while candies != 0:
        player1_move = fool_proof(candies, name_player, max_step)
        candies = candies - player1_move
        
        if candies == 0:
                print(f'Выиграл игрок {name_player.title()}!')
                break        
        elif candies < max_step + 1:
            max_step = candies      # Изменяем значение переменной для корректного отображения цифр в функции fool_proof
        else:
            player2_move = fool_proof(candies, name_player2, max_step)
            candies = candies - player2_move
            if candies == 0:
                print(f'Выиграл игрок {name_player2.title()}!')
                break
 

# Игра с ботом. Пользователь выбирает уровень сложности. 
elif opponent_player == 0:
    difficulty_level = violation_terms(2)
    first_move = candies - (candies // (max_step + 1)) * (max_step + 1)
    after_candies = candies - first_move

# Легкий использует рандом, когда берет конфеты
    if difficulty_level == 1:
        print(f'{Rules_Game(candies, max_step)}Я хожу первым! Возьму ка я {first_move} конфет.')
        
        while after_candies != 0:
            player1_move = fool_proof(after_candies, name_player, max_step)
            after_candies = after_candies - player1_move
            
            if player1_move < (max_step + 1) and after_candies == 0:
                    print('Для меня не осталось конфет :( Ты выиграл!')
                    break
            elif after_candies > (max_step + 1):
                bot_move = random.randint(1, max_step)
                print(Bot_M(after_candies, bot_move))
                after_candies = after_candies - bot_move
                if after_candies < max_step:
                    max_step = after_candies    # Изменяем значение переменной для корректного отображения цифр в функции fool_proof
            elif after_candies == 1:
                print(Bot_M(after_candies, after_candies) + ' ' + Bot_Win())
                break
            elif after_candies < (max_step + 1) and after_candies != 1:
                max_step = after_candies        # Изменяем значение переменной для корректного отображения цифр в функции fool_proof
                bot_move = random.randint(1, max_step)
                print(Bot_M(after_candies, bot_move))
                after_candies = after_candies - bot_move
                if after_candies == 0:
                    print(Bot_Win())
                    break
           
# При сложном уровне выиграть у бота нельзя.
    elif difficulty_level == 2:
        print(f'{Rules_Game(candies, max_step)}Я хожу первым! Возьму ка я {first_move} конфет.')
        
        while after_candies != 0:
            player1_move = fool_proof(after_candies, name_player, max_step)
            after_candies = after_candies - player1_move
            
            if after_candies >= (max_step + 1):
                bot_move = (max_step + 1) - player1_move
                print(Bot_M(after_candies, bot_move))
                after_candies = after_candies - bot_move
            else:
                print(Bot_M(after_candies, after_candies) + ' ' + Bot_Win())
                break

input()   # Чтоб не закрывалось