__author__ = 'theep_000'

import random
import operator

mutate_chance = 2
base_pop = 10
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
            total += self.__chrom_fitdict[chrom]
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
        for num in range(0,4):
            random_layout = random.randint(0,6)
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
        child = pasta(mutated_child[0], mutated_child[1], mutated_child[2], mutated_child[3])
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
hella.set_fitvalue()
print hella.list_ing()
print hella.get_fitvalue()
generation = Chrom_Population([])
generation.reset_population()
print generation.get_generation()
generation.dict_producer()
generation.probability_parent()
generation.parent_select()