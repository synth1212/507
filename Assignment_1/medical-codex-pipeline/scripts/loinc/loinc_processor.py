import pandas as pd

## Inputs/Loinc.csv
lonic = pd.read_csv('Assignment_1/medical-codex-pipeline/scripts/loinc/Loinc.csv')

### Info to describe 
lonic.info()

### Strings 
lonic.STATUS.value_counts()

### Print first row 
lonic.iloc[0]

#### Check potential column names that we think we want to keep: LOINC_NUM, DefinitionDescription
lonic.LOINC_NUM
lonic['LOINC_NUM']
lonic.LONG_COMMON_NAME

list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME']

### List of columns to keep
lonic_small = lonic[['LOINC_NUM', 'LONG_COMMON_NAME']]
lonic_small = lonic[list_cols]

lonic_small['last_updated'] = "2025-09-03"

# lonic_small = lonic_small.rename(columns={})
lonic_small = lonic_small.rename(columns={
    'LOINC_NUM': 'code',
    'LONG_COMMON_NAME': 'long_common_name'
})


file_output_path = 'Assignment_1/medical-codex-pipeline/outputs/lonic_small.csv'

lonic_small.to_csv(file_output_path)

print(f"Output saved to {file_output_path}")

