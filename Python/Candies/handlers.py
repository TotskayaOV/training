from create import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
import emoji
from random import randint
from kb_candies import kb_main_menu
import datetime

total = 200
difficulty_level = 1
max_step = 28



@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Candies\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer(f'Привет, {message.from_user.full_name}. Ты садишься за стол "Battle for Candy!"', reply_markup=kb_main_menu)

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Candies\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer('/rules - правила игры\n/set новое количество - изменить количество конфет лежащих на столе\n/step новое количество - изменить коичество конфет, которое можно взять за ход\n/difficult - поставить уровень сложности выше')

@dp.message_handler(commands=['rules'])
async def mes_rules(message: types.Message):
    global total
    global max_step   
    await message.answer(f'На столе лежит {total} конфет.  За один ход можно забрать не более чем {max_step} конфет. Все конфеты оппонента достаются сделавшему последний ход.\nЕсли хочешь изменить количество конфет лежащих на столе, то напиши /set новое количество конфет\nЕсли хочешь изменить максимальное количество конфет, которое можно взять, то напиши /step новое количество конфет.\nЕсли стало скучно играть, то поставь уровень повыше, написав /difficult')

# Изменение уровня сложности
@dp.message_handler(commands=['difficult'])
async def mes_dif(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Candies\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global difficulty_level
    global total
    global max_step
    bot_step = total//(max_step + 1)
    total -= bot_step
    difficulty_level = 2
    await message.answer(emoji.emojize(f'Установлен высокий уровень сложности :thumbsup:. Я возьму {bot_step} :candy:, осталось {total} :candy:', language='alias'))

# Изменения изначальных установок
@dp.message_handler(commands=['step'])
async def mes_step(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Candies\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global total
    global max_step
    if len(message.text.split()) < 2:
        await message.answer(f'Ошибка в команде. Напиши /step и число. Например /step 20')
    else:
        temp = int(message.text.split()[1])
        if temp > 2:
            max_step = temp
            await message.answer(f'Теперь можно взять максимум {max_step} конфет за ход.')
        else:
            await message.answer(emoji.emojize('Слишком мало конфет. Это не серьезно :baby_chick:', language='alias'))

@dp.message_handler(commands=['set'])
async def mes_settings(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Candies\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global total
    if len(message.text.split()) < 2:
        await message.answer(f'Ошибка в команде. Напиши /set и число. Например /set 100')
    else:
        count = int(message.text.split()[1])
        if count > 29:
            total = count
            await message.answer(emoji.emojize(f'Количество конфет установлено {total} :candy:.', language='alias'))
        else:
            await message.answer(emoji.emojize('Слишком мало конфет. Это не серьезно :baby_chick:', language='alias'))

@dp.message_handler(text=['Бла'])
async def mes_start(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Candies\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer('Бла бла бла')

@dp.message_handler()
async def mes_all(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Candies\TestBot.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global total
    global max_step
    if message.text.isdigit():
        global difficulty_level
        if max_step < int(message.text):
            await message.answer(emoji.emojize(f'Не хулигань! :disappointed_face: Можно взять максимум {max_step} конфет', language='alias'))
        elif difficulty_level == 1:
            temp_total = total - int(message.text)
            if temp_total == 0:
                await message.answer(emoji.emojize('Для меня не осталось конфет :disappointed_face: Ты выиграл!:fireworks:', language='alias'))
                total = 200
                difficulty_level = 1
                max_step = 28
            elif temp_total > max_step:
                bot_step = randint(1, max_step)
                total = temp_total - bot_step
                await message.answer(emoji.emojize(f'Осталось {temp_total} :candy:. Я возьму {bot_step} :candy:. На столе осталось {total} :candy:', language='alias'))
            else:
                bot_step = randint(1, temp_total+1)
                total = temp_total - bot_step
                if total == 0:
                    await message.answer(emoji.emojize(f'Осталось {temp_total} конфет. Я возьму {bot_step}. Я выиграл :cowboy_hat_face:', language='alias'))
                    total = 200
                    difficulty_level = 1
                    max_step = 28
                else:
                    await message.answer(f'Осталось {temp_total} конфет. Я возьму {bot_step}. На столе осталось {total} конфет')
        elif difficulty_level == 2:
            temp_total = total - int(message.text)
            if temp_total == 0:
                await message.answer(emoji.emojize('Для меня не осталось конфет :disappointed_face: Ты выиграл!:fireworks:', language='alias'))
                total = 200
                difficulty_level = 1
                max_step = 28
            elif temp_total > max_step:
                bot_step = (max_step + 1) - int(message.text)
                total = temp_total - bot_step
                await message.answer(emoji.emojize(f'Осталось {temp_total} :candy:. Я возьму {bot_step} :candy:. На столе осталось {total} :candy:', language='alias'))
            else:
                bot_step = temp_total
                await message.answer(emoji.emojize(f'Осталось {temp_total} конфет. Я возьму {bot_step}. Я выиграл :cowboy_hat_face:', language='alias'))
                total = 200
                difficulty_level = 1
                max_step = 28
    else:
         await message.answer('Чтобы вызвать помощь, введите /help')
