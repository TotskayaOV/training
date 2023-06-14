from create import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
import controller
import modul
import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext, MessageHandler, filters


controller.input_handler(2)
modul.db_list
new_contact = dict()
mark_list = ['lastname', 'firstname', 'phone', 'comment']
user_chois = 0



@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('telephone_directory\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer(f"Добрый день, {message.from_user.full_name}")

@dp.message_handler(commands=['help'])
async def mes_start(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('telephone_directory\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer(f"Для начала работы со справочником напишите /start\nЧтобы увидеть весь список контактов - /show_all\nЧтобы внести новый контакт - /new_contact\nЧтобы изменить существующий контакт введите команду /to_change и порядковый номер контакта через пробел, который вы хотели бы изменить\nЧтобы сохранить изменения -/save_change")


@dp.message_handler(commands=['to_change'])
async def mes_start(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('telephone_directory\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global user_chois
    modul.db_list
    user_input = message.text.split(' ')
    user_chois = int(user_input[1]) -1
    show_string = ''
    for i in modul.db_list[user_chois].values():
        show_string += i + " "
    user_chois = int(user_input[1]) + 1
    await message.answer(f"Будут изменены данные: {show_string}\nВведите фамилию начав со слова Фамилия")

@dp.message_handler(commands=['show_all'])
async def mes_start(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('telephone_directory\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    modul.db_list
    my_string = ''
    for i in range(len(modul.db_list)):
            user_id = i + 1
            my_string += str(user_id) + '.\t'
            for v in modul.db_list[i].values():
                my_string += ''.join(v) +' '
            my_string += '\n'
    await message.answer(my_string)

@dp.message_handler(commands=['change_contact'])
async def mes_start(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('telephone_directory\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer('Введите команду /to_change и номер контакта через пробел, который вы хотели бы изменить')

@dp.message_handler(commands=['new_contact'])
async def mes_start(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('telephone_directory\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer('Введите фамилию начав со слова Фамилия')

@dp.message_handler(commands=['save_change'])
async def mes_start(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('telephone_directory\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global new_contact
    global user_chois
    temp_list = list(new_contact.keys())
    if temp_list == mark_list:
        controller.input_handler(3)
        controller.input_handler(7)
        new_contact = dict()        
        user_chois = 0
        await message.answer('Данные сохранены') 
    else:
        new_contact = dict()        
        user_chois = 0
        await message.answer('Данные введены некорректно. Начните сначала и следуйте инструкциям на экране')


@dp.message_handler()
async def mes_start(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('telephone_directory\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global new_contact
    global mark_list
    global user_chois
    user_string = message.text.split(' ')
    if user_string[0].title() == 'Фамилия':
        new_contact[mark_list[0]] = user_string[1]
        await message.answer('Введите имя начав со слова Имя')
    elif user_string[0].title() == 'Имя':
        new_contact[mark_list[1]] = user_string[1]
        await message.answer('Введите телефон без - и пробелов начав со слова Телефон')
    elif user_string[0].title() == 'Телефон':
        new_contact[mark_list[2]] = user_string[1]
        await message.answer('Введите комментарий: личный или рабочий')
    elif user_string[0] in ['личный', 'рабочий']:
        new_contact[mark_list[3]] = user_string[0]
        prt_string = ''
        for value in new_contact.values():
            prt_string += value + " "
            if user_chois == 0 and len(new_contact) == 4:
                modul.set_gb(new_contact)
            elif user_chois > 0 and len(new_contact) == 4:
                modul.insert_db(user_chois - 1, new_contact)                
        await message.answer(f'вы добавили контакт: {prt_string}')
    else:
        await message.answer('некорректный ввод')
