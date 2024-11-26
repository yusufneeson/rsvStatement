import tabula
import pandas as pd
import numpy as np
from pypdf import PdfReader
import os
import argparse
import re

# pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

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

def mandiriEstatementPass(file, password):
    reader = PdfReader(file, password=password)
    number_of_pages = len(reader.pages) + 1
    
    area_first = (323.6, 43.9, 799, 1000)
    columns_first = [114.9, 321.9, 440.8, 590.9]

    area_others = (207.9, 43.9, 799, 1000)
    columns_others = [114.9, 321.9, 440.8, 590.9]

    df_first_list = tabula.read_pdf(
        file,
        password=password,
        pages=1,
        area=area_first,
        columns=columns_first,
        pandas_options={'header': None, "dtype": str},
        stream=True,
    )

    df_others_list = tabula.read_pdf(
        file,
        password=password,
        pages='2-'+str(number_of_pages-1),
        area=area_others,
        columns=columns_others,
        pandas_options={'header': None, "dtype": str},
        stream=True,
    )

    df_first = pd.concat(df_first_list) if isinstance(df_first_list, list) else df_first_list
    df_others = pd.concat(df_others_list) if isinstance(df_others_list, list) else df_others_list

    df = pd.concat([df_first, df_others], ignore_index=True)
    df = df[df[0].apply(lambda x: is_date_format(x) or is_time(x) or pd.isna(x))]
    df = df[df[1].apply(lambda x: not is_batas_akhir(x))]
    
    new_rows = {}
    index = 0
    bertemu_tgl = 0
    bertemu_tf = 0
    ketemu_index_unik = 0


    df["Grp"] = 0
    # df["Tngl"] = 0
    # df["TF"] = 0

    for i, row in df.iterrows():
        if i > 1 and is_date_format(row[0]):
            bertemu_tgl += 1

        if "Transfer" in str(row[1]) or "Biaya" in str(row[1]):
            if i > 1:
                if index > bertemu_tf:
                    index = bertemu_tf
                else:
                    index += 1
                bertemu_tf += 1

        if bertemu_tgl > index:
            index = bertemu_tgl
            ketemu_index_unik = bertemu_tgl

        df.at[i, "Grp"] = index
        
    df.columns = ["Tanggal", "Keterangan", "Nominal", "Saldo", "Grp"]

    df = df.replace('NaN', np.nan)
    df = df.fillna("")

    result = df.groupby("Grp").agg({
        "Tanggal": lambda x: " ".join(map(str, x)).strip(),
        "Keterangan": lambda x: " ".join(map(str, x)).strip(),
        "Nominal": lambda x: " ".join(map(str, x)).strip(),
        "Saldo": lambda x: " ".join(map(str, x)).strip(),
    }).reset_index(drop=True)
    
    result.to_csv(file.replace('.pdf', '.csv'), index=False)


# Fungsi untuk mendeteksi apakah awal baris baru
def is_new_row(value):
    if pd.isna(value):
        return False
    return bool(re.match(r"^(Biaya|Transfer)", value))

# Fungsi untuk memeriksa apakah nilai adalah waktu
def is_time(value):
    if pd.isna(value):
        return False
    return bool(re.match(r"^\d{2}:\d{2}:\d{2} WIB$", value))

def is_date_format(string):
    if pd.isna(string):
        return False
    return bool(re.match(r"^\d{2} \w{3} \d{4}$", str(string)))

def is_batas_akhir(value):
    if isinstance(value, str):
        return bool(re.search(r'ini\s+adalah\s+batas\s+akhir', value.lower()))
    return False

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
    columns_first = [69.5, 105.9, 291.9, 338.9, 446, 540.9, 690.9]

    area_others = (112.9, 0, 1000, 1000)
    columns_others = [69.5, 105.9, 291.9, 338.9, 446, 540.9, 690.9]

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

    df_cleaned.columns = ["Tgl", "Jam", "Uraian", "Teller", "Debet", "Kredit", "Saldo", "Ignore"]

    df_cleaned.to_csv(file.replace('.pdf', '.csv'), index=False)

def main():
    parser = argparse.ArgumentParser(description="YSRV Converter to CSV")
    parser.add_argument(
        "bank",
        type=str,
        choices=["BCA", "BRI", "Mandiri", "MandiriPasswd"],
        help="Pilih bank sumber mutasi"
    )
    parser.add_argument(
        "file_path",
        type=str,
        help="File yang akan di convert"
    )
    parser.add_argument(
        "paswd",
        type=str,
        help="Password"
    )

    args = parser.parse_args()

    converters = {
        "BCA": bcaRSV,
        "BRI": briRSV,
        "Mandiri": mandiriRSV,
        "MandiriPasswd": mandiriEstatementPass
    }

    if os.path.isfile(args.file_path):
        converters[args.bank](args.file_path, args.paswd)
    else:
        print(f"Error: File tidak ditemukan pada {args.file_path}")

if __name__ == "__main__":
    main()