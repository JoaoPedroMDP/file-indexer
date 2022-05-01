# coding: utf-8
from utils import hash_string

class File:
    def __init__(self, filename: str, hashed_name: int):
        self.name = filename
        self.word_count = 0
        self.hashed_name = str(hashed_name)
        self.next_file = None

