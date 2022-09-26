#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    n_str = ""
    for ch in str:
        if i != n:
            n_str += ch
        i += 1
    return n_str
