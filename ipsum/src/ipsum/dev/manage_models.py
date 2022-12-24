import os.path
import sys

from ipsum.corpus import Corpus
from ipsum.model import LanguageModel
from ipsum.parse import load_parser
from ipsum.parse import Parser
from ipsum.supported_languages import SupportedLanguage


def build_models_all() -> None:
    """(Re)-Train all language models."""
    for language in SupportedLanguage:
        parser = load_parser(language)
        corpus = Corpus(f"corpora/{language.value}.zip")
        _train_and_save_model(language, parser, corpus)


def build_model(language: SupportedLanguage) -> None:
    """Train a single language model."""
    parser = load_parser(language)
    corpus = Corpus(f"corpora/{language.value}.zip")
    _train_and_save_model(language, parser, corpus)


def _train_and_save_model(
    language: SupportedLanguage, parser: Parser, corpus: Corpus
) -> None:
    print(f"Training {language.name} model...")
    try:
        model = LanguageModel.from_corpus(parser, corpus)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        models_dir_path = os.path.join(dir_path, "..", "..", "..", "trained_models")
        model_path = os.path.join(models_dir_path, f"{language.value}.zip")

        model.save_model(model_path)
    except Exception:
        print("Model training failed.", file=sys.stderr)
        raise
    else:
        print(f"Sucessfully saved {language.name} model.")
