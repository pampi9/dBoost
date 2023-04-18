import pytest


@pytest.fixture
def stats_stream_numerical():
    yield [
        [
            {"sum": 1, "sum2": 1, "min": False, "max": True, "count": 14, "elems": {False, True}, "avg": 0.07142857142857142, "sigma": 0.25753937681885636, "card": 2},
            {"sum": 0, "sum2": 0, "min": False, "max": False, "count": 14, "elems": {False}, "avg": 0.0, "sigma": 0.0, "card": 1},
            {"sum": 0, "sum2": 0, "min": False, "max": False, "count": 14, "elems": {False}, "avg": 0.0, "sigma": 0.0, "card": 1},
            {"sum": 0, "sum2": 0, "min": False, "max": False, "count": 14, "elems": {False}, "avg": 0.0, "sigma": 0.0, "card": 1},
            {"sum": 94, "sum2": 646, "min": 3, "max": 7, "count": 14, "elems": {3, 7}, "avg": 6.714285714285714, "sigma": 1.0301575072754257, "card": 2},
            {"sum": 0, "sum2": 0, "min": False, "max": False, "count": 14, "elems": {False}, "avg": 0.0, "sigma": 0.0, "card": 1},
            {"sum": 0, "sum2": 0, "min": False, "max": False, "count": 14, "elems": {False}, "avg": 0.0, "sigma": 0.0, "card": 1}
        ], [
            {"sum": 20712504558, "sum2": 33000603074622970148, "min": 123, "max": 1593271588, "count": 14, "elems": {1593268448, 1593271588, 1593271461, 1593269669, 1593269708, 1593268492, 1593269166, 1593270896, 1593269744, 1593268528, 1593268409, 1593269818, 123, 1593268508}, "avg": 1479464611.2857144, "sigma": 410329620.9815358, "card": 14},
            {"sum": 28230, "sum2": 56926100, "min": 1970, "max": 2020, "count": 14, "elems": {1970, 2020}, "avg": 2016.4285714285713, "sigma": 12.876968840962377, "card": 2},
            {"sum": 79, "sum2": 469, "min": 1, "max": 6, "count": 14, "elems": {1, 6}, "avg": 5.642857142857143, "sigma": 1.2876968840942804, "card": 2},
            {"sum": 352, "sum2": 9478, "min": 1, "max": 27, "count": 14, "elems": {1, 27}, "avg": 25.142857142857142, "sigma": 6.696023797290269, "card": 2},
            {"sum": 185, "sum2": 2635, "min": 0, "max": 15, "count": 14, "elems": {0, 14, 15}, "avg": 13.214285714285714, "sigma": 3.6874027140400925, "card": 3},
            {"sum": 503, "sum2": 21521, "min": 2, "max": 56, "count": 14, "elems": {33, 2, 26, 35, 34, 14, 46, 54, 55, 24, 56}, "avg": 35.92857142857143, "sigma": 15.695605780482845, "card": 11},
            {"sum": 378, "sum2": 15068, "min": 3, "max": 58, "count": 14, "elems": {3, 6, 8, 44, 52, 21, 56, 58, 28, 29}, "avg": 27.0, "sigma": 18.63560340546327, "card": 10},
            {"sum": 68, "sum2": 334, "min": 3, "max": 5, "count": 14, "elems": {3, 5}, "avg": 4.857142857142857, "sigma": 0.5150787536377163, "card": 2},
            {"sum": 2328, "sum2": 416534, "min": 1, "max": 179, "count": 14, "elems": {1, 179}, "avg": 166.28571428571428, "sigma": 45.84200907375649, "card": 2},
            {"sum": 13, "sum2": 13, "min": False, "max": True, "count": 14, "elems": {False, True}, "avg": 0.9285714285714286, "sigma": 0.2575393768188564, "card": 2},
            {"sum": 4, "sum2": 4, "min": 0, "max": 1, "count": 14, "elems": {0, 1}, "avg": 0.2857142857142857, "sigma": 0.45175395145262565, "card": 2},
            {"sum": 3, "sum2": 3, "min": 0, "max": 1, "count": 14, "elems": {0, 1}, "avg": 0.21428571428571427, "sigma": 0.41032590332414487, "card": 2},
            {"sum": 7, "sum2": 7, "min": 0, "max": 1, "count": 14, "elems": {0, 1}, "avg": 0.5, "sigma": 0.5, "card": 2},
            {"sum": 7, "sum2": 7, "min": 0, "max": 1, "count": 14, "elems": {0, 1}, "avg": 0.5, "sigma": 0.5, "card": 2},
            {"sum": 7, "sum2": 7, "min": 0, "max": 1, "count": 14, "elems": {0, 1}, "avg": 0.5, "sigma": 0.5, "card": 2},
            {"sum": 11, "sum2": 11, "min": 0, "max": 1, "count": 14, "elems": {0, 1}, "avg": 0.7857142857142857, "sigma": 0.4103259033241449, "card": 2},
            {"sum": 3, "sum2": 3, "min": False, "max": True, "count": 14, "elems": {False, True}, "avg": 0.21428571428571427, "sigma": 0.41032590332414487, "card": 2},
            {"sum": 0, "sum2": 0, "min": False, "max": False, "count": 14, "elems": {False}, "avg": 0.0, "sigma": 0.0, "card": 1},
            {"sum": 88, "sum2": 648, "min": 1, "max": 9, "count": 14, "elems": {1, 2, 3, 4, 6, 8, 9}, "avg": 6.285714285714286, "sigma": 2.6029810226126573, "card": 7}
        ]
    ]


@pytest.fixture
def data_stream_numerical():
    yield [
        (
            (True, False, False, False, 3, False, False),
            (123, 1970, 1, 1, 0, 2, 3, 3, 1, False, 1, 1, 0, 1, 1, 1, True, False, 3)
        ),
        (
            (False, False, False, False, 7, False, False),
            (1593270896, 2020, 6, 27, 15, 14, 56, 5, 179, True, 0, 0, 0, 0, 1, 1, False, False, 6)
        ),
        (
            (False, False, False, False, 7, False, False),
            (1593271461, 2020, 6, 27, 15, 24, 21, 5, 179, True, 1, 0, 1, 0, 0, 1, True, False, 1)
        ),
        (
            (False, False, False, False, 7, False, False),
            (1593269744, 2020, 6, 27, 14, 55, 44, 5, 179, True, 0, 0, 0, 0, 1, 1, False, False, 4)
        ),
        (
            (False, False, False, False, 7, False, False),
            (1593269818, 2020, 6, 27, 14, 56, 58, 5, 179, True, 0, 1, 0, 1, 1, 1, False, False, 8)
        ),
        (
            (False, False, False, False, 7, False, False),
            (1593269669, 2020, 6, 27, 14, 54, 29, 5, 179, True, 1, 0, 1, 0, 0, 1, False, False, 9)
        ),
        (
            (False, False, False, False, 7, False, False),
            (1593271588, 2020, 6, 27, 15, 26, 28, 5, 179, True, 0, 0, 1, 0, 0, 1, False, False, 8)
        ),
        (
            (False, False, False, False, 7, False, False),
            (1593269166, 2020, 6, 27, 14, 46, 6, 5, 179, True, 0, 1, 1, 1, 0, 1, True, False, 6)
        ),
        (
            (False, False, False, False, 7, False, False),
            (1593269708, 2020, 6, 27, 14, 55, 8, 5, 179, True, 0, 0, 1, 1, 0, 0, False, False, 8)
        ),
        (
            (False, False, False, False, 7, False, False),
            (1593268409, 2020, 6, 27, 14, 33, 29, 5, 179, True, 1, 0, 0, 1, 1, 1, False, False, 9)
        ),
        (
            (False, False, False, False, 7, False, False),
            (1593268528, 2020, 6, 27, 14, 35, 28, 5, 179, True, 0, 0, 0, 0, 1, 1, False, False, 8)
        ),
        (
            (False, False, False, False, 7, False, False),
            (1593268492, 2020, 6, 27, 14, 34, 52, 5, 179, True, 0, 0, 1, 1, 0, 0, False, False, 2)
        ),
        (
            (False, False, False, False, 7, False, False),
            (1593268448, 2020, 6, 27, 14, 34, 8, 5, 179, True, 0, 0, 0, 0, 0, 1, False, False, 8)
        ),
        (
            (False, False, False, False, 7, False, False),
            (1593268508, 2020, 6, 27, 14, 35, 8, 5, 179, True, 0, 0, 1, 1, 1, 0, False, False, 8)
        )
    ]


@pytest.fixture
def data_stream_categorical():
    yield [
        (
            ('Lu,Lu,Lu', 'ABC', 'NONE', 'ABC', None)
        ),
        (
            ('Nd,Nd,Nd,Nd,Pd,Nd,Nd', '<num>-<num>', 'NONE', '2020-06', None),
        ),
        (
            ('Nd,Nd,Nd,Nd,Pd,Nd,Nd', '<num>-<num>', 'NONE', '2020-06', None),
        ),
        (
            ('Nd,Nd,Nd,Nd,Pd,Nd,Nd', '<num>-<num>', 'NONE', '2020-06', None),
        ),
        (
            ('Nd,Nd,Nd,Nd,Pd,Nd,Nd', '<num>-<num>', 'NONE', '2020-06', None),
        ),
        (
            ('Nd,Nd,Nd,Nd,Pd,Nd,Nd', '<num>-<num>', 'NONE', '2020-06', None),
        ),
        (
            ('Nd,Nd,Nd,Nd,Pd,Nd,Nd', '<num>-<num>', 'NONE', '2020-06', None),
        ),
        (
            ('Nd,Nd,Nd,Nd,Pd,Nd,Nd', '<num>-<num>', 'NONE', '2020-06', None),
        ),
        (
            ('Nd,Nd,Nd,Nd,Pd,Nd,Nd', '<num>-<num>', 'NONE', '2020-06', None),
        ),
        (
            ('Nd,Nd,Nd,Nd,Pd,Nd,Nd', '<num>-<num>', 'NONE', '2020-06', None),
        ),
        (
            ('Nd,Nd,Nd,Nd,Pd,Nd,Nd', '<num>-<num>', 'NONE', '2020-06', None),
        ),
        (
            ('Nd,Nd,Nd,Nd,Pd,Nd,Nd', '<num>-<num>', 'NONE', '2020-06', None),
        ),
        (
            ('Nd,Nd,Nd,Nd,Pd,Nd,Nd', '<num>-<num>', 'NONE', '2020-06', None),
        ),
        (
            ('Nd,Nd,Nd,Nd,Pd,Nd,Nd', '<num>-<num>', 'NONE', '2020-06', None),
        )
    ]
