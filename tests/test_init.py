import pytest

from dboost import expand_field, expand, expand_hints, expand_stream
from dboost.utils.read import stream_tuples


@pytest.mark.parametrize(
    ("field", "field_expanded"),
    [
        (
            "value",
            (
                False,
                True,
                False,
                False,
                5,
                "Ll,Ll,Ll,Ll,Ll",
                "value",
                False,
                "NONE",
                "value",
                False,
            ),
        ),
        (
            "Velocity, Variety, Volume! 4BigData?",
            (
                False,
                False,
                False,
                False,
                36,
                "Lu,Ll,Ll,Ll,Ll,Ll,Ll,Ll,Po,Zs,Lu,Ll,Ll,Ll,Ll,Ll,Ll,Po,Zs,Lu,Ll,Ll,Ll,Ll,Ll,Po,Zs,Nd,Lu,Ll,Ll,Lu,Ll,Ll,Ll,Po",
                "Velocity, Variety, Volume! <num>BigData?",
                False,
                "NONE",
                "Velocity, Variety, Volume! 4BigData?",
                False,
            ),
        ),
        (
            "name@domain.com",
            (
                False,
                True,
                False,
                False,
                15,
                "Ll,Ll,Ll,Ll,Po,Ll,Ll,Ll,Ll,Ll,Ll,Po,Ll,Ll,Ll",
                "name@domain.com",
                True,
                "com",
                "name@domain.com",
                False,
            ),
        ),
        (
            "2022-12",
            (
                False,
                False,
                False,
                False,
                7,
                "Nd,Nd,Nd,Nd,Pd,Nd,Nd",
                "<num>-<num>",
                False,
                "NONE",
                "2022-12",
                False,
            ),
        ),
        (
            1680876276,
            (
                1680876276,
                None,
                2023,
                4,
                7,
                14,
                4,
                36,
                4,
                97,
                False,
                0,
                0,
                1,
                0,
                1,
                1,
                True,
                False,
                6,
            ),
        ),
        (3.1415, (3.1415, 1970, 1, 1, 0, 0, 3, 3, 1, 0.14150000000000018)),
    ],
)
def test_fct__expand_field(field, field_expanded, expansion_rules):
    test_fct__expand_field.__test_type__ = "fct"
    assert expand_field(field, expansion_rules) == field_expanded


def test_fct__expand(expansion_rules):
    assert expand(["Test", "my value,01", 123], expansion_rules) == (
        (
            False,
            False,
            True,
            False,
            4,
            "Lu,Ll,Ll,Ll",
            "Test",
            False,
            "NONE",
            "Test",
            False,
        ),
        (
            False,
            True,
            False,
            False,
            11,
            "Ll,Ll,Zs,Ll,Ll,Ll,Ll,Ll,Po,Nd,Nd",
            "my value,<num>",
            False,
            "NONE",
            "my value,01",
            False,
        ),
        (123, None, 1970, 1, 1, 0, 2, 3, 3, 1, False, 1, 1, 0, 1, 1, 1, True, False, 3),
    )


def test_fct__expand_hints():
    assert expand_hints((("ABC", "DEF"), (123, 456)), hints=[((0, 0), (1, 0))]) == (
        (("ABC", 123),),
        ("ABC", "DEF"),
        (123, 456),
    )


@pytest.mark.parametrize(
    ("csv_input", "separator", "floats_only", "maxrecords", "hints", "expected_output"),
    [
        (
            ["ABC\t123\t120.2", "ABC\t123\t120.2", "DEF\t123\t120.2"],
            "\t",
            True,
            1,
            [((0, 0), (1, 0))],
            [
                (
                    ("ABC", 123.0, 120.2),
                    (
                        ((True, 123.0),),
                        (
                            True,
                            False,
                            False,
                            False,
                            3,
                            "Lu,Lu,Lu",
                            "ABC",
                            False,
                            "NONE",
                            "ABC",
                            False,
                        ),
                        (123.0, 1970, 1, 1, 0, 2, 3, 3, 1, 0.0),
                        (120.2, 1970, 1, 1, 0, 2, 0, 3, 1, 0.20000000000000284),
                    ),
                ),
            ],
        ),
        (
            ["ABC\t123\t120.2", "ABC\t123\t120.2", "DEF\t123\t120.2"],
            "\t",
            True,
            1,
            None,
            [
                (
                    (
                        True,
                        False,
                        False,
                        False,
                        3,
                        "Lu,Lu,Lu",
                        "ABC",
                        False,
                        "NONE",
                        "ABC",
                        False,
                    ),
                    (123.0, 1970, 1, 1, 0, 2, 3, 3, 1, 0.0),
                    (120.2, 1970, 1, 1, 0, 2, 0, 3, 1, 0.20000000000000284),
                )
            ],
        ),
    ],
)
def test_fct__expand_stream(
    expansion_rules,
    csv_input,
    separator,
    floats_only,
    maxrecords,
    hints,
    expected_output,
):
    stream = stream_tuples(
        input=csv_input,
        fs=separator,
        floats_only=floats_only,
        preload=True,
        maxrecords=maxrecords,
    )
    expanded_stream = expand_stream(
        generator=stream,
        rules=expansion_rules,
        keep_x=True,
        hints=hints,
        maxrecords=maxrecords,
    )
    assert len(list(expanded_stream)) == len(expected_output)
    for key, item in enumerate(expanded_stream):
        print(item)
        assert item == expected_output[key]
