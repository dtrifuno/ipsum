from ipsum.corpus import Corpus

good_texts = [
    "0a5daa25-2996-4b0d-b2d3-0e0772bf09a6",
    "6a7cf18b-b0a9-49c0-bd73-ff9c31cb5a13",
    "57352b04-7667-43f4-bb98-3508fe7d7bab",
]

bad_texts = [
    "039e1f02-ed30-4231-9972-0aa571e90ccb",
    "3c5ee1d9-426b-4b82-8dfb-a797b61ba949",
]


def test_corpus_includes_only_files_matching_regex_in_zip_archive() -> None:
    """It returns the content of all files whose names match a given regex."""
    corpus = Corpus("tests/data/test_corpus.zip", valid_filename_regex=r".*\.yes$")
    expected = set(good_texts)
    seen = set(text for text in corpus)
    assert expected == seen
