import os.path

from funcs.main import main_func

test = os.path.join(os.path.dirname(__file__), "test_list.json")

def test_main_func():
    expected_output = ('30.08.2019 Пополнение счета телефона\n'
 'Maestro 1596 83** **** 5199 -> Maestro 2396 83** **** 5199\n'
 '1000.00 USD.\n'
 '29.08.2019 Перевод на карту\n'
 'Maestro 1596 83** **** 5199 ->  4276 12** **** 9012\n'
 '1500.00 руб..\n'
 '28.08.2019 Оплата услуг связи\n'
 'Maestro 1596 83** **** 5199 -> Visa Classic 4596 83** **** 5199\n'
 '2000.00 EUR.\n'
 '27.08.2019 Покупка товаров в интернет-магазине\n'
 'Maestro 1596 83** **** 5199 -> Visa Gold 3589 27** **** 1603\n'
 '5000.00 USD.\n'
 '26.08.2019 Перевод организации\n'
 'Maestro 1596 83** **** 5199 -> Счет **9589\n'
 '10000.00 руб..')
    actual_output = main_func(test)
    assert actual_output == expected_output