__author__ = 'theep_000'

from Gene_Analyzer import Gene

min_clusters = 3
sim_dict = {}
simple_sim_dict = {}

#I may have to do some major rethinking of how I want to process the gene data in order to cluster it, my current plan may get out of hand.

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
    tracksim = TrackLength_percenetsimilar(gene1, gene2)
    eighteensim = eighteenmer_percentsimilar(gene1, gene2)
    exon_lensim = avgexon_length(gene1, gene2)
    intron_lensim = avgintron_length(gene1, gene2)
    total_lensim = total_length(gene1, gene2)
    lowersim = lower_length(gene1, gene2)
    sim_dict[gene1] = (gene2, GCsim, tracksim, eighteensim, exon_lensim, intron_lensim, total_lensim, lowersim)


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


def TrackLength_percenetsimilar(genes1, genes2):

    pass


def eighteenmer_percentsimilar(genes1, genes2):

    pass


def avgexon_length(genes1, genes2):

    pass


def avgintron_length(genes1, genes2):

    pass


def total_length(genes1, genes2):

    len1 = genes1.get_totalleng()
    len2 = genes2.get_totalleng()
    if len1 >= len2:
        sim_score = len1 - len2
    if len2 > len1:
        sim_score = len2 - len1
    return sim_score


def lower_length(genes1, genes2):

    lower1 = genes1.get_Lower()
    lower2 = genes2.get_Lower()
    if lower1 >= lower2:
        sim_score = lower1 - lower2
    if lower2 > lower1:
        sim_score = lower2 - lower1
    return sim_score

# gene_produce(gene_list) this must be run first
# Agglomerative_cluster using this gene list to create clusters
