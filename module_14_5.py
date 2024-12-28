from  aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import os
import crud_functions2

api = ('7819580953:AAFuBzeAWszkwBhhQ8u7633eTAqhZtrZLUw')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')
kb.row(button1, button2)
kb.add(button3, button4)

inline = InlineKeyboardMarkup()
inl_but1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inl_but2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline.row(inl_but1, inl_but2)

inline_products = InlineKeyboardMarkup()
inl_pr1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
inl_pr2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
inl_pr3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
inl_pr4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
inline_products.row(inl_pr1, inl_pr2, inl_pr3, inl_pr4)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

@dp.message_handler(text = ['Регистрация'])
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state = RegistrationState.username)
async def set_username(message, state):
    await state.update_data(username=message.text)
    if not crud_functions2.is_included(message.text):
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()

@dp.message_handler(state = RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state = RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    crud_functions2.add_user(data["username"], data["email"], int(data["age"]))
    await message.answer('Регистрация прошла успешно')
    await state.finish()

@dp.message_handler(text = ['Купить'])
async def get_buying_list(message):
    lst_photos = os.listdir()
    products = crud_functions2.get_all_products()
    for product in products:
        with open(lst_photos[product[0]-1], 'rb') as img:
            await message.answer_photo(img, f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
    await message.answer('Выберите продукт для покупки:', reply_markup = inline_products)

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text = ['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = inline)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state= UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    await message.answer(f'{10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) + 5}')
    await state.finish()

@dp.message_handler(commands=['start'])
async def start(message):
    # print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)

@dp.message_handler()
async def all_messages(message):
    # print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    crud_functions2.initiate_db()
    os.chdir('photo')
    executor.start_polling(dp, skip_updates=True)
