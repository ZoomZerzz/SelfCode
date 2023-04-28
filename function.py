import urllib.request
import requests
import json
import webbrowser
from typing import List

def phone_info(phone):
    getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone

    try:
        infoPhone = urllib.request.urlopen(getInfo)
        infoPhone = json.load(infoPhone)

        region_name = infoPhone["region"]["name"]
        operator_name = infoPhone["0"]["oper"]
        country_name = infoPhone["country"]["name"]
        okrug_name = infoPhone["region"]["okrug"]
        lang_name = infoPhone["country"]["lang"]

        return region_name, operator_name, country_name, okrug_name, lang_name

    except Exception as e:
        return 'Телефон не найден', 'Телефон не найден', 'Телефон не найден'
    
def crypto():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Cdogecoin%2Ctether&vs_currencies=rub")
    data = response.json()

    usdt = f"{data['tether']['rub']:.2f} \U0001F4B5"
    btc = f"{data['bitcoin']['rub']:.2f} \U0001F680"
    eth = f"{data['ethereum']['rub']:.2f} \U0001F6E1"
    dogecoin = f"{data['dogecoin']['rub']:.2f} \U0001F436"

    return f"💰 Курсы криптовалют (в рублях):\n\nUSDT: {usdt}\nBITCOIN: {btc}\nETH: {eth}\nDOGECOIN: {dogecoin}"
    