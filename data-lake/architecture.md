# Architecture du Data Lake  TP 1

## Zones (buckets MinIO)

| Zone | Rôle |
|---|---|
| `raw` | Données brutes, telles qu'ingérées, jamais modifiées |
| `trusted` | Données nettoyées et validées |
| `curated` | Données prêtes pour l'analyse, la BI et l'IA |

## Outils et ports

| Outil | Rôle | Port(s) |
|---|---|---|
| MinIO | Stockage objet S3 des zones | 9000 (API S3), 9001 (console web) |
| PostgreSQL | Base relationnelle source | 5433 côté Windows (5432 dans le réseau Docker) |
| Jupyter | Notebooks Python d'ingestion | 8888 |

## Données ingérées

| Fichier | Type | Emplacement dans `raw` |
|---|---|---|
| `ventes.csv` | Structuré | `raw/ventes/2026/09/11/ventes.csv` |
| `clients.json` | Semi-structuré | `raw/clients/2026/09/11/clients.json` |

## Flux

sources (data/) → ingestion Python (Jupyter + boto3) → raw → trusted → curated

## Relancer l'environnement

docker compose up -d
