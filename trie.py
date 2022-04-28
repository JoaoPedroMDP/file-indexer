# coding: utf-8
import re
from word import Word
from utils import sanitize_word
class Trie:
    def __init__(self):
        self.root = {}  # inicializando raiz

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

        word_obj.add_instance(file_name)

    def word_exists(self, word):
        current_node = self.root

        word = sanitize_word(word)

        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]

        return "word" in current_node