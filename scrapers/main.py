from scraper import WebScraper
from utils import save_csv
from env import settings
import os


def main():
    scraper = WebScraper(settings.BASE_URL)
    soup = scraper.get_html_soup(settings.BASE_URL)
    if not soup:
        print("Erro ao carregar a página inicial.")
        return

    opcoes = scraper.get_opcoes(soup, {"class": "btn_opt"})
    for key in settings.OPCOES_EXCLUIR:
        opcoes.pop(key, None)

    results = scraper.fetch_data(opcoes, settings.OPCOES_LIMITADAS)
    for value, table in results:
        filename = os.path.join(settings.OUTPUT_DIR, f"{value}.csv")
        save_csv(table, filename)
        print(f"Dados salvos em {filename}")


if __name__ == "__main__":
    main()
