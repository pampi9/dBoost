import pathlib
import sys

import pytest
from py.xml import html

sys.path.append(str(pathlib.Path(__file__).parents[2]))

from dboost.features import rules


@pytest.fixture
def expansion_rules():
    yield {t: [r for r in rs] for t, rs in rules.items()}


def pytest_html_report_title(report):
    report.title = "Pytest report for dboost"


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th("Test type"))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.test_type))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.test_type = (
        item.function.__test_type__
        if hasattr(item.function, "__test_type__")
        else "..."
    )
