__author__ = 'theep_000'
import unittest
import PastaGA

test_gen = PastaGA.ChromPopulation([])
test_chrom = PastaGA.PastaDish("spaghetti", "spaghetti", "spaghetti", "pesto")
test_gen.resetPopulation(100)
test_gen.dictProducer()
test_gen.probabilityParent()

class Test(unittest.TestCase):

    def testParentDouble(self):
        """checks that the same parent is not selected twice
        """
        test_gen = PastaGA.ChromPopulation([])
        test_gen.resetPopulation(100)
        test_gen.dictProducer()
        test_gen.probabilityParent()
        parent_tuple = test_gen.parentSelect()
        self.assertNotEqual(parent_tuple[0], parent_tuple[1])

    def testChromList(self):
        """makes sure ingredients populate the chromosome lists
        """
        self.assertTrue('pesto' in test_chrom.listIng())

    def testDictProducer(self):
        """checks that a list of chromosomes is generated when the generation is reset
        """
        test_gen.resetPopulation(100)
        self.assertTrue(test_gen.getGeneration() != [])

    def testFitSetTest(self):
        """tests that the fitness value of the test chromosome is a non-negative number
        """
        self.assertTrue(test_chrom.fit_value != -1)

if __name__ == '__main__':
    unittest.main()
