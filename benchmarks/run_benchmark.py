import random
import timeit
import numpy as np
from src.seqstats.composition import gc_content,sliding_gc_content,kmer_frequency
from src.seqstats.reference import gc_content_loop,sliding_gc_content_loop,kmer_frequency_loop
from benchmarks.experiment_b import gc_content_fast

def main():
    sizes=[1000, 10000, 100000, 1000000]
    func=[
        {"name":"calculate the content of GC","numpy":gc_content, "loop":gc_content_loop,"extra":()},
        {"name":"calculate the sliding GC content","numpy":sliding_gc_content, "loop":sliding_gc_content_loop,"extra":(3,)},
        {"name":"calculat the frequency of kmer","numpy":kmer_frequency, "loop": kmer_frequency_loop,"extra":(3,)},
    ]
    for m in func: 
        print(f"Name of function:{m["name"]}")
        for n in sizes:
            seq=make_seq(n,0)
            a = m["numpy"](seq, *m["extra"])
            b = m["loop"](seq, *m["extra"])
            same={
                "GC":np.isclose,
                "sliding gc":np.allclose,
                "kmer": lambda a,b: a==b
                }
            if m["name"]=="calculate the content of GC":
                assert same["GC"](a,b)
            elif m["name"]=="calculate the sliding GC content":
                assert same["sliding gc"](a,b)
            else:
                assert same["kmer"](a,b)
            loop_func=m["loop"]
            numpy_func=m["numpy"]
            t_numpy=bench(numpy_func,seq,*m["extra"])
            t_loop=bench(loop_func,seq,*m["extra"])
            print(n)
            print(f"time of loop: {t_loop*1000:.2f}")
            print(f"time of Numpy:{t_numpy*1000:.2f}")
            print(f"time_loop/time_numpy:{t_loop/t_numpy}")
    return None


def make_seq(n,seed=0):
    random.seed(seed)
    seq="".join(random.choices("ATGC",k=n))
    return seq

def bench(func,*arg,repeat=5,number=1):
    t=timeit.repeat(
        lambda: func(*arg),
        repeat=repeat,
        number=number
    )
    t=min(t)/number
    return t

if __name__=="__main__":
    main()