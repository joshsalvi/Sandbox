__author__ = 'joshsalvi'


# Define a seqanalyze class
class seqanalyze(object):
    def __init__(self, seq):
        self.seq = seq

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


# Define a number of sequences, as many as you'd like
sequence = {}
sequence[
    0] = 'NNNGTCGCTGCTCCGGCCGCCATGGCGGCCGCGGGAATTCGATTCAAACGCAGATACACCCCTAATCTGATCTCTGCAGCCAGTTCTCCTTGGATCCAACAGAAATAGGAGCCTTTATCTTCCAGCTGCACAGGCGTGAAGTGTAGATGGTGACCGCTGTCAATGAAGACCCGAGACGTCCTATTCAGCCCCTCCATATACTGAGATAGATAAAGCGGCTTTGAGCCTTTATCCCAGGCCACTGCATACTGCGGTTTGGCACCAGGACAAATCAGGACCAGATCAGAGTCTGTGGGGTGGTTGTAGAAGTGGATGGAAACCCCTGAAGAAGCTTGATCTTCAATCTCAAGGAACTTCATTAGAGCTTGTCTCTCTGGATATACTTTAGGTTTTGGAGGACAGGTGGCATGACAGTCCCTCACCTCAAGCTCAGCTCCGTAGCTGCTGCCTGAAAGGCCAAATTGTAAAGGAACAGCTGAGGAACCGCAGGGAGCCTCTGTCTCTGAATCACTCTGATAACGTACCTGAAGGTAGATGCTTTTGACAAAACAAAGTCCTACACGGGTCTGCTCACCCTGGATGTCACAACGGTCACATTTAGACCATGACTGGTGCCGCGTGAACGCCTGAAACATCTCTGCATCCTCTGCTTGAGTTCTCCGGTTGAGGTTCCAGGGAAATAAAACGTGTCGGACCAACTGGACGTCAACATCGTAGCCGTAGAAGAATTCACCAGAGGCCGTGCCACAGATGTAGTGGCCCGAGTCGGCTTTCTGGACCCTGAAGATGAGAAGGCTAAACAAGCGAATCACTAGTGAATTCGCGGCCGCCTGCAGGTCGACCATATGGGAGAGCTCCCAACGCGTTGGATGCATAGCTTGAGTATTCTATAGTGTCACCTAAATAGCTTGCGTAATCATGGTCATAGCTGTTTCCTGTGTGAAATTGTTATCCGCTCACAATTCCACACAACATACGAGCCGGAAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGTGAGCTAACTCACATTAATTGCGTTGCG'
sequence[
    1] = 'GTCGAGTCGCTGCTCCGGCCGCCATGGCGGCCGCGGGATTCGATTCGTCCTATTCAGCCCCTCCATATACTGAGATAGATAAAGCGGCTTTGAGCCTTTATCCCAGGCCACTGCATACTGCGGTTTGGCACCAGGACAAATCAGGACCAGATCAGAGTCTGTGGGGTGGTTGTAGAAGTGGATGGAAACCCCTGAAGAAGCTTGATCTTCAATCTCAAGGAACTTCATTAGAGCTTGTCTCTCTGGATATACTTTAGGTTTTGGAGGACAGGTGGCATGACAGTCCCTCACCTCAAGCTCAGCTCCGTAGCTGCTGCCTGAAAGGCCAAATTGTAAAGGAACAGCTGAGGAACCGCAGGGAGCCTCTGTCTCTGAATCACTCTGATAACGTACCTGAAGGTAGATGCTTTTGACAAAACAAAGTCCTACACGGGTCTGCTCACCCCGGATGTCACAACGGTCACATTTAGACCATGACTGGTGCCGCGTGAACACCTGAAACATCTTTGCATCCTCTGCTTGAGTTCTCCGGTTGAGGTTCCAGGGAAATAAAACGTGTCGGACCAACTGGACGTCAACATCGTAGCCGTAGAAGAATTCACCAGAGGCCGTGCCACAGATGTAGTGGCCCGAGTCGGCTTTCTGGACCCTGAAGATGAGAAGGCTAAACAAGCGAATCACTAGTGAATTCGCGGCCGCCTGCAGGTCGACCATATGGGAGAGCTCCCAACGCGTTGGATGCATAGCTTGAGTATTCTATAGTGTCACCTAAATAGCTTGGCGTAATCATGGTCATAGCTGTTTCCTGTGTGAAATTGTTATCCGCTCACAATTCCACACAACATACGAGCCGGAAGCATAAAGTGTAAAGCCTGGGGTGCCTAATGAGTGAGCTAACTCACATTAATTGCGTTGCGCTCACTGCTCGCTTTCCAGTCGGGAAACCTGTCGTGTAGCTGCATTAATGAATCGGTAACGCGCGGGGAGAGGCGGTTGCGTATGGGCGCTCTTCGCTTCTCGCTCACTGACTCGCTGCGCTCGGTCGTC'
sequence[
    2] = 'agttgctaggcaaccacagctgcgggcgtggtctgcgcggggttgccctcctgttctggtttatcaggggatccccaaagaaagcaaggggaccaaggccgggactgctggggtgaaggtccgggaggctgagtaaggggacggaagggcacaggccatggaaaggaatgacatcatcaacttcaaggctttggagaaagagctgcaggctgcactcactgctgatgagaagtacaaacgggagaatgctgccaagttacgggcagtggaacagagggtggcttcctatgaggagttcaggggtattgtccttgcatcacatctgaagccactggagcggaaggataagatgggaggaaagagaactgtgccctggaactgtcacactattcagggaaggaccttccaggatgtggccactgaaatctccccggagaaagcccccctccagcccgagacgtctgctgacttctatcgtgattggcgacgacacttgccaagtgggccagagcgctaccaggctctactgcagcttgggggtccaaggctcggctgcctcttccagacagatgtgggatttggacttcttggggagctgctggtggcactggctgatcacgtggggccggctgaccgggcagcggtgctggggatcctatgcagcctggcgagcactgggcgcttcaccctgaacctaagcctgctgagccgggcagagagagagagctgcaagggcttgtttcagaagctgcaagccatgggcaaccccagatccgtgaaggaggggctcagctgggaggagcagggtctggaggagcagtctggtgggctccaggaggaggagaggctcctgcaggagctgctggagctgtaccaggttgactgatgcggcaagctaccctcagaggtcccagtggtcactggaggcagttttttggttgttgtcttgggggttctgcaggaccataataagaaacccacacctggttcccttctcaacttggaattttcagagcaaaaacaggaatcaagtcttccccacttctccagtccctcagtgtctcgctgttttgaactgtgtgtatccatggacagtcaagagctcaggaagttgagagcggttttgtttcccacccttagagtctgccaagcctctagcccactggccttgagagatgagtgtgtgcccaaccaaatgctggctataccagttacagcctccactcataaaagggaaaaagcaaaatctttatggtaaacaaacactgatctccacagctcttaacaagaatgtttatagccccaaaccaatgaatggacatgtaatcaacaaatgatcaaatactacatcatttgaggtgttgaattttcccctagagactcagttcttgtgcaggttgggcctgggaaagtcccaagccatcagctcaggtccagccagcctcccggatggccagatatgcaggagggt'

sequences = seqanalyze(sequence)
sequences.GCcontent()
sequences.ATcontent()
