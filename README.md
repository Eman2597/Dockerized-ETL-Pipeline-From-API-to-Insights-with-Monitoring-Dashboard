# 🚀 Dockerized ETL Pipeline: From API to Insights with Monitoring Dashboard

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Grafana](https://img.shields.io/badge/grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Prometheus](https://img.shields.io/badge/prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)

---

## 🧠 Project Overview

This project is a **production-ready, containerized ETL pipeline** that automates the full data lifecycle:

➡️ Extract data from API
➡️ Transform & clean data
➡️ Load into PostgreSQL
➡️ Generate insights & visualizations
➡️ Monitor performance in real-time

---

## 🏗️ Architecture

![Architecture](./assets/diagram.png)

---

## ⚙️ ETL Pipeline

### 🔹 1. Extract (`app/extract.py`)

* Fetch data from API using pagination
* Convert JSON → structured format

---

### 🔹 2. Transform (`app/transform.py`)

* Data cleaning & preprocessing
* Handle missing values
* Remove duplicates
* Feature Engineering:

  * Age Groups
  * BMI
  * Email Domains

---

### 🔹 3. Load (`app/load.py`)

* Save data to:

  * CSV → `output/data/`
  * PostgreSQL (Data Warehouse)

---
### 📊 4. Generated Visualizations

The pipeline generates the following insights:

* **Average Age by Role** (Bar Chart)
* **Average Age by Gender** (Bar Chart)
* **User Count per Gender** (Count Plot)
* **Top 10 Cities with Most Users** (Bar Chart)
* **Height Distribution** (Histogram with KDE)
* **Weight Distribution** (Histogram with KDE)
* **Age vs. Height Correlation** (Scatter Plot)
* **Age vs. Weight Correlation** (Scatter Plot)

* Generate multiple plots:
* Saved in:

```
output/plots/
```

---

## 📡 Monitoring

The pipeline is fully monitored using:

* Prometheus → collects metrics
* Grafana → dashboards 


### 📈 Metrics:

* `etl_processing_seconds` → execution time
* `etl_users_total` → processed users


---
## 🐳 Docker Environment

The entire system runs using **Docker Compose**, including:

* ETL Pipeline
* PostgreSQL
* Prometheus
* Grafana


---

## ▶️ How to Run

### 1️⃣ Clone repo

```
# Clone the repository
git clone https://github.com/Eman2597/Dockerized-ETL-Pipeline-From-API-to-Insights-with-Monitoring-Dashboard.git

# Navigate to project folder
cd Dockerized-ETL-Pipeline-From-API-to-Insights-with-Monitoring-Dashboard
```

---

### 2️⃣ Run project

```
# Build and run all services
docker-compose up --build -d
```

---

## 3️⃣ Access Services

Since the project is hosted on a Virtual Machine, you can access the monitoring and data tools from your host browser using the following URLs:

| Service              | Protocol | URL                                | Default Credentials |
| -------------------- | -------- | ---------------------------------- | ------------------- |
| 📊 Grafana Dashboard | HTTP     | http://192.168.56.101:3000         | admin / admin       |
| 📡 Prometheus        | HTTP     | http://192.168.56.101:9090         | Public / No Auth    |
| 🐍 App Metrics       | HTTP     | http://192.168.56.101:8000/metrics | Public / No Auth    |
| 🐘 PostgreSQL        | TCP/IP   | 192.168.56.101:5432                | etl_user / etl_pass |


---
![📊Dashborad](./assets/grafana.png)
---

## 📂 Project Structure

```
.
.
├── app/
│   ├── main.py          # Pipeline Orchestrator
│   ├── extract.py       # API Ingestion
│   ├── transform.py     # Cleaning & Logic
│   └── load.py          # DB Persistence
├── config/
│   ├── prometheus.yml   # Metrics Config
│   └── dashboard.json   # Pre-configured Grafana Dashboard
├── output/
│   ├── data/            # Processed CSV Backups
│   └── plots/           # Seaborn/Matplotlib Visualizations
├── docker-compose.yml   # Multi-container Orchestration
└── Dockerfile           # Python Environment Image
└── README.md
```

---

## 🛠️ Tech Stack

* Python
* Pandas
* Requests
* Seaborn & Matplotlib
* PostgreSQL
* Docker & Docker Compose
* Prometheus
* Grafana

---

## 🎯 Key Learnings

* Building modular ETL pipelines
* Containerizing data workflows
* Working with Data Warehouses
* Monitoring pipelines in real-time
* Structuring production-ready projects

---

## 👩‍💻 Author

**Eman Abdelmohsen Elbordeny**

*Data Engineer | Data Enthusiast*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eman-elbordeny-2511e997/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Eman2597)
