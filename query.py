import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

connection_string = os.environ.get("AZURE_CONNECTION_STRING")
cnxn = pyodbc.connect(connection_string)
data = pd.read_sql("SELECT * FROM SalesLT.Customer WHERE CustomerId < 10;", cnxn)
data.to_parquet("customers.parquet")

