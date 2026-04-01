import time
import os
from prometheus_client import start_http_server, Summary, Counter
from app.extract import fetch_users
from app.transform import create_dataframe, add_age_groups
from app.load import (
    save_to_csv,
    save_to_postgres,
    plot_avg_age_by_role,
    plot_avg_age_by_gender,
    plot_users_per_gender,
    plot_top_cities,
    plot_height_distribution,
    plot_weight_distribution,
    plot_age_vs_height,
    plot_age_vs_weight
)
# Metrics
ETL_TIME = Summary('etl_processing_seconds', 'Time spent processing ETL pipeline')
USER_COUNT = Counter('etl_users_total', 'Total users processed')

@ETL_TIME.time()
def run_pipeline():
    print("Starting ETL Pipeline...")

    # 1. Extract
    users = fetch_users()
    if not users:
        print(" No data fetched. Skipping this run.")
        return

    # 2. Transform
    df = create_dataframe(users)
    df = add_age_groups(df)
    print("Transformation completed")

    # 3. Save transformed data
    save_to_csv(df, path="output/data/users_transformed.csv")  
    # 4. Generate plots
    plot_avg_age_by_role(df)
    plot_avg_age_by_gender(df)
    plot_users_per_gender(df)
    plot_top_cities(df)
    plot_height_distribution(df)
    plot_weight_distribution(df)
    plot_age_vs_height(df)
    plot_age_vs_weight(df)
    
    # Count users
    USER_COUNT.inc(len(df))

    # Load to DB
    save_to_postgres('output/data/users_transformed.csv')

    print("ETL Pipeline Finished")

    print("Pipeline finished successfully!")
    print("All CSVs and plots are saved in 'output' directory")
    
if __name__ == "__main__":
    # Start metrics server
    print("Prometheus Metrics server started on port 8000")
    start_http_server(8000)
    print("Metrics server started on port 8000...")

    while True:
        run_pipeline()
        time.sleep(60)  