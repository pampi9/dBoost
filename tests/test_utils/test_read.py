import pytest

from dboost.utils.read import parse_line_blind, stream_tuples


@pytest.mark.parametrize(
    ("row", "floats_only", "expected_response"),
    [
        (["ABC", "123", "1.12"], True, ("ABC", 123.0, 1.12)),
        (["ABC", "123", "1.12"], False, ("ABC", 123, 1.12)),
    ],
)
def test_fct__parse_line_blind(row, floats_only, expected_response):
    test_fct__parse_line_blind.__test_type__ = "fct"
    assert parse_line_blind(row=row, floats_only=floats_only) == expected_response
    for index in range(0, len(expected_response)):
        assert isinstance(
            parse_line_blind(row=row, floats_only=floats_only)[index],
            type(expected_response[index]),
        )


@pytest.mark.parametrize(
    (
        "csv_input",
        "separator",
        "floats_only",
        "maxrecords",
        "expected_output",
        "expected_types",
    ),
    [
        (
            ["ABC\t123\t120.2", "ABC\t123\t120.2", "DEF\t123\t120.2"],
            "\t",
            True,
            2,
            [("ABC", 123.0, 120.2), ("DEF", 123.0, 120.2)],
            (str, float, float),
        ),
        (
            ["ABC\t123\t120.2", "ABC\t123\t120.2", "DEF\t123\t120.2"],
            "\t",
            True,
            1,
            [("ABC", 123.0, 120.2)],
            (str, float, float),
        ),
        (
            ["ABC 123 120.2", "ABC 123 120.2"],
            " ",
            True,
            1,
            [("ABC", 123.0, 120.2)],
            (str, float, float),
        ),
        (
            ["ABC 123 120.2", "ABC 123 120.2"],
            " ",
            False,
            1,
            [("ABC", 123.0, 120.2)],
            (str, int, float),
        ),
    ],
)
def test_fct__stream_tuples(
    csv_input, separator, floats_only, maxrecords, expected_output, expected_types
):
    test_fct__stream_tuples.__test_type__ = "fct"
    stream = stream_tuples(
        input=csv_input,
        fs=separator,
        floats_only=floats_only,
        preload=True,
        maxrecords=maxrecords,
    )
    assert stream() == expected_output
    for item in stream():
        for index in range(0, len(item)):
            assert isinstance(item[index], expected_types[index])
