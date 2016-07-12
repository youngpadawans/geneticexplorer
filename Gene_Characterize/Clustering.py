__author__ = 'theep_000'

from Gene_Analyzer import Gene

min_clusters = 3

def gene_produce(gene_list):
    for gene in gene_list:
        gene = Gene(stuff)
        pass

def Agglomerative_cluster(clusters):
    cluster_count = 0
    clusters_base = clusters
    clusters_compair = clusters
    while cluster_count > 3:
        #pairs clusters unitl amount reaches min_clusters
        for avg_gene in clusters_base:
            clusters_compair = clusters
            for avg_gene2 in clusters_compair:
                compairison_suite(avg_gene, avg_gene2)

    pass

def compairison_suite(gene1, gene2):
    GCcontent_percentsimilar(gene1, gene2)
    TrackLength_percenetsimilar(gene1, gene2)
    eighteenmer_percentsimilar(gene1, gene2)
    avgexon_length(gene1, gene2)
    avgintron_length(gene1, gene2)

def GCcontent_percentsimilar(genes1, genes2):

    pass

def TrackLength_percenetsimilar(genes1, genes2):

    pass

def eighteenmer_percentsimilar(genes1, genes2):

    pass

def avgexon_length(genes1, genes2):

    pass

def avgintron_length(genes1, genes2):

    pass