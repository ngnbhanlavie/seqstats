from src.seqstats.composition import seq_to_array, gc_content,base_composition, sliding_gc_content
import numpy as np

def test_read_fasta_returns_correct_number_of_sequence():
    result = seq_to_array("ATGC")
    assert np.array_equal(result, ['A','T','G','C'])

def test_gc_content_returns_correct_percentage_of_gc():
    result = gc_content("ATGCGC")
    assert result==66.6667

def test_base_compostition_returns_correct_number_of_bases():
    result = base_composition("ATGCTTGA")
    assert result=={'A': 2, 'C': 1, 'G': 2, 'T': 3}

def test_sliding_gc_content_returns_correct_percent():
    result=sliding_gc_content("ATGCGC",3)
    assert np.array_equal(result,[33.33, 66.67, 100., 100. ])