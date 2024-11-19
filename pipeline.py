import logging
import os
import pandas as pd
import sqlite3
from datetime import datetime
from .validators import validate_data
from .transformers import transform_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataPipeline:
    def __init__(self, input_path: str, output_db: str):
        """         
        Args:
          input_path: Input CSV file path
          output_db:  output SQLite database path
        """
        self.input_path = input_path
        self.output_db = output_db

  
    def extract(self) -> pd.DataFrame:
        """Extract data from CSV file."""
        logger.info(f"Reading data from {self.input_path}")
        return pd.read_csv(self.input_path)
    
    def load(self, df: pd.DataFrame) -> None:
        """Load transformed data into SQLite database."""
        logger.info(f"Loading data into {self.output_db}")
        
        # Ensure the output directory exists
        output_dir = os.path.dirname(self.output_db)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        with sqlite3.connect(self.output_db) as conn:
            df.to_sql('sales', conn, if_exists='replace', index=False)
            
                
    def run(self) -> None:
        """Execute the complete ETL pipeline."""
        try:
            # Extract
            df = self.extract()
            
            # Validate
            df = validate_data(df)
            
            # Transform
            df = transform_data(df)
            
            # Load
            self.load(df)
            
            logger.info("Pipeline completed successfully")
            
        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}")
            raise

if __name__ == "__main__":
    # Create sample data if it doesn't exist
    sample_data = pd.DataFrame({
        'transaction_id': ['T1', 'T2', 'T3', 'T4'],
        'date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
        'product_id': ['P1', 'P2', 'P1', 'P2'],
        'category': ['A', 'B', 'A', 'B'],
        'amount': [100.0, 200.0, 150.0, 250.0],
        'customer_id': ['C1', 'C2', 'C1', 'C2'],
        'store_id': ['S1', 'S1', 'S2', 'S2']
    })
    
    input_path = "data/raw/sales_data.csv"
    
    # Ensure the raw data directory exists
    os.makedirs("data/raw", exist_ok=True)
    
    # Save sample data
    sample_data.to_csv(input_path, index=False)
    
    # Run pipeline
    pipeline = DataPipeline(
        input_path=input_path,
        output_db="data/processed/sales.db"
    )
    pipeline.run()
