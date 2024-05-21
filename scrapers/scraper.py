from urllib.request import urlopen
from bs4 import BeautifulSoup
from utils import trata_html, flatten
import re


class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_html_soup(self, url):
        try:
            response = urlopen(url)
            html = response.read()
            html = trata_html(html)
            soup = BeautifulSoup(html, "html.parser")
            return soup
        except Exception as e:
            print(f"Erro ao obter HTML de {url}: {e}")
            return None

    def get_opcoes(self, soup, parameters):
        opcoes = {}
        btn_opt = soup.findAll("button", parameters)
        for btn in btn_opt:
            opcoes[btn.get("value")] = btn.getText()
        return opcoes

    def get_periodo(self, soup):
        try:
            periodo = soup.find("label", {"class": "lbl_pesq"}).getText()
            periodo = [int(x) for x in re.findall(r"\d+", periodo)]
            return periodo
        except AttributeError:
            print("Erro ao obter período.")
            return []

    def get_table(self, soup, param):
        try:
            table = soup.findAll("table", {"class": "tb_base tb_dados"})[0]
            rows = table.findAll("tr")
            header = rows[0].findAll("th")
            csv_rows = []
            for row in rows[1:]:  # Pulando o header
                csv_row = {}
                for idx, values in enumerate(row.findAll(["td", "th"])):
                    column_name = (
                        header[idx]
                        .get_text()
                        .split("(")[0]
                        .strip()
                        .lower()
                        .replace("sem definição", "sem_definicao")
                    )
                    csv_row[column_name] = values.get_text().strip()
                csv_rows.append({**csv_row, **param})
            return csv_rows
        except IndexError:
            print("Erro ao processar tabela.")
            return []

    def fetch_data(self, opcoes, opcao_limite=None):
        results = []
        for key, value in (opcao_limite or opcoes).items():
            tables = []
            url_opcao = f"?opcao={key}"
            _URL = self.base_url + url_opcao
            print(f"Acessando URL: {_URL}")
            soup = self.get_html_soup(_URL)
            if not soup:
                continue
            periodo = self.get_periodo(soup)
            if not periodo:
                continue
            sub_opcoes = self.get_opcoes(soup, {"class": "btn_sopt"})
            print(f"Opção: {value}, Período: {periodo}, Subopções: {sub_opcoes}")

            for ano in range(periodo[0], periodo[1] + 1):
                param = {"ano": ano}
                url_ano = f"&ano={ano}"

                if sub_opcoes:
                    for k, v in sub_opcoes.items():
                        param.update({"opcao": v})
                        url_subopcao = f"&subopcao={k}"
                        _URL = self.base_url + url_opcao + url_ano + url_subopcao
                        soup = self.get_html_soup(_URL)
                        if not soup:
                            continue
                        table = self.get_table(soup, param)
                        tables.append(table)
                        print(f"Acessando Subopção URL: {_URL}")
                else:
                    _URL = self.base_url + url_opcao + url_ano
                    soup = self.get_html_soup(_URL)
                    if not soup:
                        continue
                    table = self.get_table(soup, param)
                    tables.append(table)
                    print(f"Acessando Ano URL: {_URL}")

            results.append((value, flatten(tables)))
        return results
