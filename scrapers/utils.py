import os
import pandas as pd

def trata_html(imput):
    try:
        imput = imput.decode("utf-8")
    except AttributeError:
        return ""
    return " ".join(imput.split()).replace("> <", "><")

def flatten(xss):
    return [x for xs in xss for x in xs]

def save_csv(table, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df = pd.DataFrame(table).fillna('-')
    df.to_csv(filename, index=False, sep=";")
