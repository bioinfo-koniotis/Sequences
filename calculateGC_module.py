# Calculate GC (and optionally AT content from a DNA sequence to predict if a sequence originates from Plasmodium.

def calculateGC(seq):
    """
    Calculate GC content
    :param seq: String containing DNA sequence
    :return: Float GC content expressed as a percentage
    """
    # get the sequence length
    seqLength = len(seq)
    # count Gs and Cs
    c_count = seq.upper().count('C')
    g_count = seq.upper().count('G')
    # calculate GC content as a percentage ((c+g)/len*100)
    gcContent = ((c_count + g_count) / seqLength) * 100
    return gcContent

# these lines of code are included to show what the __name__ variable contains
# if you RUN this script, __name__ == '__main__'
# if you IMPORT this script, the name will be 'calculateGC_module'
print('My name is:')
print(__name__)

# do not run if this module is imported
# use the name variable above to prevent the code below from being run if the module is imported
if __name__ == '__main__':
    seqFile = 'BCPy/mySequences.txt'
    showAT = False
    cutoff = 30

    count = 0
    # for each line in the file
    with open(seqFile) as sequences:
        for seq in sequences:
            count += 1
            # calculate GC content and create output string
            gcContent = calculateGC(seq)
            output = 'Sequence {}: GC content {}%\n'.format(count, round(gcContent, 2))
            # if requested, calculate AT content and add to output string
            if showAT:
                atContent = 100 - gcContent
                output = output + 'Sequence {}: AT content {}%\n'.format(count, round(atContent, 2))
            # if gcContent is less than the cutoff, report that this is likely Plasmodium
            if gcContent < cutoff:
                output = output + 'Sequence {} is likely Plasmodium\n'.format(count)
            print(output)

    # print the docstring for the function
    # print(calculateGC.__doc__)
