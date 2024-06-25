# Data ingestion pipeline
This project implements a robust data ingestion pipeline designed to efficiently handle data from various sources and prepare it for analytics. Here’s an overview of key components and technologies used:

- Data Sources: Various sources ingested into PostgreSQL. 
- Data Transformation: Using dbt for transformations. 
- Analytics Database: PostgreSQL for storing analytics-ready data. 
- Pipeline Orchestration: Dagster for workflow and dependencies management. 
- Partitioning: The transformed table is partitioned by day for efficient querying.

## Usage
### Prerequisites
- Docker installed on your machine
- Clone this repository to your local environment

### Steps to set up the project and run
1. **Build the Docker image and start services** \
 Run the following command in the project's root directory:
   ```bash
   docker-compose up --build
   ```
2. **Access the Dagster UI** \
   Open your web browser and go to http://localhost:3000 to access the Dagster UI.
3. **Trigger the data ingestion pipeline** \
Inside the Dagster UI:
   1. Navigate to Overview. 
   2. Go to Jobs. 
   3. Find the job named data-ingestion-pipeline. 
   4. Click the dropdown menu on the right, select Launch new run, and choose the latest partition.
4. **Access the data warehouse** \
Open your web browser and visit http://localhost:5050 to access pgAdmin UI. \
Use the credentials provided in `pgadmin.env` to log in.
5. **Run analytics queries** \
In the pgAdmin UI:
   1. Navigate to`Query Tool`.
   2. Execute SQL queries located in the `analytics_queries` directory in the root directory of this project.

## Summary
Given additional time, the following improvements would be added:
1. Implementing unit tests for custom CSV Loader and DB IO manager.
2. Writing additional data validation checks.
3. Writing unit tests for DBT models.
4. Integrating Clickhouse with Dagster for enhanced data warehousing capabilities.
