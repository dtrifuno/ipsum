from ipsum.corpus import Corpus
from ipsum.parse import load_parser
from ipsum.supported_languages import SupportedLanguage


def parser_diagnostics(language: SupportedLanguage) -> None:
    """Print corpus/parser diagnostic data for a single language."""
    diagnostics = _get_parser_diagnostics(language)
    print(diagnostics)


def parser_diagnostics_all() -> None:
    """Print corpus/parser diagnostic data for all available languages."""
    for language in SupportedLanguage:
        diagnostics = _get_parser_diagnostics(language)
        print(diagnostics)
        print()


def _get_parser_diagnostics(language: SupportedLanguage) -> str:
    parser = load_parser(language)
    corpus = Corpus(f"corpora/{language.value}.zip")

    result = [f"{language.name} corpus/parser diagnostics:"]

    words = parser.get_words(corpus)
    result.append(f"  ▪ Words: {len(words)}")

    sentences = parser.get_sentences(corpus)
    result.append(f"  ▪ Sentences: {len(sentences)}")

    lowercase_words, uppercase_words = parser.get_word_counts(corpus)
    skeletons = parser.get_skeletons(corpus, set(lowercase_words), set(uppercase_words))
    result.append(
        f"  ▪ Valid sentence skeletons: {len(skeletons)} "
        f"({round(100 * len(skeletons) / len(sentences), 2)}%)",
    )

    return "\n".join(result)
