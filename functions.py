# coding: utf-8
from math import log

from utils import sanitize_line, DEB_viz
from trie import Trie
from frequencyTable import FrequencyTable
from word import Word

def freq(trie: Trie, frequency):
    freq_table = FrequencyTable(frequency)

    for file_obj in trie.files:
        with open(file_obj.name, "r", encoding="ISO-8859-1") as file:
            count= 0
            for line in file:
                line = sanitize_line(line)
                for word in line:
                    if len(word) > 2:
                        word_obj = trie.insert_word(word, file_obj)
                        freq_table.insert_word(word_obj)
                        count += 1
    freq_table.print()

def freq_word(trie: Trie, word_frequency):
    for file_obj in trie.files:
        with open(file_obj.name, "r") as file:
            for line in file:
                line = sanitize_line(line)

                for word in line:
                    if len(word) > 2:
                        trie.insert_word(word, file_obj)
    
    word = trie.word_exists(word_frequency)
    if word:
        print("Aparicoes da palavra {}: {}".format(word.word, word.overall_frequency))
    else:
        print("Palavra nao encontrada")

def calc_tf(trie: Trie, word_obj: Word, file_index: int):
    file = trie.files[file_index]
    word_occurrences_in_file = word_obj.files[file_index]
    return  word_occurrences_in_file / file.word_count

def calc_idf(trie: Trie, word_obj: Word, file_index: int):
    file_count = trie.file_count
    n_files_word_present = word_obj.file_count
    return log(file_count/n_files_word_present, 10)


def search(trie: Trie, search_word: Word):
    for file_obj in trie.files:
        with open(file_obj.name, "r") as file:
            for line in file:
                line = sanitize_line(line)

                for word in line:
                    if len(word) > 2:
                       trie.insert_word(word, file_obj)

    words = sanitize_line(search_word)
    all_tfidf = {}
    for word in words:
        word_obj = trie.word_exists(word)
        for i in range(trie.file_count):
            if word_obj.files[i] is not None:
                tf = calc_tf(trie, word_obj, i)
                idf = calc_idf(trie, word_obj, i)
                all_tfidf[word] = tf * idf

    average = sum(all_tfidf.values()) / len(all_tfidf)
    print("TF-IDF de '{}': {}".format(search_word, average))