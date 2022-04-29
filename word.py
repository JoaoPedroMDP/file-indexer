# coding: utf-8
from utils import hash_string

class Word:
    def __init__(self):
        self.word = ""
        self.files = {}
        self.overall_frequency = 0

    def __repr__(self):
        return "<{}:{}>".format(self.word, self.overall_frequency)

    def __str__(self) -> str:
        return "<Word: {}>".format(self.word)

    def insert_file_name(self, file_name, table_range):
        hashed_file_name = hash_string(file_name, table_range)
        if hashed_file_name in self.files:
            self.files[hashed_file_name] += 1
        else:
            self.files[hashed_file_name] = 1
        
        self.overall_frequency+=1

    def add_instance(self, file_name, table_range):
        self.insert_file_name(file_name, table_range)