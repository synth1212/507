import polars as pl
import pandas as pd

npi_file_path = ('Assignment_1/medical-codex-pipeline/scripts/npi/npidata_pfile_20050523-20250810.csv')

## just load the first 1000 rows
df = pl.read_csv(npi_file_path, n_rows=1000)
df_panads = pd.read_csv(npi_file_path, nrows=1000, low_memory=False)

print(df_panads)

print(f"Successfully loaded {len(df)} records from NPI data")
print(f"Columns: {df.columns}")
print(f"\nDataset Shape: {df.shape}")
print(f"\fFirst 5 rows:")
print(df.head())

print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")

df_polars_small = df_polars.select([
    'NPI', 
    'Provider Last Name (Legal Name)', 
    'Provider First Name',
])

## Add in a last updated column 
df_polars_small = df_polars_small.with_columns(
    pl.lit("2025-09-03").alias("last_updated")
)

## 



## Save to CSV 
output_path = 'Assignment_1/medical-codex-pipeline/Outputs/npi_small.csv'
df_polars_small.write_csv(output_path)