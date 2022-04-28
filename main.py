# coding: utf-8
import click

from utils import DEB_viz, sanitize_line, hash_string
from trie import Trie

# @click.command("indexer")
# @click.option("--freq", "frequency")
# @click.option("--freq-word", "word_frequency")
# @click.option("--search", "search")
# @click.option("--word", "word")
# @click.argument('files', nargs=-1, type=click.Path(exists=True))

# def indexer(frequency, word_frequency, word, search, files):
#     print("freq: " + str(frequency))
#     print("wordfreq: " + str(word_frequency))
#     print("search: " + str(search))
#     print("word: " + str(word))
#     print("files: " + str(files))


def insert_line(line, file_name):
    line = sanitize_line(line)

    for word in line.split():
        if len(word) >= 2:
            trie.insert_word(word, file_name)

if __name__ == "__main__":
    # indexer()
    trie = Trie()

    files = ["10499.txt"]
    files += ["dummyTest1.txt", "dummyTest2.txt"]
    for file_name in files:
        with open(file_name, "r") as file:
            for line in file:
                insert_line(line, file_name)

    #  Precisa dar 'pip install lolviz' e descomentar a declaração da função ali em cima. Recomendo venv.
    # Gera um PDF e demora um pouco, é bem pesado SERVE SÓ PRA DEBUGAR 
    # DEB_viz(trie.root['t']['h']['e'])
    
    # words = ["felipe", "feliz"]

    # for word in words:
    #     trie.insert_word(word)

    # print(trie.word_exists("felipe"))
    # print(trie.word_exists("feliz"))
    # print(trie.word_exists("fel"))