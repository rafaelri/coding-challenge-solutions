from data_center_critical_conn import findCriticalConn
from hamcrest import *

def test_4_conns():
    assert_that(findCriticalConn(4,4, [[1, 2], [1, 3], [3, 2], [3, 4]]), equal_to([3,4]))