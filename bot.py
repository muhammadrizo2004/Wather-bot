from aiogram import Router,Dispatcher,Bot
from aiogram.types import Message
from asyncio import run
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery
from bot1 import get_date
from config import BOT_TOKEN
City=InlineKeyboardMarkup(
    inline_keyboard=[
    [
    InlineKeyboardButton(text='Tashkent',callback_data='Tashkent'),
    InlineKeyboardButton(text='Fergana',callback_data='Fergana'),
    InlineKeyboardButton(text='Andijan',callback_data='Andijan'),
    ],
    [
    InlineKeyboardButton(text='Namangan',callback_data='Namangan'),
    InlineKeyboardButton(text='Qashqadaryo',callback_data='Qashqadaryo'),
    InlineKeyboardButton(text='Samarqand',callback_data='Samarqand'),
    ],
     [
    InlineKeyboardButton(text='Buxoro',callback_data='Buxoro'),
    InlineKeyboardButton(text='Jizzax',callback_data='Jizzax'),
    InlineKeyboardButton(text='Xorazm',callback_data='Urganch'),
    ],
     [
    InlineKeyboardButton(text='Navoiy',callback_data='Navoiy'),
    InlineKeyboardButton(text='Sirdaryo',callback_data='Sirdaryo'),
    InlineKeyboardButton(text='Surxondaryo',callback_data='Termez'),
    ],
    ]
)

greet=Router()
@greet.message(Command(commands=["start"]))
async def funk(msg:Message,bot:Bot):
    await msg.answer("Bu 12 viloyatning ob-havo ma'lumot boti ⛅️",reply_markup=City)

echo_bot=Router()
@echo_bot.callback_query()
async def funk1(call:CallbackQuery):
    city=call.data
    weather=round(get_date(city),2)
    await  call.answer(f"{weather}°C")

async def start_bot():
    dic=Dispatcher()
    tok=Bot(token=BOT_TOKEN)
    dic.include_router(greet)
    dic.include_router(echo_bot)
    try:
        await dic.start_polling(tok)
    except Exception :
        await tok.session.close()    
if __name__=="__main__":
    run(start_bot())