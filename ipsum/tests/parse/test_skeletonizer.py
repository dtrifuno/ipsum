from typing import Callable, List

import pytest

from ipsum.parse.skeletonizer import CAPITALIZED_WORD
from ipsum.parse.skeletonizer import LOWERCASE_WORD
from ipsum.parse.skeletonizer import Skeletonizer


@pytest.fixture
def german_skeletonizer() -> Callable[[str], List[str]]:
    lowercase_words = set(
        [
            "braucht",
            "drum",
            "geschlossen",
            "helfen",
            "kommt",
            "können",
            "nicht",
            "seinem",
            "weil",
            "wie",
            "wir",
            "wird",
        ]
    )
    stop_words = set(
        [
            "auch",
            "aus",
            "das",
            "der",
            "die",
            "ein",
            "er",
            "est",
            "ist",
            "mit",
            "so",
            "und",
        ]
    )
    capitalized_words = set(
        [
            "Chausseestraße",
            "Davies",
            "Hr",
            "Ihnen",
            "Kind",
            "Klammer",
            "Kleider",
            "Mensch",
            "Schuh",
            "Vater",
            "Wales",
        ]
    )

    skeletonizer = Skeletonizer(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÜÖẞabcdefghijklmnopqrstuvwxyzäüöß",
        [",", "-"],
        [".", "?", "!"],
        matched_punctuation=[("(", ")")],
    )

    return lambda sentence: skeletonizer(
        sentence, lowercase_words, capitalized_words, stop_words
    )


def test_can_skeletonize_a_conforming_sentence(
    german_skeletonizer: Callable[[str], List[str]]
) -> None:
    sentence = (
        "Und weil der Mensch ein Mensch ist, drum braucht er auch Kleider und Schuh!"
    )

    skeleton = german_skeletonizer(sentence)

    expected_skeleton = (
        ["Und", " ", LOWERCASE_WORD, " ", "der", " ", CAPITALIZED_WORD, " "]
        + ["ein", " ", CAPITALIZED_WORD, " ", "ist", ",", " "]
        + [LOWERCASE_WORD, " ", LOWERCASE_WORD, " ", "er", " ", "auch", " "]
        + [CAPITALIZED_WORD, " ", "und", " ", CAPITALIZED_WORD, "!"]
    )
    assert skeleton == expected_skeleton


@pytest.mark.parametrize(
    "bad_sentence",
    [
        ("Es ist der Vater mit seinem Kind",),
        ("Hr. Davies kommt aus Wales.",),
        ("-Ist das so?",),
        ("Die Klammer ( wird nicht geschlossen.",),
        ("Chausseestraße 125, wie können wir Ihnen helfen?",),
    ],
)
def test_raises_an_error_for_invalid_sentence(
    german_skeletonizer: Callable[[str], List[str]], bad_sentence: str
) -> None:
    with pytest.raises(Exception):
        german_skeletonizer(bad_sentence)
