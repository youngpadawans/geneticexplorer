
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as npy
from Gene_Analyzer import Gene
gene_list = []
var_num = 0

def listpopulator():

    pass


def clustermethod(gene_list):
    array_val = 0
    for gene in gene_list:
        array_val += 1
        #loop produces a ndarray for every gene, containing it's data, for use in concatenation then clustering
        array_val = npy.ndarray([var_num, ], buffer = [gene.get_GCperc(), gene.get_Lower(), gene.get_totalleng()])
    data = npy.concatenate()
    heirclust = linkage(data, "ward")
    return heirclust

print npy.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100, ])
