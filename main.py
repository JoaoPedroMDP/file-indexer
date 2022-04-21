import click

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

class Trie:
    def __init__(self):
        self.root = {"*":"*"} # inicializando raiz

    def insert_word(self, word):
        current_node = self.root

        for letter in word:
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]
        current_node["*"] = ["*"] # fim de uma palavra
    
    def word_exists(self, word):
        current_node = self.root
        
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return "*" in current_node # retorna se * ou nao


if __name__ == "__main__":
    # indexer()

    trie = Trie()

    with open("10499.txt", "r") as file:
        for line in file:
            for word in line.split():
                trie.insert_word(word)

    print(trie.word_exists("The"))
    print(trie.word_exists("teste"))
    
    # words = ["felipe", "feliz"]

    # for word in words:
    #     trie.insert_word(word)

    # print(trie.word_exists("felipe"))
    # print(trie.word_exists("feliz"))
    # print(trie.word_exists("fel"))