import pandas as pd

# Read the ICD-10 file from the "Medical_Codexes" folder
icd10cm = pd.read_xml("./Medical_Codexes/icd10cm_tabular_2025.xml", xpath=".//chapter/sectionIndex")

# Display the first few rows of the dataframe
print(icd10cm.head())