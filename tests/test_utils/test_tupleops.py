import pytest

from dboost.utils.tupleops import (
    zeroif,
    extract_types,
    types_consistent,
    defaultif,
    defaultif_masked,
    make_mask_abc,
    deepmap,
    id,
    sqr,
    not_null,
    keep_if,
    plus,
    minus,
    mul,
    div0,
    incrkey,
    tuplify,
    flatten,
)


@pytest.fixture
def test_X():
    yield [["ABC", 123, 3.1415], ["DEFG", 123, 3.1415]]


@pytest.fixture
def test_tuple_X():
    yield ("ABC", 123, 3.1415), ("DEFG", 123, 3.1415)


@pytest.fixture
def test_abc():
    yield str, int, float


@pytest.fixture
def test_mask():
    yield (True, False, True), (True, False, True)


@pytest.mark.parametrize(
    ("S", "expected_output"),
    [
        (None, ((0, 0, 0), (0, 0, 0))),
        (((1, 2, 3), (4, 5, 6), (7, 8, 9)), ((1, 2, 3), (4, 5, 6), (7, 8, 9)))
    ],
)
def test_fct__zeroif(S, test_X, expected_output):
    test_fct__zeroif.__test_type__ = "fct"
    assert zeroif(S=S, X=test_X) == expected_output


def test_fct__extract_types(test_X, test_abc):
    test_fct__extract_types.__test_type__ = "fct"
    assert extract_types(X=test_X) == (test_abc, test_abc)


def test_fct__types_consistent(test_X, test_abc):
    test_fct__types_consistent.__test_type__ = "fct"
    assert types_consistent((test_abc, test_abc), test_X)


def test_fct__make_mask_abc(test_X, test_abc):
    assert make_mask_abc(X=test_X, abc=test_abc) == ((True, True, True), (True, True, True))


def test_fct__deepmap(test_X, test_tuple_X):
    def fct(x):
        return x

    assert deepmap(fct, test_X) == test_tuple_X

@pytest.mark.parametrize(
    ("S", "default_value", "expected_output"),
    [
        (None, "default1", (("default1", "default1", "default1"), ("default1", "default1", "default1"))),
        (((1, 2, 3), (4, 5, 6), (7, 8, 9)), "default2", ((1, 2, 3), (4, 5, 6), (7, 8, 9)))
    ],
)
def test_fct__defaultif(S, expected_output, default_value, test_X):
    test_fct__defaultif.__test_type__ = "fct"

    def default():
        return default_value

    assert defaultif(S=S, X=test_X, default=default) == expected_output


@pytest.mark.parametrize(
    ("S", "default_value", "expected_output"),
    [
        (None, "default1", (("default1", None, "default1"), ("default1", None, "default1"))),
        (((1, 2, 3), (4, 5, 6), (7, 8, 9)), "default2", ((1, 2, 3), (4, 5, 6), (7, 8, 9)))
    ],
)
def test_fct__defaultif_masked(S, expected_output, default_value, test_X, test_mask):
    test_fct__defaultif_masked.__test_type__ = "fct"

    def default():
        return default_value

    assert defaultif_masked(S=S, X=test_X, default=default, mask=test_mask) == expected_output


class TestValueTransformation:
    @pytest.mark.parametrize(
        ("argument", "expected_output"),
        [(1, 1), ("A", "A"), (None, None)]
    )
    def test_fct__id(self, argument, expected_output):
        TestValueTransformation.test_fct__id.__test_type__ = "fct"
        assert id(argument) == expected_output

    @pytest.mark.parametrize(
        ("argument", "expected_output"),
        [(2, 4), (None, None)]
    )
    def test_fct__sqr(self, argument, expected_output):
        TestValueTransformation.test_fct__sqr.__test_type__ = "fct"
        assert sqr(argument) == expected_output

    @pytest.mark.parametrize(
        ("argument", "expected_output"),
        [(2, True), ("A", True), (None, False)]
    )
    def test_fct__not_null(self, argument, expected_output):
        TestValueTransformation.test_fct__not_null.__test_type__ = "fct"
        assert not_null(argument) == expected_output

    @pytest.mark.parametrize(
        ("argument1", "argument2", "expected_output"),
        [(2, True, 2), (2, False, None), ("A", True, "A"), ("A", False, None)]
    )
    def test_fct__keep_if(self, argument1, argument2, expected_output):
        TestValueTransformation.test_fct__keep_if.__test_type__ = "fct"
        assert keep_if(argument1, argument2) == expected_output

    @pytest.mark.parametrize(
        ("argument1", "argument2", "expected_output"),
        [(2, 3, 5), (2, None, 2), ("A", "B", "AB"), ("A", None, "A")]
    )
    def test_fct__plus(self, argument1, argument2, expected_output):
        TestValueTransformation.test_fct__plus.__test_type__ = "fct"
        assert plus(argument1, argument2) == expected_output

    @pytest.mark.parametrize(
        ("argument1", "argument2", "expected_output"),
        [(2, 3, -1), (2, None, 2)]
    )
    def test_fct__minus(self, argument1, argument2, expected_output):
        TestValueTransformation.test_fct__minus.__test_type__ = "fct"
        assert minus(argument1, argument2) == expected_output

    @pytest.mark.parametrize(
        ("argument1", "argument2", "expected_output"),
        [(2, 3, 6), (2, None, 2)]
    )
    def test_fct__mul(self, argument1, argument2, expected_output):
        TestValueTransformation.test_fct__mul.__test_type__ = "fct"
        assert mul(argument1, argument2) == expected_output

    @pytest.mark.parametrize(
        ("argument1", "argument2", "expected_output"),
        [(6, 3, 2), (None, 3, 0), (6, 0, 0)]
    )
    def test_fct__div0(self, argument1, argument2, expected_output):
        TestValueTransformation.test_fct__div0.__test_type__ = "fct"
        assert div0(argument1, argument2) == expected_output

    @pytest.mark.parametrize(
        ("argument1", "argument2", "expected_output"),
        [
            ([1, 2, 3], 0, [2, 2, 3]),
            ([1, 2, 3], 1, [1, 3, 3]),
            ([1, 2, 3], 2, [1, 2, 4]),
            (None, 1, None),
        ]
    )
    def test_fct__incrkey(self, argument1, argument2, expected_output):
        TestValueTransformation.test_fct__incrkey.__test_type__ = "fct"
        assert incrkey(argument1, argument2) == expected_output

    @pytest.mark.parametrize(
        ("argument1", "argument2", "expected_output"),
        [(6, 3, (6, 3)), (None, 3, (None, 3)), (6, 0, (6, 0))]
    )
    def test_fct__tuplify(self, argument1, argument2, expected_output):
        TestValueTransformation.test_fct__tuplify.__test_type__ = "fct"
        assert tuplify(argument1, argument2) == expected_output

    @pytest.mark.parametrize(
        ("argument", "expected_output"),
        [(("ABC", "DEF"), ["A", "B", "C", "D", "E", "F"])]
    )
    def test_fct__flatten(self, argument, expected_output):
        TestValueTransformation.test_fct__flatten.__test_type__ = "fct"
        assert flatten(argument) == expected_output
