__author__ = 'theep_000'

import random
import operator

base_pop = 100
poss_ingredients = ["spaghetti", "pesto", "mousalini"]

class pasta:
    #format and functions of the pasta chromosome

    __gene_1 = ""
    __gene_2 = ""
    __gene_3 = ""
    __gene_4 = ""
    fitvalue = 0

    def __init__ (self, gene_1, gene_2, gene_3, gene_4):
        #creates object from 4 genes

        pasta.gene_1 = gene_1
        pasta.gene_2 = gene_2
        pasta.gene_3 = gene_3
        pasta.gene_4 = gene_4

    def list_ing(self):
        #gives a list of the genes
        return [self.gene_1, self.gene_2, self.gene_3, self.gene_4]

    def set_fitvalue(self):
        #use to set fitvalue
        self.fitvalue = 100

    def get_fitvalue(self):
        #gives the set fitvalue
        return self.fitvalue

class Chrom_Population:

    __chrom_list = []
    __chrom_fitdict = {}
    __prob_dict = {}

    def __init__(self, chrom_list):
        Chrom_Population.chrom_dict = chrom_list

    def cull(self):
        #remove 10% of self and move to next generation
        pass

    def probability_parent(self):
        #creates a dictionary containing the probability of being selected as a parent
        self.__prob_dict = {}
        total = 0
        prev_chance = 0
        fit_copy1 = self.__chrom_fitdict
        fit_copy2 = self.__chrom_fitdict
        for chrom in fit_copy1:
            total += fit_copy1[chrom]
        for chrom in fit_copy2:
            selection_chance = (fit_copy2[chrom]/total) + prev_chance
            self.__prob_dict[chrom] = selection_chance
            prev_chance = selection_chance
        pass

    def parent_select(self):
        #selects parents based on probability dict
        parent_1 = random.random()
        parent_2 = random.random()
        prob_dic1 = self.__prob_dict
        prob_dic2 = self.__prob_dict
        for chrom in prob_dic1:
            if prob_dic1[chrom] <= parent_1:
                parent_1 = chrom
                break
        for chrom in prob_dic2:
            if prob_dic2[chrom] <= parent_2:
                parent_2 = chrom
                break
        parent_tuple = (parent_1, parent_2)
        return parent_tuple

    def dict_producer(self):
        for chrom in self.__chrom_list:
            self.chrom_fidict[chrom] = chrom.get_fitvalue()
        pass

    def breed_et_mutate(self, couple_tuple):
        #mutates children after bred from two chromosomes

        pass

    def reset_population(self):
        #replaces current dict with new generated genes/use to create initial population
        pasta_count = 0
        for chrom in range(0, base_pop):
            pasta_count += 1
            pasta_name = pasta_count
            ingredient_1 = poss_ingredients[random.randint(0, len(poss_ingredients)-1)]
            ingredient_2 = poss_ingredients[random.randint(0, len(poss_ingredients)-1)]
            ingredient_3 = poss_ingredients[random.randint(0, len(poss_ingredients)-1)]
            ingredient_4 = poss_ingredients[random.randint(0, len(poss_ingredients)-1)]
            pasta_name = pasta(ingredient_1, ingredient_2, ingredient_3, ingredient_4)
            self.__chrom_list.append(pasta_name)
        pass

    def get_generation(self):
        #returns the generation dict
        return self.__chrom_list

    def give_most_fit(self):
        #returns fitteset chromosome
        return max(self.chrom_dict.iteritems(), key=operator.itemgetter(1))[0]

hella = pasta("h", "e", "l", "l")
hella.set_fitvalue(100)
print hella.list_ing()
print hella.get_fitvalue()
generation = Chrom_Population([])
generation.reset_population()
print generation.get_generation()
