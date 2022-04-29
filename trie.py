# coding: utf-8
import re
from word import Word
from utils import sanitize_word
class Trie:
    def __init__(self, files):
        self.root = {}  # inicializando raiz
        self.files = files
        self.file_amount = len(files)

    def insert_word(self, word, file_name):
        current_node = self.root

        word = sanitize_word(word)

        for letter in word:
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]

        word_obj = current_node.get("word", None)
        if not word_obj:
            current_node["word"] = Word()
            current_node["word"].word = word
            word_obj = current_node.get("word", None)

        word_obj.add_instance(file_name, self.file_amount)
        return word_obj

    def word_exists(self, word):
        current_node = self.root

        word = sanitize_word(word)

        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
            word_obj = current_node.get("word", None)

        return word_obj