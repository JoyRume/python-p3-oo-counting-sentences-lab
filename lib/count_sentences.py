#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, string):
        if isinstance(string, str):
            self._value = string
        else:
            print('The value must be a string.')

    value = property(get_value, set_value)

    def is_sentence(self):
        if self._value.endswith('.'):
            return True
        else:
            return False
        
    def is_question(self):
        if self._value.endswith('?'):
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self._value.endswith('!'):
            return True
        else:
            return False
        
    def count_sentences(self):
        for punctuation in ['!', '?']:
            self._value = self._value.replace(punctuation, '.')
        result_list = self._value.split('.')
        result_list = [s for s in result_list if s != '']
        print(len(result_list))
        return len(result_list)
