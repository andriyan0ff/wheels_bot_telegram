from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_users = KeyboardButton('Выбрать автомобиль')
replykb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_users)

def genmarkup_brand(data):

    markup_brand = InlineKeyboardMarkup()
    markup_brand.row_width = 2
    data.sort()
    for i in data:
        markup_brand.add(InlineKeyboardButton(i[0], callback_data=i[0]))
    return markup_brand

def genmarkup_model(model_data):

    markup_model = InlineKeyboardMarkup()
    markup_model.row_width = 2
    model_data.sort()
    for i in model_data:
        markup_model.add(InlineKeyboardButton(i[0], callback_data=i[0]))
    return markup_model

def genmarkup_years(years_data):

    markup_years = InlineKeyboardMarkup()
    markup_years.row_width = 2
    years_data.sort()
    for i in years_data:
        markup_years.add(InlineKeyboardButton(i[0], callback_data=i[0]))
    return markup_years

def genmarkup_modify(modify_data):

    markup_modify = InlineKeyboardMarkup()
    markup_modify.row_width = 2
    modify_data.sort()
    for i in modify_data: #
        markup_modify.add(InlineKeyboardButton(i[0], callback_data=i[0]))
    return markup_modify