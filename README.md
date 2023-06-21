# DVC Azure SQL example

A simple DVC pipeline to fetch from an SQL DB, cache as parquet for
reproducibility and faster processing.

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Depending on the setup and machine, you might need to install ODBC driver. It
depends on the OS, please refer to MS ODBC setup docs.

## Setup

Create and `.env` file with:


```env
AZURE_CONNECTION_STRING="DRIVER={ODBC Driver 18 for SQL Server};SERVER=<server>.database.windows.net,1433;DATABASE=<db>;UID=<user>;PWD=<password>"
```

This file is in `.gitignore`. 

> Note! There should be a better way to manage Azure credentials (e.g. using AD
> or managed identities. This is example is made simple, but we recommend to
> explore other options.

## Running

Run `dvc repro` or `dvc exp run` to reproduce the pipeline. Use regular
`dvc push`, `dvc pull`, etc, to save and load artifacts.
