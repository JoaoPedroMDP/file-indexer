# coding: utf-8
from file import File
from word import Word
from utils import sanitize_word, hash_string


class Trie:
    def __init__(self, files_names):
        self.root = {}  # inicializando raiz
        self.files = self.wrap_files(files_names)
        self.file_count = len(files_names)

    def insert_word(self, word, file: File):
        current_node = self.root

        word = sanitize_word(word)

        for letter in word:
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]

        word_obj = current_node.get("word", None)
        if not word_obj:
            current_node["word"] = Word(self.file_count)
            current_node["word"].word = word
            word_obj = current_node.get("word", None)

        word_obj.add_instance(file)
        file.word_count += 1
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
    
    def wrap_files(self, files_names):
        table_size = len(files_names)
        wrapped = [None] * table_size

        for file in files_names:
            hashed_name = hash_string(file, table_size)
            wrapped[hashed_name] = File(file, hashed_name)

        return wrapped