import pandas as pd

df = pd.read_parquet("customers.parquet")

with open("result.txt", "a", encoding="utf-8") as f:
   f.write(f"{df.shape}")

