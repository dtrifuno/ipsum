import collections
from math import ceil
from typing import Counter

from ipsum import SupportedLanguage
from ipsum.corpus import Corpus
from ipsum.parse import load_parser


def most_common_characters(language: SupportedLanguage) -> None:
    """Print most frequent characters in a language corpus."""
    num_of_chars = 120
    language_code = language.value

    corpus = Corpus(f"corpora/{language_code}.zip")
    character_count: Counter[str] = collections.Counter()
    for text in corpus:
        text_without_whitespace = "".join(text.split())
        character_count += collections.Counter(text_without_whitespace)
    top_n_characters = [
        character for character, _ in character_count.most_common(num_of_chars)
    ]

    row_size = 20
    print(f"{num_of_chars} Most Common Characters in {language.name} Corpus")
    for row in range(ceil(num_of_chars / row_size)):
        print(" ".join(top_n_characters[row * row_size : (row + 1) * row_size]))


def most_common_words(language: SupportedLanguage) -> None:
    """Print most frequent words in a language corpus."""
    num_of_words = 100

    language_code = language.value
    parser = load_parser(language)
    corpus = Corpus(f"corpora/{language_code}.zip")

    words = parser.get_words(corpus)
    word_count = collections.Counter([word.lower() for word in words])
    top_n_words = [word for word, _ in word_count.most_common(num_of_words)]

    row_size = 10
    print(f"{num_of_words} Most Common Words in {language.name} Corpus")
    for row in range(ceil(num_of_words / row_size)):
        print(", ".join(top_n_words[row * row_size : (row + 1) * row_size]))
