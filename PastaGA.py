
__author__ = "Paul Comeau"
__credits__ = ["Paul Comeau", "Kaixin Cui"]
__maintainer__ = "Paul Comeau"
__email__ = "comeaupaul98@gmail.com"
__status__ = "Development"

import random
import operator
from collections import Counter
from sys import argv
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


POSS_INGREDIENTS = ["tomato sauce", "pesto", "mozzarella",
                    "alfredo sauce", "pasta shells", "chile sauce", "pasta bowties",
                    "parmesan", "meatballs", "pasta tubes", "shredded chicken", "basil", "spinach", "chives", "shrimp",
                    "mushroom", "macaroni", "feta cheese", "noodles", "sausage", "olives"]


class Gene:
    """formatting for the object of a single ingredient
    """

    __ingredient = ""
    ingredient_score = {"tomato sauce": 7, "pesto": 5,
                        "mozzarella": 5, "alfredo sauce": 10, "pasta shells": 7, "chile sauce": 5,
                        "pasta bowties": 5, "parmesan": 10, "meatballs": 8,
                        "pasta tubes": 10, "shredded chicken": 10, "basil": 7,
                        "spinach": 10, "chives": 2, "shrimp": 2,
                        "mushroom": 2, "macaroni": 5, "feta cheese": 2, "noodles": 7,
                        "sausage": 7, "olives": 0}

    def __init__(self, ingredient):
        """creates object from single ingredient
        """

        self.__ingredient = ingredient


class PastaDish:
    """format and functions of the pasta chromosome
    """

    __gene_1 = ""
    __gene_2 = ""
    __gene_3 = ""
    __gene_4 = ""
    fit_value = 0

    def __init__(self, gene_1, gene_2, gene_3, gene_4):
        """creates object from 4 genes
        :param gene_1: ingredient one in chromosome
        :param gene_2: ingredient two in chromosome
        :param gene_3: ingredient three in chromosome
        :param gene_4: ingredient four in chromosome
        """

        self.__gene_1 = gene_1
        self.__gene_2 = gene_2
        self.__gene_3 = gene_3
        self.__gene_4 = gene_4

    def listIng(self):
        """gives a list of the genes
        :returns: a list of ingredients contained in the chromosome
        """

        return [self.__gene_1, self.__gene_2, self.__gene_3, self.__gene_4]

    def setFitValue(self):
        """sets the fitness value of a chromosome
        """

        fit_val = 0
        fit_val += Gene.ingredient_score[self.__gene_1]
        fit_val += Gene.ingredient_score[self.__gene_2]
        fit_val += Gene.ingredient_score[self.__gene_3]
        fit_val += Gene.ingredient_score[self.__gene_4]
        self.fitvalue = fit_val

class ChromPopulation:
    """format and fuctions of a population of chromosomes
    """
    __chroms = []
    __chrom_fit = {}
    __probabilities = {}

    def __init__(self, chrom_list):
        """the given list defines the chomosome population
        :param chrom_list: list of chromosomes to populate the ChromPopulation
        """

        self.__chroms = chrom_list

    def cull(self):
        """remove 10% of self
        """

        count_rem = (len(self.__chroms)/10)
        execution = reversed(Counter(self.__chrom_fit).most_common()[-count_rem:])
        for object in execution:
            del self.__chrom_fit[object[0]]
        pass

    def probabilityParent(self):
        """creates a dictionary containing the probability of being selected as a parent
        """

        self.__probabilities = {}
        total = 0
        prev_chance = 0
        fit_copy1 = self.__chrom_fit
        fit_copy2 = self.__chrom_fit
        for chrom in fit_copy1:
            total += self.__chrom_fit[chrom]
        for chrom in fit_copy2:
            selection_chance = float(fit_copy2[chrom])/float(total) + prev_chance
            self.__probabilities[chrom] = selection_chance
            prev_chance = selection_chance
        pass

    def parentSelect(self):
        """selects parents based on probability dict
        :returns: a pair of parent chromosomes
        """
        parent_chance_1 = random.random()
        parent_chance_2 = random.random()
        chance_list = []
        list_probs = self.__probabilities
        probs1 = self.__probabilities
        probs2 = self.__probabilities
        for vals in list_probs:
            chance_list.append(probs1[vals])
        chance_list2 = sorted(chance_list)
        chance_list.sort()
        def_check = 0
        for chrom in chance_list:
            if chrom >= parent_chance_1:
                for key in probs1:
                    if probs1[key] == chrom:
                        parent_1 = key
                        break
                def_check = 1
            if def_check == 1:
                break
        def_check = 0
        prev_parent = None
        for chrom in chance_list2:
            if chrom >= parent_chance_2:
                for key in probs2:
                    if probs2[key] == chrom:
                        parent_2 = key
                        break
                    prev_parent = key
                if parent_2 == parent_1:
                    if prev_parent == None:
                        pass
                    else:
                        parent_2 = prev_parent
                def_check = 1
            if def_check == 1:
                break
        parent_pair = (parent_1, parent_2)
        return parent_pair

    def fitnessProducer(self):
        """creates a dictionary containing pasta types and their fitness value
        """

        for chrom in self.__chroms:
            chrom.setFitValue()
            self.__chrom_fit[chrom] = chrom.fitvalue
        pass

    def breedEtMutate(self, parent_couple, mutate_chance):
        """mutates children after bred from two chromosomes
        :param parent_couple: a tuple containing the two parents of the new chromosome
        :param mutate_chance: int of percentage chance to mutate gene
        """
        pasta1 = parent_couple[0]
        pasta2 = parent_couple[1]
        ingredients_1 = pasta1.listIng()
        ingredients_2 = pasta2.listIng()
        ingredients_3 = [None, None, None, None]
        mutated_child = []
        p_count1 = 0
        p_count2 = 0
        for num in range(0, len(ingredients_2)):
            random_layout = random.randint(0, 1)
            if random_layout == 1:
                if p_count1 <= len(ingredients_1):
                    ingredients_3[num] = ingredients_1[num]
                    p_count1 += 1
                else:
                    ingredients_3[num] = ingredients_2[num]
                    p_count2 +=1
            else:
                if p_count2 <= len(ingredients_1):
                    ingredients_3[num] = ingredients_2[num]
                    p_count2 += 1
                else:
                    ingredients_3[num] = ingredients_1[num]
                    p_count1 += 1
        for ing in ingredients_3:
            mutate_poss = random.randint(0, 100)
            if mutate_poss < mutate_chance:
                ing = POSS_INGREDIENTS[random.randint(0, len(POSS_INGREDIENTS)-1)]
            mutated_child.append(ing)
        child = PastaDish(mutated_child[0], mutated_child[1], mutated_child[2], mutated_child[3])
        self.__chroms.append(child)

    def resetPopulation(self, base_pop):
        """replaces current dict with new generated genes/use to create initial population
        :param base_pop: number of chromosomes in the base population
        """
        pasta_count = 0
        for chrom in range(0, base_pop):
            pasta_count += 1
            pasta_name = pasta_count
            ingredient_1 = POSS_INGREDIENTS[random.randint(0, len(POSS_INGREDIENTS)-1)]
            ingredient_2 = POSS_INGREDIENTS[random.randint(0, len(POSS_INGREDIENTS)-1)]
            ingredient_3 = POSS_INGREDIENTS[random.randint(0, len(POSS_INGREDIENTS)-1)]
            ingredient_4 = POSS_INGREDIENTS[random.randint(0, len(POSS_INGREDIENTS)-1)]
            pasta_name = PastaDish(ingredient_1, ingredient_2, ingredient_3, ingredient_4)
            self.__chroms.append(pasta_name)
        pass

    def getGeneration(self):
        """returns the generation dict
        """
        return self.__chroms

    def giveMostFit(self):
        """returns fitteset chromosome
        """
        return max(self.__chrom_fit.iteritems(), key=operator.itemgetter(1))[0]

def commandLine(arg_list=argv):
    """defines command line arguments
    """
    options_parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)

    options_parser.add_argument('-m', help='percentage chance of every gene to mutate', action="store", dest="percent", type=int, default=2)
    options_parser.add_argument('-b', help='amount of chromosomes the GA generates to as a base population', action="store", dest="population", type=int, default=10)
    options_parser.add_argument('-g', help='amount of times the GA goes through its cycle', action="store", dest="cycle", type=int, default=10)

    opts, unkown = options_parser.parse_known_args(args = arg_list)

    return opts

def main(args, args_parsed=None):
    """defines variables based off of command line arguments
    """
    if args_parsed is not None:
        opts = args_parsed

    else:
        opts = commandLine(args)

    if opts.cycle > 0:
        generation_max = opts.cycle

    if opts.population > 0:
        base_pop = opts.population

    if opts.percent >= 0:
        mutate_chance = opts.percent

    workflow(generation_max, mutate_chance, base_pop)

def workflow(generation_max, mutation_chance, base_pop):
    """the main process which uses the class outlines and processes to run a genetic algorithm
    :param generation_max: number of generations the program cycles through
    :param mutation_chance: percentage chance to mutate each gene
    :param base_pop: number of chromosomes in base population
    """
    population = []
    for gens in range(0, generation_max):
        gens = ChromPopulation(population)
        if population == []:
            gens.resetPopulation(base_pop)
        gens.fitnessProducer()
        gens.probabilityParent()
        gens.cull()
        for pairs in range(0, base_pop/2):
            gens.breedEtMutate(gens.parentSelect(), mutation_chance)
        population = gens.getGeneration()
        current_best = gens.giveMostFit()
    for chrom in population:
        print chrom.listIng()
    print current_best.listIng()
    print current_best.fitvalue



if __name__ == "__main__":
    main(argv)
