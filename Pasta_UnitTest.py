__author__ = 'theep_000'
import unittest
import PastaGA


class Test(unittest.TestCase):

    def setup(self):
        self.test_gen = PastaGA.ChromPopulation([])
        self.test_chrom = PastaGA.PastaDish("spaghetti", "spaghetti", "spaghetti", "pesto")
        self.test_gen.resetPopulation(100)
        self.test_gen.fitnessProducer()
        self.test_gen.probabilityParent()

    def testParentDouble(self):
        """checks that the same parent is not selected twice
        """
        self.setup()
        parent_tuple = self.test_gen.parentSelect()
        self.assertNotEqual(parent_tuple[0], parent_tuple[1])

    def testChromList(self):
        """makes sure ingredients populate the chromosome lists
        """
        self.setup()
        self.assertTrue('pesto' in self.test_chrom.listIng())

    def testDictProducer(self):
        """checks that a list of chromosomes is generated when the generation is reset
        """
        self.setup()
        self.test_gen.resetPopulation(100)
        self.assertTrue(self.test_gen.getGeneration() != [])

    def testFitSetTest(self):
        """tests that the fitness value of the test chromosome is a non-negative number
        """
        self.setup()
        self.assertTrue(self.test_chrom.fit_value != -1)

if __name__ == '__main__':
    unittest.main()
