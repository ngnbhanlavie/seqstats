
import pytest

from src.seqstats.reference import (
    gc_content_loop,
    sliding_gc_content_loop,
    kmer_frequency_loop,
)


def test_gc_content_loop():
    assert gc_content_loop("ATGC") == 50.0
    assert gc_content_loop("GGCC") == 100.0
    assert gc_content_loop("AATT") == 0.0
    assert gc_content_loop("ATGCGC") == pytest.approx(66.6666667)


def test_gc_content_loop_empty_sequence():
    with pytest.raises(ZeroDivisionError):
        gc_content_loop("")


def test_sliding_gc_content_loop():
    assert sliding_gc_content_loop("ATGC", window=2) == [
        0.0, 50.0, 100.0
    ]
    assert sliding_gc_content_loop("GGCC", window=4) == [100.0]
    assert sliding_gc_content_loop("AAAA", window=2) == [
        0.0, 0.0, 0.0
    ]


def test_sliding_gc_content_loop_window_too_large():
    assert sliding_gc_content_loop("ATGC", window=5) == []


def test_kmer_frequency_loop():
    assert kmer_frequency_loop("ATATAT", k=2) == {
        "AT": 3,
        "TA": 2,
    }

    assert kmer_frequency_loop("ATGC", k=3) == {
        "ATG": 1,
        "TGC": 1,
    }


def test_kmer_frequency_loop_k_equals_sequence_length():
    assert kmer_frequency_loop("ATGC", k=4) == {
        "ATGC": 1
    }


def test_kmer_frequency_loop_k_too_large():
    assert kmer_frequency_loop("ATGC", k=5) == {}


def test_kmer_frequency_loop_empty_sequence():
    assert kmer_frequency_loop("", k=2) == {}
