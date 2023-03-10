import collections
import os
from typing import Counter, Sequence

import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

from ipsum.corpus import Corpus
from ipsum.model import load_model
from ipsum.parse import load_parser
from ipsum.supported_languages import SupportedLanguage
from ipsum.utils import iterate_over_chunks

matplotlib.use("Agg")


def model_diagnostics(language: SupportedLanguage) -> None:
    """Plot all diagnostic graphs for a single language."""
    figure = plot_diagnostic_graphs(language)

    if not os.path.exists("diagnostics/"):
        os.makedirs("diagnostics/")
    figure.savefig(f"diagnostics/{language.value}.png")


def model_diagnostics_all() -> None:
    """Plot all diagnostic graphs for all available languages."""
    if not os.path.exists("diagnostics/"):
        os.makedirs("diagnostics/")

    for language in SupportedLanguage:
        figure = plot_diagnostic_graphs(language)
        path = f"diagnostics/{language.value}.png"
        figure.savefig(path)
        print(f"Diagnostic graph saved as {path}.\n")


def plot_diagnostic_graphs(language: SupportedLanguage):
    """Returns a figure containing all model diagnostic plots for a given language."""
    model = load_model(language)
    language_code = language.value
    parser = load_parser(language_code)
    corpus = Corpus(f"corpora/{language_code}.zip")

    print(f"Plotting diagnostic graphs for {language.name} model:")

    fig, axs = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle(
        f"{language.name} Language Model Diagnostics", size="xx-large", weight="bold"
    )

    corpus_words = []
    for text in corpus:
        corpus_words += parser.extract_words(text.lower())
    model_words = [word.lower() for word in model.generate_words(len(corpus_words))]

    print("  ▪ Computing character frequencies...")
    plot_ngram_frequency(corpus_words, model_words, ax=axs[0, 0])
    axs[0, 0].set_title("Character Frequency")

    print("  ▪ Computing word lengths...")
    plot_word_length(corpus_words, model_words, ax=axs[0, 1])
    axs[0, 1].set_title("Word Lengths")

    print("  ▪ Computing distinct word ratios...")
    plot_unique_words(corpus_words, model_words, ax=axs[1, 0])
    axs[1, 0].set_title("Ratio of Distinct Words (Heaps' Law)")

    print("  ▪ Computing sentence lengths...")
    plot_sentence_lengths(corpus, parser, model, ax=axs[1, 1])
    axs[1, 1].set_title("Sentence Lengths")

    print("  ▪ Computing word frequencies (rank)...")
    plot_word_rank_frequency(corpus_words, model_words, ax=axs[0, 2])
    axs[0, 2].set_title("Word Rank-Frequency (Zipf's Law)")

    print("  ▪ Computing word frequencies (length)...")
    plot_length_rank_frequency(corpus_words, model_words, ax=axs[1, 2])
    axs[1, 2].set_title("Word Length-Frequency (Brevity Law)")

    return fig


def plot_ngram_frequency(
    corpus_words: Sequence[str],
    model_words: Sequence[str],
    ngram_size: int = 1,
    ax=None,
):
    """Plot the frequency of ngrams in text generated by the model versus the corpus."""
    corpus_ngram_counts: Counter[str] = collections.Counter()
    model_ngram_counts: Counter[str] = collections.Counter()

    for word in corpus_words:
        corpus_ngram_counts += collections.Counter(
            str(ngram) for ngram in iterate_over_chunks(word, ngram_size)
        )

    for word in model_words:
        model_ngram_counts += collections.Counter(
            str(ngram) for ngram in iterate_over_chunks(word, ngram_size)
        )

    ngrams = list(set().union(corpus_ngram_counts.keys(), model_ngram_counts.keys()))
    ngrams.sort()

    data = [[ngram, corpus_ngram_counts[ngram], "corpus"] for ngram in ngrams] + [
        [ngram, model_ngram_counts[ngram], "model"] for ngram in ngrams
    ]
    df = pd.DataFrame(data, columns=[f"{ngram_size}-gram", "count", "type"])

    return sns.barplot(data=df, x=f"{ngram_size}-gram", y="count", hue="type", ax=ax)


def plot_word_length(
    corpus_words: Sequence[str],
    model_words: Sequence[str],
    max_word_length: int = 20,
    ax=None,
):
    """Plot frequency of different word lengths in model-generated and corpus text."""
    corpus_lengths = collections.Counter(len(word) for word in corpus_words)
    model_lengths = collections.Counter(len(word) for word in model_words)

    corpus_total = sum(corpus_lengths.values())
    model_total = sum(model_lengths.values())
    data = []
    for word_length in range(1, max_word_length + 1):
        data.append([word_length, corpus_lengths[word_length] / corpus_total, "corpus"])
        data.append([word_length, model_lengths[word_length] / model_total, "model"])

    df = pd.DataFrame(data, columns=["word length", "frequency", "type"])

    return sns.barplot(data=df, x="word length", y="frequency", hue="type", ax=ax)


def plot_unique_words(
    corpus_words: Sequence[str],
    model_words: Sequence[str],
    text_sizes: Sequence[int] = (50, 100, 250, 1000, 2500, 5000),
    ax=None,
):
    """Plot the distributions of the ratio of distinct words at different text sizes."""
    data = []
    for text_size in text_sizes:
        for words_chunk in iterate_over_chunks(model_words, text_size):
            data.append([text_size, len(set(words_chunk)) / text_size, "corpus"])
        for words_chunk in iterate_over_chunks(corpus_words, text_size):
            data.append([text_size, len(set(words_chunk)) / text_size, "model"])

    df = pd.DataFrame(
        data, columns=["text size", "proportion of distinct words", "type"]
    )

    return sns.violinplot(
        data=df,
        x="text size",
        y="proportion of distinct words",
        hue="type",
        gridsize=24,
        ax=ax,
    )


def plot_sentence_lengths(corpus, parser, model, ax=None):
    """Plot the distribution of sentence lengths in corpus and model-generated texts."""
    data = []
    for text in corpus:
        text_sentences = parser.extract_sentences(text)
        for sentence in text_sentences:
            text_sentence_words = parser.extract_words(sentence)
            data.append([len(text_sentence_words), "corpus"])

        generated_sentences = model.generate_sentences(len(text_sentences))
        for sentence in generated_sentences:
            generated_sentence_words = parser.extract_words(sentence)
            data.append([len(generated_sentence_words), "model"])

    df = pd.DataFrame(data, columns=["sentence length (words)", "type"])

    plot = sns.kdeplot(
        data=df,
        x="sentence length (words)",
        hue="type",
        fill=True,
        common_norm=True,
        alpha=0.5,
        linewidth=0,
        gridsize=50,
        ax=ax,
    )
    plot.set(xlim=(0, 100), ylabel="density")
    return plot


def plot_word_rank_frequency(
    corpus_words: Sequence[str],
    model_words: Sequence[str],
    num_of_words: int = 500,
    ax=None,
):
    """Plot a log-log rank-frequency graph for the most common words."""
    corpus_word_counter = collections.Counter(corpus_words)
    num_examples = sum(corpus_word_counter.values())
    corpus_word_freqs = [
        count / num_examples
        for _, count in corpus_word_counter.most_common(num_of_words)
    ]
    corpus_data = [[i + 1, freq, "corpus"] for i, freq in enumerate(corpus_word_freqs)]

    model_word_counter = collections.Counter(model_words)
    model_word_freqs = [
        count / num_examples
        for _, count in model_word_counter.most_common(num_of_words)
    ]
    model_data = [[i + 1, freq, "model"] for i, freq in enumerate(model_word_freqs)]

    df = pd.DataFrame(
        corpus_data + model_data, columns=["word rank", "frequency", "type"]
    )

    plot = sns.lineplot(df, x="word rank", y="frequency", hue="type", ax=ax)
    plot.set(xscale="log", yscale="log")
    return plot


def plot_length_rank_frequency(
    corpus_words: Sequence[str],
    model_words: Sequence[str],
    num_of_words: int = 2_000,
    ax=None,
):
    """Plot a semi-log word length-frequency line plot for the most common words."""
    corpus_word_counter = collections.Counter(corpus_words)
    num_examples = len(corpus_words)
    corpus_data = [
        [len(word), count / num_examples, "corpus"]
        for word, count in corpus_word_counter.most_common(num_of_words)
    ]

    model_word_counter = collections.Counter(model_words)
    model_data = [
        [len(word), count / num_examples, "model"]
        for word, count in model_word_counter.most_common(num_of_words)
    ]

    df = pd.DataFrame(
        corpus_data + model_data, columns=["word length", "frequency", "type"]
    )

    plot = sns.lineplot(df, x="word length", y="frequency", hue="type")
    plot.set(yscale="log")
    return plot
