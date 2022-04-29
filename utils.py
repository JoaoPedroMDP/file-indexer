# coding: utf-8
import re

from lolviz import objviz

RANGE = 5

def sanitize_line(line):
    return line.replace("-", " ")

def sanitize_word(word):
    reg = re.compile("[^a-zA-Z ]")
    return reg.sub("", word).lower()

def DEB_viz(object):
    viz = objviz(object)
    viz.view()

def hash_string(string, table_range):
    hashed = 0
    chars = [char for char in string]
    for letter in chars:
        hashed += ord(letter) % table_range


    return str(hashed % table_range)