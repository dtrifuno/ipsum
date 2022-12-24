import itertools

from ipsum.model.choices import ChoicesModel


def test_model_can_generate_choices() -> None:
    model = ChoicesModel([("a", 1), ("b", 1), ("c", 1)])
    choices = model.generate_choices(100)

    assert len(choices) == 100
    for symbol in ("a", "b", "c"):
        assert any(choice == symbol for choice in choices)


def test_identical_models_are_equal() -> None:
    model_a = ChoicesModel([("a", 3), ("b", 2), ("c", 5)])
    model_b = ChoicesModel([("c", 5), ("a", 3), ("b", 2)])
    assert model_a == model_b


def test_different_models_are_not_equal() -> None:
    distinct_models = [
        ChoicesModel([("a", 3), ("b", 2), ("c", 5)]),
        ChoicesModel([("a", 5), ("b", 2), ("c", 5)]),
        ChoicesModel([("d", 3), ("e", 2), ("f", 5)]),
        ChoicesModel([("w", 7)]),
        None,
    ]

    for model_a, model_b in itertools.combinations(distinct_models, 2):
        assert model_a != model_b


def test_can_save_model_to_and_recover_from_json() -> None:
    model = ChoicesModel([("a", 3), ("b", 2), ("c", 5)])
    model_json = model.to_json()
    recovered_model: ChoicesModel[str] = ChoicesModel.from_json(model_json)
    assert model == recovered_model
