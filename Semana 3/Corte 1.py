# import sys
# import subprocess

# subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "matplotlib", "scipy", "seaborn", "ipywidgets", "tqdm"])

import pandas as pd
import numpy as np

# from pyodide.http import pyfetch

# async def download(url, filename):
#     response = await pyfetch(url)
#     if response.status == 200:
#         with open(filename, "wb") as f:
#             f.write(await response.bytes())

path = 'c:/Users/Mario/Desktop/3er semestre/programacion analitica/Cohorte I/Semana 3/auto.csv'
print(path)
# Read the online file by the URL provides above, and assign it to variable "df"
df = pd.read_csv(path, header=None)

# # show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
print(df.head(5))

print("the last 10 rows of the dataframe\n")
print(df.tail(10))

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

df.columns = headers
print(df.head(10))

df1=df.replace('?',np.NaN)
print(df1)

df=df1.dropna(subset=["price"], axis=0)
print(df.head(20))

print(df.columns)

df.to_csv("automobile.csv", index=False)

df.dtypes
print(df.dtypes)

df.describe(include = "all")

print(df.info())

#question 3 
print(df[['length', 'compression-ratio']].describe())

#module 4_pandas 

