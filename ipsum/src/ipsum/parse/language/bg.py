"""Module containing parser instance for Bulgarian language corpora."""

from ipsum.parse.parser import Parser

bg_parser = Parser(
    "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЮЯабвгдежзийклмнопрстуфхцчшщъьюя",
    internal_punctuation=[",", ":", ";", "-", "–", "—"],
    endings=["?!", "!?", ".", "!", "?", "…"],
    matched_punctuation=[("(", ")"), ('"', '"')],
    stop_words=(
        ["и", "на", "да", "се", "в", "от", "не", "с", "е", "си", "за", "по"]
        + ["кой", "къде", "какво", "защо", "как", "който", "кога", "колко"]
        + ["че", "ще", "му", "като", "го", "но", "ми", "а", "беше", "това"]
        + ["той", "ти", "аз", "до", "след", "ли", "са", "я", "тя", "бе", "ни"]
        + ["те", "така", "ме", "към", "ги", "които", "още", "няма", "него", "съм"]
    ),
    additional_substitutions=[(r"[„|“|”]", r'"')],
)