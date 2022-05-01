# coding: utf-8
import re

from lolviz import objviz

RANGE = 5

def sanitize_line(line):
    splitted = line.replace("-", " ")
    return [word for word in splitted.split(" ") if len(word) > 2]

def sanitize_word(word):
    reg = re.compile("[^a-zA-Z ]")
    return reg.sub("", word).lower()

def DEB_viz(object):
    viz = objviz(object)
    viz.view()

def hash_string(string, table_range) -> int:
    hashed = 0
    chars = [char for char in string]
    for letter in chars:
        hashed += ord(letter) % table_range

    return hashed % table_range