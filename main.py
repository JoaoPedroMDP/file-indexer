import click

@click.command("indexer")
@click.option("--freq", "frequency")
@click.option("--freq-word", "word_frequency")
@click.option("--search", "search")
@click.option("--word", "word", type=int)
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def indexer(frequency, word_frequency, word, search, files):
    print("freq: " + str(frequency))
    print("wordfreq: " + str(word_frequency))
    print("search: " + str(search))
    print("word: " + str(word))
    print("files: " + str(files))

if __name__ == "__main__":
    indexer()