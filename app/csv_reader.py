import pandas as pd

class CSVReader:
    @staticmethod
    def ler_csv(filename):
        df = pd.read_csv(filename, sep=";")
        return df.to_dict(orient="records")
