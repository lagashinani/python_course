import unittest
from unittest.mock import patch

import sys
from contextlib import contextmanager
from io import StringIO

from task import *

# перенаправляет выход из стандартного потока в переменнуые. OHHHH
# можно сделать как декоратор, но не будем усложнять
@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestTaskMethods(unittest.TestCase):

    @patch('builtins.input', lambda *args: '2207 876234')
    def test_docs_person(self):
        with captured_output() as (out, err):
            print_docs_person()
        output = out.getvalue().strip()
        self.assertEqual(output, "Василий Гупкин")

    @patch('builtins.input', lambda *args: '2207 876234')
    def test_docs_shelf(self):
        with captured_output() as (out, err):
            print_docs_shelf()
        output = out.getvalue().strip()
        self.assertEqual(output, "1")

    @patch('builtins.input', side_effect=['111', 'test_doc', 'Тестовый Человек', '4', '2',
        '111', '1'])
    def test_addmove(self, mock_input):
        with captured_output() as (out, err):
            add_doc()
            move_doc()
            print_all_docs()

        output = out.getvalue().strip()
        self.assertEqual(output, 'No such shelf\n' + 
            'passport "2207 876234" "Василий Гупкин"\n' + 
            'invoice "11-2" "Геннадий Покемонов"\n' + 
            'insurance "10006" "Аристарх Павлов"\n' + 
            'test_doc "111" "Тестовый Человек"')

    @patch('builtins.input', side_effect=['11-2'])
    def test_delete(self, mock_input):
        with captured_output() as (out, err):
            delete_doc()
            print_all_docs()

        output = out.getvalue().strip()
        self.assertEqual(output, 'passport "2207 876234" "Василий Гупкин"\n' +  
            'insurance "10006" "Аристарх Павлов"\n' +
            'test_doc "111" "Тестовый Человек"')

if __name__ == '__main__':
    unittest.main()