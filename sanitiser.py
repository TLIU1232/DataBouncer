import pandas as pd
import os


def generate_placeholder(column, index, dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return index
    elif pd.api.types.is_float_dtype(dtype):
        return float(index)
    else:
        return f"{column.upper()}_{index}"

def anonymise_column(series, column):
    mapping = {}
    counter = 1

    dtype = series.dtype

    def replace(value):
        nonlocal counter
        if pd.isna(value):
            return value
        if value not in mapping:
            mapping[value] = generate_placeholder(
                column,
                counter,
                dtype)
            counter += 1
        return mapping[value]
    return series.apply(replace)



def anonymise(
        input_file,
        sensitive_columns,
        output_file=None
):
    extension = os.path.splitext(
        input_file
    )[1].lower()
    # Load file
    if extension == ".csv":
        df = pd.read_csv(
            input_file
        )
    elif extension == ".xlsx":
        df = pd.read_excel(
            input_file
        )
    else:
        raise ValueError(
            "Expecting .csv or .xlsx"
        )
    for column in sensitive_columns:
        if column in df.columns:
            df[column] = anonymise_column(df[column],column)

    if output_file is None:
        filename = os.path.splitext(
            input_file
        )[0]
        output_file = (filename + "_SAFE" + extension)

    if extension == ".csv":
        df.to_csv(output_file,index=False)
    else:
        df.to_excel(output_file,index=False)
    return output_file