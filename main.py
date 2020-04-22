import asyncio
import uvloop
import logging
from aiogram import Bot, Dispatcher, executor, types

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

API_TOKEN = '1248027386:AAG5YIRpzvZsPhsis0A1C_qCpdwengXH5Iw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['save'])
async def send_welcome(message: types.Message):
    await message.reply("Wow!\nAre you going to save your routines!\nChoose the kind of routines.")
    await show_choose_excercise_keyboard(message)

@dp.message_handler(commands=['stats'])
async def send_welcome(message: types.Message):
    await message.reply("I will show your achivements!")

root_menu_data = ["Push Ups", "Crunches"]


async def show_choose_excercise_keyboard(message):
    choose_excercise = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text='Push Ups'),
                                                            types.KeyboardButton(text='Crunches')], ],
                                                 one_time_keyboard=True,
                                                 resize_keyboard=True)

    await bot.send_message(message.chat.id, text="Wow!\nAre you going to save your routines!\n"
                                                 "Choose the kind of routines.", reply_markup=choose_excercise)



@dp.message_handler(regexp="Push Ups")
async def register_push_ups(message: types.Message):
    await message.reply("How many push ups?")

@dp.message_handler(regexp="Crunches")
async def register_crunches(message: types.Message):
    await message.reply("How many Crunches?")

@dp.message_handler(regexp=\d)
async def echo(message: types.Message):
    await message.answer("Registered!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)