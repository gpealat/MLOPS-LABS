#import sys
#sys.path += ['../src']

from unit_testing_best_practices.src import sample

def test_answer():
    assert sample.func(3) == 4

    #test comment ff