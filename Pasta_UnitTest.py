__author__ = 'theep_000'
import unittest
import PastaGA

test_gen = PastaGA.Chrom_Population([])
test_chrom = PastaGA.pasta("spaghetti","spaghetti","spaghetti","spaghetti")
test_gen.reset_population()
test_gen.dict_producer()
test_gen.probability_parent()

class Test(unittest.TestCase):

    def test(self):
        self.assertNotEqual(PastaGA.generation.parent_select()[0], PastaGA.generation.parent_select()[1])

    def test_chrom_list(self):
        print test_chrom.list_ing()
        self.assertTrue('pesto' in test_chrom.list_ing())

    def test_dict_producer(self):
        test_gen.dict_producer()
        self.assertTrue(test_gen.get_generation() != [])

    def test_fit_set_test(self):
        self.assertTrue(test_chrom.get_fitvalue() != -1)

if __name__ == '__main__':
    unittest.main()