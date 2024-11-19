import pandas as pd
from typing import List

def check_missing_values(df: pd.DataFrame) -> List[str]:
    """ Check for missing values in the DataFrame.
        Returns:
        List of columns with missing values
    """
    missing_cols = df.columns[df.isnull().any()].tolist()
    return missing_cols

def validate_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """  Validate and convert data types.    
    Returns:        DataFrame with correct data types    """
    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Ensure numeric columns are correct type
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df['product_id'] = df['product_id'].astype(str)
    df['customer_id'] = df['customer_id'].astype(str)
    df['store_id'] = df['store_id'].astype(str)
    
    return df

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """    Perform all data validations.    
    Returns:        Validated DataFrame    """
    # Check for missing values
    missing_cols = check_missing_values(df)
    if missing_cols:
        raise ValueError(f"Missing values found in columns: {missing_cols}")
    
    # Validate data types
    df = validate_data_types(df)    

    return df
