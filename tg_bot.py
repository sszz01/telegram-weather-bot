import requests
import datetime
from config import bot_token, ow_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pprint import pprint

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hey, I'm Weather Bot! So, let's get started \U0001F603"
                        "\nJust type any city or place to receive its weather information!")


@dp.message_handler()
async def get_weather(message: types.Message):
    global country_flag, full_country_name, tzsuns, tzsunr, tz_loc_time
    json_to_smile = {"Clear": "Clear sky \U00002600",
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
            f"&units=metric"
        )
        data = r.json()
        pprint(data)
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
        elif country == "US":
            full_country_name = "United States"
            country_flag = "\U0001F1FA\U0001F1F8"
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
            wd = "I couldn't recognize the weather condition in this place. Maybe you can?"

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

        if tl.hour >= ts1.hour and tl.hour < ts2.hour:
            day_emoji = "\U00002600"
        else:
            day_emoji = "\U0001F319"

        tz_loc_time = tl.strftime("%H:%M")
        tzsunr = ts1.strftime("%H:%M")
        tzsuns = ts2.strftime("%H:%M")
        tz_loc_time_1 = tl.strftime("%d.%m.%Y")

        await message.reply(
            f"\U0001F4C5 Local time: {tz_loc_time_1}, {tz_loc_time}{day_emoji}\n"
            f"\U0001F4CD Location: {lat}° N,  {lon}° W\n"
            f"\nAt the moment, the weather in {city}, {full_country_name}{country_flag} is:\n\n\U0001F321"
            f"Temperature: {current_w}°C,  {wd}\n"
            f"\U0001F321Max Temperature for Today: {max_temp}°C\n\U0001F321Min Temperature for Today: {min_temp}°C\n"
            f"\U0001F321Feels like: {fls_like}°C\n"
            f"\U0001F4A6Humidity: {humidity}%\n\U0001F4A8Wind speed: {wind_sp} m/s\n"
            f"\U0001F9EDWind Direction: {w_dir1}\n\U0001F32BVisibility: {vis} km\n"
            f"\U0001F30EAtmospheric pressure: {pressure} hPa\n"
            f"\U0001F305Sunrise time: {tzsunr}\n\U0001F307Sunset time: {tzsuns}\n"
            f"\nThanks for using Weather Bot!\U0001F601"
        )

    except Exception as ex:
        await message.reply("City or place are not found. Could you check your input once again please? \U0001F643")
        print(ex)


if __name__ == "__main__":
    executor.start_polling(dp)
