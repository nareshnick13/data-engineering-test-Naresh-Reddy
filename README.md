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
- `transaction_id`: transaction Id for each sale
- `date`: Transaction date
- `product_id`: Product ID
- `category`:  category
- `amount`:  amount
- `customer_id`: Customer Id
- `store_id`: Store ID

## Requirements

### Technical Requirements
- Python 
- packages: pandas, sqlite3, pytest
  
### Functional Requirements
1. Data Validation
   - Check for missing values
   - Validate data types
   - Ensure date formats are consistent
   
2. Transformations
   - Convert dates to ISO format
   - Aggregate sales by category and store
   - Calculate daily revenue metrics
       
4. Data Loading
   - Store processed data in SQLite database
   - Create appropriate indexes for efficient querying

 #### References
   1. https://stackoverflow.com/
   2. https://www.w3schools.com/python/
   3. https://www.codeconvert.ai/csharp-to-python-converter
   4. https://medium.com/@devedium/python-crash-course-for-c-developers-a-quick-reference-guide-86ca519b83c8
   5. https://www.google.com/search?q=python+pipeline+read+data+from+csv&oq=python+pipeline+read+data+from+csv+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTEyMDU1ajBqMagCALACAA&sourceid=chrome&ie=UTF-8
