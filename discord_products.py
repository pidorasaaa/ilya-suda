
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from configure import bot, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import urllib.parse

@dp.message_handler(text="🌞Discord")
async def buy_discord_menu(message):
    discord1 = KeyboardButton('🎁Nitro Full QR-COD [1 month]')
    discord2 = KeyboardButton('🎁Nitro Full QR-COD [1 Year]')
    discord3 = KeyboardButton('🎁Nitro Classic QR-COD [1 month]')
    discord4 = KeyboardButton('🎁Nitro Classic QR-COD [1 Year]')
    discord_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(discord1, discord2, discord3, discord4)
    await bot.send_message(message.chat.id, "Выберите товар", reply_markup=discord_menu)
@dp.message_handler(text='🎁Nitro Full QR-COD [1 month]')
async def buy_discord_if(message):
    await buy_discord_menu12(message)
@dp.message_handler(text='🎁Nitro Full QR-COD [1 Year]')
async def buy_discord_if2(message):
    await buy_discord_menu22(message)
@dp.message_handler(text='🎁Nitro Classic QR-COD [1 month]')
async def buy_discord_if3(message):
    await buy_discord_menu32(message)
@dp.message_handler(text='🎁Nitro Classic QR-COD [1 Year]')
async def buy_discord_if4(message):
    await buy_discord_menu42(message)

async def buy_discord_menu12(message):
    buy_button = KeyboardButton('💳 Купить')
    menu_button = KeyboardButton('📋 Главное меню')
    back_button = KeyboardButton('↩️ Назад')
    BuyDiscord1 = ReplyKeyboardMarkup(resize_keyboard=True).add(buy_button, menu_button, back_button)
    await bot.send_message(message.chat.id, "Выберите товар", reply_markup=BuyDiscord1)
@dp.message_handler(text='💳 Купить')
async def buy_discord_1(message):
    url = "t.me/rainytinker"
    product_name = 'Название товара'
    product_description = 'Описание товара'
    product_price = 10  # Цена товараt.me/rainytinker
    buy_button = types.InlineKeyboardButton('💳 Купить',url="t.me/rainytinker")
    menu = InlineKeyboardMarkup().add(buy_button)
    text = f"<b>{product_name}</b>\n\n{product_description}\n\nЦена: {product_price} рублей"
    await bot.send_message(message.chat.id, text, reply_markup=menu, parse_mode=types.ParseMode.HTML)



@dp.message_handler(text='🎁Nitro Full QR-COD [1 Year]')
async def buy_discord_menu22(message):
    buy_button = KeyboardButton('💳 Купить')
    menu_button = KeyboardButton('📋 Главное меню')
    back_button = KeyboardButton('↩️ Назад')
    BuyDiscord1 = ReplyKeyboardMarkup(resize_keyboard=True).add(buy_button, menu_button, back_button)
    await bot.send_message(message.chat.id, "Выберите товар", reply_markup=BuyDiscord1)
@dp.message_handler(text='💳 Купить')
async def buy_discord_2(message):
    url = "t.me/rainytinker"
    product_name = 'Название товара'
    product_description = 'Описание товара'
    product_price = 10  # Цена товараt.me/rainytinker
    buy_button = types.InlineKeyboardButton('💳 Купить',url="t.me/rainytinker")
    menu = InlineKeyboardMarkup().add(buy_button)
    text = f"<b>{product_name}</b>\n\n{product_description}\n\nЦена: {product_price} рублей"
    await bot.send_message(message.chat.id, text, reply_markup=menu, parse_mode=types.ParseMode.HTML)



@dp.message_handler(text='🎁Nitro Classic QR-COD [1 month]')
async def buy_discord_menu32(message):
    buy_button = types.InlineKeyboardButton('💳 Купить', callback_data='button3')
    menu_button = types.InlineKeyboardButton('📋 Главное меню', callback_data='button3')
    back_button = types.InlineKeyboardButton('↩️ Назад↩️', callback_data='button3')
    BuyDiscord1 = ReplyKeyboardMarkup(resize_keyboard=True).add(buy_button, menu_button, back_button)
    await bot.send_message(message.chat.id, "Выберите товар", reply_markup=BuyDiscord1)
@dp.message_handler(text='💳 Купить')
async def buy_discord_3(message):
    url = "t.me/rainytinker"
    product_name = 'Название товара'
    product_description = 'Описание товара'
    product_price = 10  # Цена товараt.me/rainytinker
    buy_button = types.InlineKeyboardButton('💳 Купить',url="t.me/rainytinker")
    menu = InlineKeyboardMarkup().add(buy_button)
    text = f"<b>{product_name}</b>\n\n{product_description}\n\nЦена: {product_price} рублей"
    await bot.send_message(message.chat.id, text, reply_markup=menu, parse_mode=types.ParseMode.HTML)



@dp.message_handler(text='🎁Nitro Classic QR-COD [1 Year]')
async def buy_discord_menu42(message):
    buy_button = KeyboardButton('💳 Купить')
    menu_button = KeyboardButton('📋 Главное меню')
    back_button = KeyboardButton('↩️ Назад')
    BuyDiscord1 = ReplyKeyboardMarkup(resize_keyboard=True).add(buy_button, menu_button, back_button)
    await bot.send_message(message.chat.id, "Выберите товар", reply_markup=BuyDiscord1)
@dp.message_handler(text='💳 Купить')
async def buy_discord_4(message):
    url = "t.me/rainytinker"
    product_name = 'Название товара'
    product_description = 'Описание товара'
    product_price = 10  # Цена товараt.me/rainytinker
    buy_button = types.InlineKeyboardButton('💳 Купить',url="t.me/rainytinker")
    menu = InlineKeyboardMarkup().add(buy_button)
    text = f"<b>{product_name}</b>\n\n{product_description}\n\nЦена: {product_price} рублей"
    await bot.send_message(message.chat.id, text, reply_markup=menu, parse_mode=types.ParseMode.HTML)

