from ipsum.parse.worderizer import Worderizer


def test_can_extract_words() -> None:
    """It returns all words contained in the text."""
    worderizer = Worderizer("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-")
    text = (
        "I now understand the need for faith—pure, blind, "
        "fly-in-the-face-of-reason faith—as a small life preserver in the wild "
        "and endless sea of a universe ruled by unfeeling laws and totally "
        "indifferent to the small, reasoning beings that inhabit it."
    )

    extracted_words = worderizer(text)

    expected_words = (
        ["I", "now", "understand", "the", "need", "for", "faith", "pure", "blind"]
        + ["fly-in-the-face-of-reason", "faith", "as", "a", "small", "life"]
        + ["preserver", "in", "the", "wild", "and", "endless", "sea", "of", "a"]
        + ["universe", "ruled", "by", "unfeeling", "laws", "and", "totally"]
        + ["indifferent", "to", "the", "small", "reasoning", "beings", "that"]
        + ["inhabit", "it"]
    )
    assert expected_words == extracted_words
