## Lightning Monitoring Dashboard for NRSC/ISRO

A real-time lightning strike monitoring dashboard built with **PostgreSQL/PostGIS** and **Apache Superset 6.0**, integrated with **Bhuvan TMS services** via a Python proxy server.

## File Structure
lightning_nrsc/
│
├── README.md
├── INSTALL.md
├── .gitignore
│
├── proxy/
│ ├── bhuvan_proxy.py
│ └── test_proxy.py
│
├── config/
│ ├── superset_config.py
│ └── requirements.txt
│
└── database/
│ └── schema.sql


## 🛠️ Software Versions

| Component | Version |
|-----------|---------|
| **PostgreSQL** | 15 |
| **PostGIS** | 3.4 |
| **Apache Superset** | 6.0 |
| **Python** | 3.11 |
| **Flask** | 2.3.3 |
| **Git** | Latest |


### 1. Clone Repository

```sh
git clone https://github.com/Varuncc891/lightning_nrsc.git
cd lightning_nrsc
```


### 2. Database Setup

Create database
```
psql -U <db_user> -c "CREATE DATABASE nrsc_lightning_db;"
```

Enable PostGIS
```
psql -U <db_user> -d nrsc_lightning_db -c "CREATE EXTENSION postgis;"
```

Import schema (creates tables, indexes, views)
```
psql -U <db_user> -d nrsc_lightning_db -f database/schema.sql
```



## 3. Python Proxy Server

Install dependencies
```
cd proxy
pip install -r ../config/requirements.txt
```

Start proxy server
```
python bhuvan_proxy.py
```

## 4. Superset Configuration
```
set SUPERSET_CONFIG_PATH=C:\path\to\superset_config.py
superset run -p 8088
```


## 5. Database Connection String

```postgresql://<username>:<password>@<host>:5432/nrsc_lightning_db```


alright, we're done with readme, tell me if this is good or not
