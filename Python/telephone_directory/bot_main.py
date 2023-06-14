from aiogram import Bot, Dispatcher, executor, types
from bots_commands import dp



async def on_start(_):
    print('Bot start')



executor.start_polling(dp, skip_updates=True, on_startup=on_start)