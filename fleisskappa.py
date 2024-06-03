import os
import pandas as pd
from statsmodels.stats.inter_rater import aggregate_raters, fleiss_kappa

df = pd.read_excel('Konačne anotacije1.xlsx', index_col=0)

df.head()

df["KONAČNA ANOTACIJA"].unique()

string_to_int = {"negativno":0, "neutralno":1 ,"pozitivno":2, "pozitivno ":2,  "mješovito":3}

df=df.replace(to_replace=string_to_int)

df_data = df[["Marijeta", "Lara", "Petra"]]

df_dropped = df_data.dropna()

df_dropped.head().values.tolist()

agg,cat = aggregate_raters(df_dropped.values.tolist())

print(fleiss_kappa(agg)) #rezultat = 0.8972848663451253



