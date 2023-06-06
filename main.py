from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from configure import bot, dp
import urllib.parse
from async_payok import PayOk
from async_payok.models import Method, Currency
import asyncio


@dp.message_handler(commands=['start'])
async def command_start(message):
    await bot.send_message(message.from_user.id, 'Привет @{0.username}!'.format(message.from_user))
    await menu(message)
@dp.message_handler(text='📋 Главное меню')
async def menu(message):
    btnProducts = KeyboardButton('🏷️Товары')
    btnChat = KeyboardButton('💭Чат')
    btnRules = KeyboardButton('🫡Правила')
    btnProfile = KeyboardButton('🐥Профиль')
    MainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnProducts, btnChat, btnRules, btnProfile)
    await bot.send_message(message.chat.id, "📋 Главное меню", reply_markup=MainMenu)

@dp.message_handler(text='🏷️Товары')
async def products_if(message):
    from markups import menu_products
    await menu_products(message)  # Вызов функции menu_command_products
@dp.message_handler(text='💭Чат')
async def chat_if(message):
    await bot.send_message(message.chat.id, "😎Наш чат крутых людей - @SecretShop_chat")

async def get_balance():
    payok = PayOk(token2='3738EF1646FA8DA742A6EA7703297951-AB8C5C446C50D3ECB0BAD0BAC67D7B85-6040B303915AFF9ED95C045C36504258', secret_key='50e9b7124a6a281210b4697188ad92a0')
    balance = await payok.getBalance()
    try:
        # Вызов метода API для получения баланса
        balance = await payok.getBalance()
        print(f"Баланс пользователя: {balance}")
    except Exception as e:
        print(f"Ошибка при получении баланса: {e}")
loop = asyncio.get_event_loop()
loop.run_until_complete(get_balance())

@dp.message_handler(text='🐥Профиль')
async def profile_if(message):
    buy_button = types.InlineKeyboardButton('💳 Пополнить баланс: 100', url="https://payok.io/payment_link/m29dy-b33f5-n66q0")
    menu = InlineKeyboardMarkup().add(buy_button)
    await bot.send_message(message.chat.id, f'📱 Ваш профиль:\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n🔑 Мой ID: {message.from_user.id}\n👤 Логин: @{message.from_user.username}\n 🕜 Регистрация: хуйню сюда\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n💳 Баланс: {PayOk.getBalance()} n💵 Всего пополнено: 0руб\n🎁 Куплено товаров: 0шт\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⛓ Кол-во рефералов: 0\n 💵 Заработано на рефералах: 0',reply_markup=menu, parse_mode=types.ParseMode.HTML)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
