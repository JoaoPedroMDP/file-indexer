import click
import re

RANGE = 5
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

class Word:
    def __init__(self, word):
        self.word = word
        self.amount = 1

class Trie:
    def __init__(self):
        self.root = {} # inicializando raiz

    def insert_word(self, word):
        current_node = self.root

        word = sanitize_word(word)

        for letter in word:
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]
        
        word_obj = current_node.get("word", None)
        if word_obj:
            word_obj.amount += 1
            # word_obj.insert_filename(filename)
        else:
            current_node["word"] = Word(word)
    
    def word_exists(self, word):
        current_node = self.root

        word = sanitize_word(word)

        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        
        return "word" in current_node

# NÃO ESTÁ FUNCIONANDO AINDA
# def hash_string(string):
#     hashed = 0
#     chars = [char for char in string]
#     for letter in chars:
#         hashed += ord(letter) % RANGE

#     print("{} ficará na posição {}".format(string, hashed % RANGE))

#     return str(hashed % RANGE)

def sanitize_line(line):
    return line.replace("-", " ")

def sanitize_word(word):
    reg = re.compile("[^a-zA-Z ]")
    return reg.sub("", word).lower()

def DEB_viz(object):
    from lolviz import objviz
    viz = objviz(object)
    viz.view()


def insert_line(line):
    line = sanitize_line(line)

    for word in line.split():
        if len(word) >= 2:
            trie.insert_word(word)

if __name__ == "__main__":
    # indexer()

    trie = Trie()

    # files = ["10499.txt"]
    files = ["dummyTest1.txt", "dummyTest2.txt"]
    for filename in files:
        with open(filename, "r") as file:
            for line in file:
                insert_line(line)

    #  Precisa dar 'pip install lolviz' e descomentar a declaração da função ali em cima. Recomendo venv.
    # Gera um PDF e demora um pouco, é bem pesado
    DEB_viz(trie)
    
    # words = ["felipe", "feliz"]

    # for word in words:
    #     trie.insert_word(word)

    # print(trie.word_exists("felipe"))
    # print(trie.word_exists("feliz"))
    # print(trie.word_exists("fel"))