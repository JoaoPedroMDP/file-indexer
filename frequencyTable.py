
# O array de palavras começa da palavra com menor frequência no top N palavras
class FrequencyTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.table = [None] * self.table_size
        self.word_count = 0

    def print(self):
        for i in range(self.table_size - 1, 0, -1):
            if self.table[i] is not None:
                print("{} - Frequencia {}".format(self.table[i].word, self.table[i].overall_frequency))

    def search_word(self, word):
        for i in range(self.table_size):
            if self.table[i] == word:
                return i
        return None

    def insert_ordered(self, word, starting_index = 0):
        self.table[starting_index] = word
        for i in range(starting_index, self.table_size - 1):
            if self.table[i + 1] is None:
                self.table[i + 1] = word
                self.table[i] = None
            elif self.table[i + 1].overall_frequency < self.table[i].overall_frequency:
                aux = self.table[i + 1]
                self.table[i + 1] = word
                self.table[i] = aux

    def insert_word(self, word):
        potential_duplicate = self.search_word(word)
        if potential_duplicate is not None:
            self.insert_ordered(word, potential_duplicate)
        else:
            self.insert_ordered(word)
