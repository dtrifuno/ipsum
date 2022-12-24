import pytest

from ipsum.parse.standardizer import Standardizer


@pytest.fixture
def standardizer() -> Standardizer:
    return Standardizer()


def test_standardizer_removes_line_breaks_and_extra_whitespace(
    standardizer: Standardizer,
) -> None:
    original_text = (
        "It was my brother, hunger\n"
        "Made us one, I know,\n"
        "And I am marching, marching\n"
        "With my own and my brother's foe.\n"
        "\n\n"
        "So I have lost my  brother,\n"
        "I wove his winding sheet. \n"
        "I know now by this victory\r\n"
        "I wrought my own \t defeat.\r\n"
    )

    expected_text = (
        "It was my brother, hunger "
        "Made us one, I know, "
        "And I am marching, marching "
        "With my own and my brother's foe. "
        "So I have lost my brother, "
        "I wove his winding sheet. "
        "I know now by this victory "
        "I wrought my own defeat. "
    )

    standardized_text = standardizer(original_text)

    assert expected_text == standardized_text


def test_standardizer_replaces_spaced_hyphens_with_mdashes(
    standardizer: Standardizer,
) -> None:
    original_text = (
        "For paradoxically it was he who wanted to give her a "
        "Japanese name and I – perhaps out of some selfish desire not to be "
        "reminded of the past - insisted on an English one."
    )

    expected_text = (
        "For paradoxically it was he who wanted to give her a "
        "Japanese name and I—perhaps out of some selfish desire not to be "
        "reminded of the past—insisted on an English one."
    )

    standardized_text = standardizer(original_text)

    assert expected_text == standardized_text


def test_standardizer_dehyphenates(standardizer: Standardizer) -> None:
    original_text = (
        "I'll make my report as if I told a story,\n"
        "for I was taught as a child on my home-\n"
        "world that Truth is a matter of the imagi–\n"
        "nation."
    )

    expected_text = (
        "I'll make my report as if I told a story, "
        "for I was taught as a child on my homeworld "
        "that Truth is a matter of the imagination."
    )

    standardized_text = standardizer(original_text)

    assert expected_text == standardized_text


def test_standardizer_replaces_series_of_periods_with_an_ellipsis(
    standardizer: Standardizer,
) -> None:
    original_text = "Money...? In a voice that rustled."
    expected_text = "Money…? In a voice that rustled."

    standardized_text = standardizer(original_text)

    assert expected_text == standardized_text


def test_standardizer_can_accept_additional_substitutions() -> None:
    custom_standardizer = Standardizer(
        additional_substitutions=[(r"\(\s+", "("), (r"\s+\)", ")")]
    )
    original_text = "(  Let others speak of her shame, I speak of my own.  )"
    expected_text = "(Let others speak of her shame, I speak of my own.)"

    standardized_text = custom_standardizer(original_text)

    assert expected_text == standardized_text
