with open('seqs.rtf') as f:
    seqs = []
    keys = []
    counter = 1
    for l in f:
        if counter % 2 > 0:
            m = l.strip().split('\n')
            m = m[0].replace(':', '')
            keys.append(m)
        elif counter % 2 == 0:
            m = l.strip().split('\n')
            m = m[0]
            seqs.append(m)
        counter += 1
    print [keys, seqs]
