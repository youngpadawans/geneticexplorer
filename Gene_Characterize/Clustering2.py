#!bin/bash

from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as npy
from Gene_Analyzer import Gene
gene_list = []
var_num = 0


def listpopulator():
    """creates list of genes for use in clustering
    """
    pass


def clustermethod(gene_list):
    """clusters a list of genes using scipy linkage
    """
    array_val = 0
    array_list = []
    past_point = False
    for gene in gene_list:
        array_val += 1
        gene_vals = (gene.get_GCperc(), gene.get_Lower(), gene.get_totalleng())
        array_val = npy.fromiter(gene_vals, float)
        array_list.append(array_val)
        #loop produces a ndarray for every gene, containing it's data, for use in concatenation then clustering
    for point in array_list:
        #loop concatenates all the data
        current_point = point
        if past_point is False:
            past_point = True
            past_data = point
            pass
        else:
            data = npy.concatenate(past_data, current_point)
            past_data = data
    heirclust = linkage(data, "ward")
    return heirclust

def main(args, ar):
    pass

if __name__ == "__main__":
    main(argv)
