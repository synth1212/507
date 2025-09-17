import pandas as pd 
from sqlalchemy import create_engine 

## Load in .sql file as string
with open('.\Assignment_2_DBS\patient_query.sql', 'r') as file:
sql_depression_query = file.read()

db_location = 'example.db'

engine = create_engine(f'sqlite:///{db_location}') # You can eventually add in ursername, port code to the database, password if needed

patients_df = pd.read_csv('#insertoffilepathhere.csv')

patients_df.sample(10) # .sample() method to view random rows of data, keeps information unbiased

patients_df.to_sql('patients_details', con=engine, if_exist='replace', index=False) ## con=engine connection strenth, if_exist=replace table if it already exists, index='False' prevents pandas from writing row indices into the table, index=True would write row indices into the table

#read the data from the database into a pandas Dataframe
df = pd.read_sql('SELECT * FROM 'insertoffilepathhere'', engine)

# Example query to select all patients with anxiety disorder (ICD-10 code F41.9).
query = "SELECT * FROM 'insertoffilepathhere' WHERE primary_icd10 = 'F41.9'"
result_df = pd.read_sql_query(query_anxiety, con=engine)
# OR you can modify the query as needed with this cmd.
query_x = "SELECT * FROM 'insertoffilepathhere' WHERE primary_icd10 = 'F41.9'"
result_c_df = pd.read_sql_query(query_x, con=engine)


result_df = pd.read_sql_query(query_anxiety, con=engine)
len(result_df) # Will output the number of rows in the result dataframe

print(df.head())