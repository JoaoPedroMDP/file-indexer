# coding: utf-8
from file import File

class Word:
    def __init__(self, trie_file_count: int):
        self.word = ""
        self.files = {}
        self.file_count = 0
        self.overall_frequency = 0
        self.idf = 0

    def __repr__(self):
        return "<{}:{}>".format(self.word, self.overall_frequency)

    def __str__(self) -> str:
        return "<Word: {}>".format(self.word)

    def insert_file_name(self, file: File):
        if file.hashed_name in self.files.keys():
            self.files[file.hashed_name] += 1
        else:
            self.file_count += 1
            self.files[file.hashed_name] = 1

        self.overall_frequency+=1

    def add_instance(self, file: File):
        self.insert_file_name(file)