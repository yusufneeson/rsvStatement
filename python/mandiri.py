import tabula
import pandas as pd
import numpy as np
from pypdf import PdfReader
import locale
import re
import os
import argparse

def rsvConvert(file):
    # df = tabula.read_pdf(file, pages=2, area=(53.5, 19.9, 1000, 821.8), columns=[150.9, 285.9, 420.9, 555.9, 690.9, 821.8], pandas_options={'header': None, 'dtype': str})

    # print(df[0].iloc[0,1])

    reader = PdfReader(file)
    number_of_pages = len(reader.pages) + 1

    pandas_dfs = []

    for i in range(1, number_of_pages):
        if i == 1:
            dfs = tabula.read_pdf(file, pages=1, area=(261.5, 19.9, 1000, 1000), columns=[150.9, 285.9, 420.9, 555.9, 690.9, 821.8], pandas_options={'header': None, 'dtype': str})
            dfhead = tabula.read_pdf(file, pages=1, area=(242.9, 19.9, 261.5, 821.8))
        else:
            dfs = tabula.read_pdf(file, pages=i, area=(53.5, 19.9, 1000, 1000), columns=[150.9, 285.9, 420.9, 555.9, 690.9, 821.8], pandas_options={'header': None, 'dtype': str})
            dfhead = tabula.read_pdf(file, pages=i, area=(35.0, 19.9, 53.5, 821.8))

        df = dfs[0]

        # merged_keterangan = df1['KETERANGAN'].fillna('').groupby(df1['TANGGAL'].notna().cumsum()).transform(' '.join)
        # df1 = df
        # merged_keterangan = df1[1].fillna('').groupby(df1[0].notna().cumsum()).transform(' '.join);
        # df1.loc[df[0].isna(), 1] = merged_keterangan
        # df1 = df1[df1[0].notna()]

        # print(df1)

        # Tambahkan kolom grup berdasarkan apakah kolom pertama bukan NaN
        df['group'] = df[0].notna().cumsum()

        # for x in range(1, len(df)):
        #     if pd.isna(df.iloc[i, 0] and pd.notna(df.iloc[i-1,0])):
        #         df.iloc[i-1, 1] += " " + str(df.iloc[i, 1])
        # df_cleaned = df.dropna(subset=[0])
        # df_cleaned.reset_index(drop=True, inplace=True)

        # print(df_cleaned)

        # Gabungkan data berdasarkan grup yang telah ditentukan
        grouped_df = df.groupby('group').apply(lambda g: [
            g[0].iloc[0],                           # Tanggal dan waktu dari kolom 0
            g[1].dropna().str.cat(sep=" "),         # Gabungkan semua teks pada kolom 1
            g[2].iloc[0] if pd.notna(g[2].iloc[0]) else "",  # Kolom 2, jika ada data
            g[3].iloc[0] if pd.notna(g[3].iloc[0]) else "",  # Kolom 3, jika ada data
            g[4].iloc[0] if pd.notna(g[4].iloc[0]) else "",  # Kolom 4, jika ada data
            g[5].iloc[0] if pd.notna(g[5].iloc[0]) else ""   # Kolom 5, jika ada data
        ]).apply(pd.Series)

        # Atur ulang nama kolom sesuai data asli
        grouped_df.columns = ['tanggal', 'keterangan', 'ref', 'debet', 'kredit', 'saldo']

        # Reset indeks hasil akhir
        grouped_df.reset_index(drop=True, inplace=True)

        # if i != number_of_pages-1:
        # for x in range(1, len(grouped_df)):
        #     if pd.isna(grouped_df.iloc[i, 0] and pd.notna(grouped_df.iloc[i-1,0])):
        #         grouped_df.iloc[i-1, 1] += " " + str(grouped_df.iloc[i, 1])
        # df_cleaned = grouped_df.dropna(subset=[0])
        # df_cleaned.reset_index(drop=True, inplace=True)

        # # Tampilkan hasil
        # print(df_cleaned)
        pandas_dfs.append(grouped_df)
        # print(grouped_df)

        # result = pd.concat(pandas_dfs, ignore_index=True)

    result = pd.concat(pandas_dfs, ignore_index=True)
    result.to_csv(file.replace('.pdf', '.csv'), index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename a file to remove special characters.")
    parser.add_argument("file_path", help="The path to the file to be renamed")
    args = parser.parse_args()

    if os.path.isfile(args.file_path):
        rsvConvert(args.file_path)
    else:
        print(f"Error: File not found at path {args.file_path}")