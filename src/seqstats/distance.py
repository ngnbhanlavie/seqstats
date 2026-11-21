import numpy as np
from .composition import seq_to_array

def hamming_distance(seq1,seq2) -> int:
    if len(seq1) != len(seq2):
        raise ValueError (f"Invalid as the length of sequence 1 ({len(seq1)} is not equal to length of sequence 2({len(seq2)}))")
    if len(seq1)==0 or len(seq2)==0:
        raise ValueError("Invalid as there is empty sequence(s)")
    
    seq1=seq_to_array(seq1)
    seq2=seq_to_array(seq2)

    diff=(np.sum(seq1!=seq2))

    diff=diff.tolist()

    return diff

