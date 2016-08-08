#/usr/env/bin python
# file **filename**.py
from __future__ import division

""" description
"""

__author__ = "Kaixin Cui"
__copyright__ = "Copyright 2016, ArcherDX"
__credits__ = ["Kaixin Cui"]
__maintainer__ = "Kaixin Cui"
__email__ = "kcui@archerdx.com"

import unittest
from gene_clusters.geneticexplorer.gene_analyzer.py import Gene


class TestModuleName(unittest.TestCase):
    """Tests for <ModuleName>.
    """

    def setUp(self):
        """Setup function for <ModuleName>Tests
        """
        pass

    def test_homoa_polytrack(self):
        gene1 = Gene("aaaCCCAAA", 25, 23, 23, 23, 23, 23, 23, 23, 23)
        gene1.get_TrackLength_a()
        self.assertEqual(gene1.base_a_list, [3, 3])
        pass

    def test_homoc_polytrack(self):
        gene1 = Gene("AACCCAACCC", 25, 23, 23, 23, 23, 23, 23, 23, 23)
        gene1.get_TrackLength_c()
        self.assertEqual(gene1.base_c_list, [3, 3])
        print gene1.base_c_track

    def test_tracklength_average(self):
        gene1 = Gene("AATTAAGGCC", 25, 23, 23, 23, 23, 23, 23, 23, 23)
        gene1.get_Track_average()
        print gene1.total_base_list

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
