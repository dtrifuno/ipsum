from ipsum.parse.parser import Parser

sr_parser = Parser(
    "АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШабвгдђежзијклљмнњопрстћуфхцчџш",
    internal_punctuation=[",", ":", ";", "-", "–", "—"],
    endings=["?!", "!?", ".", "!", "?", "…"],
    matched_punctuation=[("(", ")"), ("„", "“")],
    stop_words=(
        ["и", "је", "у", "да", "се", "на", "за", "су", "од", "са", "а"]
        + ["како", "где", "шта", "ко", "зашто", "који", "га", "ће"]
        + ["не", "из", "о", "то", "као", "ће", "што", "није", "до", "би", "по"]
        + ["али", "које", "све", "или", "која", "само", "сам", "бити"]
        + ["био", "јер", "он", "када", "тако", "смо", "било", "с", "још", "ми"]
        + ["може", "већ", "ни", "има", "па", "кога", "колико", "чији", "ли"]
    ),
    additional_substitutions=[(r"„\s+", r"„"), (r"\s+“", r"“")],
)