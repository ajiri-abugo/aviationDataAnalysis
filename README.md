# aviationDataAnalysis

📌 Project Overview

The Aviation Data Analysis Project is an end-to-end data engineering pipeline designed to help a travel agency become more profitable by analyzing aviation data. The pipeline collects, processes, stores, and visualizes key insights, such as busiest routes and ticket price trends.

🛠️ Technologies Used

Programming Languages: Python (ETL scripts, data cleaning)

Databases: MongoDB (Data Lake), PostgreSQL (Data Warehouse), MySQL (Data Quality Logs)

Orchestration: Airflow

Streaming: Kafka

Visualization: Google Looker

Other Tools: Docker (Containers), .env files for environment variables

🗂️ Project Structure

aviationDataAnalysis/
├── etl/
│   ├── extract/
│   │   └── api_scraper.py
│   ├── load/
│   │   └── airports_datalake.py
│   └── transform/
│       └── routes_cleaning.py
├── config/
│   ├── __init__.py
│   ├── dbconnect.py
│   ├── mongoconnect.py
│   └── mysqlconnect.py
├── logs/
│   └── data_quality.log
├── docker-compose.yml
└── README.md


💾 Data Pipeline Workflow

Data Ingestion: Collects real-time flight data from APIs using Kafka.

Data Cleaning: Applies tailored cleaning and validation functions.

Data Loading: Stores raw data in MongoDB and cleaned data in PostgreSQL.

Data Quality Checks: Logs issues (duplicates, missing values) into MySQL.

Data Visualization: Displays insights on Google Looker dashboards.

📊 Key Datasets

Airport List: Contains airport codes, city, timezone, and country.

Airport Routes: Shows departure and arrival airports, state, and region.


🚀 How to Run the Project

1. Set Up Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2. Configure .env File
Create a .env file with:
MONGO_URI=<your_mongo_uri>
POSTGRES_URI=<your_postgres_uri>
API_KEY=<your_api_key>

3. Start Kafka and MongoDB (if using Docker)
docker-compose up

4. Run ETL Scripts
python3 etl/extract/extract-countries.py
python3 etl/load/countries-datalake.py
python3 etl/load/airports_datalake.py

🚧 Future Enhancements

Implement pipeline monitoring with Prometheus and Grafana

*Add schema enforcement with Avro or Protobuf

Expand orchestration with Airflow

Deploy using containers and cloud services

👤 Author

Ajiri - Data Engineer

💬 Feedback

Contributions and suggestions are welcome! Open an issue or fork the repository to propose changes.


