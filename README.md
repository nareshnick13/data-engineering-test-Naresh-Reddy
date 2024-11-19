# data-engineering-test-Naresh-Reddy

## Introduction
This is a test to design and implement a data pipeline that processes raw data, performs transformations, and loads it into a structured format.

## Objective
Create an ETL (Extract, Transform, Load) pipeline that:
- Processes raw sales data
- Applies data validation and cleaning
- Performs necessary transformations
- Loads data into a SQLite database

## Dataset
The sample dataset (`data/sales_data.csv`) contains retail sales information with the following columns:
- `transaction_id`: Unique identifier for each sale
- `date`: Transaction date
- `product_id`: Product identifier
- `category`: Product category
- `amount`: Sale amount
- `customer_id`: Customer identifier
- `store_id`: Store identifier

## Requirements

### Technical Requirements
- Python 3.8+
- Required packages: pandas, sqlite3, pytest
  
### Functional Requirements
1. Data Validation
   - Check for missing values
   - Validate data types
   - Ensure date formats are consistent
   
2. Transformations
   - Convert dates to ISO format
   - Aggregate sales by category and store
   - Calculate daily revenue metrics
   
3. Data Loading
   - Store processed data in SQLite database
   - Create appropriate indexes for efficient querying
