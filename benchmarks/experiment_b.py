from benchmarks.run_benchmark import make_seq, bench
from src.seqstats.composition import seq_to_array, gc_content
import numpy as np

seq=make_seq(1000000)

arr=np.frombuffer(seq.encode(),dtype=np.uint8)

def gc_content_fast(seq):
    gc_content=0
    array_seq=np.frombuffer(seq.encode(),dtype=np.uint8)
    total_nu=len(array_seq)

    gc_content += np.sum((array_seq==ord("G"))|(array_seq==ord("C")))

    gc_percent=round(gc_content/total_nu*100,4)
    return gc_percent

def gc_content_compute_only(arr) -> float:
    gc_content=0
    total_nu=len(arr)

    for base in ["G","C"]:
        bool=arr==ord(base)
        gc_content += np.sum(bool)

    gc_percent=round(gc_content/total_nu*100,4)
    return gc_percent

t_total= bench(gc_content_fast,seq)

t_convert_to_array=bench(lambda seq:np.frombuffer(seq.encode(),dtype=np.uint8),seq)

t_compute=bench(gc_content_compute_only,arr)

print(f"time for running total gc_content: {t_total}")
print(f"time for converting sequence to array: {t_convert_to_array}")
print(f"time for coputing the content: {t_compute}")