#!/usr/bin/env python3

def return_evens(num_list):
    even = (n for n in num_list if n % 2 == 0)
    even_list = list(even)
    print(even_list)
    if not even_list:
        return []
    else:
        return even_list
    pass
return_evens([0, 1, 3, 5, 7, 8, 9,11,34,5,43,44])


def make_exclamation(sentence_list):
    excalamation = [f"{n}!"  for n in sentence_list]
    print(excalamation)
    if not excalamation:
        return []
    else:
        return excalamation
    pass

make_exclamation(["Hello", "I'm doing great", "Python is fun"])