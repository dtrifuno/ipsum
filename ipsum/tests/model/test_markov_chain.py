import pytest

from ipsum.exceptions import ModelAlreadyFinalizedError
from ipsum.exceptions import ModelNotFinalizedError
from ipsum.model.markov_chain import MarkovChain
from ipsum.model.markov_chain import MarkovChainWithMemory


def test_chain_trained_on_nothing_will_produce_nothing() -> None:
    chain: MarkovChain[list] = MarkovChain()
    chain.train([[]])
    chain.finalize()

    generated_seq = chain.generate_sequence()

    assert generated_seq == []


def test_chain_trained_on_a_heterogram_will_always_reproduce_it() -> None:
    examples = ["subdermatoglyphic"]
    chain: MarkovChain[str] = MarkovChain()
    chain.train(examples)
    chain.finalize()

    generated_seqs = ["".join(chain.generate_sequence()) for _ in range(10)]

    seq = examples[0]
    assert all(seq == generated_seq for generated_seq in generated_seqs)


def test_chain_learns_from_all_examples() -> None:
    examples = ["a", "b", "d"]
    chain: MarkovChain[str] = MarkovChain()
    chain.train(examples)
    chain.finalize()

    generated_seqs = ["".join(chain.generate_sequence()) for _ in range(100)]
    assert set(examples) == set(generated_seqs)


def test_chain_can_produce_novel_examples() -> None:
    examples = ["abacadbcdbda"]
    chain: MarkovChain[str] = MarkovChain()
    chain.train(examples)
    chain.finalize()

    generated_seqs = ["".join(chain.generate_sequence()) for _ in range(10)]
    seq = examples[0]
    assert any(seq != generated_seq for generated_seq in generated_seqs)


def test_generating_from_unfinalized_chain_will_fail() -> None:
    chain: MarkovChain = MarkovChain()
    with pytest.raises(ModelNotFinalizedError):
        chain.generate_sequence()


def test_training_a_finalized_chain_will_fail() -> None:
    chain: MarkovChain[list] = MarkovChain()
    chain.train([[]])
    chain.finalize()
    with pytest.raises(ModelAlreadyFinalizedError):
        chain.train([[]])

    chain_with_memory: MarkovChainWithMemory[list] = MarkovChainWithMemory(2)
    chain_with_memory.train([[]])
    chain_with_memory.finalize()
    with pytest.raises(ModelAlreadyFinalizedError):
        chain_with_memory.train([[]])


def test_markov_chains_can_be_of_higher_order() -> None:
    chain: MarkovChainWithMemory[str] = MarkovChainWithMemory(2)
    chain.train(["aabacb"])
    chain.finalize()

    assert "".join(chain.generate_sequence()) == "aabacb"
