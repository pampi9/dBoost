from collections import defaultdict

import pytest

from dboost.features import (
    descriptions,
    length,
    rule,
    rules,
    string_case,
    string_is_digit,
)


def test_fct__descriptions(expansion_rules):
    test_fct__descriptions.__test_type__ = "fct"
    assert descriptions(expansion_rules) == {
        str: [
            "upper case",
            "lower case",
            "title case",
            "is digit",
            "length",
            "signature",
            "strp",
            "simple email check",
            "email domain",
            "id",
            "empty",
        ],
        int: [
            "id",
            "nil",
            "tm_year",
            "tm_mon",
            "tm_mday",
            "tm_hour",
            "tm_min",
            "tm_sec",
            "tm_wday",
            "tm_yday",
            "is weekend",
            "bit 0",
            "bit 1",
            "bit 2",
            "bit 3",
            "bit 4",
            "bit 5",
            "div 3",
            "div 5",
            "mod 10",
        ],
        float: [
            "id",
            "tm_year",
            "tm_mon",
            "tm_mday",
            "tm_hour",
            "tm_min",
            "tm_sec",
            "tm_wday",
            "tm_yday",
            "frac part",
        ],
    }


@pytest.mark.parametrize(
    "test_rule",
    [
        length,
        string_case,
        string_is_digit,
    ],
)
def test_fct__rule__for_valid_rule(test_rule):
    test_fct__rule__for_valid_rule.__test_type__ = "fct"
    previous_rules = rules.copy()
    assert rule(test_rule) == test_rule
    next_rules = rules.copy()
    deleted_keys = []
    for key in previous_rules:
        if previous_rules[key] == next_rules[key]:
            deleted_keys.append(key)
    for key in deleted_keys:
        previous_rules.pop(key, None)
        next_rules.pop(key, None)
    assert previous_rules == defaultdict(list)
    assert next_rules == defaultdict(list)


def test_fct__rule__for_invalid_rule(unknow_rule, capsys):
    test_fct__rule__for_invalid_rule.__test_type__ = "fct"
    with pytest.raises(SystemExit):
        rule(unknow_rule["fct"])
    captured = capsys.readouterr()
    assert captured.err == f"Invalid rule {unknow_rule['name']}"
