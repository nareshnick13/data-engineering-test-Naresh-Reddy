
import pandas as pd

def standardize_dates(df: pd.DataFrame) -> pd.DataFrame:
    """  Convert dates to ISO format. """
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    return df

def aggregate_sales(df: pd.DataFrame) -> pd.DataFrame:
    """ Aggregate sales by category and store. """
    agg_df = df.groupby(['category', 'store_id', 'date']).agg({
        'amount': ['sum', 'count'],
        'transaction_id': 'nunique'
    }).reset_index()
    
    # Flatten column names
    agg_df.columns = ['category', 'store_id', 'date', 
                     'total_sales', 'transaction_count',
                     'unique_transactions']
    
    return agg_df

def calculate_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """ Calculate additional sales metrics.  """
    # Calculate average transaction value
    df['avg_transaction_value'] = df['total_sales'] / df['transaction_count']
    
    # Calculate daily revenue share by category
    daily_totals = df.groupby('date')['total_sales'].transform('sum')
    df['category_revenue_share'] = df['total_sales'] / daily_totals
    
    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """    Apply all transformations to the data.    
    Returns:    Transformed DataFrame    """
    # Standardize dates
    df = standardize_dates(df)
    
    # Aggregate sales
    df = aggregate_sales(df)
    
    # Calculate additional metrics
    df = calculate_metrics(df)
    
    return df
