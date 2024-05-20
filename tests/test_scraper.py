import os
import pytest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from pathlib import Path

from scrapers.utils import trata_html, flatten, save_csv
from scrapers.scraper import WebScraper
from scrapers.env import settings


@pytest.fixture
def mocked_html(filename):
    return b"<html><body>Mock Page</body></html>"


@pytest.fixture
def mocked_response(mocked_html):
    mock_response = MagicMock()
    mock_response.read.return_value = mocked_html
    return mock_response


@pytest.fixture
def mocked_urlopen(mocked_response):
    with patch("urllib.request.urlopen") as mock_urlopen:
        mock_urlopen.return_value = mocked_response
        yield mock_urlopen


def test_trata_html():
    html_input = b"<html> <body> Teste </body> </html>"
    expected_output = "<html><body> Teste </body></html>"
    assert trata_html(html_input) == expected_output


def test_flatten():
    nested_list = [[1, 2, 3], [4, 5], [6]]
    expected_output = [1, 2, 3, 4, 5, 6]
    assert flatten(nested_list) == expected_output


def test_save_csv(filename="./test.csv"):
    table = [{"col1": "data1", "col2": "data2"}]
    save_csv(table, filename)
    assert Path(filename).read_text() == "col1;col2\ndata1;data2\n"
    os.remove(filename)


def test_get_opcoes():
    html_content = "<button value='opt_01'>Option 1</button><button value='opt_02'>Option 2</button>"
    soup = BeautifulSoup(html_content, "html.parser")
    scraper = WebScraper(settings.BASE_URL)
    opcoes = scraper.get_opcoes(soup, {})
    expected_output = {"opt_01": "Option 1", "opt_02": "Option 2"}
    assert opcoes == expected_output


def test_get_periodo():
    html_content = "<label class='lbl_pesq'>Período: 2010 a 2020</label>"
    soup = BeautifulSoup(html_content, "html.parser")
    scraper = WebScraper(settings.BASE_URL)
    periodo = scraper.get_periodo(soup)
    expected_output = [2010, 2020]
    assert periodo == expected_output


def test_get_table():
    html_content = """
    <table class="tb_base tb_dados">
        <tr><th>Col1</th><th>Col2</th></tr>
        <tr><td>Data1</td><td>Data2</td></tr>
        <tr><td>Data3</td><td>Data4</td></tr>
    </table>
    """
    soup = BeautifulSoup(html_content, "html.parser")
    scraper = WebScraper(settings.BASE_URL)
    param = {"ano": 2020}
    table = scraper.get_table(soup, param)
    expected_output = [
        {"col1": "Data1", "col2": "Data2", "ano": 2020},
        {"col1": "Data3", "col2": "Data4", "ano": 2020},
    ]
    assert table == expected_output
