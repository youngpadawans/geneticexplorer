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
    eighteenmer_count = {}
    exonlength = 0
    intronlength = 0
    totallength = 0
    percent_intronic = 0
    percent_exonic = 0
    ex_seq = extract_sequence_from_genome
    base_a_list = []
    base_c_list = []
    base_g_list = []
    base_t_list = []
    base_a_counter = 0
    base_c_counter = 0
    base_g_counter = 0
    base_t_counter = 0
    base_a_track = 0
    base_c_track = 0
    base_g_track = 0
    base_t_track = 0
    stndard_deviation_tracklength = 0
    exon_track = 0
    intron_track = 0
    exon_list = []
    intron_list = []
    average_exon = 0
    standard_deviation_exon = 0


    def __
    init__(self, GCpercent, LowerCasePercent, NucleotideTracklength,
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

    def get_TrackLength_average(self):
        for base in ex_seq:
            if base == 'a':
                self.base_a_counter += 1
            if base == 'A':
                self.base_a_counter += 1
            if base == 'c':
                self.base_c_counter += 1
            if base == 'C':
                self.base_c_counter += 1
            if base == 'g':
                self.base_g_counter += 1
            if base == 'G':
                self.base_g_counter += 1
            if base == 't':
                self.base_t_counter += 1
            if base == 'T':
                self.base_t_counter += 1
            self.base_a_list.append(self.base_a_counter)
            self.base_c_list.append(self.base_c_counter)
            self.base_g_list.append(self.base_g_counter)
            self.base_t_list.append(self.base_t_counter)
            total_base_list = self.base_a_list + self.base_c_list + self.base_g_list + self.base_t_list
        self.NucleotideTrackLength = sum(total_base_list) * 1.0 / len(total_base_list)
        variance_tracklength = map(lambda x: (x - self.NucleotideTrackLength) ** 2, total_base_list)
        self.standard_deviation_tracklength = math.sqrt(self.NucleotideTrackLength(variance_tracklength))
        return self.NucleotideTrackLength and self.standard_deviation_tracklength

    def get_TrackLength_exon(self):
        return self.exon_track

    def get_TrackLength_intron(self):
        return self.intron_track

    def get_TrackLength_a(self):
        for base in ex_seq:
            if base == 'a':
                self.base_a_counter += 1
            if base == 'A':
                self.base_a_counter += 1
            self.base_a_list.append(self.base_a_counter)
            self.base_a_track = sum(self.base_a_list) * 1.0 / len(self.base_a_list)
        return self.base_a_track

    def get_TrackLength_c(self):
        for base in ex_seq:
            if base == 'c':
                self.base_c_counter += 1
            if base == 'C':
                self.base_c_counter += 1
            self.base_c_list.append(self.base_c_counter)
            self.base_c_track = sum(self.base_c_list) * 1.0 / len(self.base_c_list)
        return self. base_c_track

    def get_TrackLength_g(self):
        for base in ex_seq:
            if base == 'g':
                self.base_g_counter += 1
            if base == 'G':
                self.base_g_counter += 1
            self.base_g_list.append(self.base_g_counter)
            self.base_g_track = sum(self.base_g_list) * 1.0 / len(self.base_g_list)
        return self. base_g_track

    def get_TrackLength_t(self):
        for base in ex_seq:
            if base == 't':
                self.base_t_counter += 1
            if base == 'T':
                self.base_t_counter += 1
            self.base_t_list.append(self.base_t_counter)
            self.base_t_track = sum(self.base_t_list) * 1.0 / len(self.base_t_list)
        return self. base_t_track

    def get_eighteen(self):
        k = 18
        for i in range(len(seq) - k + 1):
            EighteenMer_Count = seq[i:i + k]
            if EighteenMer_Count.haskey(EighteenMer_Count):
                EighteenMer_Count[EighteenMer_Count] += 1
            else:
                EighteenMer_Count[EighteenMer_Count] = 1
            for EighteenMer_Count, count in EighteenMer_Count.items():
                return self.eighteenmer_count

    def get_exleng(self):
        exon_count = 0
        for character in exon:
            if character:
                exon_count += 1
                self.exon_list.append(exon_count)
        self.exonlength = sum(int(exon_count) for exon_count in exon_list)
        return self.exonlength

    def get_intleng(self):
        intron_count = 0
        for character in intron:
            if character:
                intron_count += 1
                self.intron_list.append(intron_count)
        self.intronlength = sum(int(intron_count) for intron_count in intron_list)
        return self.intronlength

        return self.intronlength

    def get_totalleng(self):
        length_count = 0
        for character in ex_seq:
            if character:
                length_count += 1
        self.exonlength = sum(int(exon_count) for exon_count in exon_list)
        self.percent_exonic = ((self.exonlength) / (length_count)) * 100
        self.intronlength = sum(int(intron_count) for intron_count in intron_list)
        self.percent_intronic = ((self.intronlength) / (length_count)) * 100
        return self.length_count, self.percent_exonic, self.percent_intronic

    def standarddev_exon(self):
        self.average_exon = sum(exon_list) * 1.0 / len(exon_list)
        variance_exon = map(lambda x: (x - self.average_exon) ** 2, exon_list)
        self.standard_deviation_exon = math.sqrt(self.average_exon(variance_exon))
        return self.average_exon and self.standard_deviation_exon

    def standarddev_intron(self):
        self.average_intron = sum(intron_list) * 1.0 / len(intron_list)
        variance_intron = map(lambda x: (x - self.average_intron) ** 2, intron_list)
        self.standard_deviation_intron = math.sqrt(self.average_intron(variance_intron))
        return self.average_intron and self.standard_deviation_intron


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
