from funcs.utils import change_date_format, get_all_executed, sort_last_five_operations, hide_card, hide_account


def test_change_date_format():
    assert change_date_format("2019-08-26T10:50:58.294041") == "26.08.2019"


def test_get_all_executed():
    operations_list = [
        {
            "id": 1,
            "state": "EXECUTED"
        },
        {
            "id": 2,
            "state": "FAILED"
        },
        {
            "id": 3,
            "state": "EXECUTED"
        },
        {
            "id": 4,
            "state": "SUCCEEDED"
        },
        {
            "id": 5,
            "state": "EXECUTED"
        },
        {
            "id": 6
        }
    ]
    executed_list = get_all_executed(operations_list)
    assert executed_list == [
        {
            "id": 1,
            "state": "EXECUTED"
        },
        {
            "id": 3,
            "state": "EXECUTED"
        },
        {
            "id": 5,
            "state": "EXECUTED"
        }
    ]


def test_sort_last_five_operations():
    operations_list = [
        {
            "id": 1,
            "date": "2020-08-30T11:00:00.000000"
        },
        {
            "id": 2,
            "date": "2019-08-20T11:00:00.000000"
        },
        {
            "id": 3,
            "date": "2019-08-29T15:30:45.123456"
        },
        {
            "id": 4,
            "date": "2019-08-25T18:00:00.000000"
        },
        {
            "id": 5,
            "date": "2019-08-27T12:30:15.978084"
        },
        {
            "id": 6,
            "date": "2019-07-27T12:30:15.978084"
        }
    ]
    sorted_list = sort_last_five_operations(operations_list)
    assert sorted_list == [
        {
            "id": 1,
            "date": "2020-08-30T11:00:00.000000"
        },
        {
            "id": 3,
            "date": "2019-08-29T15:30:45.123456"
        },
        {
            "id": 5,
            "date": "2019-08-27T12:30:15.978084"
        },
        {
            "id": 4,
            "date": "2019-08-25T18:00:00.000000"
        },
        {
            "id": 2,
            "date": "2019-08-20T11:00:00.000000"
        }
    ]


def test_hide_card():
    assert hide_card("super puper mega card 1546468513657985") == "super puper mega card 1546 46** **** 7985"


def test_hide_account():
    assert hide_account("Счет 96292138399386853355") == "Счет **3355"



