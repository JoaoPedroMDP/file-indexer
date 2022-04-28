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

def hash_string(string):
    hashed = 0
    chars = [char for char in string]
    for letter in chars:
        hashed += ord(letter) % RANGE

    print("{} ficará na posição {}".format(string, hashed % RANGE))

    return str(hashed % RANGE)