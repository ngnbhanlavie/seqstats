import numpy as np

def seq_to_array(seq: str) ->np.ndarray:
    array_seq=np.array(list(seq))
    return array_seq

def gc_content(seq: str) -> float:
    gc_content=0
    array_seq=seq_to_array(seq)
    total_nu=len(array_seq)

    for base in ["G","C"]:
        bool=array_seq==base
        gc_content += np.sum(bool)

    gc_percent=round(gc_content/total_nu*100,4)
    return gc_percent

def base_composition(seq: str) ->dict:
    array_seq=seq_to_array(seq)
    bases,counts=np.unique(array_seq,return_counts=True)
    base_counts=dict(zip(bases.tolist(),counts.tolist()))
    return base_counts

def sliding_gc_content(seq:str,window:int=10)->np.ndarray:
    if window>len(seq) or window<=0:
        raise ValueError(f"{window} is not within the length of sequence - {len(seq)}")
    
    array_seq=seq_to_array(seq)
    array_seq=np.lib.stride_tricks.sliding_window_view(array_seq,window)
    mask_array=(array_seq=="G")|(array_seq=="C")
    number_of_GC_per_window=mask_array.sum(axis=1)
    percent_of_CG_per_window=np.round((number_of_GC_per_window/window)*100,decimals=2)
    return percent_of_CG_per_window

def kmer_frequency(seq:str,k:int=2) -> dict:
    if k>len(seq) or k<=0:
        raise ValueError (f"{k} is not within the length of sequence - {len(seq)}")

    array_seq=seq_to_array(seq)
    kmer=np.lib.stride_tricks.sliding_window_view(array_seq,k)
    kmer_seq=["".join(row) for row in kmer]
    kmers,counts=np.unique(kmer_seq,return_counts=True)
    kmer_counts=dict(zip(kmers.tolist(),counts.tolist()))
    return kmer_counts


        



