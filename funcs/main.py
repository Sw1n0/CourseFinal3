import os.path

from funcs.utils import get_data, get_all_executed, sort_last_five_operations, hide_account, hide_card, \
    change_date_format

path_to_operations = os.path.join(os.path.dirname(__file__), "operation_list.json")


def main_func(file):
    """Основная функция - принимает в качестве аргумента файл со списком словарей данных.
    выводит на экран список из 5 последних выполненных клиентом операций в формате:

<дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта>"""
    result = []
    list_python = get_data(file)
    filtered_list = get_all_executed(list_python)
    sorted_list = sort_last_five_operations(filtered_list)
    for dictionary in sorted_list:
        date = change_date_format(dictionary["date"])
        if "from" not in dictionary:
            line_from = ""
        elif dictionary["from"][:4] == "Счет":
            line_from = hide_account(dictionary["from"])
        else:
            line_from = hide_card(dictionary["from"])
        if dictionary["to"][:4] == "Счет":
            line_to = hide_account(dictionary["to"])
        else:
            line_to = hide_card(dictionary["to"])
        line = f"{date} {dictionary["description"]}\n{line_from} -> {line_to}\n{dictionary["operationAmount"]["amount"]} {dictionary["operationAmount"]["currency"]["name"]}."
        result.append(line)
    return "\n".join(result)


print(main_func(path_to_operations))
