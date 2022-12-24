from typing import Sequence, TypeVar

import pytest

from ipsum.utils import (
    capitalize_sentence,
    compute_length_weights,
    is_capitalized,
    is_lower,
    is_word,
    iterate_over_chunks,
    LastChunkMethods,
    reweight_by_length,
)


@pytest.mark.parametrize(
    "s,expected",
    [("mcManus", False), ("'рбет", True), ("banana", True), ("Vince", False)],
)
def test_is_lower(s: str, expected: bool) -> None:
    assert is_lower(s) == expected


@pytest.mark.parametrize(
    "s,expected",
    [
        ("mcManus", False),
        ("'Рбет", True),
        ("Banana", True),
        ("-+!", False),
        ("", False),
    ],
)
def test_is_capitalized(s: str, expected: bool) -> None:
    assert is_capitalized(s) == expected


@pytest.mark.parametrize(
    "candidate,expected",
    [
        ("mcManus", True),
        ("'Рбет", True),
        ("Banana", True),
        ("-+!", False),
        ("", False),
    ],
)
def test_is_word(candidate: str, expected: bool) -> None:
    assert is_word(candidate) == expected


@pytest.mark.parametrize(
    "sentence,expected",
    [
        ("the chair no guest has sat on.", "The chair no guest has sat on."),
        (
            "Don’t worry about watering the flowers.",
            "Don’t worry about watering the flowers.",
        ),
        ("— in fact, don’t plant them.", "— In fact, don’t plant them."),
        ("- + !", "- + !"),
    ],
)
def test_capitalize_sentence(sentence: str, expected: str) -> None:
    assert capitalize_sentence(sentence) == expected


T = TypeVar("T")


@pytest.mark.parametrize(
    "sequence,chunk_size,last_chunk_method,expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, "drop", [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        ((1, 2, 3, 4, 5), 2, "drop", [(1, 2), (3, 4)]),
        ("apple", 2, "incomplete", ["ap", "pl", "e"]),
    ],
)
def test_iterate_over_chunks(
    sequence: Sequence[T],
    chunk_size: int,
    last_chunk_method: LastChunkMethods,
    expected: Sequence[T],
) -> None:
    assert list(iterate_over_chunks(sequence, chunk_size, last_chunk_method)) == list(
        expected
    )


def test_compute_length_weights() -> None:
    population = ["", "", "--", "----", "--"]
    weights = [1, 1, 2, 6, 2]

    computed_weights = compute_length_weights(population, weights)

    expected_weights = [2, 0, 4, 0, 6]
    assert computed_weights == expected_weights


def test_reweight_by_length_weights() -> None:
    population = ["", "-", "a", "--"]
    population_weights = [1, 1, 1, 1]
    length_weights = [4, 4, 4]

    new_weights = reweight_by_length(population, population_weights, length_weights)

    assert pytest.approx(new_weights) == [4, 2, 2, 4]
