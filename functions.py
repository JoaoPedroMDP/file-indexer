from utils import sanitize_line
from trie import Trie
from frequencyTable import FrequencyTable

def freq(trie: Trie, frequency):
    freq_table = FrequencyTable(frequency)

    for file_name in trie.files:
        with open(file_name, "r") as file:
            for line in file:
                line = sanitize_line(line)

                for word in line.split():
                    if len(word) > 2:
                        word_obj = trie.insert_word(word, file_name)
                        freq_table.insert_word(word_obj)
    freq_table.print()
    # from utils import DEB_viz
    # DEB_viz(freq_table)
