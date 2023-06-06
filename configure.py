from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from async_payok import AsyncPayok
from async_payok.models import Method, Currency
import asyncio



TOKEN = '6201397926:AAEVqIruMqdy5TmTvRtQ8uR2ueOKtaPtd1o'
#--------------FSM--------------
#------------------------------
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


