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
            # count = 0
            for line in file:
                line = sanitize_line(line)
                for word in line:
                    if len(word) > 2:
                        word_obj = trie.insert_word(word, file_obj)
                        freq_table.insert_word(word_obj)
                # count += 1
                # print("Linha: {}".format(count))
    freq_table.print()

def freq_word(trie: Trie, word_frequency):
    for file_obj in trie.files:
        with open(file_obj.name, "r", encoding="ISO-8859-1") as file:
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

def calc_tf(trie: Trie, word_obj: Word, file_index: str):
    file = trie.files[int(file_index)]
    word_occurrences_in_file = word_obj.files[file_index]
    return  word_occurrences_in_file / file.word_count

def calc_idf(trie: Trie, word_obj: Word):
    file_count = trie.file_count
    n_files_word_present = word_obj.file_count
    return log(file_count/n_files_word_present, 10)

def search(trie: Trie, search_word: Word):
    for file_obj in trie.files:
        with open(file_obj.name, "r", encoding="ISO-8859-1") as file:
            for line in file:
                line = sanitize_line(line)

                for word in line:
                    if len(word) > 2:
                       trie.insert_word(word, file_obj)

    words = sanitize_line(search_word)

    files_tfidf = {}
    for word in words:
        word_obj = trie.word_exists(word)
        if not word_obj:
            print("Uma palavra do termo não existe nos arquivos. Encerrando programa")
            return 0
        word_obj.idf = calc_idf(trie, word_obj)
        for i in range(trie.file_count):
            dict_key_index = str(i)
            if dict_key_index in word_obj.files.keys():
                tf = calc_tf(trie, word_obj, dict_key_index)
                if dict_key_index in files_tfidf.keys():
                    files_tfidf[dict_key_index] = (tf * word_obj.idf + files_tfidf[dict_key_index]) / 2
                else:
                    files_tfidf[dict_key_index] = tf * word_obj.idf
    import operator
    files_tfidf = dict(sorted(files_tfidf.items(), key=operator.itemgetter(1), reverse=True))

    for file.hashed_name in files_tfidf.keys():
        print("TF-IDF Arquivo {}: {}".format(file.hashed_name, files_tfidf[file.hashed_name]))

    # for file in trie.files:
    #     if file.hashed_name in files_tfidf.keys():
    #         print("{} - {}".format(file.name, files_tfidf[file.hashed_name]))
    # average = sum(all_tfidf.values()) / len(all_tfidf)
    # print("TF-IDF de '{}': {}".format(search_word, average))