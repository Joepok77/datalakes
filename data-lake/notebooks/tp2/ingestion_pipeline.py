"""Pipeline d'ingestion multi-sources (TP 2) : PostgreSQL, API REST et fichier plat vers la zone raw."""
import csv
import json
from datetime import date, datetime

import boto3
import pandas as pd
import requests
from sqlalchemy import create_engine

# Noms de service Docker : le script s'execute dans le conteneur Jupyter
POSTGRES_URL = "postgresql+psycopg2://tp_user:tp_password@postgres:5432/tp_datalake"
MINIO_URL = "http://minio:9000"
BUCKET = "raw"

s3 = boto3.client(
    "s3",
    endpoint_url=MINIO_URL,
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin123",
)


def log_ingestion(source, nb_lignes, fichier):
    with open("journal_ingestion.csv", "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([datetime.now().isoformat(), source, nb_lignes, fichier])
    print(f"Journal mis a jour : {source} - {nb_lignes} lignes")


def today_path():
    return date.today().isoformat().replace("-", "/")


def ingest_postgres():
    df = pd.read_sql("SELECT * FROM commandes", create_engine(POSTGRES_URL))
    df.to_csv("commandes_export.csv", index=False)
    key = f"postgres_commandes/{today_path()}/commandes.csv"
    s3.upload_file("commandes_export.csv", BUCKET, key)
    log_ingestion("postgres_commandes", len(df), key)


def ingest_api():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()
    users = response.json()
    with open("api_users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)
    key = f"api_clients/{today_path()}/users.json"
    s3.upload_file("api_users.json", BUCKET, key)
    log_ingestion("api_clients", len(users), key)


def ingest_stock():
    df_stock = pd.read_csv("stock.csv")
    key = f"fichiers_stock/{today_path()}/stock.csv"
    s3.upload_file("stock.csv", BUCKET, key)
    log_ingestion("fichiers_stock", len(df_stock), key)


if __name__ == "__main__":
    ingest_postgres()
    ingest_api()
    ingest_stock()
    print("Pipeline termine : 3 sources ingerees dans raw")
