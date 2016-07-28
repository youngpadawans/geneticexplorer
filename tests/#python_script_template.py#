#!/usr/env/bin python
# file **filename**.py
from __future__ import division

""" description
"""

__author__ = "FirstName LastName"
__copyright__ = "Copyright 2016, ArcherDX"
__credits__ = ["FirstName LastName"]
__maintainer__ = "FirstName LastName"
__email__ = "name@domain.com"

from sys import argv
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

def workflow():
    """description of workflow
    
    :param <parameter_type> <parameter_name>: <parameter description>
    :returns : <what function returns>
    """
    raise NotImplementedError

def parseCmdlineParams(arg_list=argv):
    """Parses commandline arguments.
    
    :param list arg_list: Arguments to parse. Default is argv when called from the
    command-line.
    """
    #Create instance of ArgumentParser
    options_parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    #Script arguments.  Use:
    # options_parser.add_argument('--argument',help='help string')
    
    #Parse options
    opts, unknown = options_parser.parse_known_args(args=arg_list)
    
    return opts

def main(args,args_parsed=None):
    
    #If parsed arguments is passed in, do not parse command-line arguments
    if args_parsed is not None:
        opts = args_parsed
    #Else, parse arguments from command-line
    else:
        opts = parseCmdlineParams(args)

    #Call workflow for script after parsing command line parameters.
    workflow()

if __name__ == "__main__":
    main(argv)
