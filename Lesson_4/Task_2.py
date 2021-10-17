#2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
# возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере,
# посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы
# с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
# функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.


import requests
from requests import get, utils

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
response = requests.utils.get_unicode_from_response(response)


def currency_rates(abbreviation):
    content = response.split('Valute ID=')
    for i in content:
        if abbreviation.upper() in i:
            return float(i.replace("/", "").split('<Value>')[1].replace(',', '.'))

if __name__ == '__main__':
    print(currency_rates('EUR'))
    print(currency_rates('Usd'))
