from benchmarks.run_benchmark import make_seq, bench
from src.seqstats.composition import seq_to_array, gc_content
import numpy as np

seq=make_seq(1000000)
arr=seq_to_array(seq)

def gc_content_compute_only(arr) -> float:
    gc_content=0
    total_nu=len(arr)

    for base in ["G","C"]:
        bool=arr==base
        gc_content += np.sum(bool)

    gc_percent=round(gc_content/total_nu*100,4)
    return gc_percent

t_total= bench(gc_content,seq)

t_convert_to_array=bench(seq_to_array,seq)

t_compute=bench(gc_content_compute_only,arr)

print(f"time for running total gc_content: {t_total}")
print(f"time for converting sequence to array: {t_convert_to_array}")
print(f"time for coputing the content: {t_compute}")