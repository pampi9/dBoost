import pytest

from dboost import expand_field


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
    print(expand_field(field, expansion_rules))
    assert expand_field(field, expansion_rules) == field_expanded
