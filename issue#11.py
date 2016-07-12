import math
#length of exons
exon_list = []
def exon_len():
    exon_count=0
    for exon in exon_list:
        for character in exon:
            if character:
                exon_count+=1
            exon_list.append(exon_count)

#average total exon length
def exon_length():
    total_exon= sum (int(exon_count) for exon_count in exon_list)
    return total_exon

#length of introns
intron_list = []
def intron_len():
    intron_count=0
    for intron in intron_list:
        for character in intron:
            if character:
                intron_count+=1
            intron_list.append(intron_count)

# total intron length
def intron_length():
    total_intron= sum (int(intron_count) for intron_count in intron_list)
    return total_intron

#total length, percent exonic, and percent intronic
def percents():
    length_count=0
    for character in genome:
        if character:
            length_count+=1
    total_exon= sum (int(exon_count) for exon_count in exon_list)
    percent_exonic1= (total_exon)/(length_count)
    percent_exonic =(percent_exonic1)*100
    total_intron= sum (int(intron_count) for intron_count in intron_list)
    percent_intronic1= (total_intron)/(length_count)
    percent_intronic =(percent_intronic1)*100
    return length_count, percent_exonic, percent_intronic

# average exon length
def average_exon(exon_list):
    return sum(exon_list) * 1.0 / len(exon_list)
avg_exon = average_exon(exon_list)
#standard devation for exon length
def standard_deviation_exon():
    variance_exon = map(lambda x: (x - avg_exon)**2, exon_list)
    standard_deviation_exon = math.sqrt(average_exon(variance_exon))
    return standard_deviation_exon

#average intron length
def average_intron(intron_list):
    return sum(intron_list) * 1.0 / len(intron_list)
avg_intron = average_intron(intron_list)
#standard devation for intron length
def standard_deviation_intron():
    variance_intron = map(lambda x: (x - avg_intron)**2, intron_list)
    standard_deviation_intron = math.sqrt(average_intron(variance_intron))
    return standard_deviation_intron