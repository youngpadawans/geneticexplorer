#/usr/env/bin python
# file **filename**.py
from __future__ import division

""" description
"""

__author__ = "FirstName LastName"
__copyright__ = "Copyright 2016, ArcherDX"
__credits__ = ["FirstName LastName"]
__maintainer__ = "FirstName LastName"
__email__ = "name@archerdx.com"

import unittest
from geneticexplorer.gene_analyzer import Gene


# Replace ModuleName with actual modules you're testing.
class TestModuleName(unittest.TestCase):
    """Tests for <ModuleName>.
    """

    def setUp(self):
        """Setup function for <ModuleName>Tests
        """
        pass

    def test_homo_polytrack(self):
        gene1 = Gene("AAA", 25, 23, 23, 23, 23, 23, 23, 23, 23)
        gene1.calculate_base_statistics()
        self.assertEqual(gene1.base_homo_mapping['A'], 3)

    def test_gene_constructor(self):
        """tests for <methodName>.
        """
        gene1 = Gene("AACAAACAAA", 25, 23, 23, 23, 23, 23, 23, 23, 23)
        gene1.calculate_base_statistics()
        self.assertEqual(gene1.base_homo_mapping['A'], 3, "Incorrect number of poly A tracks!")

    def tearDown(self):
        """Last test executed: cleans up all files initially created"""
        # remove the tempdir and contents
        pass

# Put test data here.  Instead of a file for testing, use TEST_INPUT_DATA
# as a multiline string and put in a temporary file if testing a function
# that takes a file as input.
# TEST_INPUT_DATA = """"""

#run if called from command-line
if __name__ == "__main__":
    unittest.main()
