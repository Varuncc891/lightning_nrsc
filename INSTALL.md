### Installation Guide

# Prerequisites

PostgreSQL 15 with PostGIS 3.4
Python 3.11 or higher
Apache Superset 6.0
Git

# Step 1: Clone Repository

git clone https://github.com/Varuncc891/lightning_nrsc.git
cd lightning_nrsc


# Step 2: Database Setup

Connect to PostgreSQL

psql -U postgres


Create database and enable PostGIS

CREATE DATABASE nrsc_lightning_db;
\c nrsc_lightning_db;
CREATE EXTENSION postgis;
\q


Import schema

psql -U postgres -d nrsc_lightning_db -f database/schema.sql


# Step 3: Python Proxy Server

copy config\superset_config.py %USERPROFILE%\.superset6\
set SUPERSET_CONFIG_PATH=%USERPROFILE%\.superset6\superset_config.py
superset run -p 8088


# Step 5: Database Connection String


postgresql://<username>:<password>@<host>:5432/nrsc_lightning_db


# Step 6: Create Datasets in Superset


Dataset Name	Source View
Lightning Master	lightning_master
Daily Summary	lightning_daily_summary
