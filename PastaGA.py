__author__ = 'theep_000'

import random
import operator
from collections import Counter
import sys
import argparse

mutate_chance = 2
base_pop = 10
generation_max = 10

poss_ingredients = ["tomato sauce","pesto","mozzarella","alfredo sauce", "pasta shells","chile sauce", "pasta bowties", "parmesan","meatballs","pasta tubes","shredded chicken","basil", "spinach","chives","shrimp","mushroom","macaroni","feta cheese","noodles","sausage","olives"]

class Gene:

    __ingredient = ""
    score_dict = {"tomato sauce" : 7,"pesto" : 5,"mozzarella" : 5,"alfredo sauce" : 10, "pasta shells" : 7,"chile sauce" : 5, "pasta bowties" : 5, "parmesan" : 10,"meatballs" : 8,"pasta tubes" : 10,"shredded chicken" : 10,"basil" : 7, "spinach" : 10,"chives" : 2,"shrimp" : 2,"mushroom" : 2,"macaroni" : 5,"feta cheese" : 2,"noodles" : 7,"sausage" : 7,"olives": 0}

    def __init__(self, ingredient):

        self.__ingredient = ingredient


class PastaDish:
    #format and functions of the pasta chromosome

    __gene_1 = ""
    __gene_2 = ""
    __gene_3 = ""
    __gene_4 = ""
    fitvalue = 0

    def __init__ (self, gene_1, gene_2, gene_3, gene_4):
        #creates object from 4 genes

        self.__gene_1 = gene_1
        self.__gene_2 = gene_2
        self.__gene_3 = gene_3
        self.__gene_4 = gene_4

    def list_ing(self):
        #gives a list of the genes
        return [self.__gene_1, self.__gene_2, self.__gene_3, self.__gene_4]

    def set_fitvalue(self):
        fit_val = 0
        fit_val += Gene.score_dict[self.__gene_1]
        fit_val += Gene.score_dict[self.__gene_2]
        fit_val += Gene.score_dict[self.__gene_3]
        fit_val += Gene.score_dict[self.__gene_4]
        self.fitvalue = fit_val

    def old_set_fitvalue(self):
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
        self.fitvalue = fit_val

    def get_fitvalue(self):
        #gives the set fitvalue
        return self.fitvalue

class ChromPopulation:

    __chrom_list = []
    __chrom_fitdict = {}
    __prob_dict = {}

    def __init__(self, chrom_list):
        self.__chrom_list = chrom_list

    def cull(self):
        #remove 10% of self
        count_rem = (len(self.__chrom_list)/10)
        execution =reversed(Counter(self.__chrom_fitdict).most_common()[-count_rem:])
        for object in execution:
            del self.__chrom_fitdict[object[0]]
        pass

    def probability_parent(self):
        #creates a dictionary containing the probability of being selected as a parent
        self.__prob_dict = {}
        total = 0
        prev_chance = 0
        fit_copy1 = self.__chrom_fitdict
        fit_copy2 = self.__chrom_fitdict
        for chrom in fit_copy1:
            total += self.__chrom_fitdict[chrom]
        for chrom in fit_copy2:
            selection_chance = float(fit_copy2[chrom])/float(total) + prev_chance
            self.__prob_dict[chrom] = selection_chance
            prev_chance = selection_chance
        pass

    def parent_select(self):
        #selects parents based on probability dict
        parentchance_1 = random.random()
        parentchance_2 = random.random()
        prob_dic1 = self.__prob_dict
        prob_dic2 = self.__prob_dict
        def_check = 0
        for chrom in prob_dic1:
            if prob_dic1[chrom] >= parentchance_1:
                parent_1 = chrom
                def_check = 1
            if def_check == 1:
                break
        def_check = 0
        prev_parent = None
        for chrom in prob_dic2:
            if prob_dic2[chrom] >= parentchance_2:
                parent_2 = chrom
                def_check = 1
            if def_check == 1:
                break
            prev_parent = chrom
        parent_tuple = (parent_1, parent_2)
        return parent_tuple

    def dict_producer(self):
        for chrom in self.__chrom_list:
            chrom.set_fitvalue()
            self.__chrom_fitdict[chrom] = chrom.get_fitvalue()
        pass

    def breed_et_mutate(self, couple_tuple):
        #mutates children after bred from two chromosomes
        pasta1 = couple_tuple[0]
        pasta2 = couple_tuple[1]
        ingredients_1 = pasta1.list_ing()
        ingredients_2 = pasta2.list_ing()
        ingredients_3 = []
        mutated_child = []
        for num in range(0,1):
            random_layout = random.randint(1, 6)
            if random_layout == 1:
                ingredients_3 = [ingredients_1[0],ingredients_1[1], ingredients_2[2], ingredients_2[3]]
            if random_layout == 2:
                ingredients_3 = [ingredients_1[0],ingredients_2[1], ingredients_1[2], ingredients_2[3]]
            if random_layout == 3:
                ingredients_3 = [ingredients_1[0],ingredients_2[1], ingredients_2[2], ingredients_1[3]]
            if random_layout == 4:
                ingredients_3 = [ingredients_2[0],ingredients_2[1], ingredients_1[2], ingredients_1[3]]
            if random_layout == 5:
                ingredients_3 = [ingredients_2[0],ingredients_1[1], ingredients_1[2], ingredients_2[3]]
            if random_layout == 6:
                ingredients_3 = [ingredients_2[0],ingredients_1[1], ingredients_2[2], ingredients_1[3]]
        for ing in ingredients_3:
            mutate_poss = random.randint(0,100)
            if mutate_poss < mutate_chance:
                ing = poss_ingredients[random.randint(0, len(poss_ingredients)-1)]
            mutated_child.append(ing)
        child = PastaDish(mutated_child[0], mutated_child[1], mutated_child[2], mutated_child[3])
        self.__chrom_list.append(child)

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
            pasta_name = PastaDish(ingredient_1, ingredient_2, ingredient_3, ingredient_4)
            self.__chrom_list.append(pasta_name)
        pass

    def get_generation(self):
        #returns the generation dict
        return self.__chrom_list

    def give_most_fit(self):
        #returns fitteset chromosome
        return max(self.__chrom_fitdict.iteritems(), key=operator.itemgetter(1))[0]

def main():
    #parse line arguments
    population = []
    for gens in range(0, generation_max):
        gens = ChromPopulation(population)
        if population == []:
            gens.reset_population()
        gens.dict_producer()
        gens.probability_parent()
        gens.cull()
        for pairs in range(0, base_pop/2):
            gens.breed_et_mutate(gens.parent_select())
        population = gens.get_generation()
        current_best = gens.give_most_fit()
    print current_best.list_ing()
    print current_best.get_fitvalue()



if __name__ == "__main__":
    main()
