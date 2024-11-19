import pytest
import pandas as pd from src.transformers
import osfrom src.pipeline 
import DataPipeline
import (
    standardize_dates,
    aggregate_sales,
    validate_data,
    check_missing_values, 
    validate_data_types
    
)

@pytest.fixture
def sample_data():
    """Create sample data for testing transformations."""
    return pd.DataFrame({
        'transaction_id': ['T1', 'T2', 'T3', 'T4'],
        'date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
        'product_id': ['P1', 'P2', 'P1', 'P2'],
        'category': ['A', 'B', 'A', 'B'],
        'amount': [100.0, 200.0, 150.0, 250.0],
        'customer_id': ['C1', 'C2', 'C1', 'C2'],
        'store_id': ['S1', 'S1', 'S2', 'S2']
    })

def test_standardize_dates(sample_data):   
    df = standardize_dates(sample_data)
    assert all(df['date'].str.match(r'\d{4}-\d{2}-\d{2}'))

def test_aggregate_sales(sample_data):   
    df = aggregate_sales(sample_data)
    assert 'total_sales' in df.columns
    assert 'transaction_count' in df.columns
    assert len(df) == len(sample_data.groupby(['category', 'store_id', 'date']))

def test_validate_data_types(sample_data):   
    df = validate_data_types(sample_data)
    assert pd.api.types.is_datetime64_any_dtype(df['date'])
    assert pd.api.types.is_numeric_dtype(df['amount'])

@pytest.fixture
def invalid_data():   
    return pd.DataFrame({
        'transaction_id': ['T1', 'T2'],
        'date': ['2023-01-01', None],
        'product_id': ['P1', 'P2'],
        'category': ['A', 'B'],
        'amount': [100.0, 'invalid'],
        'customer_id': ['C1', 'C2'],
        'store_id': ['S1', 'S2']
    })

ef test_check_missing_values(invalid_data):   
    missing_cols = check_missing_values(invalid_data)
    assert 'date' in missing_cols

def test_validate_data_with_invalid_input(invalid_data):   
    with pytest.raises(ValueError):
        validate_data(invalid_data)
