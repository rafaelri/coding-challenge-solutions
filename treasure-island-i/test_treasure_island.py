from hamcrest import *
from treasure_island import treasure_path

def test_sample():
    m = [ \
            ['O', 'O', 'O', 'O'], \
            ['D', 'O', 'D', 'O'], \
            ['O', 'O', 'O', 'O'], \
            ['X', 'D', 'D', 'O'], \
        ]
    assert_that(treasure_path(m), equal_to([ (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) ]))