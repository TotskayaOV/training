# Создайте программу для игры в ""Крестики-нолики"".
import tkinter

def run_game():
    valid = False
    while valid == False:
        result = input('С кем ты будешь играть? 1 - компьютер, 2 - другой игрок\nВведите цифру: ')
        try:
            result = int(result)
            if 0 < result < 3: valid = True                                               
            else:
                print('Ошибка ввода. Введите или 1 или 2')
                continue
        except:
            print('Ошибка ввода. Введите цифру')
            continue
        print('Игра началась!')
        return result

def table_drawing(table_fields):
    print("-------------")
    for i in range(3):
        print("|", table_fields[0 + i * 3], "|", table_fields[1 + i * 3], "|", table_fields[2 + i * 3], "|")
        print("-------------")

# Проверка бота на возможную победу
def win_botsstep(sign):
    result = 0
    count = 0        
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    while count < 1:
        for each in win_coord:
            if str(table_fields[each[0]]) == str(table_fields[each[1]]) == "x" and (str(table_fields[each[2]]) not in "xo"):
                    table_fields[each[2]] = sign
                    result = table_fields[each[2]]                
                    break
            elif str(table_fields[each[0]]) == str(table_fields[each[2]]) == "x" and (str(table_fields[each[1]]) not in "xo"):
                    table_fields[each[1]] = sign
                    result = table_fields[each[1]]
                    break
            elif str(table_fields[each[1]]) == str(table_fields[each[2]]) == "x" and (str(table_fields[each[0]]) not in "xo"):
                    table_fields[each[0]] = sign
                    result = table_fields[each[0]]
                    break
            count += 1
    return result

#Если победа невозможна запускается эта функция
def self_botsstep(sign):
    opp_coord = ((0,1,2), (6,7,8),(0,3,6),(2,5,8), (0,7,5), (2,7,3), (6,1,5), (1,3,8))     
    for each in opp_coord:
        if str(table_fields[each[0]]) == str(table_fields[each[1]]) == "o":
            table_fields[each[2]] = sign
            result = table_fields[each[2]]
            break
        elif str(table_fields[each[0]]) == str(table_fields[each[2]]) == "o":
            table_fields[each[1]] = sign     
            result = table_fields[each[1]]                   
        elif str(table_fields[each[1]]) == str(table_fields[each[2]]) == "o":
            table_fields[each[0]] = sign
            result = table_fields[each[0]]
    return result


def bot_step(x, sign):
    if x == 0:
        table_fields[5-1] = sign
    elif x == 2:
        opp_coord = ((0,1,2), (6,7,8),(0,3,6),(2,5,8), (1, 2, 5), (3, 8, 7))
        for each in opp_coord:
            if "o" == str(table_fields[each[0]])  or str(table_fields[each[2]]) == "o":
                table_fields[each[1]] = sign
                break
    elif x > 2:
        result = win_botsstep(sign)
        if type(result) != str:
            result = self_botsstep(sign)
            return result
        else:
            return result                            
 
    
def checking_field(table_fields):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if table_fields[each[0]] == table_fields[each[1]] == table_fields[each[2]]:
            return table_fields[each[0]]
    return False

def take_input(player_move):
    valid = False
    while not valid:
        player_answer = input(f'Куда поставим {player_move}?\nВведите номер клетки поля: ')
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Нужно ввести число цифрой.")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(table_fields[player_answer-1]) not in "xo"):
                table_fields[player_answer-1] = player_move
                valid = True
            else:
                print("Эта клетка уже занята, выберите другую")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

def main(table_fields):
    mb_bot = run_game()
    exit_number = 0
    win = False
    while not win:
        table_drawing(table_fields)
        if exit_number % 2 == 0:
            if mb_bot == 1:
                bot_step(exit_number, "x")
            else:
                take_input("x")
        else:
            take_input("o")
        exit_number += 1
        if exit_number > 4:
            temp = checking_field(table_fields)
            if temp:
                print(f'{temp}-ики, выиграл!')
                win = True
                break
        if exit_number == 9:
            print('Ничья')
            break
    table_drawing(table_fields)

table_fields = list(range(1,10))

if __name__ == "__main__":     # точка входа
    main(table_fields)

input()