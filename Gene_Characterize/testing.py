__author__ = 'theep_000'

p = open('testbed', 'r')
o = open('fastqtest', 'r')

def GC_Content_entgene(extracted_seq):
    ex_seq = extracted_seq
    gc_counter = 0
    total_base = 0
    for line in ex_seq:
        if '>' not in line:
            for base in line:
                if base != '\n':
                    total_base += 1
                if base == 'g':
                    gc_counter += 1
                if base == 'c':
                    gc_counter += 1
                if base == 'G':
                    gc_counter += 1
                if base == 'C':
                    gc_counter += 1
    GC_percent = float(gc_counter)/float(total_base)
    return GC_percent

def Lower_case_count_entgene(extraced_seq):
    ex_seq = extraced_seq
    lower_count = 0
    total = 0
    for line in ex_seq:
        for base in line:
            if base != '\n':
                total += 1
            if base.islower():
                lower_count += 1
    percent_lower = float(lower_count)/float(total)
    return percent_lower

print GC_Content_entgene(o)
o.close()
o = open('fastqtest', 'r')
print Lower_case_count_entgene(o)
o.close()

def extract_sequence_from_genome(chromosome, start, stop,
                                 human_genome = os.environ["ARCHER_GENOME"]):
    """Extracts a sequence from the human genome given a chromosom, start and stop

    :param str chromosome: Chromsome to extract from
    :param int start: Bed coordinate start of the sequence
    :parm int stop: Bed coordinate stop of the sequence
    """

    # Create a dummy bed line to use fastaFromBed of bedtools
    bed_lines = ["\t".join([chromosome, str(start), str(stop), "Name", "0", "+"])]

    temp_output_fasta = tempfile.NamedTemporaryFile()
    result = extract_fasta_using_bed(bed_lines, human_genome, temp_output_fasta.name)

    # Grab the resulting output file
    output_file = result['output_file']
    output_fasta = output_file.readlines()

    # The sequence will be the second line in the result
    return \
        "".join(output_fasta[1:]).rezzplace.strip()