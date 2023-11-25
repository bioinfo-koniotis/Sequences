
# create the class
class Sequence:

    # constructor
    def __init__(self, id, seq):
        self._id = id
        self._seq = seq.upper()

    # getter and setter for id
    @property
    def id(self):
        return self._id 
    
    # the setter is here as an example
    """
    @id.setter
    def id(self, id):
        self._id = id
    """

    # getter and setter for seq
    @property
    def seq(self):
        return self._seq
    
    # the setter is here as an example
    """
    @seq.setter
    def seq(self, seq):
        self._seq = seq.upper()
    """

    # gc content method
    def calc_gc_content(self, dp=2):
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)


# make two instances of this class
seq1 = Sequence('geneA', 'ATGCATG')
seq2 = Sequence('geneB', 'ATTTTAGCGAAA')

# get the gc content for each seq instance
print(f'The GC content for {seq1.id} is {seq1.calc_gc_content()}')
print(f'The GC content for {seq2.id} is {seq2.calc_gc_content(3)}')