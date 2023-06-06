from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from configure import dp, bot

@dp.message_handler(text='🏷️Товары')
async def menu_products(message):
    btnDiscord = KeyboardButton('🌞Discord')
    btnMenu = KeyboardButton('📋 Главное меню')
    MainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDiscord, btnMenu)
    await bot.send_message(message.chat.id, "Выберите категорию", reply_markup=MainMenu)
@dp.message_handler(text='🌞Discord')
async def discord_if(message):
    if message.text == '🌞Discord':
        from discord_products import buy_discord_menu
        await buy_discord_menu(message) 
    else:
        menu_if(message)
@dp.message_handler(text='📋 Главное меню')
async def menu_if(message):
    if message.text == '📋 Главное меню':  # Используем "elif" вместо "if"
       from main import command_start
       await command_start(message)

