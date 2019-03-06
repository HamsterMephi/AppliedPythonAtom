#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    '''
    Метод проверяющий строку на то, является ли
    она палиндромом.
    :param input_string: строка
    :return: True, если строка являестя палиндромом
    False иначе
    '''
	for i in range(len(input_string)//2):
        if input_string[i] != input_string[-1-i]:
            return False
        else:
            return True
    raise NotImplementedError
