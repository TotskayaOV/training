from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import view
from compute import compute2
from user_input import *


heap = {
    'count': 0,
    'first': None,
    'second': None,
    'operator': None
}

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Для того, чтобы начать, введите /start, после введите отдельными сообщениями первое число, второе число и опернад (+, -, *, /)')

async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if heap['count'] != 0:
        if heap['count'] == 1:
            heap['first'] = update.message.text
            heap['count'] += 1
        elif heap['count'] == 2:
            heap['second'] = update.message.text
            heap['count'] +=1
        elif heap['count'] == 3:
            heap['operator'] = update.message.text
            a, b = inp(heap['first'], heap['second'])
            await update.message.reply_text(f"{a} {heap['operator']} {b} = {compute2(a,b, heap['operator'])}")
            heap['count'] = 0
            heap['first'] = None
            heap['second'] = None
            heap['operator'] = None
           
async def startcalc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    heap ['count'] = 1
    print('Start Bot')

app = ApplicationBuilder().token("").build()
app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("start", startcalc))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

app.run_polling()