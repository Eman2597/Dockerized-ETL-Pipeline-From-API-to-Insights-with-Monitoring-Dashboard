import pandas as pd

def create_dataframe(users_list):
    """
    Convert the list of users (dicts) into a pandas DataFrame
    and perform basic cleaning.
    """
    # Convert to DataFrame
    df = pd.json_normalize(users_list)

    # ------------------- Cleaning -------------------
    # 1. Handle missing maidenName
    df['maidenName'] = df.get('maidenName', '').replace('', 'Unknown')
    df['maidenName'] = df['maidenName'].fillna('Unknown')

    # 2. Extract useful columns
    df['country'] = df['address.country']
    df['city'] = df['address.city']

    # 3. Standardize text columns
    df['gender'] = df['gender'].str.lower().str.strip()
    df['role'] = df['role'].str.lower().str.strip()
    df['city'] = df['city'].str.title().str.strip()
    df['country'] = df['country'].str.title().str.strip()

    # 4. Remove duplicate emails
    df.drop_duplicates(subset='email', inplace=True)

    return df

def add_age_groups(df):
    """
    Feature engineering: add age_group, email_domain, BMI and BMI_category
    """
    # ------------------- Age Groups -------------------
    df['age_group'] = pd.cut(
        df['age'],
        bins=[0, 25, 35, 50, 100],
        labels=['Young', 'Adult', 'Mid-Age', 'Senior']
    )

    # ------------------- Email Domain -------------------
    df['email_domain'] = df['email'].str.split('@').str[1]

    # ------------------- BMI Calculation -------------------
    df['height_meter'] = df['height'] / 100
    df['BMI'] = df['weight'] / (df['height_meter'] ** 2)

    # BMI categories
    df['BMI_category'] = pd.cut(
        df['BMI'],
        bins=[0, 18.5, 25, 30, 100],
        labels=['Underweight', 'Normal', 'Overweight', 'Obese']
    )

    return df