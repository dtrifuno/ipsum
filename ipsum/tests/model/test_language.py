import pytest

from ipsum.exceptions import ModelNotFinalizedError
from ipsum.model import LanguageModel
from ipsum.model import load_model
from ipsum.utils import is_word


@pytest.fixture
def trained_model() -> LanguageModel:
    model = load_model("en")
    return model


def test_can_generate_words(trained_model: LanguageModel) -> None:
    words = trained_model.generate_words(50)
    assert all(is_word(word) for word in words)
    assert len(words) == 50


def test_can_generate_sentences(trained_model: LanguageModel) -> None:
    sentences = trained_model.generate_sentences(10)
    assert all(len(sentence) > 1 for sentence in sentences)
    assert len(sentences) == 10


def test_can_generate_paragraphs(trained_model: LanguageModel) -> None:
    paragraphs = trained_model.generate_paragraphs(5)
    assert all(len(paragraph) > 1 for paragraph in paragraphs)
    assert len(paragraphs) == 5


def test_cannot_generate_from_an_untrained_model() -> None:
    model = LanguageModel()

    with pytest.raises(ModelNotFinalizedError):
        model.generate_words(5)

    with pytest.raises(ModelNotFinalizedError):
        model.generate_sentences(5)

    with pytest.raises(ModelNotFinalizedError):
        model.generate_paragraphs(5)
