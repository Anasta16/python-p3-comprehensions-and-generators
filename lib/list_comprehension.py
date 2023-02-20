#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = []
    for n in num_list:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers

def make_exclamation(sentence_list):
    new_list = []
    for i in sentence_list:
        new_list = [i + '!' for i in sentence_list]
    return new_list