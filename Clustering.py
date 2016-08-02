__author__ = 'theep_000'

from Gene_Analyzer import Gene
try:
    import numpy
except ImportError:
    print "numpy no"
min_clusters = 3
sim_dict = {}
simple_sim_dict = {}

"""I may have to do some major rethinking of how I want to
process the gene data in order to cluster it, my current plan may get out of hand."""


def gene_produce(gene_list):
    for gene in gene_list:
        gene = Gene(stuff)
        pass


def Agglomerative_cluster(clusters):
    cluster_count = 0
    clusters_base = clusters
    clusters_compair = clusters
    while cluster_count > 3:
        # pairs clusters unitl amount reaches min_clusters
        for avg_gene in clusters_base:
            clusters_compair = clusters
            for avg_gene2 in clusters_compair:
                if sim_dict[avg_gene2](0) != avg_gene:
                    compairison_suite(avg_gene, avg_gene2)
        # cluster genes based off of sim_dict
        SimpleSimilar(sim_dict)
        for clust in simple_sim_dict:
            pass
        # average the values of the genes in the clusters and save values as gene objects for use in next cycle

    pass


def compairison_suite(gene1, gene2):
    GCsim = GCcontent_percentsimilar(gene1, gene2)
    lowersim = lower_length(gene1, gene2)
    total_lensim = total_length(gene1, gene2)
    tracksim = TrackLength_percenetsimilar(gene1, gene2)
    stdevtracksim = StandardDeviation_percenetsimilar(gene1, gene2)
    exontracklensim = Exontracklength_percenetsimilar(gene1, gene2)
    stdevexontracklensim = StandardDeviationExontrack_percenetsimilar(gene1, gene2)
    introntracklensim = Introntracklength_percenetsimilar(gene1, gene2)
    stdevintrontracklensim = StandardDeviationIntrontrack_percenetsimilar(gene1, gene2)
    baseA_avgsim = BaseAtrack_percenetsimilar(gene1, gene2)
    baseC_avgsim = BaseCtrack_percenetsimilar(gene1, gene2)
    baseG_avgsim = BaseGtrack_percenetsimilar(gene1, gene2)
    baseT_avgsim = BaseTtrack_percenetsimilar(gene1, gene2)
    eighteensim = eighteenmer_percentsimilar(gene1, gene2)
    exon_lensim = exon_length(gene1, gene2)
    intron_lensim = intron_length(gene1, gene2)
    percentintronicsim = Percentintronic_percentsimilar(gene1, gene2)
    percentexonicsim = Percentexonic_percentsimilar(gene1, gene2)
    stdevexonsim = StandardDeviationExon_percenetsimilar(gene1, gene2)
    avexonsim = AverageExon_percenetsimilar(gene1, gene2)
    stdevintronsim = StandardDeviationIntron_percenetsimilar(gene1, gene2)
    avintronsim = AverageIntron_percenetsimilar(gene1, gene2)
    sim_dict[gene1] = (gene2, GCsim, tracksim, stdevtracksim, exontracklensim, stdevexontracklensim,
                       introntracklensim, stdevintrontracklensim, baseA_avgsim, baseC_avgsim, baseG_avgsim,
                       baseT_avgsim, eighteensim, exon_lensim, intron_lensim, total_lensim, lowersim,
                       percentintronicsim, percentexonicsim, stdevexonsim, avexonsim,
                       stdevintronsim, avintronsim)


def SimpleSimilar(sim_dict):
    combined_perc = 0
    for item in sim_dict:
        for perc in sim_dict[item]:
            if not sim_dict[item](0):
                combined_perc += sim_dict[item]
        simple_sim_dict[item] = (sim_dict[item](0), combined_perc)
    pass


def GCcontent_percentsimilar(genes1, genes2):
    gc1 = genes1.get_GCperc()
    gc2 = genes2.get_GCperc()
    if gc1 >= gc2:
        sim_score = gc1 - gc2
    if gc2 > gc1:
        sim_score = gc2 - gc1
    return sim_score


def lower_length(genes1, genes2):
    lower1 = genes1.get_Lower()
    lower2 = genes2.get_Lower()
    if lower1 >= lower2:
        sim_score = lower1 - lower2
    if lower2 > lower1:
        sim_score = lower2 - lower1
    return sim_score


def total_length(genes1, genes2):
    len1 = genes1.get_totalleng()
    len2 = genes2.get_totalleng()
    if len1 >= len2:
        sim_score = len1 - len2
    if len2 > len1:
        sim_score = len2 - len1
    return sim_score


def TrackLength_percenetsimilar(genes1, genes2):
    track1 = genes1.get_trackperc()
    track2 = genes2.get_trackperc()
    if track1 >= track2:
        sim_score = track1 - track2
    if track2 > track1:
        sim_score = track2 - track1
    return sim_score


def StandardDeviation_percenetsimilar(genes1, genes2):
    stdevtrack1 = genes1.get_stdevtrackperc()
    stdevtrack2 = genes2.get_stdevtrackperc()
    if stdevtrack1 >= stdevtrack2:
        sim_score = stdevtrack1 - stdevtrack2
    if stdevtrack2 > stdevtrack1:
        sim_score = stdevtrack2 - stdevtrack1
    return sim_score


def Exontracklength_percenetsimilar(genes1, genes2):
    exontrack1 = genes1.get_exontrackperc()
    exontrack2 = genes2.get_exontrackperc()
    if exontrack1 >= exontrack2:
        sim_score = exontrack1 - exontrack2
    if exontrack2 > exontrack1:
        sim_score = exontrack2 - exontrack1
    return sim_score


def StandardDeviationExontrack_percenetsimilar(genes1, genes2):
    stdevexontrack1 = genes1.get_stdevexontrackperc()
    stdevexontrack2 = genes2.get_stdevexontrackperc()
    if stdevexontrack1 >= stdevexontrack2:
        sim_score = stdevexontrack1 - stdevexontrack2
    if stdevexontrack2 > stdevexontrack1:
        sim_score = stdevexontrack2 - stdevexontrack1
    return sim_score


def Introntracklength_percenetsimilar(genes1, genes2):
    introntrack1 = genes1.get_introntrackperc()
    introntrack2 = genes2.get_introntrackperc()
    if introntrack1 >= introntrack2:
        sim_score = introntrack1 - introntrack2
    if introntrack2 > introntrack1:
        sim_score = introntrack2 - introntrack1
    return sim_score


def StandardDeviationIntrontrack_percenetsimilar(genes1, genes2):
    stdeintrontrack1 = genes1.get_stdevexontrackperc()
    stdeintrontrack2 = genes2.get_stdevexontrackperc()
    if stdeintrontrack1 >= stdeintrontrack2:
        sim_score = stdeintrontrack1 - stdeintrontrack2
    if stdeintrontrack2 > stdeintrontrack1:
        sim_score = stdeintrontrack2 - stdeintrontrack1
    return sim_score


def BaseAtrack_percenetsimilar(genes1, genes2):
    baseA1 = genes1.get_BaseAperc()
    baseA2 = genes2.get_BaseAperc()
    if baseA1 >= baseA2:
        sim_score = baseA1 - baseA2
    if baseA2 > baseA1:
        sim_score = baseA2 - baseA1
    return sim_score


def BaseCtrack_percenetsimilar(genes1, genes2):
    baseC1 = genes1.get_BaseCperc()
    baseC2 = genes2.get_BaseCperc()
    if baseC1 >= baseC2:
        sim_score = baseC1 - baseC2
    if baseC2 > baseC1:
        sim_score = baseC2 - baseC1
    return sim_score


def BaseGtrack_percenetsimilar(genes1, genes2):
    baseG1 = genes1.get_BaseGperc()
    baseG2 = genes2.get_BaseGperc()
    if baseG1 >= baseG2:
        sim_score = baseG1 - baseG2
    if baseG2 > baseG1:
        sim_score = baseG2 - baseG1
    return sim_score


def BaseTtrack_percenetsimilar(genes1, genes2):
    BaseT1 = genes1.get_BaseTperc()
    BaseT2 = genes2.get_BaseTperc()
    if BaseT1 >= BaseT2:
        sim_score = BaseT1 - BaseT2
    if BaseT2 > BaseT1:
        sim_score = BaseT2 - BaseT1
    return sim_score


def eighteenmer_percentsimilar(genes1, genes2):
    eighteenmer1 = genes1.get_eighteenmerperc()
    eighteenmer2 = genes2.get_eighteenmerperc()
    if eighteenmer1 >= eighteenmer2:
        sim_score = eighteenmer1 - eighteenmer2
    if eighteenmer2 > eighteenmer1:
        sim_score = eighteenmer2 - eighteenmer1
    return sim_score


def exon_length(genes1, genes2):
    exonlen1 = genes1.get_exonperc()
    exonlen2 = genes2.get_exonperc()
    if exonlen1 >= exonlen2:
        sim_score = exonlen1 - exonlen2
    if exonlen2 > exonlen1:
        sim_score = exonlen2 - exonlen1
    return sim_score


def intron_length(genes1, genes2):
    intronlen1 = genes1.get_intronperc()
    intronlen2 = genes2.get_intronperc()
    if intronlen1 >= intronlen2:
        sim_score = intronlen1 - intronlen2
    if intronlen2 > intronlen1:
        sim_score = intronlen2 - intronlen1
    return sim_score


def Percentintronic_percentsimilar(genes1, genes2):
    percentintron1 = genes1.get_percentintronperc()
    percentintron2 = genes2.get_percentintronperc()
    if percentintron1 >= percentintron2:
        sim_score = percentintron1 - percentintron2
    if percentintron2 > percentintron1:
        sim_score = percentintron2 - percentintron1
    return sim_score


def Percentexonic_percentsimilar(genes1, genes2):
    percentexon1 = genes1.get_percentexonperc()
    percentexon2 = genes2.get_percentexonperc()
    if percentexon1 >= percentexon2:
        sim_score = percentexon1 - percentexon2
    if percentexon2 > percentexon1:
        sim_score = percentexon2 - percentexon1
    return sim_score


def StandardDeviationExon_percenetsimilar(genes1, genes2):
    stdevexon1 = genes1.get_stdevexonsperc()
    stdevexon2 = genes2.get_stdevexonsperc()
    if stdevexon1 >= stdevexon2:
        sim_score = stdevexon1 - stdevexon2
    if stdevexon2 > stdevexon1:
        sim_score = stdevexon2 - stdevexon1
    return sim_score


def StandardDeviationIntron_percenetsimilar(genes1, genes2):
    stdevintron1 = genes1.get_stdevintronsperc()
    stdevintron2 = genes2.get_stdevintronsperc()
    if stdevintron1 >= stdevintron2:
        sim_score = stdevintron1 - stdevintron2
    if stdevintron2 > stdevintron1:
        sim_score = stdevintron2 - stdevintron1
    return sim_score


def AverageExon_percenetsimilar(genes1, genes2):
    averageexon1 = genes1.get_averageexonperc()
    averageexon2 = genes2.get_averageexonperc()
    if averageexon1 >= averageexon2:
        sim_score = averageexon1 - averageexon2
    if averageexon2 > averageexon1:
        sim_score = averageexon2 - averageexon1
    return sim_score


def AverageIntron_percenetsimilar(genes1, genes2):
    averageintron1 = genes1.get_averageintronperc()
    averageintron2 = genes2.get_averageintronperc()
    if averageintron1 >= averageintron2:
        sim_score = averageintron1 - averageintron2
    if averageintron2 > averageintron1:
        sim_score = averageintron2 - averageintron1
    return sim_score


# gene_produce(gene_list) this must be run first
# Agglomerative_cluster using this gene list to create clusters
