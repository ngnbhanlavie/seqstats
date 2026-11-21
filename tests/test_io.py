from src.seqstats.io import read_fasta

def test_read_fasta_returns_correct_number_of_sequence():
    result=read_fasta("data/sample.fasta")
    assert len(result)==2


