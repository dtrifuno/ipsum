from ipsum.parse.sentencizer import Sentencizer


def test_sentencizer_can_split_text_into_sentences() -> None:
    sentencizer = Sentencizer("", [], endings=[".", "?"])

    original_text = (
        "Every page a victory.\n"
        "Who cooked the feast for the victors?\n"
        "Every ten years a great man?\n"
        "Who paid the bill?\n"
        "\n"
        "So many reports.\n"
        "So many questions.\n"
    )
    extracted_sentences = sentencizer(original_text)

    expected_sentences = [
        "Every page a victory.",
        "Who cooked the feast for the victors?",
        "Every ten years a great man?",
        "Who paid the bill?",
        "So many reports.",
        "So many questions.",
    ]

    assert extracted_sentences == expected_sentences
