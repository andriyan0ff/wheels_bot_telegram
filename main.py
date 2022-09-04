from aiogram import Bot, types, Dispatcher, executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging
import buttons
from config import Token, host, user, password, db_name
import psycopg2

data = []
datastring = []
model_string = []
years_string = []
modify_string =[]
wheels_string = []
callback_years = ''
#Логгирование
logging.basicConfig(level=logging.INFO)

#Подключение к боту
bot = Bot(token=Token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	await bot.send_message(message.from_user.id, '<b>Добро пожаловать!</b>', parse_mode='HTML', reply_markup=buttons.replykb)

@dp.message_handler(content_types=['text'], text='Выбрать автомобиль')
async def buy(message: types.Message):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("""SELECT DISTINCT(brand) from auto;""")
            data = cursor.fetchall()
            for i in data:
                datastring.append(str(i[0]))

            await bot.send_message(message.from_user.id, 'Выберите марку автомобиля:', reply_markup=buttons.genmarkup_brand(data))


    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


@dp.callback_query_handler(lambda call: True)
async def stoptopupcall(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            if callback_query.data in datastring:
                cursor.execute("""SELECT DISTINCT(model) FROM auto WHERE brand = '"""+callback_query.data+"""';""")
                model_data = cursor.fetchall()
                for i in model_data:
                    model_string.append(str(i[0]))
                await bot.send_message(callback_query.from_user.id, 'Выберите модель:', reply_markup=buttons.genmarkup_model(model_data))

        with connection.cursor() as cursor:
            if callback_query.data in model_string:
                cursor.execute("""SELECT DISTINCT(years) FROM auto WHERE model = '"""+callback_query.data+"""';""")
                years_data = cursor.fetchall()
                for i in years_data:
                    years_string.append(str(i[0]))
                await bot.send_message(callback_query.from_user.id, 'Выберите кузов и год выпуска:', reply_markup=buttons.genmarkup_years(years_data))

        with connection.cursor() as cursor:
            if callback_query.data in years_string:
                cursor.execute("""SELECT DISTINCT(modify) FROM auto WHERE years = '"""+callback_query.data+"""';""")
                modify_data = cursor.fetchall()
                global callback_years
                callback_years = callback_query.data
                print(callback_years)
                for i in modify_data:
                    modify_string.append(str(i[0]))
                await bot.send_message(callback_query.from_user.id, 'Выберите модификацию:', reply_markup=buttons.genmarkup_modify(modify_data))

        with connection.cursor() as cursor:
            if callback_query.data in modify_string:
                cursor.execute("""SELECT wheels FROM auto WHERE modify = '"""+callback_query.data+"""' AND  years = '"""+callback_years+"""';""")
                wheels_data = cursor.fetchall()
                print(callback_query.data)
                print(wheels_data)
                print('--------')

                for i in wheels_data:
                    wheels_string.append(str(i[0]))
                print(wheels_string)
                await bot.send_message(callback_query.from_user.id, ' '.join(wheels_string))

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

if __name__ == "__main__":
	executor.start_polling(dp)
