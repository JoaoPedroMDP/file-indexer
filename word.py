# coding: utf-8
from utils import hash_string

class Word:
    def __init__(self):
        self.word = ""
        self.files = {}

    def insert_file_name(self, file_name):
        hashed_file_name = hash_string(file_name)
        if hashed_file_name in self.files:
            self.files[hashed_file_name] += 1
        else:
            self.files[hashed_file_name] = 1

    def add_instance(self, file_name):
        self.insert_file_name(file_name)