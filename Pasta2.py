__author__ = 'theep_000'

import random
import operator
from collections import Counter

base_pop = 100
poss_ingredients = ["tomato sauce","pesto","mozzarella","alfredo sauce", "pasta shells","chile sauce", "pasta bowties", "parmesan","meatballs","pasta tubes","shredded chicken","basil", "spinach","chives","shrimp","mushroom","macaroni","feta cheese","noodles","sausage","olives"]

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

    def set_fitvalue(self, fit_val):
        # Use to set fit value for each ingredient.
        fit_val = 0
        if self.__gene_1 == "tomato_sauce":
            fit_val += 7
        if self.__gene_2 == "tomato_sauce":
            fit_val += 7
        if self.__gene_3 == "tomato_sauce":
            fit_val += 7
        if self.__gene_4 == "tomato_sauce":
            fit_val += 7
        if self.__gene_1 == "pesto":
            fit_val += 5
        if self.__gene_2 == "pesto":
            fit_val += 5
        if self.__gene_3 == "pesto":
            fit_val += 5
        if self.__gene_4 == "pesto":
            fit_val += 5
        if self.__gene_1 == "mozzarella":
            fit_val += 5
        if self.__gene_2 == "mozzarella":
            fit_val += 5
        if self.__gene_3 == "mozzarella":
            fit_val += 5
        if self.__gene_4 == "mozzarella":
            fit_val += 5
        if self.__gene_1 == "alfredo sauce":
            fit_val += 10
        if self.__gene_2 == "alfredo sauce":
            fit_val += 10
        if self.__gene_3 == "alfredo sauce":
            fit_val += 10
        if self.__gene_4 == "alfredo sauce":
            fit_val += 10
        if self.__gene_1 == "pasta shells":
            fit_val += 7
        if self.__gene_2 == "pasta shells":
            fit_val += 7
        if self.__gene_3 == "pasta shells":
            fit_val += 7
        if self.__gene_4 == "pasta shells":
            fit_val += 7
        if self.__gene_1 == "chile sauce":
            fit_val += 5
        if self.__gene_2 == "chile sauce":
            fit_val += 5
        if self.__gene_3 == "chile sauce":
            fit_val += 5
        if self.__gene_4 == "chile sauce":
            fit_val += 5
        if self.__gene_1 == "pasta bowties":
            fit_val += 5
        if self.__gene_2 == "pasta bowties":
            fit_val += 5
        if self.__gene_3 == "pasta bowties":
            fit_val += 5
        if self.__gene_4 == "pasta bowties":
            fit_val += 5
        if self.__gene_1 == "parmesan":
            fit_val += 10
        if self.__gene_2 == "parmesan":
            fit_val += 10
        if self.__gene_3 == "parmesan":
            fit_val += 10
        if self.__gene_4 == "parmesan":
            fit_val += 10
        if self.__gene_1 == "meatballs":
            fit_val += 8
        if self.__gene_2 == "meatballs":
            fit_val += 8
        if self.__gene_3 == "meatballs":
            fit_val += 8
        if self.__gene_4 == "meatballs":
            fit_val += 8
        if self.__gene_1 == "pasta tubes":
            fit_val += 10
        if self.__gene_2 == "pasta tubes":
            fit_val += 10
        if self.__gene_3 == "pasta tubes":
            fit_val += 10
        if self.__gene_4 == "pasta tubes":
            fit_val += 10
        if self.__gene_1 == "shredded chicken":
            fit_val += 10
        if self.__gene_2 == "shredded chicken":
            fit_val += 10
        if self.__gene_3 == "shredded chicken":
            fit_val += 10
        if self.__gene_4 == "shredded chicken":
            fit_val += 10
        if self.__gene_1 == "basil":
            fit_val += 7
        if self.__gene_2 == "basil":
            fit_val += 7
        if self.__gene_3 == "basil":
            fit_val += 7
        if self.__gene_4 == "basil":
            fit_val += 7
        if self.__gene_1 == "spinach":
            fit_val += 10
        if self.__gene_2 == "spinach":
            fit_val += 10
        if self.__gene_3 == "spinach":
            fit_val += 10
        if self.__gene_4 == "spinach":
            fit_val += 10
        if self.__gene_1 == "chives":
            fit_val += 2
        if self.__gene_2 == "chives":
            fit_val += 2
        if self.__gene_3 == "chives":
            fit_val += 2
        if self.__gene_4 == "chives":
            fit_val += 2
        if self.__gene_1 == "shrimp":
            fit_val += 2
        if self.__gene_2 == "shrimp":
            fit_val += 2
        if self.__gene_3 == "shrimp":
            fit_val += 2
        if self.__gene_4 == "shrimp":
            fit_val += 2
        if self.__gene_1 == "mushroom":
            fit_val += 2
        if self.__gene_2 == "mushroom":
            fit_val += 2
        if self.__gene_3 == "mushroom":
            fit_val += 2
        if self.__gene_4 == "mushroom":
            fit_val += 2
        if self.__gene_1 == "macaroni":
            fit_val += 5
        if self.__gene_2 == "macaroni":
            fit_val += 5
        if self.__gene_3 == "macaroni":
            fit_val += 5
        if self.__gene_4 == "macaroni":
            fit_val += 5
        if self.__gene_1 == "feta cheese":
            fit_val += 2
        if self.__gene_2 == "feta cheese":
            fit_val += 2
        if self.__gene_3 == "feta cheese":
            fit_val += 2
        if self.__gene_4 == "feta cheese":
            fit_val += 2
        if self.__gene_1 == "olives":
            fit_val += 0
        if self.__gene_2 == "olives":
            fit_val += 0
        if self.__gene_3 == "olives":
            fit_val += 0
        if self.__gene_4 == "olives":
            fit_val += 0
        if self.__gene_1 == "noodles":
            fit_val += 7
        if self.__gene_2 == "noodles":
            fit_val += 7
        if self.__gene_3 == "noodles":
            fit_val += 7
        if self.__gene_4 == "noodles":
            fit_val += 7
        if self.__gene_1 == "sausage":
            fit_val += 7
        if self.__gene_2 == "sausage":
            fit_val += 7
        if self.__gene_3 == "sausage":
            fit_val += 7
        if self.__gene_4 == "sausage":
            fit_val += 7
        self.fit_value = fit_val

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
        self.__chrom_list = ["chickens","books", "love", "kracken","loooooouve"]
        self.__chrom_fitdict = {"chickens": 5, 'books':10000, "love":0, "kracken":9, "loooooouve":1 }

        print self.__chrom_fitdict


        execution =reversed(Counter(self.__chrom_fitdict).most_common()[-3:])

        print (execution)
        for object in execution:
            del self.__chrom_fitdict[object[0]]
            print self.__chrom_fitdict



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
generation.cull()