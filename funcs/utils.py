import json
from datetime import datetime
import re


def change_date_format(date):
    """конвертирует дату в формат день/месяц/год"""
    dt = datetime.fromisoformat(date)
    formatted_date = dt.strftime("%d.%m.%Y")
    return formatted_date


def get_data(data):
    """Принимает файл json и конвертирует его в формат для питона"""
    with open(data, "r", encoding="utf-8") as operation_list_json:
        operation_list_txt = operation_list_json.read()
        operation_list_python = json.loads(operation_list_txt)
        return operation_list_python


def get_all_executed(operations_list):
    """убирает из списка все элементы, статус которых не Executed"""
    executed_list = []
    for operation in operations_list:
        if 'state' in operation and operation['state'] == "EXECUTED":
            executed_list.append(operation)
    return executed_list


def date_key(dictionary):
    """вспомогательная функция для функции sort_last_five_operations
    она создает ключ сортировки, принимая словарь как аргумент и извлекая значение ключа date"""
    return dictionary["date"]


def sort_last_five_operations(operations_list):
    """Сортирует список по дате и оставляет только 5 последних операций"""
    sorted_list = sorted(operations_list, key=date_key, reverse=True)
    last_five_operations = sorted_list[:5]
    return last_five_operations


def hide_card(card_number):
    """Принимает обычный формат ввода карты и маскирует 6 цифр"""
    only_digits = re.sub(r'[^0-9]', '', card_number)
    only_letters = re.sub(r'[^A-z ]', '', card_number)
    hidden_number = only_digits[:4] + " " + only_digits[4:6] + "** **** " + only_digits[-4:]
    return only_letters + hidden_number


def hide_account(account_number):
    """Принимает обычный формат ввода счета и маскирует все цифры кроме последних 4"""
    only_digits = re.sub(r'[^0-9]', '', account_number)
    hidden_number = "Счет **" + only_digits[-4:]
    return hidden_number
