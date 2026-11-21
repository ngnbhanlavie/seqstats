def gc_content_loop(seq)->float:
    gc_number=0
    for c in seq:
        if c=="G" or c=="C":
            gc_number += 1
    gc_content=(gc_number/len(seq))*100
    return gc_content

def sliding_gc_content_loop(seq:str,window:int=10)->list:
    list_gc_percent=[]
    for i in range(0,len(seq)-window+1):
        sequence=seq[i:i+window]
        gc_percent=round((sequence.count("G")+sequence.count("C"))/window*100,2)
        list_gc_percent.append(gc_percent)
    return list_gc_percent

def kmer_frequency_loop(seq,k:int)->dict:
    counts={}

    for i in range(len(seq)-k+1):
        kmer=seq[i:i+k]
        counts[kmer]=counts.get(kmer,0)+1

    return counts

