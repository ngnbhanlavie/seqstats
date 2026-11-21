def read_fasta(filepath: str) ->dict:
    sequences = {}
    current_header = None
    current_seq = []

    with open(filepath,"r") as f:
        for line in f:
            line=line.strip()

            if line=="":
                continue

            if line[0]==">":
                if current_header is not None:
                    sequences[current_header]="".join(current_seq)
                current_header = line [1:]
                current_seq=[]
            else:
                current_seq.append(line)
        if current_header is not None:
           sequences[current_header]="".join(current_seq) 
    return sequences
