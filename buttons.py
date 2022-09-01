from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_users = KeyboardButton('Выбрать автомобиль')
replykb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_users)

def genmarkup_brand(data): # передаём в функцию data

    markup_brand = InlineKeyboardMarkup() # создаём клавиатуру
    markup_brand.row_width = 2 # кол-во кнопок в строке
    for i in data: # цикл для создания кнопок
        markup_brand.add(InlineKeyboardButton(i[0], callback_data=i[0])) #Создаём кнопки, i[1] - название, i[2] - каллбек дата
    return markup_brand #возвращаем клавиатуру

def genmarkup_model(model_data): # передаём в функцию data

    markup_model = InlineKeyboardMarkup() # создаём клавиатуру
    markup_model.row_width = 2 # кол-во кнопок в строке
    for i in model_data: # цикл для создания кнопок
        markup_model.add(InlineKeyboardButton(i[0], callback_data=i[0])) #Создаём кнопки, i[1] - название, i[2] - каллбек дата
    return markup_model #возвращаем клавиатуру

def genmarkup_years(years_data): # передаём в функцию data

    markup_years = InlineKeyboardMarkup() # создаём клавиатуру
    markup_years.row_width = 2 # кол-во кнопок в строке
    for i in years_data: # цикл для создания кнопок
        markup_years.add(InlineKeyboardButton(i[0], callback_data=i[0])) #Создаём кнопки, i[1] - название, i[2] - каллбек дата
    return markup_years #возвращаем клавиатуру

def genmarkup_modify(modify_data): # передаём в функцию data

    markup_modify = InlineKeyboardMarkup() # создаём клавиатуру
    markup_modify.row_width = 2 # кол-во кнопок в строке
    for i in modify_data: # цикл для создания кнопок
        markup_modify.add(InlineKeyboardButton(i[0], callback_data=i[0])) #Создаём кнопки, i[1] - название, i[2] - каллбек дата
    return markup_modify #возвращаем клавиатуру