# coding: utf-8
import argparse

from utils import DEB_viz, sanitize_line, hash_string
from trie import Trie

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--freq",
                    metavar = "freq",
                    required = False,
                    help = "Numero de ocorrencias das N palavras mais frequentes no documento passado em ordem decrescente"
                    )
parser.add_argument("-fw", "--freq-word",
                    metavar = "freqword",
                    required = False,
                    help = "Contagem de uma palavra especifica no documento passado"
                    )
parser.add_argument("-s", "--search",
                    metavar = "search",
                    required = False,
                    help = "Listagem dos documentos mais relevantes para um dado termo de busca"
                    )
parser.add_argument("files",
                    nargs="*",
                    help="Documentos passados para busca")

args = parser.parse_args()

frequency = args.freq
word_frequency = args.freq_word
search = args.search
files = args.files

def indexer(frequency, word_frequency, search, files):
    print("freq: " + str(frequency))
    print("wordfreq: " + str(word_frequency))
    print("search: " + str(search))
    print("files: " + str(files))

def insert_line(line, file_name):
    line = sanitize_line(line)

    for word in line.split():
        if len(word) >= 2:
            trie.insert_word(word, file_name)

if __name__ == "__main__":
    indexer(frequency=frequency, word_frequency=word_frequency, search=search, files=files)
    trie = Trie()

    files = ["dummyTest1.txt", "dummyTest2.txt"]
    for file_name in files:
        with open(file_name, "r") as file:
            for line in file:
                insert_line(line, file_name)

    #  Precisa dar 'pip install lolviz' e descomentar a declaração da função ali em cima. Recomendo venv.
    # Gera um PDF e demora um pouco, é bem pesado SERVE SÓ PRA DEBUGAR 
    # DEB_viz(trie.root['t']['h']['e'])