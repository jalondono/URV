#!/usr/bin/python3
"""Convert a string to number"""
from word2number import w2n


def word_to_number(number):
    """Convert a string into integer"""
    str_number = ''
    int_number = 0
    try:
        int_number = int(number)
        return int_number
    except Exception:
        list_str_numbers = number.split("ty")
        if len(list_str_numbers) > 1:
            list_str_numbers[0] += 'ty'
            for item in list_str_numbers:
                str_number += item + ' '
            int_number = w2n.word_to_num(str_number)
        else:
            int_number = w2n.word_to_num(number)
        return int_number


"""
    if __name__ == '__main__':
    word_to_number("0r")
"""