__author__ = 'theep_000'
import unittest
import PastaGA

test_gen = PastaGA.ChromPopulation([])
test_chrom = PastaGA.PastaDish("spaghetti","spaghetti","spaghetti","pesto")
test_gen.reset_population()
test_gen.dict_producer()
test_gen.probability_parent()

class Test(unittest.TestCase):

    def test_parent_double(self):
        #checks that the same parent is not selected twice
        self.assertNotEqual(PastaGA.generation.parent_select()[0], PastaGA.generation.parent_select()[1])

    def test_chrom_list(self):
        #makes sure ingredients populate the chromosome lists
        print test_chrom.list_ing()
        self.assertTrue('pesto' in test_chrom.list_ing())

    def test_dict_producer(self):
        #checks that a list of chromosomes is generated when the generation is reset
        test_gen.reset_population()
        self.assertTrue(test_gen.get_generation() != [])

    def test_fit_set_test(self):
        #tests that the fitness value of the test chromosome is a non-negative number
        self.assertTrue(test_chrom.get_fitvalue() != -1)

if __name__ == '__main__':
    unittest.main()
