__author__ = 'joshsalvi'


# Define a seqanalyze class
class seqanalyze(object):
    def __init__(self, seq):
        self.seq = seq
        for ind in range(0, len(self.seq)):
            self.seq[ind] = self.seq[ind].upper()

    def GCcontent(self):
        from numpy import zeros
        self.GCcont = zeros(len(self.seq))
        for ind in range(0, len(self.seq)):
            self.GCcont[ind] = len(
                [x for x in self.seq[ind].upper() if x == 'G' or x == 'C'])  # Where the magic happens
            self.GCcont[ind] = float(self.GCcont[ind]) / float(len(self.seq[ind]))
            print 'Sequence %d has a GC content of %f' % (ind + 1, self.GCcont[ind])  # Print the result
        return self.GCcont

    def ATcontent(self):
        from numpy import zeros
        self.ATcont = zeros(len(self.seq))
        for ind in range(0, len(self.seq)):
            self.ATcont[ind] = len(
                [x for x in self.seq[ind].upper() if x == 'A' or x == 'T'])  # Where the magic happens
            self.ATcont[ind] = float(self.ATcont[ind]) / float(len(self.seq[ind]))
            print 'Sequence %d has an AT content of %f' % (ind + 1, self.ATcont[ind])  # Print the result
        return self.ATcont

    def findcomplement(self):
        from string import maketrans
        self.complement = {}
        for ind in range(0, len(self.seq)):
            basecomplement = maketrans('ATGC', 'TACG')
            self.complement[ind] = self.seq[ind].translate(basecomplement)[::-1]
        return self.complement

    def transcribe(self):
        from string import maketrans
        self.RNA = {}
        for ind in range(0, len(self.seq)):
            basecomplement = maketrans('ATGC', 'TACG')
            self.RNA[ind] = self.seq[ind].translate(basecomplement)[::-1]
            self.RNA[ind] = self.RNA[ind].replace('T', 'U')
        return self.complement

    def translate(self):
        codontable = {
            'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
            'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
            'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
            'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
            'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
            'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
            'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
            'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
            'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
            'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
            'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
            'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
            'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
        }
        self.protein = {}
        for ind in range(0, len(self.seq)):
            start = self.seq[ind].find('ATG')
            seqstart = self.seq[ind][int(start):]
            stop = seqstart.find('TAA')
            cds = str(seqstart[:int(stop) + 3])
            self.protein[ind] = ''
            for n in range(0, len(cds), 3):
                if cds[n:n + 3] in codontable:
                    self.protein[ind] += codontable[cds[n:n + 3]]
        return self.protein



# Define a number of sequences, as many as you'd like
sequence = {}
sequence[
    0] = 'ATGGCGCTCCGATGCGCCATGGCGGCCGCGGGAATTCGATAGTCAAACGCAGATACACCCCTCTGGGATCGGTTCAGCCGGTTCTCGCC' \
         'TTGGATCCAACAGAAATAGGAGCCTTTATCTTCCAGCTGCACAGGCGTGAAGTGTAGATGGTGACCGCTGTCAATGAAGACCCGAGACG' \
         'TCCTATTCAGCCCCTCCATATACTGAGATAGATAAAGCGGCTTTGAGCCTTTATCCCAGGCCACTGCATACTGCGGTTTGGCACCAGGA' \
         'CAAATCAGGACCAGATCAGAGTCTGTGGGGTGGTTGTAGAAGTGGATGGAAAACCCCTGAAGAAGCTTGATCTTCAATCTCAAGGACTT' \
         'CATTAGAGCTTGTCTCTCTGGATATACTTTAGGTTTTGGAGGACAGGTGGCATGACAGTCCCTCACCTCAAGCTCAGCTCCGTAGCTGC' \
         'TGCCTGAAAGGCCAAATTGTAAAGGAACAGCTGAGGAACCGCAGGGAGCCTCTGTCTCTGAATCACTCTGATAACGTACCTGAAGGTAG' \
         'ATGCTTTTGACAAAACAAAGTCCTACACGGGTCTGCTCACCCTGGATGTCACAACGGTCACATTTAGACCATGACTGGTGCCGCGTGAA' \
         'CGCCTGAAACATCTCTGCATCCTCTGCTTGAGTTCTCCGGTTGAGGTTCCAGGGAAATAAAACGTGTCGGACCAACTGGACGTCAACAT' \
         'CGTAGCCGTAGAAGAATTCACCAGAGGCCGTGCCACAGATGTAGTGGCCCGAGTCGGCTTTCTGGACCCTGAAGATGAGAAGGCTAAAC' \
         'AAGCGAATCACTAGTGAATTCGCGGCCGCCTGCAGGTCGACCATATGGGAGAGCTCCCAACGCGTTGGATGCATAGCTTGAGTATTCTA' \
         'TAGTGTCACCTAAATAGCTTGCGTAATCATGGTCATAGCTGTTTCCTGTGTGAAATTGTTATCCGCTCACAATTCCACACAACATACGA' \
         'GCCGGAAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGTGAGCTAACTCACATTAATTGCGTTGCCCGTAA'
sequence[
    1] = 'GTCGAGTCGCTGCTCCGGCCCGCCATGGGGCCGCGGGATTCGATTCGTCCTATTCAGCCCCTCCATATACTGAGATAGAAGCGCCGGCT' \
         'TTGAGCCTTTATCCCAGGCCACATGTGCATACTGCGGTTTGGCACCAGGACAAATCAGGACCAGATCAGAGTCTGTGGGGTTGTAGAAG' \
         'TGGATGGAAACCCCTGAAGAAGCTTGATCTTCAATCTCAAGGAACTTCATTAGAGCTTGTCTCTCTGGATATACTTTAGGTTTTGGAGG' \
         'ACAGGTGGCATGACAGTCCCTCACCTCAAGCTCAGCTCCGTAGCTGCTGCCTGAAAGGCCAAATTGTAAAGGAACAGCTGAGGAACCGC' \
         'AGGGAGCCTCTGTCTCTGAATCACTCTGATAACGTACCTGAAGGTAGATGCTTTTGACAAAACAAAGTCCTACACGGGTCTGCTCACCC' \
         'CGGATGTCACAACGGTCACATTTAGACCATGACTGGTGCCGCGTGAACACCTGAAACATCTTTGCATCCTCTGCTTGAGTTCTCCGGTT' \
         'GAGGTTCCAGGGAAATAAAACGTGTCGGACCAACTGGAGTCAACATCGTAGCCGTAGAAGAATTCACCAGAGGCCGTGCCACAGATGTC' \
         'AGTGGCCCGAGTCGGCTTTCTGGACCCTGAAGATGAGAAGGCTAAACAAGCGATAAATCACTAGTGAATTCGCCGCCTGCAGGTCGACC' \
         'ATATGGGAGAGCTCCCAACGCGTTGGATGCATAGCTTGAGTATTCTATAGTGTCACCTAAATAGCTTGGCGTAATCATGGTCATAGCTG' \
         'TTTCCTGTGTGAAATTGTTATCCGCTCACAATTCCACACAACATACGAGCCGGAAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGT' \
         'GAGCTAACTCACATTAATTGCGTTGCGCTCACTGCTCGCTTTCCAGTCGGGAAACCTGTCGTGTAGCTGCATTAATGAATCGGTAACGC' \
         'GCGGGGAGAGGCGGTTGCGTATGGGCGCTCTTCGCTTCTCGCTCACTGACTCGCTGCGCTCGGTCGTC'
sequence[
    2] = 'agttgctaggcaaccacagctgcgggcgtggtctgcgcggggttgccctcctgttctggtttatcaggggatccccaaagaaagcaagg' \
         'ggaccaaggccgggactgctggggtgaaggtccgggaggctgagtaaggggacggaacgggggcacaggccatggaggaatgacatcatc' \
         'aacttcaaggctttggagaaagagctgcaggctgcactcactgctgatgagaagtacaaacgggagaatgctgccaagttacgggcagt' \
         'ggaacagagggtggcttcctatgaggagttcaggggtattgtccttgcatcacatctgaagccactggagcggaaggataagatgggag' \
         'gaaagagaactgtgccctggaatgactgtcacactattcagggaaggaccttccaggatgccactgaaatctccccggagaaagccccc' \
         'ctccagcccgagacgtctgctgacttctatcgtgattggcgacgacacttgccaagtgggccagagcgctaccaggctctactgcagct' \
         'tgggggtccaaggctcggctgcctcttccagacagatgtgggatttggacttcttggggagctgctggtggcactggctgatcacgtgg' \
         'ggccggctgaccgggcagcggtgctggggatcctatgcagcctggcgagcactgggcgcttcaccctgaacctaagcctgctgagccgg' \
         'gcagagagagagagctgcaagggcttgtttcagaagctgcaagccatgggcaaccccagatccgtgaaggaggggctcagctgggagga' \
         'gcagggtctggaggagcagtctggtgggctccaggaggaggagaggctcctgcaggagctgctggagctgtaccaggttgactgatgcg' \
         'gcaagctaccctcagaggtcccagtggtcactggaggcagttttttggttgttgtcttgggggttctgcaggaccataataagaaaccc' \
         'acacctggttcccttctcaacttggaattttcagagcaaaaacaggaatcaagtcttccccacttctccagtccctcagtgtctcgctg' \
         'ttttgaactgtgtgtatccatggacagtcaagagctcaggaagttgagagcggttttgtttcccacccttagagtctgccaagcctcta' \
         'gcccactggccttgagagatgagtgtgtgcccaaccaaatgctggctataccagttacagcctccactcataaaagggaaaaagcaaaa' \
         'tctttatggtaaacaaacactgatctccacagctcttaacaagaatgtttatagccccaaaccaatgaatggacatgtaatcaacaaat' \
         'gatcaaatactacatcatttgaggtgttgaattttcccctagagactcagttcttgtgcaggttgggcctgggaaagtcccaagccatc' \
         'agctcaggtccagccagcctcccggatggccagatattaagcaggagggt'

# Define a sequences object of class seqanalyze
sequences = seqanalyze(sequence)

# Calculate GC content, AT content, and find the complement
sequences.GCcontent()
sequences.ATcontent()
sequences.findcomplement()
sequences.transcribe()
sequences.translate()


# Print a sequence and its complement
from textwrap import fill

indcheck = 1

print "\n---------SEQUENCE---------"
print fill(sequences.seq[indcheck], 100) + "\n--------------------------"
print "\n--------COMPLEMENT--------"
print fill(sequences.complement[indcheck], 100) + "\n--------------------------"
print "\n-----------RNA------------"
print fill(sequences.RNA[indcheck], 100) + "\n--------------------------"
print "\n---------PROTEIN----------"
print fill(sequences.protein[indcheck], 25) + "\n--------------------------"
