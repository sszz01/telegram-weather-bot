import random
import requests
import datetime
import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pprint import pprint

bot_token = os.environ["TOKEN"]
ow_token = "f7eda094dcc6dcec0d68c972318e04df"

bot = Bot(token=bot_token)
dp = Dispatcher(bot)
lang = ""
i = 0
tformat = ""
format_sign = ""
ws_sign = ""
j = 0
k = 0
e = 0
e1 = 0
e2 = 0
e3 = 0
e4 = 0
e5 = 0
e6 = 0
y = 0
timecall = ""
stickers = ["./tgs/cherry.tgs", "./tgs/cherry1.tgs",
            "./tgs/cherry2.tgs", "./tgs/sus.tgs",
            "./tgs/sus1.tgs", "./tgs/marshmallow1.tgs",
            "./tgs/bear.tgs", "./tgs/bear2.tgs",
            "./tgs/bear3.tgs", "./tgs/bear4.tgs",
            "./tgs/babyyoda.tgs", "./tgs/babyyoda1.tgs",
            "./tgs/astronaut.tgs", "./tgs/astronaut1.tgs",
            "./tgs/frog.tgs", "./tgs/hand.tgs",
            "./tgs/tendy.tgs", "./tgs/hedgehog.tgs",
            "./tgs/fish.tgs", "./tgs/fish1.tgs",
            "./tgs/fish2.tgs", "./tgs/strawberry.tgs",
            "./tgs/fish3.tgs", "./tgs/fish4.tgs",
            "./tgs/hackdog.tgs", "./tgs/dragon.tgs"]

lang_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="English\U0001F1EC\U0001F1E7\U0001F1FA\U0001F1F8", callback_data="eng"),
    ],
    [
        InlineKeyboardButton(text="Русский\U0001F1F7\U0001F1FA", callback_data="rus")
    ],
    [
        InlineKeyboardButton(text="Polski\U0001F1F5\U0001F1F1", callback_data="pol")
    ]
])
lang_buttons_rus = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Английский\U0001F1EC\U0001F1E7\U0001F1FA\U0001F1F8", callback_data="eng"),
    ],
    [
        InlineKeyboardButton(text="Русский\U0001F1F7\U0001F1FA", callback_data="rus")
    ],
    [
        InlineKeyboardButton(text="Польский\U0001F1F5\U0001F1F1", callback_data="pol")
    ],
    [
        InlineKeyboardButton(text="Назад \U00002B05", callback_data="back")
    ]
])
lang_buttons1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="English\U0001F1EC\U0001F1E7\U0001F1FA\U0001F1F8", callback_data="eng"),
    ],
    [
        InlineKeyboardButton(text="Russian\U0001F1F7\U0001F1FA", callback_data="rus")
    ],
    [
        InlineKeyboardButton(text="Polish\U0001F1F5\U0001F1F1", callback_data="pol")
    ],
    [
        InlineKeyboardButton(text="Back \U00002B05", callback_data="back")
    ]
])
lang_buttons_pol = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Angielski\U0001F1EC\U0001F1E7\U0001F1FA\U0001F1F8", callback_data="eng"),
    ],
    [
        InlineKeyboardButton(text="Rosyjski\U0001F1F7\U0001F1FA", callback_data="rus")
    ],
    [
        InlineKeyboardButton(text="Polski\U0001F1F5\U0001F1F1", callback_data="pol")
    ],
    [
        InlineKeyboardButton(text="Plecy \U00002B05", callback_data="back")
    ]
])
ch_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Language  \U0001F22F", callback_data="lan"),
    ],
    [
        InlineKeyboardButton(text="System of units  \U0001F4D0", callback_data="uni")
    ],
    [
        InlineKeyboardButton(text="Time format  \U0001F552", callback_data="time1")
    ],
    [
        InlineKeyboardButton(text="Quit  \U0000274C", callback_data="stop")
    ]
])
ch_buttons_rus = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Язык  \U0001F22F", callback_data="lan"),
    ],
    [
        InlineKeyboardButton(text="Система измерений  \U0001F4CF", callback_data="uni")
    ],
    [
        InlineKeyboardButton(text="Формат времени  \U0001F552", callback_data="time1")
    ],
    [
        InlineKeyboardButton(text="Выйти  \U0000274C", callback_data="stop")
    ]
])
ch_buttons_pol = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Język  \U0001F22F", callback_data="lan"),
    ],
    [
        InlineKeyboardButton(text="System miar  \U0001F4CF", callback_data="uni")
    ],
    [
        InlineKeyboardButton(text="Format czasu  \U0001F552", callback_data="time1")
    ],
    [
        InlineKeyboardButton(text="Wyjście  \U0000274C", callback_data="stop")
    ]
])
format_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Metric", callback_data="met"),
    ],
    [
        InlineKeyboardButton(text="Imperial", callback_data="imp")
    ]
])
format_buttons_rus = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Метрическая", callback_data="met"),
    ],
    [
        InlineKeyboardButton(text="Имперская", callback_data="imp")
    ]
])
format_buttons_pol = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Metryczny", callback_data="met"),
    ],
    [
        InlineKeyboardButton(text="Imperialny", callback_data="imp")
    ]
])
format_buttons1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Metric", callback_data="met"),
    ],
    [
        InlineKeyboardButton(text="Imperial", callback_data="imp")
    ],
    [
        InlineKeyboardButton(text="Back \U00002B05", callback_data="back")
    ]
])
format_buttons_rus1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Метрическая", callback_data="met"),
    ],
    [
        InlineKeyboardButton(text="Имперская", callback_data="imp")
    ],
    [
        InlineKeyboardButton(text="Назад \U00002B05", callback_data="back")
    ]
])
format_buttons_pol1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Metryczny", callback_data="met"),
    ],
    [
        InlineKeyboardButton(text="Imperialny", callback_data="imp")
    ],
    [
        InlineKeyboardButton(text="Wyjście \U00002B05", callback_data="back")
    ]
])
time_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="12-hour format", callback_data="12"),
    ],
    [
        InlineKeyboardButton(text="24-hour format", callback_data="24")
    ]
])
time_buttons_rus = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="12-часовой формат", callback_data="12"),
    ],
    [
        InlineKeyboardButton(text="24-часовой формат", callback_data="24")
    ]
])
time_buttons_pol = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Format 12-godzinny", callback_data="12"),
    ],
    [
        InlineKeyboardButton(text="Format 24-godzinny", callback_data="24")
    ]
])
time_buttons1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="12-hour format", callback_data="12"),
    ],
    [
        InlineKeyboardButton(text="24-hour format", callback_data="24")
    ],
    [
        InlineKeyboardButton(text="Back \U00002B05", callback_data="back")
    ]
])
time_buttons_rus1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="12-часовой формат", callback_data="12"),
    ],
    [
        InlineKeyboardButton(text="24-часовой формат", callback_data="24")
    ],
    [
        InlineKeyboardButton(text="Назад \U00002B05", callback_data="back")
    ]
])
time_buttons_pol1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Format 12-godzinny", callback_data="12"),
    ],
    [
        InlineKeyboardButton(text="Format 24-godzinny", callback_data="24")
    ],
    [
        InlineKeyboardButton(text="Wyjście \U00002B05", callback_data="back")
    ]
])


@dp.message_handler(commands=["start"])
async def start_command(message: [types.Message, types.CallbackQuery]):
    global i, k, e, e1, e2, e3, e4, e5, e6
    i += 1
    if i == 1:
        await message.reply("Hey, I'm Weather Bot! So, let's get started \U0001F603"
                            "\nChoose the most suitable to you language first:", reply_markup=lang_buttons)
    elif k >= 1:
        await message.delete()
    elif j >= 3 and lang == "eng":
        k += 1
        e += 1
        if tformat == "metric" and timecall == "12":
            e2 += 1
            e4 += 1
        elif tformat == "imperial" and timecall == "12":
            e3 += 1
            e4 += 1
        elif tformat == "metric" and timecall == "24":
            e2 += 1
            e5 += 1
        elif tformat == "imperial" and timecall == "24":
            e3 += 1
            e5 += 1
        await message.reply("Welcome to the bot settings! \U00002699\U0000FE0F",
                            reply_markup=ch_buttons)
    elif j >= 3 and lang == "rus":
        k += 1
        e1 += 1
        if tformat == "metric" and timecall == "12":
            e2 += 1
            e4 += 1
        elif tformat == "imperial" and timecall == "12":
            e3 += 1
            e4 += 1
        elif tformat == "metric" and timecall == "24":
            e2 += 1
            e5 += 1
        elif tformat == "imperial" and timecall == "24":
            e3 += 1
            e5 += 1
        await message.reply("Добро пожаловать в настройки бота! \U00002699\U0000FE0F",
                            reply_markup=ch_buttons_rus)
    elif j >= 3 and lang == "pol":
        k += 1
        e6 += 1
        if tformat == "metric" and timecall == "12":
            e2 += 1
            e4 += 1
        elif tformat == "imperial" and timecall == "12":
            e3 += 1
            e4 += 1
        elif tformat == "metric" and timecall == "24":
            e2 += 1
            e5 += 1
        elif tformat == "imperial" and timecall == "24":
            e3 += 1
            e5 += 1
        await message.reply("Witamy w ustawieniach bota! \U00002699\U0000FE0F",
                            reply_markup=ch_buttons_pol)
    else:
        i -= 1
        await message.delete()


@dp.message_handler()
async def get_weather(message: types.Message):
    if j >= 3 and lang == "eng":
        await get_weather_eng(message)
    elif j >= 3 and lang == "rus":
        await get_weather_rus(message)
    elif j >= 3 and lang == "pol":
        await get_weather_pol(message)
    else:
        if i < 1:
            await message.reply("You haven't set up a bot yet. Please, type /start "
                                "and set up a bot to make your bot work properly \U0001F642")
        else:
            await message.delete()


async def get_weather_eng(message: types.Message):
    global country_flag, full_country_name, tzsuns, tzsunr, tz_loc_time, us_state, ap_text
    json_to_smile = {
        "Clear": "Clear sky \U00002600",
        "Rain": "Rainy \U00002614",
        "Clouds": "Cloudy \U00002601",
        "Drizzle": "Drizzle \U0001F326",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Fog": "Foggy \U0001F32B",
        "Tornado": "Tornado \U0001F32A",
        "Mist": "Mist \U0001F301",
        "Haze": "Haze \U0001F636\U0000200D\U0001F32B\U0000FE0F",
        "Few clouds": "Few clouds \U0001F324"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}, {message.text}&appid={ow_token}"
            f"&units={tformat}&lang=en"
        )
        data = r.json()
        pprint(data)
        r1 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={message.text},{message.text}"
                          f"&limit=3&appid={ow_token}")
        data1 = r1.json()
        # pprint(data1)
        city = data["name"]
        current_w = round(data["main"]["temp"])
        wind_sp = round(data["wind"]["speed"])
        pressure = data["main"]["pressure"]
        sunr = data["sys"]["sunrise"]
        suns = data["sys"]["sunset"]
        fls_like = round(data["main"]["feels_like"])
        humidity = data["main"]["humidity"]
        max_temp = round(data["main"]["temp_max"])
        min_temp = round(data["main"]["temp_min"])
        country = data["sys"]["country"]
        weather_description = data["weather"][0]["main"]
        wind_degree = data["wind"]["deg"]
        vis = data["visibility"]
        tz = data["timezone"]
        loc_time = data["dt"]
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]

        r2 = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,"
                          f"hourly,daily,alerts&units={tformat}&appid={ow_token}")
        data2 = r2.json()
        # pprint(data2)
        dew_p = round(data2["current"]["dew_point"])
        uvi = round(data2["current"]["uvi"])

        r3 = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={ow_token}")
        data3 = r3.json()
        # pprint(data3)
        ap_lvl = data3["list"][0]["main"]["aqi"]

        vis = round(vis / 1000)

        # A-countries
        if country == "AC":
            full_country_name = "Ascension Island"
            country_flag = "\U0001F1E6\U0001F1E8"
        elif country == "AD":
            full_country_name = "Andorra"
            country_flag = "\U0001F1E6\U0001F1E9"
        elif country == "AE":
            full_country_name = "United Arab Emirates"
            country_flag = "\U0001F1E6\U0001F1EA"
        elif country == "AF":
            full_country_name = "Afghanistan"
            country_flag = "\U0001F1E6\U0001F1EB"
        elif country == "AG":
            full_country_name = "Antigua & Barbuda"
            country_flag = "\U0001F1E6\U0001F1EC"
        elif country == "AI":
            full_country_name = "Anguilla"
            country_flag = "\U0001F1E6\U0001F1EE"
        elif country == "AL":
            full_country_name = "Albania"
            country_flag = "\U0001F1E6\U0001F1F1"
        elif country == "AM":
            full_country_name = "Armenia"
            country_flag = "\U0001F1E6\U0001F1F2"
        elif country == "AO":
            full_country_name = "Angola"
            country_flag = "\U0001F1E6\U0001F1F4"
        elif country == "AQ":
            full_country_name = "Antarctica"
            country_flag = "\U0001F1E6\U0001F1F6"
        elif country == "AR":
            full_country_name = "Argentina"
            country_flag = "\U0001F1E6\U0001F1F7"
        elif country == "AS":
            full_country_name = "American Samoa"
            country_flag = "\U0001F1E6\U0001F1F8"
        elif country == "AT":
            full_country_name = "Austria"
            country_flag = "\U0001F1E6\U0001F1F9"
        elif country == "AU":
            full_country_name = "Australia"
            country_flag = "\U0001F1E6\U0001F1FA"
        elif country == "AW":
            full_country_name = "Aruba"
            country_flag = "\U0001F1E6\U0001F1FC"
        elif country == "AX":
            full_country_name = "Åland Islands"
            country_flag = "\U0001F1E6\U0001F1FD"
        elif country == "AZ":
            full_country_name = "Azerbaijan"
            country_flag = "\U0001F1E6\U0001F1FF"
        # B-countries
        elif country == "BA":
            full_country_name = "Bosnia & Herzegovina"
            country_flag = "\U0001F1E7\U0001F1E6"
        elif country == "BB":
            full_country_name = "Barbados"
            country_flag = "\U0001F1E7\U0001F1E7"
        elif country == "BD":
            full_country_name = "Bangladesh"
            country_flag = "\U0001F1E7\U0001F1E9"
        elif country == "BE":
            full_country_name = "Belgium"
            country_flag = "\U0001F1E7\U0001F1EA"
        elif country == "BF":
            full_country_name = "Burkina Faso"
            country_flag = "\U0001F1E7\U0001F1EB"
        elif country == "BG":
            full_country_name = "Bulgaria"
            country_flag = "\U0001F1E7\U0001F1EC"
        elif country == "BH":
            full_country_name = "Bahrain"
            country_flag = "\U0001F1E7\U0001F1ED"
        elif country == "BI":
            full_country_name = "Burundi"
            country_flag = "\U0001F1E7\U0001F1EE"
        elif country == "BJ":
            full_country_name = "Benin"
            country_flag = "\U0001F1E7\U0001F1EF"
        elif country == "BL":
            full_country_name = "St. Barthélemy"
            country_flag = "\U0001F1E7\U0001F1F1"
        elif country == "BM":
            full_country_name = "Bermuda"
            country_flag = "\U0001F1E7\U0001F1F2"
        elif country == "BN":
            full_country_name = "Brunei"
            country_flag = "\U0001F1E7\U0001F1F3"
        elif country == "BO":
            full_country_name = "Bolivia"
            country_flag = "\U0001F1E7\U0001F1F4"
        elif country == "BQ":
            full_country_name = "Caribbean Netherlands"
            country_flag = "\U0001F1E7\U0001F1F6"
        elif country == "BR":
            full_country_name = "Brazil"
            country_flag = "\U0001F1E7\U0001F1F7"
        elif country == "BS":
            full_country_name = "Bahamas"
            country_flag = "\U0001F1E7\U0001F1F8"
        elif country == "BT":
            full_country_name = "Bhutan"
            country_flag = "\U0001F1E7\U0001F1F9"
        elif country == "BV":
            full_country_name = "Bouvet Island"
            country_flag = "\U0001F1E7\U0001F1FB"
        elif country == "BW":
            full_country_name = "Botswana"
            country_flag = "\U0001F1E7\U0001F1FC"
        elif country == "BY":
            full_country_name = "Belarus"
            country_flag = "\U0001F1E7\U0001F1FE"
        elif country == "BZ":
            full_country_name = "Belize"
            country_flag = "\U0001F1E7\U0001F1FF"
        # C-countries
        elif country == "CA":
            full_country_name = "Canada"
            country_flag = "\U0001F1E8\U0001F1E6"
        elif country == "CC":
            full_country_name = "Cocos Islands"
            country_flag = "\U0001F1E8\U0001F1E8"
        elif country == "CD":
            full_country_name = "Democratic Republic of the Congo"
            country_flag = "\U0001F1E8\U0001F1E9"
        elif country == "CF":
            full_country_name = "Central African Republic"
            country_flag = "\U0001F1E8\U0001F1EB"
        elif country == "CG":
            full_country_name = "Republic of the Congo"
            country_flag = "\U0001F1E8\U0001F1EC"
        elif country == "CH":
            full_country_name = "Switzerland"
            country_flag = "\U0001F1E8\U0001F1ED"
        elif country == "CI":
            full_country_name = "Ivory Coast"
            country_flag = "\U0001F1E8\U0001F1EE"
        elif country == "CK":
            full_country_name = "Cook Islands"
            country_flag = "\U0001F1E8\U0001F1F0"
        elif country == "CL":
            full_country_name = "Chile"
            country_flag = "\U0001F1E8\U0001F1F1"
        elif country == "CM":
            full_country_name = "Cameroon"
            country_flag = "\U0001F1E8\U0001F1F2"
        elif country == "CN":
            full_country_name = "China"
            country_flag = "\U0001F1E8\U0001F1F3"
        elif country == "CO":
            full_country_name = "Colombia"
            country_flag = "\U0001F1E8\U0001F1F4"
        elif country == "CP":
            full_country_name = "Clipperton Island"
            country_flag = "\U0001F1E8\U0001F1F5"
        elif country == "CR":
            full_country_name = "Costa Rica"
            country_flag = "\U0001F1E8\U0001F1F7"
        elif country == "CU":
            full_country_name = "Cuba"
            country_flag = "\U0001F1E8\U0001F1FA"
        elif country == "CV":
            full_country_name = "Cape Verde"
            country_flag = "\U0001F1E8\U0001F1FB"
        elif country == "CW":
            full_country_name = "Curaçao"
            country_flag = "\U0001F1E8\U0001F1FC"
        elif country == "CX":
            full_country_name = "Christmas Island"
            country_flag = "\U0001F1E8\U0001F1FD"
        elif country == "CY":
            full_country_name = "Cyprus"
            country_flag = "\U0001F1E8\U0001F1FE"
        elif country == "CZ":
            full_country_name = "Czechia"
            country_flag = "\U0001F1E8\U0001F1FF"
        # D-countries
        elif country == "DE":
            full_country_name = "Germany"
            country_flag = "\U0001F1E9\U0001F1EA"
        elif country == "DG":
            full_country_name = "Diego Garcia"
            country_flag = "\U0001F1E9\U0001F1EC"
        elif country == "DJ":
            full_country_name = "Djibouti"
            country_flag = "\U0001F1E9\U0001F1EF"
        elif country == "DK":
            full_country_name = "Denmark"
            country_flag = "\U0001F1E9\U0001F1F0"
        elif country == "DM":
            full_country_name = "Dominica"
            country_flag = "\U0001F1E9\U0001F1F2"
        elif country == "DO":
            full_country_name = "Dominican Republic"
            country_flag = "\U0001F1E9\U0001F1F4"
        elif country == "DZ":
            full_country_name = "Algeria"
            country_flag = "\U0001F1E9\U0001F1FF"
        # E-countries
        elif country == "EA":
            full_country_name = "Ceuta & Melilla"
            country_flag = "\U0001F1EA\U0001F1E6"
        elif country == "EC":
            full_country_name = "Ecuador"
            country_flag = "\U0001F1EA\U0001F1E8"
        elif country == "EE":
            full_country_name = "Estonia"
            country_flag = "\U0001F1EA\U0001F1EA"
        elif country == "EG":
            full_country_name = "Egypt"
            country_flag = "\U0001F1EA\U0001F1EC"
        elif country == "EH":
            full_country_name = "Western Sahara"
            country_flag = "\U0001F1EA\U0001F1ED"
        elif country == "ER":
            full_country_name = "Eritrea"
            country_flag = "\U0001F1EA\U0001F1F7"
        elif country == "ES":
            full_country_name = "Spain"
            country_flag = "\U0001F1EA\U0001F1F8"
        elif country == "ET":
            full_country_name = "Ethiopia"
            country_flag = "\U0001F1EA\U0001F1F9"
        # elif country == "EU":
        # full_country_name = "European Union"
        # country_flag = "\U0001F1EA\U0001F1FA"
        # F-countries
        elif country == "FI":
            full_country_name = "Finland"
            country_flag = "\U0001F1EB\U0001F1EE"
        elif country == "FJ":
            full_country_name = "Fiji"
            country_flag = "\U0001F1EB\U0001F1EF"
        elif country == "FK":
            full_country_name = "Falkland Islands"
            country_flag = "\U0001F1EB\U0001F1F0"
        elif country == "FM":
            full_country_name = "Micronesia"
            country_flag = "\U0001F1EB\U0001F1F2"
        elif country == "FO":
            full_country_name = "Faroe Islands"
            country_flag = "\U0001F1EB\U0001F1F4"
        elif country == "FR":
            full_country_name = "France"
            country_flag = "\U0001F1EB\U0001F1F7"
        # G-countries
        elif country == "GA":
            full_country_name = "Gabon"
            country_flag = "\U0001F1EC\U0001F1E6"
        elif country == "GB":
            full_country_name = "United Kingdom"
            country_flag = "\U0001F1EC\U0001F1E7"
        elif country == "GD":
            full_country_name = "Grenada"
            country_flag = "\U0001F1EC\U0001F1E9"
        elif country == "GE":
            full_country_name = "Georgia"
            country_flag = "\U0001F1EC\U0001F1EA"
        elif country == "GF":
            full_country_name = "French Guiana"
            country_flag = "\U0001F1EC\U0001F1EB"
        elif country == "GG":
            full_country_name = "Guernsey"
            country_flag = "\U0001F1EC\U0001F1EC"
        elif country == "GH":
            full_country_name = "Ghana"
            country_flag = "\U0001F1EC\U0001F1ED"
        elif country == "GI":
            full_country_name = "Gibraltar"
            country_flag = "\U0001F1EC\U0001F1EE"
        elif country == "GL":
            full_country_name = "Greenland"
            country_flag = "\U0001F1EC\U0001F1F1"
        elif country == "GM":
            full_country_name = "Gambia"
            country_flag = "\U0001F1EC\U0001F1F2"
        elif country == "GN":
            full_country_name = "Guinea"
            country_flag = "\U0001F1EC\U0001F1F3"
        elif country == "GP":
            full_country_name = "Guadeloupe"
            country_flag = "\U0001F1EC\U0001F1F5"
        elif country == "GQ":
            full_country_name = "Equatorial Guinea"
            country_flag = "\U0001F1EC\U0001F1F6"
        elif country == "GR":
            full_country_name = "Greece"
            country_flag = "\U0001F1EC\U0001F1F7"
        elif country == "GS":
            full_country_name = "South Georgia & South Sandwich Islands"
            country_flag = "\U0001F1EC\U0001F1F8"
        elif country == "GT":
            full_country_name = "Guatemala"
            country_flag = "\U0001F1EC\U0001F1F9"
        elif country == "GU":
            full_country_name = "Guam"
            country_flag = "\U0001F1EC\U0001F1FA"
        elif country == "GW":
            full_country_name = "Guinea-Bissau"
            country_flag = "\U0001F1EC\U0001F1FC"
        elif country == "GY":
            full_country_name = "Guyana"
            country_flag = "\U0001F1EC\U0001F1FE"
        # H-countries
        elif country == "HK":
            full_country_name = "Hong Kong"
            country_flag = "\U0001F1ED\U0001F1F0"
        elif country == "HM":
            full_country_name = "Heard & McDonald Islands"
            country_flag = "\U0001F1ED\U0001F1F2"
        elif country == "HN":
            full_country_name = "Honduras"
            country_flag = "\U0001F1ED\U0001F1F3"
        elif country == "HR":
            full_country_name = "Croatia"
            country_flag = "\U0001F1ED\U0001F1F7"
        elif country == "HT":
            full_country_name = "Haiti"
            country_flag = "\U0001F1ED\U0001F1F9"
        elif country == "HU":
            full_country_name = "Hungary"
            country_flag = "\U0001F1ED\U0001F1FA"
        # I-countries
        elif country == "IC":
            full_country_name = "Canary Islands"
            country_flag = "\U0001F1EE\U0001F1E8"
        elif country == "ID":
            full_country_name = "Indonesia"
            country_flag = "\U0001F1EE\U0001F1E9"
        elif country == "IE":
            full_country_name = "Ireland"
            country_flag = "\U0001F1EE\U0001F1EA"
        elif country == "IL":
            full_country_name = "Israel"
            country_flag = "\U0001F1EE\U0001F1F1"
        elif country == "IM":
            full_country_name = "Isle of Man"
            country_flag = "\U0001F1EE\U0001F1F2"
        elif country == "IN":
            full_country_name = "India"
            country_flag = "\U0001F1EE\U0001F1F3"
        elif country == "IO":
            full_country_name = "British Indian Ocean Territory"
            country_flag = "\U0001F1EE\U0001F1F4"
        elif country == "IQ":
            full_country_name = "Iraq"
            country_flag = "\U0001F1EE\U0001F1F6"
        elif country == "IR":
            full_country_name = "Iran"
            country_flag = "\U0001F1EE\U0001F1F7"
        elif country == "IS":
            full_country_name = "Iceland"
            country_flag = "\U0001F1EE\U0001F1F8"
        elif country == "IT":
            full_country_name = "Italy"
            country_flag = "\U0001F1EE\U0001F1F9"
        # J-countries
        elif country == "JE":
            full_country_name = "Jersey"
            country_flag = "\U0001F1EF\U0001F1EA"
        elif country == "JM":
            full_country_name = "Jamaica"
            country_flag = "\U0001F1EF\U0001F1F2"
        elif country == "JO":
            full_country_name = "Jordan"
            country_flag = "\U0001F1EF\U0001F1F4"
        elif country == "JP":
            full_country_name = "Japan"
            country_flag = "\U0001F1EF\U0001F1F5"
        # K-countries
        elif country == "KE":
            full_country_name = "Kenya"
            country_flag = "\U0001F1F0\U0001F1EA"
        elif country == "KG":
            full_country_name = "Kyrgyzstan"
            country_flag = "\U0001F1F0\U0001F1EC"
        elif country == "KH":
            full_country_name = "Cambodia"
            country_flag = "\U0001F1F0\U0001F1ED"
        elif country == "KI":
            full_country_name = "Kiribati"
            country_flag = "\U0001F1F0\U0001F1EE"
        elif country == "KM":
            full_country_name = "Comoros"
            country_flag = "\U0001F1F0\U0001F1F2"
        elif country == "KN":
            full_country_name = "St. Kitts & Nevis"
            country_flag = "\U0001F1F0\U0001F1F3"
        elif country == "KP":
            full_country_name = "North Korea"
            country_flag = "\U0001F1F0\U0001F1F5"
        elif country == "KR":
            full_country_name = "South Korea"
            country_flag = "\U0001F1F0\U0001F1F7"
        elif country == "KW":
            full_country_name = "Kuwait"
            country_flag = "\U0001F1F0\U0001F1FC"
        elif country == "KY":
            full_country_name = "Cayman Islands"
            country_flag = "\U0001F1F0\U0001F1FE"
        elif country == "KZ":
            full_country_name = "Kazakhstan"
            country_flag = "\U0001F1F0\U0001F1FF"
        # L-countries
        elif country == "LA":
            full_country_name = "Laos"
            country_flag = "\U0001F1F1\U0001F1E6"
        elif country == "LB":
            full_country_name = "Lebanon"
            country_flag = "\U0001F1F1\U0001F1E7"
        elif country == "LC":
            full_country_name = "St. Lucia"
            country_flag = "\U0001F1F1\U0001F1E8"
        elif country == "LI":
            full_country_name = "Lichtenstein"
            country_flag = "\U0001F1F1\U0001F1EE"
        elif country == "LK":
            full_country_name = "Sri Lanka"
            country_flag = "\U0001F1F1\U0001F1F0"
        elif country == "LR":
            full_country_name = "Liberia"
            country_flag = "\U0001F1F1\U0001F1F7"
        elif country == "LS":
            full_country_name = "Lesotho"
            country_flag = "\U0001F1F1\U0001F1F8"
        elif country == "LT":
            full_country_name = "Lithuania"
            country_flag = "\U0001F1F1\U0001F1F9"
        elif country == "LU":
            full_country_name = "Luxembourg"
            country_flag = "\U0001F1F1\U0001F1FA"
        elif country == "LV":
            full_country_name = "Latvia"
            country_flag = "\U0001F1F1\U0001F1FB"
        elif country == "LY":
            full_country_name = "Libya"
            country_flag = "\U0001F1F1\U0001F1FE"
        # M-countries
        elif country == "MA":
            full_country_name = "Morocco"
            country_flag = "\U0001F1F2\U0001F1E6"
        elif country == "MC":
            full_country_name = "Monaco"
            country_flag = "\U0001F1F2\U0001F1E8"
        elif country == "MD":
            full_country_name = "Moldova"
            country_flag = "\U0001F1F2\U0001F1E9"
        elif country == "ME":
            full_country_name = "Montenegro"
            country_flag = "\U0001F1F2\U0001F1EA"
        elif country == "MF":
            full_country_name = "St. Martin"
            country_flag = "\U0001F1F2\U0001F1EB"
        elif country == "MG":
            full_country_name = "Madagascar"
            country_flag = "\U0001F1F2\U0001F1EC"
        elif country == "MH":
            full_country_name = "Marshall Islands"
            country_flag = "\U0001F1F2\U0001F1ED"
        elif country == "MK":
            full_country_name = "North Macedonia"
            country_flag = "\U0001F1F2\U0001F1F0"
        elif country == "ML":
            full_country_name = "Mali"
            country_flag = "\U0001F1F2\U0001F1F1"
        elif country == "MM":
            full_country_name = "Myanmar"
            country_flag = "\U0001F1F2\U0001F1F2"
        elif country == "MN":
            full_country_name = "Mongolia"
            country_flag = "\U0001F1F2\U0001F1F3"
        elif country == "MO":
            full_country_name = "Macao"
            country_flag = "\U0001F1F2\U0001F1F4"
        elif country == "MP":
            full_country_name = "Northern Mariana Islands"
            country_flag = "\U0001F1F2\U0001F1F5"
        elif country == "MQ":
            full_country_name = "Martinique"
            country_flag = "\U0001F1F2\U0001F1F6"
        elif country == "MR":
            full_country_name = "Mauritania"
            country_flag = "\U0001F1F2\U0001F1F7"
        elif country == "MS":
            full_country_name = "Montserrat"
            country_flag = "\U0001F1F2\U0001F1F8"
        elif country == "MT":
            full_country_name = "Malta"
            country_flag = "\U0001F1F2\U0001F1F9"
        elif country == "MU":
            full_country_name = "Mauritius"
            country_flag = "\U0001F1F2\U0001F1FA"
        elif country == "MV":
            full_country_name = "Maldives"
            country_flag = "\U0001F1F2\U0001F1FB"
        elif country == "MW":
            full_country_name = "Malawi"
            country_flag = "\U0001F1F2\U0001F1FC"
        elif country == "MX":
            full_country_name = "Mexico"
            country_flag = "\U0001F1F2\U0001F1FD"
        elif country == "MY":
            full_country_name = "Malaysia"
            country_flag = "\U0001F1F2\U0001F1FE"
        elif country == "MZ":
            full_country_name = "Mozambique"
            country_flag = "\U0001F1F2\U0001F1FF"
        # N-countries
        elif country == "NA":
            full_country_name = "Namibia"
            country_flag = "\U0001F1F3\U0001F1E6"
        elif country == "NC":
            full_country_name = "New Caledonia"
            country_flag = "\U0001F1F3\U0001F1E8"
        elif country == "NE":
            full_country_name = "Niger"
            country_flag = "\U0001F1F3\U0001F1EA"
        elif country == "NF":
            full_country_name = "Norfolk Island"
            country_flag = "\U0001F1F3\U0001F1EB"
        elif country == "NG":
            full_country_name = "Nigeria"
            country_flag = "\U0001F1F3\U0001F1EC"
        elif country == "NI":
            full_country_name = "Nicaragua"
            country_flag = "\U0001F1F3\U0001F1EE"
        elif country == "NL":
            full_country_name = "Netherlands"
            country_flag = "\U0001F1F3\U0001F1F1"
        elif country == "NO":
            full_country_name = "Norway"
            country_flag = "\U0001F1F3\U0001F1F4"
        elif country == "NP":
            full_country_name = "Nepal"
            country_flag = "\U0001F1F3\U0001F1F5"
        elif country == "NR":
            full_country_name = "Nauru"
            country_flag = "\U0001F1F3\U0001F1F7"
        elif country == "NU":
            full_country_name = "Niue"
            country_flag = "\U0001F1F3\U0001F1FA"
        elif country == "NZ":
            full_country_name = "New Zealand"
            country_flag = "\U0001F1F3\U0001F1FF"
        # O-countries
        elif country == "OM":
            full_country_name = "Oman"
            country_flag = "\U0001F1F4\U0001F1F2"
        # P-countries
        elif country == "PA":
            full_country_name = "Panama"
            country_flag = "\U0001F1F5\U0001F1E6"
        elif country == "PE":
            full_country_name = "Peru"
            country_flag = "\U0001F1F5\U0001F1EA"
        elif country == "PG":
            full_country_name = "Papua New Guinea"
            country_flag = "\U0001F1F5\U0001F1EC"
        elif country == "PH":
            full_country_name = "Philippines"
            country_flag = "\U0001F1F5\U0001F1ED"
        elif country == "PK":
            full_country_name = "Pakistan"
            country_flag = "\U0001F1F5\U0001F1F0"
        elif country == "PL":
            full_country_name = "Poland"
            country_flag = "\U0001F1F5\U0001F1F1"
        elif country == "PM":
            full_country_name = "St. Pierre & Miquelon"
            country_flag = "\U0001F1F5\U0001F1F2"
        elif country == "PN":
            full_country_name = "Pitcairn Islands"
            country_flag = "\U0001F1F5\U0001F1F3"
        elif country == "PR":
            full_country_name = "Puerto Rico"
            country_flag = "\U0001F1F5\U0001F1F7"
        elif country == "PS":
            full_country_name = "Palestinian Territories"
            country_flag = "\U0001F1F5\U0001F1F8"
        elif country == "PT":
            full_country_name = "Portugal"
            country_flag = "\U0001F1F5\U0001F1F9"
        elif country == "PW":
            full_country_name = "Palau"
            country_flag = "\U0001F1F5\U0001F1FC"
        elif country == "PY":
            full_country_name = "Paraguay"
            country_flag = "\U0001F1F5\U0001F1FE"
        # Q-countries
        elif country == "QA":
            full_country_name = "Qatar"
            country_flag = "\U0001F1F6\U0001F1E6"
        # R-countries
        elif country == "RE":
            full_country_name = "Reunion"
            country_flag = "\U0001F1F7\U0001F1EA"
        elif country == "RO":
            full_country_name = "Romania"
            country_flag = "\U0001F1F7\U0001F1F4"
        elif country == "RS":
            full_country_name = "Serbia"
            country_flag = "\U0001F1F7\U0001F1F8"
        elif country == "RU":
            full_country_name = "Russia"
            country_flag = "\U0001F1F7\U0001F1FA"
        elif country == "RW":
            full_country_name = "Rwanda"
            country_flag = "\U0001F1F7\U0001F1FC"
        # S-countries
        elif country == "SA":
            full_country_name = "Saudi Arabia"
            country_flag = "\U0001F1F8\U0001F1E6"
        elif country == "SB":
            full_country_name = "Solomon Islands"
            country_flag = "\U0001F1F8\U0001F1E7"
        elif country == "SC":
            full_country_name = "Seychelles"
            country_flag = "\U0001F1F8\U0001F1E8"
        elif country == "SD":
            full_country_name = "Sudan"
            country_flag = "\U0001F1F8\U0001F1E9"
        elif country == "SE":
            full_country_name = "Sweden"
            country_flag = "\U0001F1F8\U0001F1EA"
        elif country == "SG":
            full_country_name = "Singapore"
            country_flag = "\U0001F1F8\U0001F1EC"
        elif country == "SH":
            full_country_name = "St. Helena"
            country_flag = "\U0001F1F8\U0001F1EE"
        elif country == "SJ":
            full_country_name = "Svalbard & Jan Mayen"
            country_flag = "\U0001F1F8\U0001F1EF"
        elif country == "SK":
            full_country_name = "Slovakia"
            country_flag = "\U0001F1F8\U0001F1F0"
        elif country == "SL":
            full_country_name = "Sierra Leone"
            country_flag = "\U0001F1F8\U0001F1F1"
        elif country == "SM":
            full_country_name = "San Marino"
            country_flag = "\U0001F1F8\U0001F1F2"
        elif country == "SN":
            full_country_name = "Senegal"
            country_flag = "\U0001F1F8\U0001F1F3"
        elif country == "SO":
            full_country_name = "Somalia"
            country_flag = "\U0001F1F8\U0001F1F4"
        elif country == "SR":
            full_country_name = "Suriname"
            country_flag = "\U0001F1F8\U0001F1F7"
        elif country == "SS":
            full_country_name = "South Sudan"
            country_flag = "\U0001F1F8\U0001F1F8"
        elif country == "ST":
            full_country_name = "São Tomé & Príncipe"
            country_flag = "\U0001F1F8\U0001F1F9"
        elif country == "SV":
            full_country_name = "El Salvador"
            country_flag = "\U0001F1F8\U0001F1FB"
        elif country == "SX":
            full_country_name = "Sint Maarten"
            country_flag = "\U0001F1F8\U0001F1FD"
        elif country == "SY":
            full_country_name = "Syria"
            country_flag = "\U0001F1F8\U0001F1FE"
        elif country == "SZ":
            full_country_name = "Eswatini"
            country_flag = "\U0001F1F8\U0001F1FF"
        # T-countries
        elif country == "TA":
            full_country_name = "Tristan da Cunha"
            country_flag = "\U0001F1F9\U0001F1E6"
        elif country == "TC":
            full_country_name = "Turks & Caicos Islands"
            country_flag = "\U0001F1F9\U0001F1E8"
        elif country == "TD":
            full_country_name = "Chad"
            country_flag = "\U0001F1F9\U0001F1E9"
        elif country == "TF":
            full_country_name = "French Southern Territories"
            country_flag = "\U0001F1F9\U0001F1EB"
        elif country == "TG":
            full_country_name = "Togo"
            country_flag = "\U0001F1F9\U0001F1EC"
        elif country == "TH":
            full_country_name = "Thailand"
            country_flag = "\U0001F1F9\U0001F1ED"
        elif country == "TJ":
            full_country_name = "Tajikistan"
            country_flag = "\U0001F1F9\U0001F1EF"
        elif country == "TK":
            full_country_name = "Tokelau"
            country_flag = "\U0001F1F9\U0001F1F0"
        elif country == "TL":
            full_country_name = "Timor-Leste"
            country_flag = "\U0001F1F9\U0001F1F1"
        elif country == "TM":
            full_country_name = "Turkmenistan"
            country_flag = "\U0001F1F9\U0001F1F2"
        elif country == "TN":
            full_country_name = "Tunisia"
            country_flag = "\U0001F1F9\U0001F1F3"
        elif country == "TO":
            full_country_name = "Tonga"
            country_flag = "\U0001F1F9\U0001F1F4"
        elif country == "TR":
            full_country_name = "Turkey"
            country_flag = "\U0001F1F9\U0001F1F7"
        elif country == "TT":
            full_country_name = "Trinidad & Tobago"
            country_flag = "\U0001F1F9\U0001F1F9"
        elif country == "TV":
            full_country_name = "Tuvalu"
            country_flag = "\U0001F1F9\U0001F1FB"
        elif country == "TW":
            full_country_name = "Taiwan"
            country_flag = "\U0001F1F9\U0001F1FC"
        elif country == "TZ":
            full_country_name = "Tanzania"
            country_flag = "\U0001F1F9\U0001F1FF"
        # U-countries
        elif country == "UA":
            full_country_name = "Ukraine"
            country_flag = "\U0001F1FA\U0001F1E6"
        elif country == "UG":
            full_country_name = "Uganda"
            country_flag = "\U0001F1FA\U0001F1EC"
        elif country == "UY":
            full_country_name = "Uruguay"
            country_flag = "\U0001F1FA\U0001F1FE"
        elif country == "UZ":
            full_country_name = "Uzbekistan"
            country_flag = "\U0001F1FA\U0001F1FF"
        # V-countries
        elif country == "VA":
            full_country_name = "Vatican City"
            country_flag = "\U0001F1FB\U0001F1E6"
        elif country == "VC":
            full_country_name = "St. Vincent & Grenadines"
            country_flag = "\U0001F1FB\U0001F1E8"
        elif country == "VE":
            full_country_name = "Venezuela"
            country_flag = "\U0001F1FB\U0001F1EA"
        elif country == "VG":
            full_country_name = "British Virgin Islands"
            country_flag = "\U0001F1FB\U0001F1EC"
        elif country == "VI":
            full_country_name = "U.S Virgin Islands"
            country_flag = "\U0001F1FB\U0001F1EE"
        elif country == "VN":
            full_country_name = "Vietnam"
            country_flag = "\U0001F1FB\U0001F1F3"
        elif country == "VU":
            full_country_name = "Vanuatu"
            country_flag = "\U0001F1FB\U0001F1FA"
        # W-countries
        elif country == "WF":
            full_country_name = "Wallis & Futuna"
            country_flag = "\U0001F1FC\U0001F1EB"
        elif country == "WS":
            full_country_name = "Samoa"
            country_flag = "\U0001F1FC\U0001F1F8"
        # X-countries
        elif country == "XK":
            full_country_name = "Kosovo"
            country_flag = "\U0001F1FD\U0001F1F0"
        # Y - countries
        elif country == "YE":
            full_country_name = "Yemen"
            country_flag = "\U0001F1FE\U0001F1EA"
        elif country == "YT":
            full_country_name = "Mayotte"
            country_flag = "\U0001F1FE\U0001F1F9"
        # Z-countries
        elif country == "ZA":
            full_country_name = "South Africa"
            country_flag = "\U0001F1FF\U0001F1E6"
        elif country == "ZM":
            full_country_name = "Zambia"
            country_flag = "\U0001F1FF\U0001F1F2"
        elif country == "ZW":
            full_country_name = "Zimbabwe"
            country_flag = "\U0001F1FF\U0001F1FC"

        else:
            full_country_name = country
            country_flag = ""

        if weather_description in json_to_smile:
            wd = json_to_smile[weather_description]
        else:
            wd = "I couldn't recognize the weather condition in this place. Maybe you can? \U0001F914"

        w_dir = ["North", "North North East", "North East", "East North East", "East", "East South East", "South East",
                 "South South East",
                 "South", "South South West", "South West", "West South West", "West", "West North West", "North West",
                 "North North West"]
        ix = int((wind_degree + 11.25) / 22.5)
        w_dir1 = w_dir[ix % 16]

        if tz == 0:
            tzsunr = sunr
            tzsuns = suns
            tz_loc_time = loc_time
        elif tz > 0:
            tzsunr = sunr + tz
            tzsuns = suns + tz
            tz_loc_time = loc_time + tz
        elif tz < 0:
            tzsunr = sunr + tz
            tzsuns = suns + tz
            tz_loc_time = loc_time + tz
        else:
            print("A timezone error occurred")

        tl = datetime.datetime.fromtimestamp(tz_loc_time)
        ts1 = datetime.datetime.fromtimestamp(tzsunr)
        ts2 = datetime.datetime.fromtimestamp(tzsuns)

        if ts1.hour <= tl.hour < ts2.hour:
            day_emoji = "\U00002600"
        else:
            day_emoji = "\U0001F319"

        if ap_lvl == 1:
            ap_text = "Good"
        elif ap_lvl == 2:
            ap_text = "Fair"
        elif ap_lvl == 3:
            ap_text = "Moderate"
        elif ap_lvl == 4:
            ap_text = "Poor"
        elif ap_lvl == 5:
            ap_text = "Very Poor"

        if y < 1:
            tz_loc_time = tl.strftime("%H:%M")
            tzsunr = ts1.strftime("%H:%M")
            tzsuns = ts2.strftime("%H:%M")
        elif y >= 1:
            tz_loc_time = tl.strftime("%I:%M %p")
            tzsunr = ts1.strftime("%I:%M %p")
            tzsuns = ts2.strftime("%I:%M %p")

        tz_loc_time_1 = tl.strftime("%d.%m.%Y")

        if uvi == 0:
            uvi_text = "Harmless"
        elif uvi == 1 or 2:
            uvi_text = "Low"
        elif uvi == 3 or 4 or 5:
            uvi_text = "Moderate"
        elif uvi == 6 or 7:
            uvi_text = "High"
        elif uvi == 8 or 9 or 10:
            uvi_text = "Very High"
        else:
            uvi_text = "Extreme risk"

        if country == "US":
            full_country_name = "USA"
            country_flag = "\U0001F1FA\U0001F1F8"
            us_state = data1[0]["state"]
            if us_state == "00":
                await message.reply(
                    f"\U0001F310 Local time: \n{tz_loc_time_1}, {tz_loc_time}{day_emoji}\n"
                    f"\U0001F305 Sunrise at: {tzsunr}\n\U0001F307 Sunset at: {tzsuns}\n"
                    f"\U0001F4CD Coordinates: \n{lat}° N,  {lon}° W\n"
                    f"\nAt the moment, the weather in {city}, {full_country_name}{country_flag} is:\n\n\U0001F321"
                    f"Temperature: {current_w}{format_sign},  {wd}\n"
                    f"\U0001F4C8Max Temperature for Today: {max_temp}{format_sign}\n\U0001F4C9"
                    f"Min Temperature for Today: {min_temp}"
                    f"{format_sign}\n"
                    f"\U0001F321Feels like: {fls_like}{format_sign}\n"
                    f"\U0001F33FDew point: {dew_p}{format_sign}\n"
                    f"\U0001F4A6Humidity: {humidity}%\n"
                    f"\U0001F4A8Wind speed: {wind_sp} {ws_sign}\n"
                    f"\U0001F9EDWind Direction: {w_dir1}\n\U0001F32BVisibility: {vis} km\n"
                    f"\U0001F30EAtmospheric pressure: {pressure} hPa\n"
                    f"\U0001F3EDAir pollution level: {ap_lvl} ({ap_text})\n"
                    f"\U00003030UV Index: {uvi} ({uvi_text})\n"
                    f"\nThanks for using Weather Bot!\U0001F601"
                )
            else:
                await message.reply(
                    f"\U0001F310 Local time: \n{tz_loc_time_1}, {tz_loc_time}{day_emoji}\n"
                    f"\U0001F305 Sunrise at: {tzsunr}\n\U0001F307 Sunset at: {tzsuns}\n"
                    f"\U0001F4CD Coordinates: \n{lat}° N,  {lon}° W\n"
                    f"\nAt the moment, the weather in {city}, {us_state}, {full_country_name}{country_flag} is:"
                    f"\n\n\U0001F321"
                    f"Temperature: {current_w}{format_sign},  {wd}\n"
                    f"\U0001F4C8Max Temperature for Today: {max_temp}{format_sign}\n\U0001F4C9"
                    f"Min Temperature for Today: {min_temp}"
                    f"{format_sign}\n"
                    f"\U0001F321Feels like: {fls_like}{format_sign}\n"
                    f"\U0001F33FDew point: {dew_p}{format_sign}\n"
                    f"\U0001F4A6Humidity: {humidity}%\n"
                    f"\U0001F4A8Wind speed: {wind_sp} {ws_sign}\n"
                    f"\U0001F9EDWind Direction: {w_dir1}\n\U0001F32BVisibility: {vis} km\n"
                    f"\U0001F30EAtmospheric pressure: {pressure} hPa\n"
                    f"\U0001F3EDAir pollution level: {ap_lvl} ({ap_text})\n"
                    f"\U00003030UV Index: {uvi} ({uvi_text})\n"
                    f"\nThanks for using Weather Bot!\U0001F601"
                )
        else:
            await message.reply(
                f"\U0001F310 Local time: \n{tz_loc_time_1}, {tz_loc_time}{day_emoji}\n"
                f"\U0001F305 Sunrise at: {tzsunr}\n\U0001F307 Sunset at: {tzsuns}\n"
                f"\U0001F4CD Coordinates: \n{lat}° N,  {lon}° W\n"
                f"\nAt the moment, the weather in {city}, {full_country_name}{country_flag} is:\n\n\U0001F321"
                f"Temperature: {current_w}{format_sign},  {wd}\n"
                f"\U0001F4C8Max Temperature for Today: {max_temp}{format_sign}\n\U0001F4C9"
                f"Min Temperature for Today: {min_temp}"
                f"{format_sign}\n"
                f"\U0001F321Feels like: {fls_like}{format_sign}\n"
                f"\U0001F33FDew point: {dew_p}{format_sign}\n"
                f"\U0001F4A6Humidity: {humidity}%\n"
                f"\U0001F4A8Wind speed: {wind_sp} {ws_sign}\n"
                f"\U0001F9EDWind Direction: {w_dir1}\n\U0001F32BVisibility: {vis} km\n"
                f"\U0001F30EAtmospheric pressure: {pressure} hPa\n"
                f"\U0001F3EDAir pollution level: {ap_lvl} ({ap_text})\n"
                f"\U00003030UV Index: {uvi} ({uvi_text})\n"
                f"\nThanks for using Weather Bot!\U0001F601"
            )

    except Exception as ex:
        await message.reply("City or place are not found. Could you check your input once again please? \U0001F643")
        print(ex)


@dp.message_handler()
async def get_weather_rus(message: types.Message):
    global country_flag, full_country_name, tzsuns, tzsunr, tz_loc_time, us_state1, us_state_rus, ap_text1
    json_to_smile = {
        "Clear": "Ясно \U00002600",
        "Rain": "Дождь \U00002614",
        "Clouds": "Пасмурно \U00002601",
        "Drizzle": "Морось \U0001F326",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Fog": "Туман \U0001F32B",
        "Tornado": "Торнадо \U0001F32A",
        "Mist": "Дымка \U0001F301",
        "Haze": "Мгла \U0001F636\U0000200D\U0001F32B\U0000FE0F",
        "Few clouds": "Облачно \U0001F324"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}, {message.text}&appid={ow_token}"
            f"&units={tformat}&lang=ru"
        )
        data = r.json()
        pprint(data)
        r1 = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={message.text},{message.text}"
            f"&limit=3&appid={ow_token}"
        )
        data2 = r1.json()
        pprint(data2)
        city = data["name"]
        current_w = round(data["main"]["temp"])
        wind_sp = round(data["wind"]["speed"])
        pressure = data["main"]["pressure"]
        sunr = data["sys"]["sunrise"]
        suns = data["sys"]["sunset"]
        fls_like = round(data["main"]["feels_like"])
        humidity = data["main"]["humidity"]
        max_temp = round(data["main"]["temp_max"])
        min_temp = round(data["main"]["temp_min"])
        country = data["sys"]["country"]
        weather_description = data["weather"][0]["main"]
        wind_degree = data["wind"]["deg"]
        vis = data["visibility"]
        tz = data["timezone"]
        loc_time = data["dt"]
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]

        r2 = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,"
                          f"hourly,daily,alerts&units={tformat}&appid={ow_token}")
        data1 = r2.json()
        # pprint(data1)
        dew_p = round(data1["current"]["dew_point"])
        uvi = round(data1["current"]["uvi"])

        r3 = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={ow_token}")
        data3 = r3.json()
        # pprint(data3)
        ap_lvl = data3["list"][0]["main"]["aqi"]

        vis = round(vis / 1000)

        # A-countries
        if country == "AC":
            full_country_name = "Остров Вознесения"
            country_flag = "\U0001F1E6\U0001F1E8"
        elif country == "AD":
            full_country_name = "Андорра"
            country_flag = "\U0001F1E6\U0001F1E9"
        elif country == "AE":
            full_country_name = "ОАЭ"
            country_flag = "\U0001F1E6\U0001F1EA"
        elif country == "AF":
            full_country_name = "Афганистан"
            country_flag = "\U0001F1E6\U0001F1EB"
        elif country == "AG":
            full_country_name = "Антигуа и Барбуда"
            country_flag = "\U0001F1E6\U0001F1EC"
        elif country == "AI":
            full_country_name = "Ангилья"
            country_flag = "\U0001F1E6\U0001F1EE"
        elif country == "AL":
            full_country_name = "Албания"
            country_flag = "\U0001F1E6\U0001F1F1"
        elif country == "AM":
            full_country_name = "Армения"
            country_flag = "\U0001F1E6\U0001F1F2"
        elif country == "AO":
            full_country_name = "Ангола"
            country_flag = "\U0001F1E6\U0001F1F4"
        elif country == "AQ":
            full_country_name = "Антарктида"
            country_flag = "\U0001F1E6\U0001F1F6"
        elif country == "AR":
            full_country_name = "Аргентина"
            country_flag = "\U0001F1E6\U0001F1F7"
        elif country == "AS":
            full_country_name = "Американское Самоа"
            country_flag = "\U0001F1E6\U0001F1F8"
        elif country == "AT":
            full_country_name = "Австрия"
            country_flag = "\U0001F1E6\U0001F1F9"
        elif country == "AU":
            full_country_name = "Австралия"
            country_flag = "\U0001F1E6\U0001F1FA"
        elif country == "AW":
            full_country_name = "Аруба"
            country_flag = "\U0001F1E6\U0001F1FC"
        elif country == "AX":
            full_country_name = "Аландские острова"
            country_flag = "\U0001F1E6\U0001F1FD"
        elif country == "AZ":
            full_country_name = "Азербайджан"
            country_flag = "\U0001F1E6\U0001F1FF"
        # B-countries
        elif country == "BA":
            full_country_name = "Босния и Герцеговина"
            country_flag = "\U0001F1E7\U0001F1E6"
        elif country == "BB":
            full_country_name = "Барбадос"
            country_flag = "\U0001F1E7\U0001F1E7"
        elif country == "BD":
            full_country_name = "Бангладеш"
            country_flag = "\U0001F1E7\U0001F1E9"
        elif country == "BE":
            full_country_name = "Бельгия"
            country_flag = "\U0001F1E7\U0001F1EA"
        elif country == "BF":
            full_country_name = "Буркина Фасо"
            country_flag = "\U0001F1E7\U0001F1EB"
        elif country == "BG":
            full_country_name = "Болгария"
            country_flag = "\U0001F1E7\U0001F1EC"
        elif country == "BH":
            full_country_name = "Бахрейн"
            country_flag = "\U0001F1E7\U0001F1ED"
        elif country == "BI":
            full_country_name = "Бурунди"
            country_flag = "\U0001F1E7\U0001F1EE"
        elif country == "BJ":
            full_country_name = "Бенин"
            country_flag = "\U0001F1E7\U0001F1EF"
        elif country == "BL":
            full_country_name = "Сен-Бартелеми"
            country_flag = "\U0001F1E7\U0001F1F1"
        elif country == "BM":
            full_country_name = "Бермуды"
            country_flag = "\U0001F1E7\U0001F1F2"
        elif country == "BN":
            full_country_name = "Бруней"
            country_flag = "\U0001F1E7\U0001F1F3"
        elif country == "BO":
            full_country_name = "Боливия"
            country_flag = "\U0001F1E7\U0001F1F4"
        elif country == "BQ":
            full_country_name = "Карибские Нидерланды"
            country_flag = "\U0001F1E7\U0001F1F6"
        elif country == "BR":
            full_country_name = "Бразилия"
            country_flag = "\U0001F1E7\U0001F1F7"
        elif country == "BS":
            full_country_name = "Багамы"
            country_flag = "\U0001F1E7\U0001F1F8"
        elif country == "BT":
            full_country_name = "Бутан"
            country_flag = "\U0001F1E7\U0001F1F9"
        elif country == "BV":
            full_country_name = "Остров Буве"
            country_flag = "\U0001F1E7\U0001F1FB"
        elif country == "BW":
            full_country_name = "Ботсвана"
            country_flag = "\U0001F1E7\U0001F1FC"
        elif country == "BY":
            full_country_name = "Беларусь"
            country_flag = "\U0001F1E7\U0001F1FE"
        elif country == "BZ":
            full_country_name = "Белиз"
            country_flag = "\U0001F1E7\U0001F1FF"
        # C-countries
        elif country == "CA":
            full_country_name = "Канада"
            country_flag = "\U0001F1E8\U0001F1E6"
        elif country == "CC":
            full_country_name = "Кокосовые острова"
            country_flag = "\U0001F1E8\U0001F1E8"
        elif country == "CD":
            full_country_name = "Демократическая Республика Конго"
            country_flag = "\U0001F1E8\U0001F1E9"
        elif country == "CF":
            full_country_name = "Центральная Африканская Республика"
            country_flag = "\U0001F1E8\U0001F1EB"
        elif country == "CG":
            full_country_name = "Республика Конго"
            country_flag = "\U0001F1E8\U0001F1EC"
        elif country == "CH":
            full_country_name = "Швейцария"
            country_flag = "\U0001F1E8\U0001F1ED"
        elif country == "CI":
            full_country_name = "Кот-д'Ивуар"
            country_flag = "\U0001F1E8\U0001F1EE"
        elif country == "CK":
            full_country_name = "Острова Кука"
            country_flag = "\U0001F1E8\U0001F1F0"
        elif country == "CL":
            full_country_name = "Чили"
            country_flag = "\U0001F1E8\U0001F1F1"
        elif country == "CM":
            full_country_name = "Камерун"
            country_flag = "\U0001F1E8\U0001F1F2"
        elif country == "CN":
            full_country_name = "Китай"
            country_flag = "\U0001F1E8\U0001F1F3"
        elif country == "CO":
            full_country_name = "Колумбия"
            country_flag = "\U0001F1E8\U0001F1F4"
        elif country == "CP":
            full_country_name = "Остров Клиппертон"
            country_flag = "\U0001F1E8\U0001F1F5"
        elif country == "CR":
            full_country_name = "Коста Рика"
            country_flag = "\U0001F1E8\U0001F1F7"
        elif country == "CU":
            full_country_name = "Куба"
            country_flag = "\U0001F1E8\U0001F1FA"
        elif country == "CV":
            full_country_name = "Кабо-Верде"
            country_flag = "\U0001F1E8\U0001F1FB"
        elif country == "CW":
            full_country_name = "Кюрасао"
            country_flag = "\U0001F1E8\U0001F1FC"
        elif country == "CX":
            full_country_name = "Остров Рождества"
            country_flag = "\U0001F1E8\U0001F1FD"
        elif country == "CY":
            full_country_name = "Кипр"
            country_flag = "\U0001F1E8\U0001F1FE"
        elif country == "CZ":
            full_country_name = "Чехия"
            country_flag = "\U0001F1E8\U0001F1FF"
        # D-countries
        elif country == "DE":
            full_country_name = "Германия"
            country_flag = "\U0001F1E9\U0001F1EA"
        elif country == "DG":
            full_country_name = "Диего Гарсия"
            country_flag = "\U0001F1E9\U0001F1EC"
        elif country == "DJ":
            full_country_name = "Джибути"
            country_flag = "\U0001F1E9\U0001F1EF"
        elif country == "DK":
            full_country_name = "Дания"
            country_flag = "\U0001F1E9\U0001F1F0"
        elif country == "DM":
            full_country_name = "Доминика"
            country_flag = "\U0001F1E9\U0001F1F2"
        elif country == "DO":
            full_country_name = "Доминиканская Республика"
            country_flag = "\U0001F1E9\U0001F1F4"
        elif country == "DZ":
            full_country_name = "Алжир"
            country_flag = "\U0001F1E9\U0001F1FF"
        # E-countries
        elif country == "EA":
            full_country_name = "Сеута и Мелилья"
            country_flag = "\U0001F1EA\U0001F1E6"
        elif country == "EC":
            full_country_name = "Эквадор"
            country_flag = "\U0001F1EA\U0001F1E8"
        elif country == "EE":
            full_country_name = "Эстония"
            country_flag = "\U0001F1EA\U0001F1EA"
        elif country == "EG":
            full_country_name = "Египет"
            country_flag = "\U0001F1EA\U0001F1EC"
        elif country == "EH":
            full_country_name = "Западная Сахара"
            country_flag = "\U0001F1EA\U0001F1ED"
        elif country == "ER":
            full_country_name = "Эритрея"
            country_flag = "\U0001F1EA\U0001F1F7"
        elif country == "ES":
            full_country_name = "Испания"
            country_flag = "\U0001F1EA\U0001F1F8"
        elif country == "ET":
            full_country_name = "Эфиопия"
            country_flag = "\U0001F1EA\U0001F1F9"
        # elif country == "EU":
        # full_country_name = "European Union"
        # country_flag = "\U0001F1EA\U0001F1FA"
        # F-countries
        elif country == "FI":
            full_country_name = "Финляндия"
            country_flag = "\U0001F1EB\U0001F1EE"
        elif country == "FJ":
            full_country_name = "Фиджи"
            country_flag = "\U0001F1EB\U0001F1EF"
        elif country == "FK":
            full_country_name = "Фолклендские острова"
            country_flag = "\U0001F1EB\U0001F1F0"
        elif country == "FM":
            full_country_name = "Микронезия"
            country_flag = "\U0001F1EB\U0001F1F2"
        elif country == "FO":
            full_country_name = "Фарерские острова"
            country_flag = "\U0001F1EB\U0001F1F4"
        elif country == "FR":
            full_country_name = "Франция"
            country_flag = "\U0001F1EB\U0001F1F7"
        # G-countries
        elif country == "GA":
            full_country_name = "Габон"
            country_flag = "\U0001F1EC\U0001F1E6"
        elif country == "GB":
            full_country_name = "Великобритания"
            country_flag = "\U0001F1EC\U0001F1E7"
        elif country == "GD":
            full_country_name = "Гренада"
            country_flag = "\U0001F1EC\U0001F1E9"
        elif country == "GE":
            full_country_name = "Грузия"
            country_flag = "\U0001F1EC\U0001F1EA"
        elif country == "GF":
            full_country_name = "Французская Гвиана"
            country_flag = "\U0001F1EC\U0001F1EB"
        elif country == "GG":
            full_country_name = "Гернси"
            country_flag = "\U0001F1EC\U0001F1EC"
        elif country == "GH":
            full_country_name = "Гана"
            country_flag = "\U0001F1EC\U0001F1ED"
        elif country == "GI":
            full_country_name = "Гибралтар"
            country_flag = "\U0001F1EC\U0001F1EE"
        elif country == "GL":
            full_country_name = "Гренландия"
            country_flag = "\U0001F1EC\U0001F1F1"
        elif country == "GM":
            full_country_name = "Гамбия"
            country_flag = "\U0001F1EC\U0001F1F2"
        elif country == "GN":
            full_country_name = "Гвинея"
            country_flag = "\U0001F1EC\U0001F1F3"
        elif country == "GP":
            full_country_name = "Гваделупа"
            country_flag = "\U0001F1EC\U0001F1F5"
        elif country == "GQ":
            full_country_name = "Экваториальная Гвинея"
            country_flag = "\U0001F1EC\U0001F1F6"
        elif country == "GR":
            full_country_name = "Греция"
            country_flag = "\U0001F1EC\U0001F1F7"
        elif country == "GS":
            full_country_name = "Южная Георгия и Южные Сандвичевы острова"
            country_flag = "\U0001F1EC\U0001F1F8"
        elif country == "GT":
            full_country_name = "Гватемала"
            country_flag = "\U0001F1EC\U0001F1F9"
        elif country == "GU":
            full_country_name = "Гуам"
            country_flag = "\U0001F1EC\U0001F1FA"
        elif country == "GW":
            full_country_name = "Гвинея-Бисау"
            country_flag = "\U0001F1EC\U0001F1FC"
        elif country == "GY":
            full_country_name = "Гайана"
            country_flag = "\U0001F1EC\U0001F1FE"
        # H-countries
        elif country == "HK":
            full_country_name = "Гонконг"
            country_flag = "\U0001F1ED\U0001F1F0"
        elif country == "HM":
            full_country_name = "Острова Херд и Макдональд"
            country_flag = "\U0001F1ED\U0001F1F2"
        elif country == "HN":
            full_country_name = "Гондурас"
            country_flag = "\U0001F1ED\U0001F1F3"
        elif country == "HR":
            full_country_name = "Хорватия"
            country_flag = "\U0001F1ED\U0001F1F7"
        elif country == "HT":
            full_country_name = "Гаити"
            country_flag = "\U0001F1ED\U0001F1F9"
        elif country == "HU":
            full_country_name = "Венгрия"
            country_flag = "\U0001F1ED\U0001F1FA"
        # I-countries
        elif country == "IC":
            full_country_name = "Канарские острова"
            country_flag = "\U0001F1EE\U0001F1E8"
        elif country == "ID":
            full_country_name = "Индонезия"
            country_flag = "\U0001F1EE\U0001F1E9"
        elif country == "IE":
            full_country_name = "Ирландия"
            country_flag = "\U0001F1EE\U0001F1EA"
        elif country == "IL":
            full_country_name = "Израиль"
            country_flag = "\U0001F1EE\U0001F1F1"
        elif country == "IM":
            full_country_name = "Остров Мэн"
            country_flag = "\U0001F1EE\U0001F1F2"
        elif country == "IN":
            full_country_name = "Индия"
            country_flag = "\U0001F1EE\U0001F1F3"
        elif country == "IO":
            full_country_name = "Британская территория Индийского океана"
            country_flag = "\U0001F1EE\U0001F1F4"
        elif country == "IQ":
            full_country_name = "Ирак"
            country_flag = "\U0001F1EE\U0001F1F6"
        elif country == "IR":
            full_country_name = "Иран"
            country_flag = "\U0001F1EE\U0001F1F7"
        elif country == "IS":
            full_country_name = "Исландия"
            country_flag = "\U0001F1EE\U0001F1F8"
        elif country == "IT":
            full_country_name = "Италия"
            country_flag = "\U0001F1EE\U0001F1F9"
        # J-countries
        elif country == "JE":
            full_country_name = "Джерси"
            country_flag = "\U0001F1EF\U0001F1EA"
        elif country == "JM":
            full_country_name = "Ямайка"
            country_flag = "\U0001F1EF\U0001F1F2"
        elif country == "JO":
            full_country_name = "Иордания"
            country_flag = "\U0001F1EF\U0001F1F4"
        elif country == "JP":
            full_country_name = "Япония"
            country_flag = "\U0001F1EF\U0001F1F5"
        # K-countries
        elif country == "KE":
            full_country_name = "Кения"
            country_flag = "\U0001F1F0\U0001F1EA"
        elif country == "KG":
            full_country_name = "Кыргызстан"
            country_flag = "\U0001F1F0\U0001F1EC"
        elif country == "KH":
            full_country_name = "Камбоджа"
            country_flag = "\U0001F1F0\U0001F1ED"
        elif country == "KI":
            full_country_name = "Кирибати"
            country_flag = "\U0001F1F0\U0001F1EE"
        elif country == "KM":
            full_country_name = "Коморские острова"
            country_flag = "\U0001F1F0\U0001F1F2"
        elif country == "KN":
            full_country_name = "Сент-Китс и Невис"
            country_flag = "\U0001F1F0\U0001F1F3"
        elif country == "KP":
            full_country_name = "Северная Корея"
            country_flag = "\U0001F1F0\U0001F1F5"
        elif country == "KR":
            full_country_name = "Южная Корея"
            country_flag = "\U0001F1F0\U0001F1F7"
        elif country == "KW":
            full_country_name = "Кувейт"
            country_flag = "\U0001F1F0\U0001F1FC"
        elif country == "KY":
            full_country_name = "Каймановы острова"
            country_flag = "\U0001F1F0\U0001F1FE"
        elif country == "KZ":
            full_country_name = "Казахстан"
            country_flag = "\U0001F1F0\U0001F1FF"
        # L-countries
        elif country == "LA":
            full_country_name = "Лаос"
            country_flag = "\U0001F1F1\U0001F1E6"
        elif country == "LB":
            full_country_name = "Ливан"
            country_flag = "\U0001F1F1\U0001F1E7"
        elif country == "LC":
            full_country_name = "Сент-Люсия"
            country_flag = "\U0001F1F1\U0001F1E8"
        elif country == "LI":
            full_country_name = "Лихтенштейн"
            country_flag = "\U0001F1F1\U0001F1EE"
        elif country == "LK":
            full_country_name = "Шри-Ланка"
            country_flag = "\U0001F1F1\U0001F1F0"
        elif country == "LR":
            full_country_name = "Либерия"
            country_flag = "\U0001F1F1\U0001F1F7"
        elif country == "LS":
            full_country_name = "Лесото"
            country_flag = "\U0001F1F1\U0001F1F8"
        elif country == "LT":
            full_country_name = "Литва"
            country_flag = "\U0001F1F1\U0001F1F9"
        elif country == "LU":
            full_country_name = "Люксембург"
            country_flag = "\U0001F1F1\U0001F1FA"
        elif country == "LV":
            full_country_name = "Латвия"
            country_flag = "\U0001F1F1\U0001F1FB"
        elif country == "LY":
            full_country_name = "Ливия"
            country_flag = "\U0001F1F1\U0001F1FE"
        # M-countries
        elif country == "MA":
            full_country_name = "Марокко"
            country_flag = "\U0001F1F2\U0001F1E6"
        elif country == "MC":
            full_country_name = "Монако"
            country_flag = "\U0001F1F2\U0001F1E8"
        elif country == "MD":
            full_country_name = "Молдова"
            country_flag = "\U0001F1F2\U0001F1E9"
        elif country == "ME":
            full_country_name = "Черногория"
            country_flag = "\U0001F1F2\U0001F1EA"
        elif country == "MF":
            full_country_name = "Сен-Мартен"
            country_flag = "\U0001F1F2\U0001F1EB"
        elif country == "MG":
            full_country_name = "Мадагаскар"
            country_flag = "\U0001F1F2\U0001F1EC"
        elif country == "MH":
            full_country_name = "Маршалловы острова"
            country_flag = "\U0001F1F2\U0001F1ED"
        elif country == "MK":
            full_country_name = "Северная Македония"
            country_flag = "\U0001F1F2\U0001F1F0"
        elif country == "ML":
            full_country_name = "Мали"
            country_flag = "\U0001F1F2\U0001F1F1"
        elif country == "MM":
            full_country_name = "Мьянма"
            country_flag = "\U0001F1F2\U0001F1F2"
        elif country == "MN":
            full_country_name = "Монголия"
            country_flag = "\U0001F1F2\U0001F1F3"
        elif country == "MO":
            full_country_name = "Макао"
            country_flag = "\U0001F1F2\U0001F1F4"
        elif country == "MP":
            full_country_name = "Северные Марианские острова"
            country_flag = "\U0001F1F2\U0001F1F5"
        elif country == "MQ":
            full_country_name = "Мартиника"
            country_flag = "\U0001F1F2\U0001F1F6"
        elif country == "MR":
            full_country_name = "Мавритания"
            country_flag = "\U0001F1F2\U0001F1F7"
        elif country == "MS":
            full_country_name = "Монтсеррат"
            country_flag = "\U0001F1F2\U0001F1F8"
        elif country == "MT":
            full_country_name = "Мальта"
            country_flag = "\U0001F1F2\U0001F1F9"
        elif country == "MU":
            full_country_name = "Маврикий"
            country_flag = "\U0001F1F2\U0001F1FA"
        elif country == "MV":
            full_country_name = "Мальдивы"
            country_flag = "\U0001F1F2\U0001F1FB"
        elif country == "MW":
            full_country_name = "Малави"
            country_flag = "\U0001F1F2\U0001F1FC"
        elif country == "MX":
            full_country_name = "Мексика"
            country_flag = "\U0001F1F2\U0001F1FD"
        elif country == "MY":
            full_country_name = "Малайзия"
            country_flag = "\U0001F1F2\U0001F1FE"
        elif country == "MZ":
            full_country_name = "Мозамбик"
            country_flag = "\U0001F1F2\U0001F1FF"
        # N-countries
        elif country == "NA":
            full_country_name = "Намибия"
            country_flag = "\U0001F1F3\U0001F1E6"
        elif country == "NC":
            full_country_name = "Новая Каледония"
            country_flag = "\U0001F1F3\U0001F1E8"
        elif country == "NE":
            full_country_name = "Нигер"
            country_flag = "\U0001F1F3\U0001F1EA"
        elif country == "NF":
            full_country_name = "Остров Норфолк"
            country_flag = "\U0001F1F3\U0001F1EB"
        elif country == "NG":
            full_country_name = "Нигерия"
            country_flag = "\U0001F1F3\U0001F1EC"
        elif country == "NI":
            full_country_name = "Никарагуа"
            country_flag = "\U0001F1F3\U0001F1EE"
        elif country == "NL":
            full_country_name = "Нидерланды"
            country_flag = "\U0001F1F3\U0001F1F1"
        elif country == "NO":
            full_country_name = "Норвегия"
            country_flag = "\U0001F1F3\U0001F1F4"
        elif country == "NP":
            full_country_name = "Непал"
            country_flag = "\U0001F1F3\U0001F1F5"
        elif country == "NR":
            full_country_name = "Науру"
            country_flag = "\U0001F1F3\U0001F1F7"
        elif country == "NU":
            full_country_name = "Ниуэ"
            country_flag = "\U0001F1F3\U0001F1FA"
        elif country == "NZ":
            full_country_name = "Новая Зеландия"
            country_flag = "\U0001F1F3\U0001F1FF"
        # O-countries
        elif country == "OM":
            full_country_name = "Оман"
            country_flag = "\U0001F1F4\U0001F1F2"
        # P-countries
        elif country == "PA":
            full_country_name = "Панама"
            country_flag = "\U0001F1F5\U0001F1E6"
        elif country == "PE":
            full_country_name = "Перу"
            country_flag = "\U0001F1F5\U0001F1EA"
        elif country == "PG":
            full_country_name = "Папуа - Новая Гвинея"
            country_flag = "\U0001F1F5\U0001F1EC"
        elif country == "PH":
            full_country_name = "Филиппины"
            country_flag = "\U0001F1F5\U0001F1ED"
        elif country == "PK":
            full_country_name = "Пакистан"
            country_flag = "\U0001F1F5\U0001F1F0"
        elif country == "PL":
            full_country_name = "Польша"
            country_flag = "\U0001F1F5\U0001F1F1"
        elif country == "PM":
            full_country_name = "Сен-Пьер и Микелон"
            country_flag = "\U0001F1F5\U0001F1F2"
        elif country == "PN":
            full_country_name = "Острова Питкэрн"
            country_flag = "\U0001F1F5\U0001F1F3"
        elif country == "PR":
            full_country_name = "Пуэрто-Рико"
            country_flag = "\U0001F1F5\U0001F1F7"
        elif country == "PS":
            full_country_name = "Палестина"
            country_flag = "\U0001F1F5\U0001F1F8"
        elif country == "PT":
            full_country_name = "Португалия"
            country_flag = "\U0001F1F5\U0001F1F9"
        elif country == "PW":
            full_country_name = "Палау"
            country_flag = "\U0001F1F5\U0001F1FC"
        elif country == "PY":
            full_country_name = "Парагвай"
            country_flag = "\U0001F1F5\U0001F1FE"
        # Q-countries
        elif country == "QA":
            full_country_name = "Катар"
            country_flag = "\U0001F1F6\U0001F1E6"
        # R-countries
        elif country == "RE":
            full_country_name = "Реюньон"
            country_flag = "\U0001F1F7\U0001F1EA"
        elif country == "RO":
            full_country_name = "Румыния"
            country_flag = "\U0001F1F7\U0001F1F4"
        elif country == "RS":
            full_country_name = "Сербия"
            country_flag = "\U0001F1F7\U0001F1F8"
        elif country == "RU":
            full_country_name = "Россия"
            country_flag = "\U0001F1F7\U0001F1FA"
        elif country == "RW":
            full_country_name = "Руанда"
            country_flag = "\U0001F1F7\U0001F1FC"
        # S-countries
        elif country == "SA":
            full_country_name = "Саудовская Аравия"
            country_flag = "\U0001F1F8\U0001F1E6"
        elif country == "SB":
            full_country_name = "Соломоновы острова"
            country_flag = "\U0001F1F8\U0001F1E7"
        elif country == "SC":
            full_country_name = "Сейшельские острова"
            country_flag = "\U0001F1F8\U0001F1E8"
        elif country == "SD":
            full_country_name = "Судан"
            country_flag = "\U0001F1F8\U0001F1E9"
        elif country == "SE":
            full_country_name = "Швеция"
            country_flag = "\U0001F1F8\U0001F1EA"
        elif country == "SG":
            full_country_name = "Сингапур"
            country_flag = "\U0001F1F8\U0001F1EC"
        elif country == "SH":
            full_country_name = "Остров Св. Елены"
            country_flag = "\U0001F1F8\U0001F1EE"
        elif country == "SJ":
            full_country_name = "Шпицберген и Ян Майен"
            country_flag = "\U0001F1F8\U0001F1EF"
        elif country == "SK":
            full_country_name = "Словакия"
            country_flag = "\U0001F1F8\U0001F1F0"
        elif country == "SL":
            full_country_name = "Сьерра-Леоне"
            country_flag = "\U0001F1F8\U0001F1F1"
        elif country == "SM":
            full_country_name = "Сан-Марино"
            country_flag = "\U0001F1F8\U0001F1F2"
        elif country == "SN":
            full_country_name = "Сенегал"
            country_flag = "\U0001F1F8\U0001F1F3"
        elif country == "SO":
            full_country_name = "Сомали"
            country_flag = "\U0001F1F8\U0001F1F4"
        elif country == "SR":
            full_country_name = "Суринам"
            country_flag = "\U0001F1F8\U0001F1F7"
        elif country == "SS":
            full_country_name = "Южный Судан"
            country_flag = "\U0001F1F8\U0001F1F8"
        elif country == "ST":
            full_country_name = "Сан-Томе и Принсипи"
            country_flag = "\U0001F1F8\U0001F1F9"
        elif country == "SV":
            full_country_name = "Сальвадор"
            country_flag = "\U0001F1F8\U0001F1FB"
        elif country == "SX":
            full_country_name = "Синт-Мартен"
            country_flag = "\U0001F1F8\U0001F1FD"
        elif country == "SY":
            full_country_name = "Сирия"
            country_flag = "\U0001F1F8\U0001F1FE"
        elif country == "SZ":
            full_country_name = "Эсватини"
            country_flag = "\U0001F1F8\U0001F1FF"
        # T-countries
        elif country == "TA":
            full_country_name = "Тристан-да-Кунья"
            country_flag = "\U0001F1F9\U0001F1E6"
        elif country == "TC":
            full_country_name = "Острова Теркс и Кайкос"
            country_flag = "\U0001F1F9\U0001F1E8"
        elif country == "TD":
            full_country_name = "Чад"
            country_flag = "\U0001F1F9\U0001F1E9"
        elif country == "TF":
            full_country_name = "Южные Французские Территории"
            country_flag = "\U0001F1F9\U0001F1EB"
        elif country == "TG":
            full_country_name = "Того"
            country_flag = "\U0001F1F9\U0001F1EC"
        elif country == "TH":
            full_country_name = "Таиланд"
            country_flag = "\U0001F1F9\U0001F1ED"
        elif country == "TJ":
            full_country_name = "Таджикистан"
            country_flag = "\U0001F1F9\U0001F1EF"
        elif country == "TK":
            full_country_name = "Токелау"
            country_flag = "\U0001F1F9\U0001F1F0"
        elif country == "TL":
            full_country_name = "Тимор-Лешти"
            country_flag = "\U0001F1F9\U0001F1F1"
        elif country == "TM":
            full_country_name = "Туркменистан"
            country_flag = "\U0001F1F9\U0001F1F2"
        elif country == "TN":
            full_country_name = "Тунис"
            country_flag = "\U0001F1F9\U0001F1F3"
        elif country == "TO":
            full_country_name = "Тонга"
            country_flag = "\U0001F1F9\U0001F1F4"
        elif country == "TR":
            full_country_name = "Турция"
            country_flag = "\U0001F1F9\U0001F1F7"
        elif country == "TT":
            full_country_name = "Тринидад и Тобаго"
            country_flag = "\U0001F1F9\U0001F1F9"
        elif country == "TV":
            full_country_name = "Тувалу"
            country_flag = "\U0001F1F9\U0001F1FB"
        elif country == "TW":
            full_country_name = "Тайвань"
            country_flag = "\U0001F1F9\U0001F1FC"
        elif country == "TZ":
            full_country_name = "Танзания"
            country_flag = "\U0001F1F9\U0001F1FF"
        # U-countries
        elif country == "UA":
            full_country_name = "Украина"
            country_flag = "\U0001F1FA\U0001F1E6"
        elif country == "UG":
            full_country_name = "Уганда"
            country_flag = "\U0001F1FA\U0001F1EC"
        elif country == "UY":
            full_country_name = "Уругвай"
            country_flag = "\U0001F1FA\U0001F1FE"
        elif country == "UZ":
            full_country_name = "Узбекистан"
            country_flag = "\U0001F1FA\U0001F1FF"
        # V-countries
        elif country == "VA":
            full_country_name = "Ватикан"
            country_flag = "\U0001F1FB\U0001F1E6"
        elif country == "VC":
            full_country_name = "Сент-Винсент и Гренадины"
            country_flag = "\U0001F1FB\U0001F1E8"
        elif country == "VE":
            full_country_name = "Венесуэла"
            country_flag = "\U0001F1FB\U0001F1EA"
        elif country == "VG":
            full_country_name = "Британские Виргинские острова"
            country_flag = "\U0001F1FB\U0001F1EC"
        elif country == "VI":
            full_country_name = "Виргинские острова США"
            country_flag = "\U0001F1FB\U0001F1EE"
        elif country == "VN":
            full_country_name = "Вьетнам"
            country_flag = "\U0001F1FB\U0001F1F3"
        elif country == "VU":
            full_country_name = "Вануату"
            country_flag = "\U0001F1FB\U0001F1FA"
        # W-countries
        elif country == "WF":
            full_country_name = "Уоллис и Футуна"
            country_flag = "\U0001F1FC\U0001F1EB"
        elif country == "WS":
            full_country_name = "Самоа"
            country_flag = "\U0001F1FC\U0001F1F8"
        # X-countries
        elif country == "XK":
            full_country_name = "Косово"
            country_flag = "\U0001F1FD\U0001F1F0"
        # Y - countries
        elif country == "YE":
            full_country_name = "Йемен"
            country_flag = "\U0001F1FE\U0001F1EA"
        elif country == "YT":
            full_country_name = "Майотта"
            country_flag = "\U0001F1FE\U0001F1F9"
        # Z-countries
        elif country == "ZA":
            full_country_name = "Южная Африка"
            country_flag = "\U0001F1FF\U0001F1E6"
        elif country == "ZM":
            full_country_name = "Замбия"
            country_flag = "\U0001F1FF\U0001F1F2"
        elif country == "ZW":
            full_country_name = "Зимбабве"
            country_flag = "\U0001F1FF\U0001F1FC"

        else:
            full_country_name = country
            country_flag = ""

        if weather_description in json_to_smile:
            wd = json_to_smile[weather_description]
        else:
            wd = "У меня не получилось узнать погодные условия в этом месте. Может у вас получится? \U0001F914"

        w_dir = ["Северный", "Северо-Северо-Восточный", "Северо-Западный", "Восточно-Северо-Восточный", "Восточный",
                 "Восточно-Юго-Восточный", "Юго-Восточный", "Юго-Юго-Восточный",
                 "Южный", "Юго-Юго-Западный", "Юго-Западный", "Западный-Юго-Западный", "Западный",
                 "Северо-Западный", "Западный Северо-Западный",
                 "Северо-Северо-Западный"]
        ix = int((wind_degree + 11.25) / 22.5)
        w_dir1 = w_dir[ix % 16]

        if tz == 0:
            tzsunr = sunr
            tzsuns = suns
            tz_loc_time = loc_time
        elif tz > 0:
            tzsunr = sunr + tz
            tzsuns = suns + tz
            tz_loc_time = loc_time + tz
        elif tz < 0:
            tzsunr = sunr + tz
            tzsuns = suns + tz
            tz_loc_time = loc_time + tz
        else:
            print("A timezone error occurred1")

        tl = datetime.datetime.fromtimestamp(tz_loc_time)
        ts1 = datetime.datetime.fromtimestamp(tzsunr)
        ts2 = datetime.datetime.fromtimestamp(tzsuns)

        if ts1.hour <= tl.hour < ts2.hour:
            day_emoji = "\U00002600"
        else:
            day_emoji = "\U0001F319"

        tz_loc_time_1 = tl.strftime("%d.%m.%Y")

        if y < 1:
            tz_loc_time = tl.strftime("%H:%M")
            tzsunr = ts1.strftime("%H:%M")
            tzsuns = ts2.strftime("%H:%M")
        elif y >= 1:
            tz_loc_time = tl.strftime("%I:%M %p")
            tzsunr = ts1.strftime("%I:%M %p")
            tzsuns = ts2.strftime("%I:%M %p")

        if ap_lvl == 1:
            ap_text1 = "Хороший"
        elif ap_lvl == 2:
            ap_text1 = "Удовлетворительный"
        elif ap_lvl == 3:
            ap_text1 = "Умеренный"
        elif ap_lvl == 4:
            ap_text1 = "Загрязненный"
        elif ap_lvl == 5:
            ap_text1 = "Очень загрязненный"

        if uvi == 0:
            uvi_text = "Безопасный"
        elif uvi == 1 or 2:
            uvi_text = "Низкий"
        elif uvi == 3 or 4 or 5:
            uvi_text = "Умеренный"
        elif uvi == 6 or 7:
            uvi_text = "Высокий"
        elif uvi == 8 or 9 or 10:
            uvi_text = "Очень высокий"
        else:
            uvi_text = "Чрезмерный"

        if country == "US":
            full_country_name = "США"
            country_flag = "\U0001F1FA\U0001F1F8"
            us_state1 = data2[0]["state"]
            if us_state1 == "Alabama":
                us_state_rus = "Алабама"
            elif us_state1 == "Alaska":
                us_state_rus = "Аляска"
            elif us_state1 == "Arizona":
                us_state_rus = "Аризона"
            elif us_state1 == "Arkansas":
                us_state_rus = "Арканзас"
            elif us_state1 == "California":
                us_state_rus = "Калифорния"
            elif us_state1 == "Colorado":
                us_state_rus = "Колорадо"
            elif us_state1 == "Connecticut":
                us_state_rus = "Коннектикут"
            elif us_state1 == "Delaware":
                us_state_rus = "Дэлавер"
            elif us_state1 == "District of Columbia":
                us_state_rus = "округ Колумбия"
            elif us_state1 == "Florida":
                us_state_rus = "Флорида"
            elif us_state1 == "Georgia":
                us_state_rus = "Джорджия"
            elif us_state1 == "Hawaii":
                us_state_rus = "Гавайи"
            elif us_state1 == "Idaho":
                us_state_rus = "Айдахо"
            elif us_state1 == "Illinois":
                us_state_rus = "Иллинойс"
            elif us_state1 == "Indiana":
                us_state_rus = "Индиана"
            elif us_state1 == "Iowa":
                us_state_rus = "Айова"
            elif us_state1 == "Kansas":
                us_state_rus = "Канзас"
            elif us_state1 == "Kentucky":
                us_state_rus = "Кентукки"
            elif us_state1 == "Louisiana":
                us_state_rus = "Луизиана"
            elif us_state1 == "Maine":
                us_state_rus = "Мэн"
            elif us_state1 == "Maryland":
                us_state_rus = "Мэрилэнд"
            elif us_state1 == "Massachusetts":
                us_state_rus = "Массачусетс"
            elif us_state1 == "Michigan":
                us_state_rus = "Мичиган"
            elif us_state1 == "Minnesota":
                us_state_rus = "Миннесота"
            elif us_state1 == "Mississippi":
                us_state_rus = "Миссисипи"
            elif us_state1 == "Missouri":
                us_state_rus = "Миссури"
            elif us_state1 == "Montana":
                us_state_rus = "Монтана"
            elif us_state1 == "Nebraska":
                us_state_rus = "Небраска"
            elif us_state1 == "Nevada":
                us_state_rus = "Невада"
            elif us_state1 == "New Hampshire":
                us_state_rus = "Нью-Гэмпшир"
            elif us_state1 == "New Jersey":
                us_state_rus = "Нью-Джерси"
            elif us_state1 == "New Mexico":
                us_state_rus = "Нью-Мексико"
            elif us_state1 == "New York":
                us_state_rus = "Нью-Йорк"
            elif us_state1 == "North Carolina":
                us_state_rus = "Северная Каролина"
            elif us_state1 == "North Dakota":
                us_state_rus = "Северная Дакота"
            elif us_state1 == "Ohio":
                us_state_rus = "Огайо"
            elif us_state1 == "Oklahoma":
                us_state_rus = "Оклахома"
            elif us_state1 == "Oregon":
                us_state_rus = "Орегон"
            elif us_state1 == "Pennsylvania":
                us_state_rus = "Пенсильвания"
            elif us_state1 == "Rhode-Island":
                us_state_rus = "Род-Айленд"
            elif us_state1 == "South Carolina":
                us_state_rus = "Южная Каролина"
            elif us_state1 == "South Dakota":
                us_state_rus = "Южная Дакота"
            elif us_state1 == "Tennessee":
                us_state_rus = "Теннесси"
            elif us_state1 == "Texas":
                us_state_rus = "Техас"
            elif us_state1 == "Utah":
                us_state_rus = "Юта"
            elif us_state1 == "Vermont":
                us_state_rus = "Вермонт"
            elif us_state1 == "Virginia":
                us_state_rus = "Виргиния"
            elif us_state1 == "Washington":
                us_state_rus = "Вашингтон"
            elif us_state1 == "West Virginia":
                us_state_rus = "Южная Виргиния"
            elif us_state1 == "Wisconsin":
                us_state_rus = "Висконсин"
            elif us_state1 == "Wyoming":
                us_state_rus = "Вайоминг"
            elif us_state1 == "00":
                us_state_rus = ""
            if us_state1 == "00":
                await message.reply(
                    f"\U0001F310 Местное время: \n{tz_loc_time_1}, {tz_loc_time}{day_emoji}\n"
                    f"\U0001F305 Восход солнца в: {tzsunr}\n\U0001F307 Закат солнца в: {tzsuns}\n"
                    f"\U0001F4CD Координаты: \n{lat}° с. ш.,  {lon}° в. д.\n"
                    f"\nНа данный момент, погода в {city}, {full_country_name}{country_flag}"
                    f":\n\n\U0001F321"
                    f"Температура: {current_w}{format_sign},  {wd}\n"
                    f"\U0001F4C8Макс. температура за сегодня: {max_temp}{format_sign}\n\U0001F4C9"
                    f"Мин. температура за сегодня: {min_temp}{format_sign}\n"
                    f"\U0001F321Ощущается как: {fls_like}{format_sign}\n"
                    f"\U0001F33FТочка росы: {dew_p}{format_sign}\n"
                    f"\U0001F4A6Влажность: {humidity}%\n"
                    f"\U0001F4A8Скорость ветра: {wind_sp} {ws_sign}\n"
                    f"\U0001F9EDНаправление ветра: {w_dir1}\n\U0001F32BВидимость: {vis} км\n"
                    f"\U0001F30EАтмосферное давление: {pressure} гПА\n"
                    f"\U0001F3EDУровень загрязнения воздуха: {ap_lvl} ({ap_text1})\n"
                    f"\U00003030УФ-индекс: {uvi} ({uvi_text})\n"
                    f"\nСпасибо, что используете Weather Bot!\U0001F601"
                )
            else:
                await message.reply(
                    f"\U0001F310 Местное время: \n{tz_loc_time_1}, {tz_loc_time}{day_emoji}\n"
                    f"\U0001F305 Восход солнца в: {tzsunr}\n\U0001F307 Закат солнца в: {tzsuns}\n"
                    f"\U0001F4CD Координаты: \n{lat}° с. ш.,  {lon}° в. д.\n"
                    f"\nНа данный момент, погода в {city}, {us_state_rus}, {full_country_name}{country_flag}"
                    f":\n\n\U0001F321"
                    f"Температура: {current_w}{format_sign},  {wd}\n"
                    f"\U0001F4C8Макс. температура за сегодня: {max_temp}{format_sign}\n\U0001F4C9"
                    f"Мин. температура за сегодня: {min_temp}{format_sign}\n"
                    f"\U0001F321Ощущается как: {fls_like}{format_sign}\n"
                    f"\U0001F33FТочка росы: {dew_p}{format_sign}\n"
                    f"\U0001F4A6Влажность: {humidity}%\n"
                    f"\U0001F4A8Скорость ветра: {wind_sp} {ws_sign}\n"
                    f"\U0001F9EDНаправление ветра: {w_dir1}\n\U0001F32BВидимость: {vis} км\n"
                    f"\U0001F30EАтмосферное давление: {pressure} гПА\n"
                    f"\U0001F3EDУровень загрязнения воздуха: {ap_lvl} ({ap_text1})\n"
                    f"\U00003030УФ-индекс: {uvi} ({uvi_text})\n"
                    f"\nСпасибо, что используете Weather Bot!\U0001F601"
                )
        else:
            await message.reply(
                f"\U0001F310 Местное время: \n{tz_loc_time_1}, {tz_loc_time}{day_emoji}\n"
                f"\U0001F305 Восход солнца в: {tzsunr}\n\U0001F307 Закат солнца в: {tzsuns}\n"
                f"\U0001F4CD Координаты: \n{lat}° с. ш.,  {lon}° в. д.\n"
                f"\nНа данный момент, погода в {city}, {full_country_name}{country_flag}:\n\n\U0001F321"
                f"Температура: {current_w}{format_sign},  {wd}\n"
                f"\U0001F4C8Макс. температура за сегодня: {max_temp}{format_sign}\n\U0001F4C9"
                f"Мин. температура за сегодня: {min_temp}{format_sign}\n"
                f"\U0001F321Ощущается как: {fls_like}{format_sign}\n"
                f"\U0001F33FТочка росы: {dew_p}{format_sign}\n"
                f"\U0001F4A6Влажность: {humidity}%\n"
                f"\U0001F4A8Скорость ветра: {wind_sp} {ws_sign}\n"
                f"\U0001F9EDНаправление ветра: {w_dir1}\n\U0001F32BВидимость: {vis} км\n"
                f"\U0001F30EАтмосферное давление: {pressure} гПА\n"
                f"\U0001F3EDУровень загрязнения воздуха: {ap_lvl} ({ap_text1})\n"
                f"\U00003030УФ-индекс: {uvi} ({uvi_text})\n"
                f"\nСпасибо, что используете Weather Bot!\U0001F601"
            )

    except Exception as ex:
        await message.reply(
            "Введенное вами город или место не найдены. Не могли бы вы проверить свой ввод еще раз? \U0001F643")
        print(ex)


@dp.message_handler()
async def get_weather_pol(message: types.Message):
    global country_flag, full_country_name, tzsuns, tzsunr, tz_loc_time, us_state2, us_state_pol, ap_text2, password_check
    json_to_smile = {
        "Clear": "Bezchmurny \U00002600",
        "Rain": "Deszcz \U00002614",
        "Clouds": "Zachmurzenie \U00002601",
        "Drizzle": "Mżawka \U0001F326",
        "Thunderstorm": "Burza \U000026A1",
        "Snow": "Śnieg \U0001F328",
        "Fog": "Mgiełka \U0001F32B",
        "Tornado": "Tornado \U0001F32A",
        "Mist": "Dymek \U0001F301",
        "Haze": "Mgła \U0001F636\U0000200D\U0001F32B\U0000FE0F",
        "Few clouds": "Pochmurny \U0001F324"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}, {message.text}&appid={ow_token}"
            f"&units={tformat}&lang=pl"
        )
        data = r.json()
        pprint(data)
        r1 = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={message.text},{message.text}"
            f"&limit=3&appid={ow_token}"
        )
        data2 = r1.json()
        pprint(data2)
        city = data["name"]
        current_w = round(data["main"]["temp"])
        wind_sp = round(data["wind"]["speed"])
        pressure = data["main"]["pressure"]
        sunr = data["sys"]["sunrise"]
        suns = data["sys"]["sunset"]
        fls_like = round(data["main"]["feels_like"])
        humidity = data["main"]["humidity"]
        max_temp = round(data["main"]["temp_max"])
        min_temp = round(data["main"]["temp_min"])
        country = data["sys"]["country"]
        weather_description = data["weather"][0]["main"]
        wind_degree = data["wind"]["deg"]
        vis = data["visibility"]
        tz = data["timezone"]
        loc_time = data["dt"]
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]

        r2 = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,"
                          f"hourly,daily,alerts&units={tformat}&appid={ow_token}")
        data1 = r2.json()
        # pprint(data1)
        dew_p = round(data1["current"]["dew_point"])
        uvi = round(data1["current"]["uvi"])

        r3 = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={ow_token}")
        data3 = r3.json()
        # pprint(data3)
        ap_lvl = data3["list"][0]["main"]["aqi"]

        vis = round(vis / 1000)

        # A-countries
        if country == "AC":
            full_country_name = "Wyspa Wniebowstąpienia"
            country_flag = "\U0001F1E6\U0001F1E8"
        elif country == "AD":
            full_country_name = "Andora"
            country_flag = "\U0001F1E6\U0001F1E9"
        elif country == "AE":
            full_country_name = "ZEA"
            country_flag = "\U0001F1E6\U0001F1EA"
        elif country == "AF":
            full_country_name = "Afganistan"
            country_flag = "\U0001F1E6\U0001F1EB"
        elif country == "AG":
            full_country_name = "Antigua i Barbuda"
            country_flag = "\U0001F1E6\U0001F1EC"
        elif country == "AI":
            full_country_name = "Anguilla"
            country_flag = "\U0001F1E6\U0001F1EE"
        elif country == "AL":
            full_country_name = "Albania"
            country_flag = "\U0001F1E6\U0001F1F1"
        elif country == "AM":
            full_country_name = "Armenia"
            country_flag = "\U0001F1E6\U0001F1F2"
        elif country == "AO":
            full_country_name = "Angola"
            country_flag = "\U0001F1E6\U0001F1F4"
        elif country == "AQ":
            full_country_name = "Antarktyda"
            country_flag = "\U0001F1E6\U0001F1F6"
        elif country == "AR":
            full_country_name = "Argentyna"
            country_flag = "\U0001F1E6\U0001F1F7"
        elif country == "AS":
            full_country_name = "Samoa Amerykańskie"
            country_flag = "\U0001F1E6\U0001F1F8"
        elif country == "AT":
            full_country_name = "Austria"
            country_flag = "\U0001F1E6\U0001F1F9"
        elif country == "AU":
            full_country_name = "Australia"
            country_flag = "\U0001F1E6\U0001F1FA"
        elif country == "AW":
            full_country_name = "Aruba"
            country_flag = "\U0001F1E6\U0001F1FC"
        elif country == "AX":
            full_country_name = "Wyspy Alandzkie"
            country_flag = "\U0001F1E6\U0001F1FD"
        elif country == "AZ":
            full_country_name = "Azerbejdżan"
            country_flag = "\U0001F1E6\U0001F1FF"
        # B-countries
        elif country == "BA":
            full_country_name = "Босния и Герцеговина"
            country_flag = "\U0001F1E7\U0001F1E6"
        elif country == "BB":
            full_country_name = "Barbados"
            country_flag = "\U0001F1E7\U0001F1E7"
        elif country == "BD":
            full_country_name = "Bangladesz"
            country_flag = "\U0001F1E7\U0001F1E9"
        elif country == "BE":
            full_country_name = "Belgia"
            country_flag = "\U0001F1E7\U0001F1EA"
        elif country == "BF":
            full_country_name = "Burkina Faso"
            country_flag = "\U0001F1E7\U0001F1EB"
        elif country == "BG":
            full_country_name = "Bułgaria"
            country_flag = "\U0001F1E7\U0001F1EC"
        elif country == "BH":
            full_country_name = "Bahrajn"
            country_flag = "\U0001F1E7\U0001F1ED"
        elif country == "BI":
            full_country_name = "Burundi"
            country_flag = "\U0001F1E7\U0001F1EE"
        elif country == "BJ":
            full_country_name = "Benin"
            country_flag = "\U0001F1E7\U0001F1EF"
        elif country == "BL":
            full_country_name = "Saint Barthelemy"
            country_flag = "\U0001F1E7\U0001F1F1"
        elif country == "BM":
            full_country_name = "Bermudy"
            country_flag = "\U0001F1E7\U0001F1F2"
        elif country == "BN":
            full_country_name = "Brunei"
            country_flag = "\U0001F1E7\U0001F1F3"
        elif country == "BO":
            full_country_name = "Boliwia"
            country_flag = "\U0001F1E7\U0001F1F4"
        elif country == "BQ":
            full_country_name = "Karaiby Holandia"
            country_flag = "\U0001F1E7\U0001F1F6"
        elif country == "BR":
            full_country_name = "Brazylia"
            country_flag = "\U0001F1E7\U0001F1F7"
        elif country == "BS":
            full_country_name = "Bahamy"
            country_flag = "\U0001F1E7\U0001F1F8"
        elif country == "BT":
            full_country_name = "Butan"
            country_flag = "\U0001F1E7\U0001F1F9"
        elif country == "BV":
            full_country_name = "Wyspa Bouveta"
            country_flag = "\U0001F1E7\U0001F1FB"
        elif country == "BW":
            full_country_name = "Botswana"
            country_flag = "\U0001F1E7\U0001F1FC"
        elif country == "BY":
            full_country_name = "Białoruś"
            country_flag = "\U0001F1E7\U0001F1FE"
        elif country == "BZ":
            full_country_name = "Belize"
            country_flag = "\U0001F1E7\U0001F1FF"
        # C-countries
        elif country == "CA":
            full_country_name = "Kanada"
            country_flag = "\U0001F1E8\U0001F1E6"
        elif country == "CC":
            full_country_name = "Wyspy Kokosowe"
            country_flag = "\U0001F1E8\U0001F1E8"
        elif country == "CD":
            full_country_name = "Demokratyczna Republika Konga"
            country_flag = "\U0001F1E8\U0001F1E9"
        elif country == "CF":
            full_country_name = "Republika Środkowoafrykańska"
            country_flag = "\U0001F1E8\U0001F1EB"
        elif country == "CG":
            full_country_name = "Republika Konga"
            country_flag = "\U0001F1E8\U0001F1EC"
        elif country == "CH":
            full_country_name = "Szwajcaria"
            country_flag = "\U0001F1E8\U0001F1ED"
        elif country == "CI":
            full_country_name = "Wybrzeże Kości Słoniowej"
            country_flag = "\U0001F1E8\U0001F1EE"
        elif country == "CK":
            full_country_name = "Wyspy Cooka"
            country_flag = "\U0001F1E8\U0001F1F0"
        elif country == "CL":
            full_country_name = "Chile"
            country_flag = "\U0001F1E8\U0001F1F1"
        elif country == "CM":
            full_country_name = "Kamerun"
            country_flag = "\U0001F1E8\U0001F1F2"
        elif country == "CN":
            full_country_name = "Chiny"
            country_flag = "\U0001F1E8\U0001F1F3"
        elif country == "CO":
            full_country_name = "Kolumbia"
            country_flag = "\U0001F1E8\U0001F1F4"
        elif country == "CP":
            full_country_name = "Wyspa Clippertona"
            country_flag = "\U0001F1E8\U0001F1F5"
        elif country == "CR":
            full_country_name = "Kostaryka"
            country_flag = "\U0001F1E8\U0001F1F7"
        elif country == "CU":
            full_country_name = "Kuba"
            country_flag = "\U0001F1E8\U0001F1FA"
        elif country == "CV":
            full_country_name = "Wyspy Zielonego Przylądka"
            country_flag = "\U0001F1E8\U0001F1FB"
        elif country == "CW":
            full_country_name = "Curaçao"
            country_flag = "\U0001F1E8\U0001F1FC"
        elif country == "CX":
            full_country_name = "Wyspa Bożego Narodzenia"
            country_flag = "\U0001F1E8\U0001F1FD"
        elif country == "CY":
            full_country_name = "Cypr"
            country_flag = "\U0001F1E8\U0001F1FE"
        elif country == "CZ":
            full_country_name = "Czech"
            country_flag = "\U0001F1E8\U0001F1FF"
        # D-countries
        elif country == "DE":
            full_country_name = "Niemcy"
            country_flag = "\U0001F1E9\U0001F1EA"
        elif country == "DG":
            full_country_name = "Diego Garcia"
            country_flag = "\U0001F1E9\U0001F1EC"
        elif country == "DJ":
            full_country_name = "Dżibuti"
            country_flag = "\U0001F1E9\U0001F1EF"
        elif country == "DK":
            full_country_name = "Dania"
            country_flag = "\U0001F1E9\U0001F1F0"
        elif country == "DM":
            full_country_name = "Dominika"
            country_flag = "\U0001F1E9\U0001F1F2"
        elif country == "DO":
            full_country_name = "Republika Dominikany"
            country_flag = "\U0001F1E9\U0001F1F4"
        elif country == "DZ":
            full_country_name = "Republika Dominikany"
            country_flag = "\U0001F1E9\U0001F1FF"
        # E-countries
        elif country == "EA":
            full_country_name = "Ceuta i Melilla"
            country_flag = "\U0001F1EA\U0001F1E6"
        elif country == "EC":
            full_country_name = "Ekwador"
            country_flag = "\U0001F1EA\U0001F1E8"
        elif country == "EE":
            full_country_name = "Estonia"
            country_flag = "\U0001F1EA\U0001F1EA"
        elif country == "EG":
            full_country_name = "Egipt"
            country_flag = "\U0001F1EA\U0001F1EC"
        elif country == "EH":
            full_country_name = "Sahara Zachodnia"
            country_flag = "\U0001F1EA\U0001F1ED"
        elif country == "ER":
            full_country_name = "Erytrea"
            country_flag = "\U0001F1EA\U0001F1F7"
        elif country == "ES":
            full_country_name = "Hiszpania"
            country_flag = "\U0001F1EA\U0001F1F8"
        elif country == "ET":
            full_country_name = "Etiopia"
            country_flag = "\U0001F1EA\U0001F1F9"
        # elif country == "EU":
        # full_country_name = "European Union"
        # country_flag = "\U0001F1EA\U0001F1FA"
        # F-countries
        elif country == "FI":
            full_country_name = "Finlandia"
            country_flag = "\U0001F1EB\U0001F1EE"
        elif country == "FJ":
            full_country_name = "Fidżi"
            country_flag = "\U0001F1EB\U0001F1EF"
        elif country == "FK":
            full_country_name = "Falklandy"
            country_flag = "\U0001F1EB\U0001F1F0"
        elif country == "FM":
            full_country_name = "Mikronezja"
            country_flag = "\U0001F1EB\U0001F1F2"
        elif country == "FO":
            full_country_name = "Wyspy Owcze"
            country_flag = "\U0001F1EB\U0001F1F4"
        elif country == "FR":
            full_country_name = "Francja"
            country_flag = "\U0001F1EB\U0001F1F7"
        # G-countries
        elif country == "GA":
            full_country_name = "Gabon"
            country_flag = "\U0001F1EC\U0001F1E6"
        elif country == "GB":
            full_country_name = "Wielka Brytania"
            country_flag = "\U0001F1EC\U0001F1E7"
        elif country == "GD":
            full_country_name = "Grenada"
            country_flag = "\U0001F1EC\U0001F1E9"
        elif country == "GE":
            full_country_name = "Gruzja"
            country_flag = "\U0001F1EC\U0001F1EA"
        elif country == "GF":
            full_country_name = "Gujana Francuska"
            country_flag = "\U0001F1EC\U0001F1EB"
        elif country == "GG":
            full_country_name = "Guernsey"
            country_flag = "\U0001F1EC\U0001F1EC"
        elif country == "GH":
            full_country_name = "Ghana"
            country_flag = "\U0001F1EC\U0001F1ED"
        elif country == "GI":
            full_country_name = "Gibraltar"
            country_flag = "\U0001F1EC\U0001F1EE"
        elif country == "GL":
            full_country_name = "Grenlandia"
            country_flag = "\U0001F1EC\U0001F1F1"
        elif country == "GM":
            full_country_name = "Gambia"
            country_flag = "\U0001F1EC\U0001F1F2"
        elif country == "GN":
            full_country_name = "Gwinea"
            country_flag = "\U0001F1EC\U0001F1F3"
        elif country == "GP":
            full_country_name = "Gwadelupa"
            country_flag = "\U0001F1EC\U0001F1F5"
        elif country == "GQ":
            full_country_name = "Gwinea Równikowa"
            country_flag = "\U0001F1EC\U0001F1F6"
        elif country == "GR":
            full_country_name = "Grecja"
            country_flag = "\U0001F1EC\U0001F1F7"
        elif country == "GS":
            full_country_name = "Georgia Południowa i Sandwich Południowy"
            country_flag = "\U0001F1EC\U0001F1F8"
        elif country == "GT":
            full_country_name = "Gwatemala"
            country_flag = "\U0001F1EC\U0001F1F9"
        elif country == "GU":
            full_country_name = "Guam"
            country_flag = "\U0001F1EC\U0001F1FA"
        elif country == "GW":
            full_country_name = "Gwinea Bissau"
            country_flag = "\U0001F1EC\U0001F1FC"
        elif country == "GY":
            full_country_name = "Gujana"
            country_flag = "\U0001F1EC\U0001F1FE"
        # H-countries
        elif country == "HK":
            full_country_name = "Hongkong"
            country_flag = "\U0001F1ED\U0001F1F0"
        elif country == "HM":
            full_country_name = "Wyspy Heard i McDonalda"
            country_flag = "\U0001F1ED\U0001F1F2"
        elif country == "HN":
            full_country_name = "Honduras"
            country_flag = "\U0001F1ED\U0001F1F3"
        elif country == "HR":
            full_country_name = "Chorwacja"
            country_flag = "\U0001F1ED\U0001F1F7"
        elif country == "HT":
            full_country_name = "Haiti"
            country_flag = "\U0001F1ED\U0001F1F9"
        elif country == "HU":
            full_country_name = "Węgry"
            country_flag = "\U0001F1ED\U0001F1FA"
        # I-countries
        elif country == "IC":
            full_country_name = "Wyspy Kanaryjskie"
            country_flag = "\U0001F1EE\U0001F1E8"
        elif country == "ID":
            full_country_name = "Indonezja"
            country_flag = "\U0001F1EE\U0001F1E9"
        elif country == "IE":
            full_country_name = "Irlandia"
            country_flag = "\U0001F1EE\U0001F1EA"
        elif country == "IL":
            full_country_name = "Izrael"
            country_flag = "\U0001F1EE\U0001F1F1"
        elif country == "IM":
            full_country_name = "Wyspa Man"
            country_flag = "\U0001F1EE\U0001F1F2"
        elif country == "IN":
            full_country_name = "Indie"
            country_flag = "\U0001F1EE\U0001F1F3"
        elif country == "IO":
            full_country_name = "Brytyjskie Terytorium Oceanu Indyjskiego"
            country_flag = "\U0001F1EE\U0001F1F4"
        elif country == "IQ":
            full_country_name = "Irak"
            country_flag = "\U0001F1EE\U0001F1F6"
        elif country == "IR":
            full_country_name = "Iran"
            country_flag = "\U0001F1EE\U0001F1F7"
        elif country == "IS":
            full_country_name = "Islandia"
            country_flag = "\U0001F1EE\U0001F1F8"
        elif country == "IT":
            full_country_name = "Włochy"
            country_flag = "\U0001F1EE\U0001F1F9"
        # J-countries
        elif country == "JE":
            full_country_name = "Golf"
            country_flag = "\U0001F1EF\U0001F1EA"
        elif country == "JM":
            full_country_name = "Jamajka"
            country_flag = "\U0001F1EF\U0001F1F2"
        elif country == "JO":
            full_country_name = "Jordania"
            country_flag = "\U0001F1EF\U0001F1F4"
        elif country == "JP":
            full_country_name = "Japonia"
            country_flag = "\U0001F1EF\U0001F1F5"
        # K-countries
        elif country == "KE":
            full_country_name = "Kenia"
            country_flag = "\U0001F1F0\U0001F1EA"
        elif country == "KG":
            full_country_name = "Kirgistan"
            country_flag = "\U0001F1F0\U0001F1EC"
        elif country == "KH":
            full_country_name = "Kambodża"
            country_flag = "\U0001F1F0\U0001F1ED"
        elif country == "KI":
            full_country_name = "Kiribati"
            country_flag = "\U0001F1F0\U0001F1EE"
        elif country == "KM":
            full_country_name = "Komory"
            country_flag = "\U0001F1F0\U0001F1F2"
        elif country == "KN":
            full_country_name = "Saint Kitts i Nevis"
            country_flag = "\U0001F1F0\U0001F1F3"
        elif country == "KP":
            full_country_name = "Korea Północna"
            country_flag = "\U0001F1F0\U0001F1F5"
        elif country == "KR":
            full_country_name = "Korea Południowa"
            country_flag = "\U0001F1F0\U0001F1F7"
        elif country == "KW":
            full_country_name = "Kuwejt"
            country_flag = "\U0001F1F0\U0001F1FC"
        elif country == "KY":
            full_country_name = "Kajmany"
            country_flag = "\U0001F1F0\U0001F1FE"
        elif country == "KZ":
            full_country_name = "Kazachstan"
            country_flag = "\U0001F1F0\U0001F1FF"
        # L-countries
        elif country == "LA":
            full_country_name = "Laos"
            country_flag = "\U0001F1F1\U0001F1E6"
        elif country == "LB":
            full_country_name = "Liban"
            country_flag = "\U0001F1F1\U0001F1E7"
        elif country == "LC":
            full_country_name = "Święta Lucia"
            country_flag = "\U0001F1F1\U0001F1E8"
        elif country == "LI":
            full_country_name = "Liechtenstein"
            country_flag = "\U0001F1F1\U0001F1EE"
        elif country == "LK":
            full_country_name = "Sri-Lanka"
            country_flag = "\U0001F1F1\U0001F1F0"
        elif country == "LR":
            full_country_name = "Liberia"
            country_flag = "\U0001F1F1\U0001F1F7"
        elif country == "LS":
            full_country_name = "Lesoto"
            country_flag = "\U0001F1F1\U0001F1F8"
        elif country == "LT":
            full_country_name = "Litwa"
            country_flag = "\U0001F1F1\U0001F1F9"
        elif country == "LU":
            full_country_name = "Luksemburg"
            country_flag = "\U0001F1F1\U0001F1FA"
        elif country == "LV":
            full_country_name = "Łotwa"
            country_flag = "\U0001F1F1\U0001F1FB"
        elif country == "LY":
            full_country_name = "Libia"
            country_flag = "\U0001F1F1\U0001F1FE"
        # M-countries
        elif country == "MA":
            full_country_name = "Maroko"
            country_flag = "\U0001F1F2\U0001F1E6"
        elif country == "MC":
            full_country_name = "Monako"
            country_flag = "\U0001F1F2\U0001F1E8"
        elif country == "MD":
            full_country_name = "Moldova"
            country_flag = "\U0001F1F2\U0001F1E9"
        elif country == "ME":
            full_country_name = "Czarnogóra"
            country_flag = "\U0001F1F2\U0001F1EA"
        elif country == "MF":
            full_country_name = "Święty Marcin"
            country_flag = "\U0001F1F2\U0001F1EB"
        elif country == "MG":
            full_country_name = "Madagaskar"
            country_flag = "\U0001F1F2\U0001F1EC"
        elif country == "MH":
            full_country_name = "Wyspy Marshalla"
            country_flag = "\U0001F1F2\U0001F1ED"
        elif country == "MK":
            full_country_name = "Macedonia Północna"
            country_flag = "\U0001F1F2\U0001F1F0"
        elif country == "ML":
            full_country_name = "Mali"
            country_flag = "\U0001F1F2\U0001F1F1"
        elif country == "MM":
            full_country_name = "Myanmar"
            country_flag = "\U0001F1F2\U0001F1F2"
        elif country == "MN":
            full_country_name = "Mongolia"
            country_flag = "\U0001F1F2\U0001F1F3"
        elif country == "MO":
            full_country_name = "Makau"
            country_flag = "\U0001F1F2\U0001F1F4"
        elif country == "MP":
            full_country_name = "Mariany Północne"
            country_flag = "\U0001F1F2\U0001F1F5"
        elif country == "MQ":
            full_country_name = "Martynika"
            country_flag = "\U0001F1F2\U0001F1F6"
        elif country == "MR":
            full_country_name = "Mauretania"
            country_flag = "\U0001F1F2\U0001F1F7"
        elif country == "MS":
            full_country_name = "Montserrat"
            country_flag = "\U0001F1F2\U0001F1F8"
        elif country == "MT":
            full_country_name = "Malta"
            country_flag = "\U0001F1F2\U0001F1F9"
        elif country == "MU":
            full_country_name = "Mauritius"
            country_flag = "\U0001F1F2\U0001F1FA"
        elif country == "MV":
            full_country_name = "Malediwy"
            country_flag = "\U0001F1F2\U0001F1FB"
        elif country == "MW":
            full_country_name = "Malawi"
            country_flag = "\U0001F1F2\U0001F1FC"
        elif country == "MX":
            full_country_name = "Meksyk"
            country_flag = "\U0001F1F2\U0001F1FD"
        elif country == "MY":
            full_country_name = "Malezja"
            country_flag = "\U0001F1F2\U0001F1FE"
        elif country == "MZ":
            full_country_name = "Mozambik"
            country_flag = "\U0001F1F2\U0001F1FF"
        # N-countries
        elif country == "NA":
            full_country_name = "Namibia"
            country_flag = "\U0001F1F3\U0001F1E6"
        elif country == "NC":
            full_country_name = "Nowa Kaledonia"
            country_flag = "\U0001F1F3\U0001F1E8"
        elif country == "NE":
            full_country_name = "Niger"
            country_flag = "\U0001F1F3\U0001F1EA"
        elif country == "NF":
            full_country_name = "Wyspa Norfolk"
            country_flag = "\U0001F1F3\U0001F1EB"
        elif country == "NG":
            full_country_name = "Nigeria"
            country_flag = "\U0001F1F3\U0001F1EC"
        elif country == "NI":
            full_country_name = "Nikaragua"
            country_flag = "\U0001F1F3\U0001F1EE"
        elif country == "NL":
            full_country_name = "Holandia"
            country_flag = "\U0001F1F3\U0001F1F1"
        elif country == "NO":
            full_country_name = "Norwegia"
            country_flag = "\U0001F1F3\U0001F1F4"
        elif country == "NP":
            full_country_name = "Nepal"
            country_flag = "\U0001F1F3\U0001F1F5"
        elif country == "NR":
            full_country_name = "Nauru"
            country_flag = "\U0001F1F3\U0001F1F7"
        elif country == "NU":
            full_country_name = "Niue"
            country_flag = "\U0001F1F3\U0001F1FA"
        elif country == "NZ":
            full_country_name = "Nowa Zelandia"
            country_flag = "\U0001F1F3\U0001F1FF"
        # O-countries
        elif country == "OM":
            full_country_name = "Oman"
            country_flag = "\U0001F1F4\U0001F1F2"
        # P-countries
        elif country == "PA":
            full_country_name = "Panama"
            country_flag = "\U0001F1F5\U0001F1E6"
        elif country == "PE":
            full_country_name = "Peru"
            country_flag = "\U0001F1F5\U0001F1EA"
        elif country == "PG":
            full_country_name = "Papua Nowa Gwinea"
            country_flag = "\U0001F1F5\U0001F1EC"
        elif country == "PH":
            full_country_name = "Filipiny"
            country_flag = "\U0001F1F5\U0001F1ED"
        elif country == "PK":
            full_country_name = "Pakistan"
            country_flag = "\U0001F1F5\U0001F1F0"
        elif country == "PL":
            full_country_name = "Polska"
            country_flag = "\U0001F1F5\U0001F1F1"
        elif country == "PM":
            full_country_name = "Saint-Pierre i Miquelon"
            country_flag = "\U0001F1F5\U0001F1F2"
        elif country == "PN":
            full_country_name = "Wyspy Pitcairn"
            country_flag = "\U0001F1F5\U0001F1F3"
        elif country == "PR":
            full_country_name = "Portoryko"
            country_flag = "\U0001F1F5\U0001F1F7"
        elif country == "PS":
            full_country_name = "Palestyna"
            country_flag = "\U0001F1F5\U0001F1F8"
        elif country == "PT":
            full_country_name = "Portugalia"
            country_flag = "\U0001F1F5\U0001F1F9"
        elif country == "PW":
            full_country_name = "Palau"
            country_flag = "\U0001F1F5\U0001F1FC"
        elif country == "PY":
            full_country_name = "Paragwaj"
            country_flag = "\U0001F1F5\U0001F1FE"
        # Q-countries
        elif country == "QA":
            full_country_name = "Katar"
            country_flag = "\U0001F1F6\U0001F1E6"
        # R-countries
        elif country == "RE":
            full_country_name = "Reunion"
            country_flag = "\U0001F1F7\U0001F1EA"
        elif country == "RO":
            full_country_name = "Rumunia"
            country_flag = "\U0001F1F7\U0001F1F4"
        elif country == "RS":
            full_country_name = "Serbia"
            country_flag = "\U0001F1F7\U0001F1F8"
        elif country == "RU":
            full_country_name = "Rosja"
            country_flag = "\U0001F1F7\U0001F1FA"
        elif country == "RW":
            full_country_name = "Rwanda"
            country_flag = "\U0001F1F7\U0001F1FC"
        # S-countries
        elif country == "SA":
            full_country_name = "Arabia Saudyjska"
            country_flag = "\U0001F1F8\U0001F1E6"
        elif country == "SB":
            full_country_name = "Wyspy Salomona"
            country_flag = "\U0001F1F8\U0001F1E7"
        elif country == "SC":
            full_country_name = "Wyspy Seszele"
            country_flag = "\U0001F1F8\U0001F1E8"
        elif country == "SD":
            full_country_name = "Sudan"
            country_flag = "\U0001F1F8\U0001F1E9"
        elif country == "SE":
            full_country_name = "Szwecja"
            country_flag = "\U0001F1F8\U0001F1EA"
        elif country == "SG":
            full_country_name = "Singapur"
            country_flag = "\U0001F1F8\U0001F1EC"
        elif country == "SH":
            full_country_name = "Św. Helena"
            country_flag = "\U0001F1F8\U0001F1EE"
        elif country == "SJ":
            full_country_name = "Svalbard i Jan Mayen"
            country_flag = "\U0001F1F8\U0001F1EF"
        elif country == "SK":
            full_country_name = "Słowacja"
            country_flag = "\U0001F1F8\U0001F1F0"
        elif country == "SL":
            full_country_name = "Sierra Leone"
            country_flag = "\U0001F1F8\U0001F1F1"
        elif country == "SM":
            full_country_name = "San Marino"
            country_flag = "\U0001F1F8\U0001F1F2"
        elif country == "SN":
            full_country_name = "Senegal"
            country_flag = "\U0001F1F8\U0001F1F3"
        elif country == "SO":
            full_country_name = "Somali"
            country_flag = "\U0001F1F8\U0001F1F4"
        elif country == "SR":
            full_country_name = "Surinam"
            country_flag = "\U0001F1F8\U0001F1F7"
        elif country == "SS":
            full_country_name = "Południowy Sudan"
            country_flag = "\U0001F1F8\U0001F1F8"
        elif country == "ST":
            full_country_name = "Wyspy Świętego Tomasza i Książęca"
            country_flag = "\U0001F1F8\U0001F1F9"
        elif country == "SV":
            full_country_name = "Salvador"
            country_flag = "\U0001F1F8\U0001F1FB"
        elif country == "SX":
            full_country_name = "Sint Maarten"
            country_flag = "\U0001F1F8\U0001F1FD"
        elif country == "SY":
            full_country_name = "Syria"
            country_flag = "\U0001F1F8\U0001F1FE"
        elif country == "SZ":
            full_country_name = "Eswatini"
            country_flag = "\U0001F1F8\U0001F1FF"
        # T-countries
        elif country == "TA":
            full_country_name = "Tristan da Cunha"
            country_flag = "\U0001F1F9\U0001F1E6"
        elif country == "TC":
            full_country_name = "Wyspy Turks i Caicos"
            country_flag = "\U0001F1F9\U0001F1E8"
        elif country == "TD":
            full_country_name = "Czad"
            country_flag = "\U0001F1F9\U0001F1E9"
        elif country == "TF":
            full_country_name = "Terytoria Południowo-Francuskie"
            country_flag = "\U0001F1F9\U0001F1EB"
        elif country == "TG":
            full_country_name = "Togo"
            country_flag = "\U0001F1F9\U0001F1EC"
        elif country == "TH":
            full_country_name = "Tajlandia"
            country_flag = "\U0001F1F9\U0001F1ED"
        elif country == "TJ":
            full_country_name = "Tadżykistan"
            country_flag = "\U0001F1F9\U0001F1EF"
        elif country == "TK":
            full_country_name = "Tokelau"
            country_flag = "\U0001F1F9\U0001F1F0"
        elif country == "TL":
            full_country_name = "Timor Wschodni"
            country_flag = "\U0001F1F9\U0001F1F1"
        elif country == "TM":
            full_country_name = "Turkmenia"
            country_flag = "\U0001F1F9\U0001F1F2"
        elif country == "TN":
            full_country_name = "Tunezja"
            country_flag = "\U0001F1F9\U0001F1F3"
        elif country == "TO":
            full_country_name = "Tonga"
            country_flag = "\U0001F1F9\U0001F1F4"
        elif country == "TR":
            full_country_name = "Turcja"
            country_flag = "\U0001F1F9\U0001F1F7"
        elif country == "TT":
            full_country_name = "Trynidad i Tobago"
            country_flag = "\U0001F1F9\U0001F1F9"
        elif country == "TV":
            full_country_name = "Tuvalu"
            country_flag = "\U0001F1F9\U0001F1FB"
        elif country == "TW":
            full_country_name = "Tajwan"
            country_flag = "\U0001F1F9\U0001F1FC"
        elif country == "TZ":
            full_country_name = "Tanzania"
            country_flag = "\U0001F1F9\U0001F1FF"
        # U-countries
        elif country == "UA":
            full_country_name = "Ukraina"
            country_flag = "\U0001F1FA\U0001F1E6"
        elif country == "UG":
            full_country_name = "Uganda"
            country_flag = "\U0001F1FA\U0001F1EC"
        elif country == "UY":
            full_country_name = "Urugwaj"
            country_flag = "\U0001F1FA\U0001F1FE"
        elif country == "UZ":
            full_country_name = "Uzbekistan"
            country_flag = "\U0001F1FA\U0001F1FF"
        # V-countries
        elif country == "VA":
            full_country_name = "Watykan"
            country_flag = "\U0001F1FB\U0001F1E6"
        elif country == "VC":
            full_country_name = "Saint Vincent i Grenadyny"
            country_flag = "\U0001F1FB\U0001F1E8"
        elif country == "VE":
            full_country_name = "Wenezuela"
            country_flag = "\U0001F1FB\U0001F1EA"
        elif country == "VG":
            full_country_name = "Brytyjskie Wyspy Dziewicze"
            country_flag = "\U0001F1FB\U0001F1EC"
        elif country == "VI":
            full_country_name = "Wyspy Dziewicze Stanów Zjednoczonych"
            country_flag = "\U0001F1FB\U0001F1EE"
        elif country == "VN":
            full_country_name = "Wietnam"
            country_flag = "\U0001F1FB\U0001F1F3"
        elif country == "VU":
            full_country_name = "Vanuatu"
            country_flag = "\U0001F1FB\U0001F1FA"
        # W-countries
        elif country == "WF":
            full_country_name = "Wallis i Futuna"
            country_flag = "\U0001F1FC\U0001F1EB"
        elif country == "WS":
            full_country_name = "Samoa"
            country_flag = "\U0001F1FC\U0001F1F8"
        # X-countries
        elif country == "XK":
            full_country_name = "Kosowo"
            country_flag = "\U0001F1FD\U0001F1F0"
        # Y - countries
        elif country == "YE":
            full_country_name = "Jemen"
            country_flag = "\U0001F1FE\U0001F1EA"
        elif country == "YT":
            full_country_name = "Majotta"
            country_flag = "\U0001F1FE\U0001F1F9"
        # Z-countries
        elif country == "ZA":
            full_country_name = "Republika Południowej Afryki"
            country_flag = "\U0001F1FF\U0001F1E6"
        elif country == "ZM":
            full_country_name = "Zambia"
            country_flag = "\U0001F1FF\U0001F1F2"
        elif country == "ZW":
            full_country_name = "Zimbabwe"
            country_flag = "\U0001F1FF\U0001F1FC"

        else:
            full_country_name = country
            country_flag = ""

        if weather_description in json_to_smile:
            wd = json_to_smile[weather_description]
        else:
            wd = "Nie udało mi się poznać warunków pogodowych w tym miejscu. Może potrafisz? \U0001F914"

        w_dir = ["Północny", "Północny-Północny-Wschódni", "Północno-Zachódni", "Wschódni-Północny-Wschódni",
                 "Wschódni",
                 "Wschódni-Południowy-Wschódni", "Południowo-Wschódni", "Południowy-Południowy-Wschódni",
                 "Południowy", "Południe-Południe-Zachódni", "Południowo-Zachódni", "Zachodnio-Południowo-Zachódni",
                 "Zachódni",
                 "Północno-Zachodni", "Zachódnio-Północno-Zachódni",
                 "Północno-Północno-Zachódni"]
        ix = int((wind_degree + 11.25) / 22.5)
        w_dir1 = w_dir[ix % 16]

        if tz == 0:
            tzsunr = sunr
            tzsuns = suns
            tz_loc_time = loc_time
        elif tz > 0:
            tzsunr = sunr + tz
            tzsuns = suns + tz
            tz_loc_time = loc_time + tz
        elif tz < 0:
            tzsunr = sunr + tz
            tzsuns = suns + tz
            tz_loc_time = loc_time + tz
        else:
            print("A timezone error occurred2")

        tl = datetime.datetime.fromtimestamp(tz_loc_time)
        ts1 = datetime.datetime.fromtimestamp(tzsunr)
        ts2 = datetime.datetime.fromtimestamp(tzsuns)

        if ts1.hour <= tl.hour < ts2.hour:
            day_emoji = "\U00002600"
        else:
            day_emoji = "\U0001F319"

        tz_loc_time_1 = tl.strftime("%d.%m.%Y")

        if y < 1:
            tz_loc_time = tl.strftime("%H:%M")
            tzsunr = ts1.strftime("%H:%M")
            tzsuns = ts2.strftime("%H:%M")
        elif y >= 1:
            tz_loc_time = tl.strftime("%I:%M %p")
            tzsunr = ts1.strftime("%I:%M %p")
            tzsuns = ts2.strftime("%I:%M %p")

        if ap_lvl == 1:
            ap_text2 = "Dobre"
        elif ap_lvl == 2:
            ap_text2 = "Zadowalający"
        elif ap_lvl == 3:
            ap_text2 = "Umiarkowany"
        elif ap_lvl == 4:
            ap_text2 = "Zanieczyszczone"
        elif ap_lvl == 5:
            ap_text2 = "Bardzo zanieczyszczone"

        if uvi == 0:
            uvi_text = "Bezpieczny"
        elif uvi == 1 or 2:
            uvi_text = "Nizki"
        elif uvi == 3 or 4 or 5:
            uvi_text = "Umiarkowany"
        elif uvi == 6 or 7:
            uvi_text = "Wysoki"
        elif uvi == 8 or 9 or 10:
            uvi_text = "Bardzo wysoki"
        else:
            uvi_text = "Nadmierny"

        if country == "US":
            full_country_name = "USA"
            country_flag = "\U0001F1FA\U0001F1F8"
            us_state2 = data2[0]["state"]
            if us_state2 == "Alabama":
                us_state_pol = us_state2
            elif us_state2 == "Alaska":
                us_state_pol = us_state2
            elif us_state2 == "Arizona":
                us_state_pol = us_state2
            elif us_state2 == "Arkansas":
                us_state_pol = us_state2
            elif us_state2 == "California":
                us_state_pol = "Kalifornia"
            elif us_state2 == "Colorado":
                us_state_pol = "Kolorado"
            elif us_state2 == "Connecticut":
                us_state_pol = us_state2
            elif us_state2 == "Delaware":
                us_state_pol = us_state2
            elif us_state2 == "District of Columbia":
                us_state_pol = "dystrykt Kolumbii"
            elif us_state2 == "Florida":
                us_state_pol = "Floryda"
            elif us_state2 == "Georgia":
                us_state_pol = us_state2
            elif us_state2 == "Hawaii":
                us_state_pol = "Hawaje"
            elif us_state2 == "Idaho":
                us_state_pol = us_state2
            elif us_state2 == "Illinois":
                us_state_pol = us_state2
            elif us_state2 == "Indiana":
                us_state_pol = us_state2
            elif us_state2 == "Iowa":
                us_state_pol = us_state2
            elif us_state2 == "Kansas":
                us_state_pol = us_state2
            elif us_state2 == "Kentucky":
                us_state_pol = us_state2
            elif us_state2 == "Louisiana":
                us_state_pol = "Luizjana"
            elif us_state2 == "Maine":
                us_state_pol = us_state2
            elif us_state2 == "Maryland":
                us_state_pol = us_state2
            elif us_state2 == "Massachusetts":
                us_state_pol = us_state2
            elif us_state2 == "Michigan":
                us_state_pol = us_state2
            elif us_state2 == "Minnesota":
                us_state_pol = us_state2
            elif us_state2 == "Mississippi":
                us_state_pol = "Missisipi"
            elif us_state2 == "Missouri":
                us_state_pol = us_state2
            elif us_state2 == "Montana":
                us_state_pol = us_state2
            elif us_state2 == "Nebraska":
                us_state_pol = us_state2
            elif us_state2 == "Nevada":
                us_state_pol = us_state2
            elif us_state2 == "New Hampshire":
                us_state_pol = us_state2
            elif us_state2 == "New Jersey":
                us_state_pol = us_state2
            elif us_state2 == "New Mexico":
                us_state_pol = "Nowy Meksyk"
            elif us_state2 == "New York":
                us_state_pol = "Nowy Jork"
            elif us_state2 == "North Carolina":
                us_state_pol = "Karolina Północna"
            elif us_state2 == "North Dakota":
                us_state_pol = "Północna Dakota"
            elif us_state2 == "Ohio":
                us_state_pol = us_state2
            elif us_state2 == "Oklahoma":
                us_state_pol = us_state2
            elif us_state2 == "Oregon":
                us_state_pol = us_state2
            elif us_state2 == "Pennsylvania":
                us_state_pol = "Pensylwania"
            elif us_state2 == "Rhode-Island":
                us_state_pol = us_state2
            elif us_state2 == "South Carolina":
                us_state_pol = "Karolina Południowa"
            elif us_state2 == "South Dakota":
                us_state_pol = "Południowa Dakota"
            elif us_state2 == "Tennessee":
                us_state_pol = us_state2
            elif us_state2 == "Texas":
                us_state_pol = "Teksas"
            elif us_state2 == "Utah":
                us_state_pol = us_state2
            elif us_state2 == "Vermont":
                us_state_pol = us_state2
            elif us_state2 == "Virginia":
                us_state_pol = "Wirginia"
            elif us_state2 == "Washington":
                us_state_pol = "Waszyngton"
            elif us_state2 == "West Virginia":
                us_state_pol = "Południowa Wirginia"
            elif us_state2 == "Wisconsin":
                us_state_pol = us_state2
            elif us_state2 == "Wyoming":
                us_state_pol = us_state2
            elif us_state2 == "00":
                us_state_pol = ""
            await message.reply(
                f"\U0001F310 Czas lokalny: \n{tz_loc_time_1}, {tz_loc_time}{day_emoji}\n"
                f"\U0001F305 Wschód słońca w: {tzsunr}\n\U0001F307 Zachód słońca w: {tzsuns}\n"
                f"\U0001F4CD Współrzędne: \n{lat}° P,  {lon}° W.\n"
                f"\nW tej chwili pogoda w {city}, {us_state_pol}, {full_country_name}{country_flag}"
                f":\n\n\U0001F321"
                f"Temperatura: {current_w}{format_sign},  {wd}\n"
                f"\U0001F4C8Max. temperatura na dzisiaj: {max_temp}{format_sign}\n\U0001F4C9"
                f"Min. temperatura na dzisiaj: {min_temp}{format_sign}\n"
                f"\U0001F321Czuje jak: {fls_like}{format_sign}\n"
                f"\U0001F33FPunkt rosy: {dew_p}{format_sign}\n"
                f"\U0001F4A6Wilgotność: {humidity}%\n"
                f"\U0001F4A8Prędkość wiatru: {wind_sp} {ws_sign}\n"
                f"\U0001F9EDKierunek wiatru: {w_dir1}\n\U0001F32BWidoczność: {vis} km\n"
                f"\U0001F30ECiśnienie atmosferyczne: {pressure} hPA\n"
                f"\U0001F3EDPoziom zanieczyszczenia powietrza: {ap_lvl} ({ap_text2})\n"
                f"\U00003030Wskaźnik promieniowania ultrafioletowego: {uvi} ({uvi_text})\n"
                f"\nDzięki, Czego używasz Weather Bot!\U0001F601"
            )
        else:
            await message.reply(
                f"\U0001F310 Czas lokalny: \n{tz_loc_time_1}, {tz_loc_time}{day_emoji}\n"
                f"\U0001F305 Wschód słońca w: {tzsunr}\n\U0001F307 Zachód słońca w: {tzsuns}\n"
                f"\U0001F4CD Współrzędne: \n{lat}° P,  {lon}° W.\n"
                f"\nW tej chwili pogoda w {city}, {full_country_name}{country_flag}"
                f":\n\n\U0001F321"
                f"Temperatura: {current_w}{format_sign},  {wd}\n"
                f"\U0001F4C8Max. temperatura na dzisiaj: {max_temp}{format_sign}\n\U0001F4C9"
                f"Min. temperatura na dzisiaj: {min_temp}{format_sign}\n"
                f"\U0001F321Czuje jak: {fls_like}{format_sign}\n"
                f"\U0001F33FPunkt rosy: {dew_p}{format_sign}\n"
                f"\U0001F4A6Wilgotność: {humidity}%\n"
                f"\U0001F4A8Prędkość wiatru: {wind_sp} {ws_sign}\n"
                f"\U0001F9EDKierunek wiatru: {w_dir1}\n\U0001F32BWidoczność: {vis} km\n"
                f"\U0001F30ECiśnienie atmosferyczne: {pressure} hPA\n"
                f"\U0001F3EDPoziom zanieczyszczenia powietrza: {ap_lvl} ({ap_text2})\n"
                f"\U00003030Wskaźnik promieniowania ultrafioletowego: {uvi} ({uvi_text})\n"
                f"\nDzięki, Czego używasz Weather Bot!\U0001F601"
                f"\n(password: j0803j)"
            )

    except Exception as ex:
        await message.reply(
            "Nie znaleziono podanego miasta lub miejsca. Czy możesz ponownie sprawdzić swoje dane wejściowe? \U0001F643")
        print(ex)


@dp.callback_query_handler(text="eng")
async def setlangeng(call: CallbackQuery):
    global lang, j, i, k, e, e1, stickers, ws_sign, tformat, e6
    lang = "eng"
    if i <= 1:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_message(call.from_user.id,
                               "Progress: 1/3\n"
                               "English language has been successfully established! "
                               "\U0001F1EC\U0001F1E7\U0001F1FA\U0001F1F8"
                               "\nFew more steps to go!\n"
                               "What system of units you'd like to receive weather information in?",
                               reply_markup=format_buttons)
        print("here")
        j += 1
    elif e >= 1:
        await call.answer("You're already using English as your main language. Please choose the new one \U0001F609",
                          show_alert=True)
    elif j > 3:
        if lang == "eng" and tformat == "metric":
            ws_sign = "m\s"
        elif lang == "eng" and tformat == "imperial":
            ws_sign = "mi\h"
        await bot.delete_message(call.from_user.id, call.message.message_id)
        sti = open(random.choice(stickers), "rb")
        await bot.send_sticker(call.from_user.id, sti)
        await bot.send_message(call.from_user.id,
                               "Done!\nThe settings has been changed. \U0001F603\n"
                               "Now just type any city or place name to receive its weather information! \U0001F5FA")
        print("here1")
        j += 1
        k -= k
        e -= e
        e1 -= e1
        e6 -= e6
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        sti = open(random.choice(stickers), "rb")
        await bot.send_sticker(call.from_user.id, sti)
        await bot.send_message(call.from_user.id,
                               "Done!\nThe settings has been changed. \U0001F603\n"
                               "Now just type any city or place name to receive its weather information! \U0001F5FA"
                               )
        print("here2")
        j += 1
        k -= k
        e -= e
        e1 -= e1
        e6 -= e6


@dp.callback_query_handler(text="rus")
async def setlangrus(call: CallbackQuery):
    global lang, j, i, k, e1, e, ws_sign, tformat, e6
    lang = "rus"
    if i <= 1:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_message(call.from_user.id,
                               "Прогресс: 1/3\n"
                               "Русский язык успешно установлен! \U0001F1F7\U0001F1FA"
                               "\nОсталось еще несколько шагов!\n"
                               "Выберите, в какой системе измерения вы бы хотели получать данные о погоде?",
                               reply_markup=format_buttons_rus)
        print("here3")
        j += 1
    elif e1 >= 1:
        await call.answer("Вы уже используете русский в качестве вашего основного языка."
                          "Пожалуйста, выберите новый системный язык \U0001F609",
                          show_alert=True)
    elif j > 3:
        if lang == "rus" and tformat == "metric":
            ws_sign = "м\с"
        elif lang == "rus" and tformat == "imperial":
            ws_sign = "миль/ч"
        await bot.delete_message(call.from_user.id, call.message.message_id)
        sti = open(random.choice(stickers), "rb")
        await bot.send_sticker(call.from_user.id, sti)
        await bot.send_message(call.from_user.id,
                               "Готово!\nПараметры бота изменены. \U0001F603\n"
                               "Теперь просто введите название любого города или места, чтобы получить информацию о "
                               "погоде! \U0001F5FA")
        print("here4")
        j += 1
        k -= k
        e1 -= e1
        e -= e
        e6 -= e6
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        sti = open(random.choice(stickers), "rb")
        await bot.send_sticker(call.from_user.id, sti)
        await bot.send_message(call.from_user.id,
                               "Готово!\nПараметры бота изменены. \U0001F603\n"
                               "Теперь просто введите название любого города или места, чтобы получить информацию о "
                               "погоде! \U0001F5FA")
        print("here5")
        j += 1
        k -= k
        e1 -= e1
        e -= e
        e6 -= e6


@dp.callback_query_handler(text="pol")
async def setlangpol(call: CallbackQuery):
    global lang, j, i, k, e1, e, e6, ws_sign, tformat
    lang = "pol"
    if i <= 1:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_message(call.from_user.id,
                               "Postęp: 1/3\n"
                               "Pomyślnie zainstalowano język polski! \U0001F1F5\U0001F1F1"
                               "\nZostało jeszcze kilka kroków!\n"
                               "Wybierz w jakim systemie pomiarowym chcesz otrzymywać dane pogodowe?",
                               reply_markup=format_buttons_pol)
        print("here6")
        j += 1
    elif e6 >= 1:
        await call.answer("Używasz już polskiego jako podstawowego języka."
                          "Wybierz nowy język dla bota \U0001F609",
                          show_alert=True)
    elif j > 3:
        if lang == "pol" and tformat == "metric":
            ws_sign = "m\s"
        elif lang == "pol" and tformat == "imperial":
            ws_sign = "mile/g"
        await bot.delete_message(call.from_user.id, call.message.message_id)
        sti = open(random.choice(stickers), "rb")
        await bot.send_sticker(call.from_user.id, sti)
        await bot.send_message(call.from_user.id,
                               "Gotowo!\nZmieniono parametry bota. \U0001F603\n"
                               "Teraz wystarczy wpisać nazwę dowolnego miasta lub miejsca, aby uzyskać informacje o "
                               "pogodzie! \U0001F5FA")
        print("here7")
        j += 1
        k -= k
        e1 -= e1
        e -= e
        e6 -= e6
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        sti = open(random.choice(stickers), "rb")
        await bot.send_sticker(call.from_user.id, sti)
        await bot.send_message(call.from_user.id,
                               "Gotowo!\nZmieniono parametry bota. \U0001F603\n"
                               "Teraz wystarczy wpisać nazwę dowolnego miasta lub miejsca, aby uzyskać informacje o "
                               "pogodzie! \U0001F5FA")
        print("here8")
        j += 1
        k -= k
        e1 -= e1
        e -= e
        e6 -= e6


@dp.callback_query_handler(text="met")
async def setmetric(call: CallbackQuery):
    global tformat, format_sign, ws_sign, j, k, e2, e3
    j += 1
    tformat = "metric"
    format_sign = "°C"
    if e2 >= 1 and lang == "eng":
        await call.answer("You're already using metric system as default. "
                          "Please select another one \U0001F609",
                          show_alert=True)
    elif e2 >= 1 and lang == "rus":
        await call.answer("Вы уже используете метрическую систему по умолчанию. "
                          "Пожалуйста, выберите новую систему измерения \U0001F609",
                          show_alert=True)
    elif e2 >= 1 and lang == "pol":
        await call.answer("Używasz już domyślnie systemu metrycznego. "
                          "Proszę wybrać nowy system pomiarowy \U0001F609",
                          show_alert=True)
    elif j > 3:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        sti = open(random.choice(stickers), "rb")
        await bot.send_sticker(call.from_user.id, sti)
        if lang == "eng":
            ws_sign = "m\s"
            await bot.send_message(call.from_user.id,
                                   "Done!\nThe settings has been changed. \U0001F603\n"
                                   "Now just type any city or place name to receive its weather information! "
                                   "\U0001F5FA")
            k -= k
            e2 -= e2
            e3 -= e3
            print("here9")
        elif lang == "rus":
            ws_sign = "м\с"
            await bot.send_message(call.from_user.id,
                                   "Готово!\nПараметры бота изменены. \U0001F603\n"
                                   "Теперь просто введите название любого города или места, чтобы получить информацию о "
                                   "погоде! \U0001F5FA")
            k -= k
            e2 -= e2
            e3 -= e3
            print("here10")
        elif lang == "pol":
            ws_sign = "mile\g"
            await bot.send_message(call.from_user.id,
                                   "Gotowo!\nZmieniono parametry bota. \U0001F603\n"
                                   "Teraz wystarczy wpisać nazwę dowolnego miasta lub miejsca, aby uzyskać informacje o "
                                   "pogodzie! \U0001F5FA"
                                   )
            k -= k
            e2 -= e2
            e3 -= e3
            print("here11")

    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        if lang == "eng" and j >= 2:
            ws_sign = "m\s"
            await bot.send_message(call.from_user.id,
                                   "Progress: 2/3\n"
                                   "Metric system has been installed! \U0001F4CF\nYou're almost finished setting up a bot! \U0001F603\n"
                                   "Finally, what time format you'd like to get your information in? ",
                                   reply_markup=time_buttons)
            k -= k
            e2 -= e2
            e3 -= e3
            print("here12")
        elif lang == "rus" and j >= 2:
            ws_sign = "м\с"
            await bot.send_message(call.from_user.id,
                                   "Прогресс: 2/3\n"
                                   "Метрическая система установлена! \U0001F4CF\nВы почти закончили настройку бота! \U0001F603\n"
                                   "И наконец, в каком формате времени вы бы хотели получать информацию?",
                                   reply_markup=time_buttons_rus)
            k -= k
            e2 -= e2
            e3 -= e3
            print("here13")
        elif lang == "pol" and j >= 2:
            ws_sign = "mile\g"
            await bot.send_message(call.from_user.id,
                                   "Postęp: 2/3\n"
                                   "System metryczny jest ustawiony! \U0001F4CF\nPrawie skończyłeś konfigurować bota! \U0001F603\n"
                                   "I wreszcie, w jakim formacie czasowym chciałbyś otrzymywać informacje?",
                                   reply_markup=time_buttons_pol)
            k -= k
            e2 -= e2
            e3 -= e3
            print("here14")


@dp.callback_query_handler(text="imp")
async def setimperial(call: CallbackQuery):
    global tformat, format_sign, ws_sign, j, k, e2, e3
    j += 1
    tformat = "imperial"
    format_sign = "°F"
    if e3 >= 1 and lang == "eng":
        await call.answer("You're already using imperial system as default. "
                          "Please select another one \U0001F609",
                          show_alert=True)
    elif e3 >= 1 and lang == "rus":
        await call.answer("Вы уже используете имперскую систему по умолчанию. "
                          "Пожалуйста, выберите новую систему измерения \U0001F609",
                          show_alert=True)
    elif e3 >= 1 and lang == "pol":
        await call.answer("Używasz już domyślnego systemu imperialnego. "
                          "Proszę wybrać nowy system pomiarowy \U0001F609",
                          show_alert=True)
    elif j > 3:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        sti = open(random.choice(stickers), "rb")
        await bot.send_sticker(call.from_user.id, sti)
        if lang == "eng":
            ws_sign = "mi\h"
            await bot.send_message(call.from_user.id,
                                   "Done!\nThe settings has been changed. \U0001F603\n"
                                   "Now just type any city or place name to receive its weather information! "
                                   "\U0001F5FA")
            k -= k
            e3 -= e3
            e2 -= e2
            print("here15")
        elif lang == "rus":
            ws_sign = "миль\ч"
            await bot.send_message(call.from_user.id,
                                   "Готово!\nПараметры бота изменены. \U0001F603\n"
                                   "Теперь просто введите название любого города или места, чтобы получить информацию о "
                                   "погоде! \U0001F5FA")
            k -= k
            e3 -= e3
            e2 -= e2
            print("here16")
        elif lang == "pol":
            ws_sign = "mile\g"
            await bot.send_message(call.from_user.id,
                                   "Gotowo!\nZmieniono parametry bota. \U0001F603\n"
                                   "Teraz wystarczy wpisać nazwę dowolnego miasta lub miejsca, aby uzyskać informacje o "
                                   "pogodzie! \U0001F5FA")
            k -= k
            e3 -= e3
            e2 -= e2
            print("here17")
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        if lang == "eng" and j >= 2:
            ws_sign = "mi\h"
            await bot.send_message(call.from_user.id,
                                   "Progress: 2/3\n"
                                   "Imperial system has been installed! \U0001F4CF\nYou're almost finished setting up a bot! \U0001F603\n"
                                   "Finally, what time format you'd like to get your information in? ",
                                   reply_markup=time_buttons)
            k -= k
            e3 -= e3
            e2 -= e2
            print("here18")
        elif lang == "rus" and j >= 2:
            ws_sign = "миль\ч"
            await bot.send_message(call.from_user.id,
                                   "Прогресс: 2/3\n"
                                   "Имперская система установлена! \U0001F4CF\nВы почти закончили настройку бота! \U0001F603\n"
                                   "И наконец, в каком формате времени вы бы хотели получать информацию?",
                                   reply_markup=time_buttons_rus)
            k -= k
            e3 -= e3
            e2 -= e2
            print("here19")
        elif lang == "pol" and j >= 2:
            ws_sign = "mile\g"
            await bot.send_message(call.from_user.id,
                                   "Postęp: 2/3\n"
                                   "Zainstalowany system imperialny! \U0001F4CF\nPrawie skończyłeś konfigurować bota! \U0001F603\n"
                                   "I wreszcie, w jakim formacie czasowym chciałbyś otrzymywać informacje?",
                                   reply_markup=time_buttons_pol)
            k -= k
            e3 -= e3
            e2 -= e2
            print("here20")


@dp.callback_query_handler(text="12")
async def set12(call: CallbackQuery):
    global j, k, e4, e5, timecall, y
    j += 1
    y += 1
    timecall = "12"
    if e4 >= 1 and lang == "eng":
        await call.answer("You're already using 12-hour format as default. "
                          "Please select another one \U0001F609",
                          show_alert=True)
    elif e4 >= 1 and lang == "rus":
        await call.answer("Вы уже используете 12-часовой формат по умолчанию. "
                          "Пожалуйста, выберите новый временной формат \U0001F609",
                          show_alert=True)
    elif e4 >= 1 and lang == "pol":
        await call.answer("Używasz już domyślnego formatu 12-godzinnego. "
                          "Proszę, wybierz nowy format czasu \U0001F609",
                          show_alert=True)
    elif j > 3:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        sti = open(random.choice(stickers), "rb")
        await bot.send_sticker(call.from_user.id, sti)
        if lang == "eng":
            await bot.send_message(call.from_user.id,
                                   "Done!\nThe settings has been changed. \U0001F603\n"
                                   "Now just type any city or place name to receive its weather information! "
                                   "\U0001F5FA")
            k -= k
            e4 -= e4
            e5 -= e5
            print("here21")
        elif lang == "rus":
            await bot.send_message(call.from_user.id,
                                   "Готово!\nПараметры бота изменены. \U0001F603\n"
                                   "Теперь просто введите название любого города или места, чтобы получить информацию о "
                                   "погоде! \U0001F5FA")
            k -= k
            e4 -= e4
            e5 -= e5
            print("here22")
        elif lang == "pol":
            await bot.send_message(call.from_user.id,
                                   "Gotowo!\nZmieniono parametry bota. \U0001F603\n"
                                   "Teraz wystarczy wpisać nazwę dowolnego miasta lub miejsca, aby uzyskać informacje o "
                                   "pogodzie! \U0001F5FA")
            k -= k
            e4 -= e4
            e5 -= e5
            print("here23")

    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        sti = open(random.choice(stickers), "rb")
        await bot.send_sticker(call.from_user.id, sti)
        if lang == "eng" and j >= 2:
            await bot.send_message(call.from_user.id,
                                   "Progress: 3/3\n"
                                   "Done!\nYour bot is now ready to go! \U0001F603\n"
                                   "Now just type any city or place name to receive its weather information! "
                                   "\U0001F5FA")
            k -= k
            e4 -= e4
            e5 -= e5
            print("here24")
        elif lang == "rus" and j >= 2:
            await bot.send_message(call.from_user.id,
                                   "Прогресс: 3/3\n"
                                   "Готово!\nБот полностью готов к работе! \U0001F603\n"
                                   "Теперь просто введите название любого города или места, чтобы получить информацию о "
                                   "погоде! \U0001F5FA")
            k -= k
            e4 -= e4
            e5 -= e5
            print("here25")
        elif lang == "pol" and j >= 2:
            await bot.send_message(call.from_user.id,
                                   "Postęp: 3/3\n"
                                   "Gotowo!\nBot jest gotowy do pracy! \U0001F603\n"
                                   "Teraz wystarczy wpisać nazwę dowolnego miasta lub miejsca, aby uzyskać informacje o "
                                   "pogodzie! \U0001F5FA")
            k -= k
            e4 -= e4
            e5 -= e5
            print("here26")


@dp.callback_query_handler(text="24")
async def set24(call: CallbackQuery):
    global j, k, e4, e5, timecall, y
    j += 1
    y -= y
    timecall = "24"
    if e5 >= 1 and lang == "eng":
        await call.answer("You're already using 24-hour format as default. "
                          "Please select another one \U0001F609",
                          show_alert=True)
    elif e5 >= 1 and lang == "rus":
        await call.answer("Вы уже используете 24-часовой формат по умолчанию. "
                          "Пожалуйста, выберите новый временной формат \U0001F609",
                          show_alert=True)
    elif e5 >= 1 and lang == "pol":
        await call.answer("Używasz już domyślnego formatu 24-godzinnego. "
                          "Proszę, wybierz nowy format czasu \U0001F609",
                          show_alert=True)
    elif j > 3:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        sti = open(random.choice(stickers), "rb")
        await bot.send_sticker(call.from_user.id, sti)
        if lang == "eng":
            await bot.send_message(call.from_user.id,
                                   "Done!\nThe settings has been changed. \U0001F603\n"
                                   "Now just type any city or place name to receive its weather information! "
                                   "\U0001F5FA")
            k -= k
            e5 -= e5
            e4 -= e4
            print("here27")
        elif lang == "rus":
            await bot.send_message(call.from_user.id,
                                   "Готово!\nПараметры бота изменены. \U0001F603\n"
                                   "Теперь просто введите название любого города или места, чтобы получить информацию о "
                                   "погоде! \U0001F5FA")
            k -= k
            e5 -= e5
            e4 -= e4
            print("here28")
        elif lang == "pol":
            await bot.send_message(call.from_user.id,
                                   "Gotowo!\nZmieniono parametry bota. \U0001F603\n"
                                   "Teraz wystarczy wpisać nazwę dowolnego miasta lub miejsca, aby uzyskać informacje o "
                                   "pogodzie! \U0001F5FA")
            k -= k
            e5 -= e5
            e4 -= e4
            print("here29")
    else:
        await bot.delete_message(call.from_user.id, call.message.message_id)
        sti = open(random.choice(stickers), "rb")
        await bot.send_sticker(call.from_user.id, sti)
        if lang == "eng" and j >= 3:
            await bot.send_message(call.from_user.id,
                                   "Progress: 3/3\n"
                                   "Done!\nYour bot is now ready to go! \U0001F603\n"
                                   "Now just type any city or place name to receive its weather information! \U0001F5FA")
            k -= k
            e5 -= e5
            e4 -= e4
            print("here30")
        elif lang == "rus" and j >= 3:
            await bot.send_message(call.from_user.id,
                                   "Прогресс: 3/3\n"
                                   "Готово!\nБот полностью готов к работе! \U0001F603\n"
                                   "Теперь просто введите название любого города или места, чтобы получить информацию о "
                                   "погоде! \U0001F5FA")
            k -= k
            e5 -= e5
            e4 -= e4
            print("here31")
        elif lang == "pol" and j >= 3:
            await bot.send_message(call.from_user.id,
                                   "Postęp: 3/3\n"
                                   "Gotowo!\nBot jest gotowy do pracy! \U0001F603\n"
                                   "Teraz wystarczy wpisać nazwę dowolnego miasta lub miejsca, aby uzyskać informacje o "
                                   "pogodzie! \U0001F5FA"
                                   )
            k -= k
            e5 -= e5
            e4 -= e4
            print("here32")


@dp.callback_query_handler(text="lan")
async def choice(call: CallbackQuery):
    global e, e1, e6, lang_buttons_rus, lang_buttons1, lang_buttons_pol
    if lang == "eng":
        if e >= 1:
            lang_buttons1 = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="English\U0001F1EC\U0001F1E7\U0001F1FA\U0001F1F8 \U00002705",
                                         callback_data="eng"),
                ],
                [
                    InlineKeyboardButton(text="Russian\U0001F1F7\U0001F1FA", callback_data="rus")
                ],
                [
                    InlineKeyboardButton(text="Polish\U0001F1F5\U0001F1F1", callback_data="pol")
                ],
                [
                    InlineKeyboardButton(text="Back \U00002B05", callback_data="back")
                ]
            ])
        await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=lang_buttons1)

    elif lang == "rus":
        if e1 >= 1:
            lang_buttons_rus = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="Английский\U0001F1EC\U0001F1E7\U0001F1FA\U0001F1F8",
                                         callback_data="eng"),
                ],
                [
                    InlineKeyboardButton(text="Русский\U0001F1F7\U0001F1FA \U00002705", callback_data="rus")
                ],
                [
                    InlineKeyboardButton(text="Польский\U0001F1F5\U0001F1F1", callback_data="pol")
                ],
                [
                    InlineKeyboardButton(text="Назад \U00002B05", callback_data="back")
                ]
            ])
        await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=lang_buttons_rus)

    elif lang == "pol":
        if e6 >= 1:
            lang_buttons_pol = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="Angielski\U0001F1EC\U0001F1E7\U0001F1FA\U0001F1F8",
                                         callback_data="eng"),
                ],
                [
                    InlineKeyboardButton(text="Rosyjski\U0001F1F7\U0001F1FA", callback_data="rus")
                ],
                [
                    InlineKeyboardButton(text="Polski\U0001F1F5\U0001F1F1 \U00002705", callback_data="pol")
                ],
                [
                    InlineKeyboardButton(text="Plecy \U00002B05", callback_data="back")
                ]
            ])
        await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=lang_buttons_pol)


@dp.callback_query_handler(text="uni")
async def choice1(call: CallbackQuery):
    global e2, e3, format_buttons1, format_buttons_rus1, format_buttons_pol1
    if lang == "eng":
        if e2 >= 1:
            format_buttons1 = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="Metric \U00002705", callback_data="met"),
                ],
                [
                    InlineKeyboardButton(text="Imperial", callback_data="imp")
                ],
                [
                    InlineKeyboardButton(text="Back \U00002B05", callback_data="back")
                ]
            ])
        elif e3 >= 1:
            format_buttons1 = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="Metric", callback_data="met"),
                ],
                [
                    InlineKeyboardButton(text="Imperial \U00002705", callback_data="imp")
                ],
                [
                    InlineKeyboardButton(text="Back \U00002B05", callback_data="back")
                ]
            ])
        await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=format_buttons1)

    elif lang == "rus":
        if e2 >= 1:
            format_buttons_rus1 = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="Метрическая \U00002705", callback_data="met"),
                ],
                [
                    InlineKeyboardButton(text="Имперская", callback_data="imp")
                ],
                [
                    InlineKeyboardButton(text="Назад \U00002B05", callback_data="back")
                ]
            ])
        elif e3 >= 1:
            format_buttons_rus1 = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="Метрическая", callback_data="met"),
                ],
                [
                    InlineKeyboardButton(text="Имперская \U00002705", callback_data="imp")
                ],
                [
                    InlineKeyboardButton(text="Назад \U00002B05", callback_data="back")
                ]
            ])
        await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id,
                                            reply_markup=format_buttons_rus1)
    elif lang == "pol":
        if e2 >= 1:
            format_buttons_pol1 = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="Metryczny \U00002705", callback_data="met"),
                ],
                [
                    InlineKeyboardButton(text="Imperialny", callback_data="imp")
                ],
                [
                    InlineKeyboardButton(text="Plecy \U00002B05", callback_data="back")
                ]
            ])
        elif e3 >= 1:
            format_buttons_pol1 = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="Metryczny", callback_data="met"),
                ],
                [
                    InlineKeyboardButton(text="Imperialny \U00002705", callback_data="imp")
                ],
                [
                    InlineKeyboardButton(text="Plecy \U00002B05", callback_data="back")
                ]
            ])
        await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id,
                                            reply_markup=format_buttons_pol1)


@dp.callback_query_handler(text="time1")
async def choice1(call: CallbackQuery):
    global time_buttons1, time_buttons_rus1, e4, e5, time_buttons_pol1
    if lang == "eng":
        if e4 >= 1:
            time_buttons1 = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="12-hour format \U00002705", callback_data="12"),
                ],
                [
                    InlineKeyboardButton(text="24-hour format", callback_data="24")
                ],
                [
                    InlineKeyboardButton(text="Back \U00002B05", callback_data="back")
                ]
            ])
        elif e5 >= 1:
            time_buttons1 = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="12-hour format", callback_data="12"),
                ],
                [
                    InlineKeyboardButton(text="24-hour format \U00002705", callback_data="24")
                ],
                [
                    InlineKeyboardButton(text="Back \U00002B05", callback_data="back")
                ]
            ])
        await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id,
                                            reply_markup=time_buttons1)
    elif lang == "rus":
        if e4 >= 1:
            time_buttons_rus1 = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="12-часовой формат \U00002705", callback_data="12"),
                ],
                [
                    InlineKeyboardButton(text="24-часовой формат", callback_data="24")
                ],
                [
                    InlineKeyboardButton(text="Назад \U00002B05", callback_data="back")
                ]
            ])
        elif e5 >= 1:
            time_buttons_rus1 = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="12-часовой формат", callback_data="12"),
                ],
                [
                    InlineKeyboardButton(text="24-часовой формат \U00002705", callback_data="24")
                ],
                [
                    InlineKeyboardButton(text="Назад \U00002B05", callback_data="back")
                ]
            ])
        await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id,
                                            reply_markup=time_buttons_rus1)
    elif lang == "pol":
        if e4 >= 1:
            time_buttons_pol1 = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="Format 12-godzinny \U00002705", callback_data="12"),
                ],
                [
                    InlineKeyboardButton(text="Format 24-godzinny", callback_data="24")
                ],
                [
                    InlineKeyboardButton(text="Placy \U00002B05", callback_data="back")
                ]
            ])
        elif e5 >= 1:
            time_buttons_pol1 = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="Format 12-godzinny", callback_data="12"),
                ],
                [
                    InlineKeyboardButton(text="Format 24-godzinny \U00002705", callback_data="24")
                ],
                [
                    InlineKeyboardButton(text="Placy \U00002B05", callback_data="back")
                ]
            ])
        await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id,
                                            reply_markup=time_buttons_pol1)


@dp.callback_query_handler(text="stop")
async def quitbtn(call: CallbackQuery):
    global k
    await bot.delete_message(call.from_user.id, call.message.message_id)
    k -= k


@dp.callback_query_handler(text="back")
async def backbtn(call: CallbackQuery):
    if lang == "eng":
        await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=ch_buttons)
    elif lang == "rus":
        await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=ch_buttons_rus)
    elif lang == "pol":
        await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=ch_buttons_pol)


if __name__ == "__main__":
    executor.start_polling(dp)
