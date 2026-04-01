import os
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# ---  (PostgreSQL) ---

def save_to_postgres(csv_path):
    """
            CVS to PostgreSQL  (Retry Logic).
    """
    if not os.path.exists(csv_path):
        print(f" Error: File {csv_path} not found!")
        return

    print(f" Reading data from {csv_path} to load into Postgres...")
    df = pd.read_csv(csv_path)

    #  (Environment Variables)
    #  serves name 'db' in  docker-compose.yml
    db_host = os.environ.get('DB_HOST', 'db')
    db_port = os.environ.get('DB_PORT', 5432)
    db_name = os.environ.get('DB_NAME', 'etl_db')
    db_user = os.environ.get('DB_USER', 'etl_user')
    db_pass = os.environ.get('DB_PASS', 'etl_pass')

    # (SQLAlchemy Engine)
    connection_string = f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
    engine = create_engine(connection_string)

    # retry in Docker
    max_retries = 5
    for attempt in range(max_retries):
        try:
            # context manager  (Best Practice)
            
            with engine.begin() as connection:
                df.to_sql('users', con=connection, if_exists='replace', index=False)
            
            print(" ############# Data loaded into PostgreSQL successfully ##########")
            break
        except OperationalError as e:
            if attempt < max_retries - 1:
                print(f" Database not ready, retrying in 5s... ({attempt + 1}/{max_retries})")
                time.sleep(5)
            else:
                print(f" Failed to connect to PostgreSQL after {max_retries} attempts.")
                print(f"Error Details: {e}")

# --- (CSV) ---

def save_to_csv(df, path="output/data/users.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False, encoding='utf-8-sig')
    print(f"✅ Data saved locally to {path}")

# ---  (Visualizations) ---

def create_output_dirs():
   
    os.makedirs("output/plots", exist_ok=True)

def plot_avg_age_by_role(df):
    create_output_dirs()
    plt.figure(figsize=(5,6))
    sns.barplot(
        data=df, x='role', y='age', hue='role', 
        estimator='mean', palette='Set2', legend=False, errorbar=None
    )
    plt.title("Average Age by Role")
    plt.xlabel("Role")
    plt.ylabel("Average Age")
    plt.tight_layout()
    plt.savefig("output/plots/avg_age_by_role.png")
    plt.close()

def plot_avg_age_by_gender(df):
    create_output_dirs()
    plt.figure(figsize=(5,6))
    sns.barplot(
        data=df, x="gender", y="age", hue='gender', 
        estimator='mean', palette='Set2', legend=False, errorbar=None
    )
    plt.title("Average Age by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Average Age")
    plt.tight_layout()
    plt.savefig("output/plots/avg_age_by_gender.png")
    plt.close()

def plot_users_per_gender(df):
    create_output_dirs()
    plt.figure(figsize=(5,6))
    sns.countplot(data=df, x="gender", hue='gender', palette='Set2')
    plt.title("Number of users per Gender")
    plt.xlabel("Gender")
    plt.ylabel("Number Of Users")
    plt.tight_layout()
    plt.savefig("output/plots/users_per_gender.png")
    plt.close()

def plot_top_cities(df):
    create_output_dirs()
    users_per_city = df['city'].value_counts().sort_values(ascending=False).reset_index()
    users_per_city.columns = ['city', 'user_count']
    plt.figure(figsize=(10,6))
    sns.barplot(data=users_per_city.head(10), x="city", y="user_count", hue='city', palette='Set2')
    plt.title("Top 10 cities with the most users")
    plt.xlabel("City")
    plt.ylabel("Number Of Users")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/plots/top_cities.png")
    plt.close()

def plot_height_distribution(df):
    create_output_dirs()
    plt.figure(figsize=(6,5))
    sns.histplot(data=df, x="height", hue='role', multiple='stack', kde=True)
    plt.title(f"Average height={df['height'].mean():.2f} cm")
    plt.xlabel("Height (cm)")
    plt.ylabel("Number of users")
    plt.tight_layout()
    plt.savefig("output/plots/height_distribution.png")
    plt.close()

def plot_weight_distribution(df):
    create_output_dirs()
    plt.figure(figsize=(6,5))
    sns.histplot(data=df, x="weight", hue='role', multiple='stack', kde=True)
    plt.title(f"Average Weight={df['weight'].mean():.2f} kg")
    plt.xlabel("Weight (kg)")
    plt.ylabel("Number of users")
    plt.tight_layout()
    plt.savefig("output/plots/weight_distribution.png")
    plt.close()

def plot_age_vs_height(df):
    create_output_dirs()
    plt.figure(figsize=(6,5))
    sns.scatterplot(data=df, x='age', y='height', hue='gender')
    plt.title("Relationship Between Age and Height")
    plt.xlabel("Age")
    plt.ylabel("Height (cm)")
    plt.tight_layout()
    plt.savefig("output/plots/age_vs_height.png")
    plt.close()

def plot_age_vs_weight(df):
    create_output_dirs()
    plt.figure(figsize=(6,5))
    sns.scatterplot(data=df, x='age', y='weight', hue='gender')
    plt.title("Relationship Between Age and Weight")
    plt.xlabel("Age")
    plt.ylabel("Weight (Kg)")
    plt.tight_layout()
    plt.savefig("output/plots/age_vs_weight.png")
    plt.close()