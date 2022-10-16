from unittest import mock
from unittest.mock import patch
import pytest
from main import get_doc_owner_name, get_all_doc_owners_names, add_new_doc, add_new_shelf, append_doc_to_shelf, \
    delete_doc, remove_doc_from_shelf, show_all_docs_info, check_document_existance
from parameterized import parameterized

# 0
FIXTURES_1 = [
    ('2207 876234', True),
    ('11-2', True),
    ('10006', True),
    ('1121212', False),
    ('10000', False)
]


@pytest.mark.parametrize("a, exp_result", FIXTURES_1)
def test_check_document_existance(a, exp_result):
    result = check_document_existance(a)
    assert exp_result == result


1
@mock.patch('builtins.input')
def test_get_doc_owner_name(inp):
    inp.side_effect = ["11-2"]
    result = get_doc_owner_name()
    assert "Геннадий Покемонов" == result


# 2
def test_get_all_doc_owners_names():
    result = get_all_doc_owners_names()
    assert {'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'} == result


# 3
def test_add_new_doc():
    result = add_new_doc("1", "doc", "Nas", "15")
    assert "15" == result


# 4
FIXTURES_3 = [
    ("1", ('1', False)),
    ("2", ('2', False)),
    ("3", ('3', False)),
    ("4", ('4', True)),
    ("5", ('5', True))
]


@pytest.mark.parametrize("a, exp_result", FIXTURES_3)
def test_add_new_shelf(a, exp_result):
    result = add_new_shelf(a)
    assert exp_result == result


# 5
FIXTURES_5 = [
    ("00001", "3", ["00001"]),
    ("00002", "1", ['2207 876234', '11-2', '5455 028765', '00002'])
]


@pytest.mark.parametrize("a, b, exp_result", FIXTURES_5)
def test_append_doc_to_shelf(a, b, exp_result):
    result = append_doc_to_shelf(a, b)
    assert exp_result == result


# 6
@mock.patch('builtins.input')
def test_delete_doc(inp):
    inp.side_effect = ['10006']
    result = delete_doc()
    assert ('10006', True) == result


# 7
FIXTURES_7 = [
    ('2207 876234', ['11-2', '5455 028765']),
    ('11-2', ['5455 028765']),
    ('5455 028765', []),
    ('10006', [])
]


@pytest.mark.parametrize("a, exp_result", FIXTURES_7)
def test_remove_doc_from_shelf(a, exp_result):
    result = remove_doc_from_shelf(a)
    assert exp_result == result


# 8
a = [{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
     {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
     {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}]


def test_show_all_docs_info():
    result = show_all_docs_info()
    assert a == result
