from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from async_payok import AsyncPayok
from async_payok.models import Method, Currency
import asyncio



TOKEN = '6295999138:AAGDf_5qz3wJx5oaBtpjZxLV1BQzduWF5mE'
#--------------FSM--------------
#------------------------------
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


