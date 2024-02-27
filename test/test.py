from funcs.func import *
from clases.clases_oper import *
import unittest

test_executed = [
    {'state': 'EXECUTED'},
    {'state': 'CANCELLED'},
    {'state': 'EXECUTED'},
    {'state': 'CANCELLED'},
    {'state': 'EXECUTED'},
    {'state': 'EXECUTED'},
    {'state': 'EXECUTED'},
    {'state': 'CANCELLED'},
    {'state': 'EXECUTED'},]


def test_last_executed_operation():
    assert last_executed_operation(test_executed) == [
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},]


test_date = [
    {'date': '12'},
    {'date': '14'},
    {'date': '1'},
    {'date': '17'},]


def  test_sort_by_date():
    assert sort_by_date(test_date) == [
        {'date': '17'},
        {'date': '14'},
        {'date': '12'},
        {'date': '1'},]


from_ = {'from': 'Visa Classic 2842878893689912',
         'to': 'Счет 35158586384618753655'}
to_ = {'to': 'Счет 90424923579946435907'}
date_ = {'date': '2019-12-08T22:46:21.935582',
         'description': 'Открытие вклада'}
amount_ = {'operationAmount': {'amount': '41096.24',
                               'currency': {'name': 'USD',
                                            'code': 'USD'}}}


def test_class():
    assert Operation(from_).from_to() == "Visa Classic 2842 87** **** 9012 -> Счет"
    assert Operation(to_).from_to() == "Счет **5907"
    assert Operation(date_).date() == "08.12.2019 Открытие вклада"
    assert Operation(amount_).amount() == "41096.24 USD"
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
