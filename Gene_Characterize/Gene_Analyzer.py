__author__ = 'theep_000'

import math
import logging
import os
import tempfile
import sys

logger = logging.getLogger(__file__)

sys.path.insert(0, '/var/www/code/archer_core/app/')

import archer_core.app.bedtools as bedtools
testbed = open('testbed', 'r')


class Gene:
    """format for gene object that contains collected data
    """
    GC_percent = 0
    LowerCasePercent = 0
    NucleotideTrackLength = 0
    eighteenmer_count = 0
    exonlength = 0
    intronlength = 0
    totallength = 0
    percent_intronic = 0
    percent_exonic = 0

    def __init__(self, GCpercent, LowerCasePercent, NucleotideTracklength,
                 EighteenMer_Count, ExonLength, IntronLength, TotalLength, PercentIntronic, PercentExonic):
        self.GC_percent = GCpercent
        self.LowerCasePercent = LowerCasePercent
        self.NucleotideTrackLength = NucleotideTracklength
        self.eighteenmer_count = EighteenMer_Count
        self.exonlength = ExonLength
        self.intronlength = IntronLength
        self.totallength = TotalLength
        self.percent_intronic = PercentIntronic
        self.percent_exonic = PercentExonic

    def get_GCperc(self):
        return self.GC_percent

    def get_Lower(self):
        return self.LowerCasePercent

    def get_TrackLength(self):
        return self.NucleotideTrackLength

    def get_eighteen(self):
        return self.eighteenmer_count

    def get_exleng(self):
        return self.exonlength

    def get_intleng(self):
        return self.intronlength

    def get_totalleng(self):
        return self.totallength

    def get_intperc(self):
        return self.percent_intronic

    def get_exonperc(self):
        return self.percent_exonic


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
    result = bedtools.extract_fasta_using_bed(bed_lines, human_genome, temp_output_fasta.name)

    # Grab the resulting output file
    output_file = result['output_file']
    output_fasta = [x.strip() for x in output_file.readlines()]

    print output_fasta
    # The sequence will be the second line in the result
    return \
        "".join(output_fasta[1:]).replace("\n", "").strip()


def GC_Content_entgene(extracted_seq):
    """determines percentage of bases which are G or C in the entire gene
    """
    ex_seq = extracted_seq
    gc_counter = 0
    total_base = 0
    if '>' not in ex_seq:
        for base in ex_seq:
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
    GC_percent = float(gc_counter) / float(total_base)
    return GC_percent


def TotalLength_entgene(extracted_seq):
    """gives the amount of base pairs in the gene
    """
    ex_seq = extracted_seq
    total_count = 0
    if '>' not in ex_seq:
        for base in ex_seq:
            total_count += 1
    return total_count


def Lower_case_count_entgene(extraced_seq):
    """gives amount of base pairs which are lower case in the gene
    """
    ex_seq = extraced_seq
    lower_count = 0
    total = 0
    if '>' not in ex_seq:
        for base in ex_seq:
            total += 1
            if base.islower():
                lower_count += 1
    percent_lower = float(lower_count) / float(total)
    return percent_lower


def bed_analyzer(bed):
    """the main process of Gene_Characterize
    """
    gene_list = []
    gene_num = 0
    for line in bed:
        gene_num += 1
        gene_name = gene_num
        bed_data = line.split()
        single_gene = extract_sequence_from_genome(bed_data[0], int(bed_data[1]), int(bed_data[2]))
        single_gene_clone = single_gene
        gene_lower = Lower_case_count_entgene(single_gene)
        gene_gc = GC_Content_entgene(single_gene_clone)
        totalleng = TotalLength_entgene(single_gene)
        gene_name = Gene(gene_gc, gene_lower, 0, 0, 0, 0, totalleng, 0, 0)
        gene_list.append(gene_num)
        logger.info(gene_name.get_GCperc)
        print gene_name.get_Lower()
        print gene_name.get_totalleng()


bed_analyzer(testbed)
