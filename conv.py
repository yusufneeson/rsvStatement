import tabula
import pandas as pd
from pypdf import PdfReader
import os
import argparse

def mandiriRSV(file):
    reader = PdfReader(file)
    number_of_pages = len(reader.pages) + 1
    
    area_first = (261.5, 19.9, 1000, 1000)
    columns_first = [150.9, 285.9, 420.9, 555.9, 690.9, 821.8]

    area_others = (53.5, 19.9, 1000, 1000)
    columns_others = [150.9, 285.9, 420.9, 555.9, 690.9, 821.8]

    df_first_list = tabula.read_pdf(
        file,
        pages=1,
        area=area_first,
        columns=columns_first,
        pandas_options={'header': None, "dtype": str},
        stream=True,
    )

    df_others_list = tabula.read_pdf(
        file,
        pages='2-'+str(number_of_pages-1),
        area=area_others,
        columns=columns_others,
        pandas_options={'header': None, "dtype": str},
        stream=True,
    )

    df_first = pd.concat(df_first_list) if isinstance(df_first_list, list) else df_first_list
    df_others = pd.concat(df_others_list) if isinstance(df_others_list, list) else df_others_list

    df = pd.concat([df_first, df_others], ignore_index=True)
    df['Grup'] = df[0].notna().cumsum()
    df[1] = df.groupby('Grup')[1].transform(lambda x: ' '.join(x.dropna()))

    df_cleaned = df[df[0].notna()]

    df_cleaned.reset_index(drop=True, inplace=True)

    df_cleaned.columns = ["Tanggal", "Keterangan", "Nomor Ref", "Debet", "Kredit", "Saldo", "Ignore"]

    df_cleaned.to_csv(file.replace('.pdf', '.csv'), index=False)

def bcaRSV(file):
    area_first = (250, 0, 1000, 1000)
    columns_first = [87, 300, 337, 464, 579]

    dfs = tabula.read_pdf(
        file,
        pages="all",
        area=area_first,
        columns=columns_first,
        pandas_options={'header': None, "dtype": str},
        stream=True,
    )

    df = pd.concat(dfs, ignore_index=True)
    df['Grup'] = df[0].notna().cumsum()

    df[1] = df.groupby('Grup')[1].transform(lambda x: ' '.join(x.dropna()))

    df_cleaned = df[df[0].notna()]

    df_cleaned.reset_index(drop=True, inplace=True)

    df_cleaned.columns = ["Tanggal", "Keterangan", "CBG", "Mutasi", "Saldo", "Ignore"]

    df_cleaned.to_csv(file.replace('.pdf', '.csv'), index=False)

def briRSV(file):
    reader = PdfReader(file)
    number_of_pages = len(reader.pages) + 1
    
    area_first = (345, 0, 1000, 1000)
    columns_first = [105.9, 291.9, 338.9, 446, 540.9, 690.9]

    area_others = (112.9, 0, 1000, 1000)
    columns_others = [105.9, 291.9, 338.9, 446, 540.9, 690.9]

    df_first_list = tabula.read_pdf(
        file,
        pages=1,
        area=area_first,
        columns=columns_first,
        pandas_options={'header': None, "dtype": str},
        stream=True,
    )

    df_others_list = tabula.read_pdf(
        file,
        pages='2-'+str(number_of_pages-1),
        area=area_others,
        columns=columns_others,
        pandas_options={'header': None, "dtype": str},
        stream=True,
    )

    df_first = pd.concat(df_first_list) if isinstance(df_first_list, list) else df_first_list
    df_others = pd.concat(df_others_list) if isinstance(df_others_list, list) else df_others_list

    df = pd.concat([df_first, df_others], ignore_index=True)
    df['Grup'] = df[0].notna().cumsum()
    df[1] = df.groupby('Grup')[1].transform(lambda x: ' '.join(x.dropna()))

    df_cleaned = df[df[0].notna()]

    df_cleaned.reset_index(drop=True, inplace=True)

    df_cleaned.columns = ["Tgl", "Uraian", "Teller", "Debet", "Kredit", "Saldo", "Ignore"]

    df_cleaned.to_csv(file.replace('.pdf', '.csv'), index=False)

def main():
    parser = argparse.ArgumentParser(description="YSRV Converter to CSV")
    parser.add_argument(
        "bank",
        type=str,
        choices=["BCA", "BRI", "Mandiri"],
        help="Pilih bank sumber mutasi"
    )
    parser.add_argument(
        "file_path",
        type=str,
        help="File yang akan di convert"
    )

    args = parser.parse_args()

    converters = {
        "BCA": bcaRSV,
        "BRI": briRSV,
        "Mandiri": mandiriRSV
    }

    if os.path.isfile(args.file_path):
        converters[args.bank](args.file_path)
    else:
        print(f"Error: File tidak ditemukan pada {args.file_path}")

if __name__ == "__main__":
    main()