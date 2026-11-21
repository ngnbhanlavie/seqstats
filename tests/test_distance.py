from src.seqstats.distance import hamming_distance
import pytest

def test_hamming_distance_counts_one_mismatch():
    result=hamming_distance("ATGC", "ATCC")
    assert result==1

def test_hamming_distance_counts_zero_mismatch():
    result=hamming_distance("AAAA", "AAAA")
    assert result==0

def test_hamming_distance_counts_four_mismatch():
    result=hamming_distance("AAAA", "TTTT")
    assert result==4

def test_hamming_distance_raises_on_different_length():
    with pytest.raises(ValueError):
        hamming_distance("ATG", "AT")

def test_hamming_distance_raises_on_empty_sequence():
    with pytest.raises(ValueError):
        hamming_distance("", "")
