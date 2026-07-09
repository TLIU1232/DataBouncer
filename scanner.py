import pandas as pd


def extract_headers(file):

    if file.endswith(".csv"):
        df = pd.read_csv(
            file,
            nrows=0
        )

    elif file.endswith(".xlsx"):
        df = pd.read_excel(
            file,
            nrows=0
        )

    else:
        raise Exception(
            "Unsupported file type"
        )

    return list(df.columns)