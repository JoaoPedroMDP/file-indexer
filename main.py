# coding: utf-8
import argparse

from utils import DEB_viz, sanitize_line, hash_string
from trie import Trie
from functions import freq, freq_word

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
search_word = args.search
files = args.files

def indexer(frequency, word_frequency, search_word, files):
    trie = Trie(files)
    if frequency is not None:
        freq(trie=trie, frequency=int(frequency))
    elif word_frequency is not None:
        freq_word(trie=trie, word_frequency=word_frequency)
    # else:
    #     search(trie=trie, search_word=search_word)

if __name__ == "__main__":
    files = ["dummyTest1.txt", "dummyTest2.txt"]
    indexer(frequency=frequency, word_frequency=word_frequency, search_word=search_word, files=files)
    #  Precisa dar 'pip install lolviz' e descomentar a declaração da função ali em cima. Recomendo venv.
    # Gera um PDF e demora um pouco, é bem pesado SERVE SÓ PRA DEBUGAR 
    # DEB_viz(trie.root['t']['h']['e'])