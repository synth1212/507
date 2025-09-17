# ============================================================================
# IMPORTS AND SETUP
# ============================================================================

import polars as pl
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Set seaborn style
sns.set_style("whitegrid")
sns.set_palette("husl")

# ============================================================================
# STEP 1: CREATE SAMPLE HEALTHCARE DATA
# ============================================================================

print("Creating synthetic healthcare dataset with Polars...")

# Create sample data structure
n = 1000  # Number of patients

# Generate synthetic patient data using numpy then convert to Polars
data_dict = {
    'patient_id': list(range(1, n+1)),
    'age': np.random.normal(65, 15, n).clip(18, 95).astype(int).tolist(),
    'gender': np.random.choice(['M', 'F'], n, p=[0.46, 0.54]).tolist(),
    'length_of_stay': np.random.lognormal(1.2, 0.8, n).clip(1, 30).astype(int).tolist(),
    'total_charges': np.random.lognormal(9, 1.2, n).clip(1000, 500000).tolist(),
    'discharge_disposition': np.random.choice(['Home', 'SNF', 'Rehab', 'Transfer', 'Death'], 
                                             n, p=[0.65, 0.15, 0.10, 0.08, 0.02]).tolist(),
    'primary_diagnosis': np.random.choice(['Heart Disease', 'Pneumonia', 'Diabetes', 'Stroke', 'Cancer'],
                                         n, p=[0.25, 0.20, 0.20, 0.15, 0.20]).tolist(),
    'readmission_30d': np.random.choice([0, 1], n, p=[0.85, 0.15]).tolist(),
    'surgery_performed': np.random.choice([0, 1], n, p=[0.70, 0.30]).tolist(),
    'infection_acquired': np.random.choice([0, 1], n, p=[0.95, 0.05]).tolist()
}

# Create Polars DataFrame
df = pl.DataFrame(data_dict)

# Introduce some missing values to simulate real data
missing_indices = np.random.choice(range(n), size=int(n*0.05), replace=False)
df = df.with_columns(
    pl.when(pl.int_range(pl.len()).is_in(missing_indices))
    .then(None)
    .otherwise(pl.col('total_charges'))
    .alias('total_charges')
)

print(f"Dataset created with {len(df)} patient records using Polars")

# ============================================================================
# STEP 2: DATA CLEANING AND OVERVIEW
# ============================================================================

print("=" * 60)
print("DATA CLEANING AND OVERVIEW (POLARS)")
print("=" * 60)

# Basic dataset information
print(f"Dataset shape: {df.shape}")
print(f"Each row represents: Individual patient discharge record")

# Column information
print("\nColumn names and data types:")
print(df.dtypes)

# Check for missing values - Polars way
print("\nMissing values:")
missing_summary = df.select([
    pl.col("*").null_count().alias("Missing_Count")
]).transpose(include_header=True)

# Calculate missing percentages
missing_counts = df.null_count().transpose(include_header=True)
missing_pct = (missing_counts.select(pl.col("column_0") / len(df) * 100).to_numpy().flatten())

# Create summary with column names
column_names = missing_counts.get_column("column").to_list()
missing_values = missing_counts.get_column("column_0").to_list()

print("Missing Value Summary:")
for i, (col, count, pct) in enumerate(zip(column_names, missing_values, missing_pct)):
    if count > 0:
        print(f"  {col}: {count} ({pct:.1f}%)")

# Basic descriptive statistics
print("\nBasic descriptive statistics:")
print(df.select(pl.col(pl.NUMERIC_DTYPES)).describe())

# ============================================================================
# STEP 3: FREQUENCY ANALYSIS
# ============================================================================

print("\n" + "=" * 60)
print("FREQUENCY ANALYSIS (POLARS)")
print("=" * 60)

# 3A. Categorical variable frequency analysis
print("\n1. CATEGORICAL VARIABLES - Frequency Tables")

# Gender frequency table - demonstrate all frequency types
print("\nGender Distribution:")
gender_counts = df.group_by('gender').agg(pl.count().alias('count')).sort('gender')
total_count = len(df)

# Calculate all frequency types
freq_table = gender_counts.with_columns([
    pl.col('count').alias('Absolute_Frequency'),
    (pl.col('count') / total_count).alias('Relative_Frequency'),
    pl.col('count').cumsum().alias('Cumulative_Frequency'),
    (pl.col('count').cumsum() / total_count).alias('Relative_Cumulative')
])
print(freq_table)

# 3B. Cross-tabulation example using Polars
print("\n2. CROSS-TABULATION (Pivot Tables)")
crosstab = df.group_by(['gender', 'discharge_disposition']).agg(
    pl.count().alias('count')
).pivot(
    values='count', 
    index='gender', 
    columns='discharge_disposition'
).fill_null(0)
print("\nGender vs Discharge Disposition:")
print(crosstab)

# Proportions in cross-tab
print("\nProportions (row percentages):")
# Calculate row totals for proportions
crosstab_with_totals = crosstab.with_columns(
    (pl.sum_horizontal(pl.col("*").exclude("gender"))).alias("row_total")
)
# Calculate proportions
disposition_cols = [col for col in crosstab.columns if col != 'gender']
crosstab_prop = crosstab_with_totals.with_columns([
    (pl.col(col) / pl.col("row_total")).alias(col) for col in disposition_cols
]).select(['gender'] + disposition_cols)
print(crosstab_prop)

# 3C. Grouped frequency for continuous variables
print("\n3. GROUPED FREQUENCY - Age Categories")
age_group_freq = df.with_columns(
    pl.col('age').cut([18, 35, 50, 65, 80, 95], 
                     labels=['18-34', '35-49', '50-64', '65-79', '80+']).alias('age_group')
).group_by('age_group').agg(
    pl.count().alias('count')
).sort('age_group')
print(age_group_freq)

# ============================================================================
# STEP 4: RATIOS, PROPORTIONS, AND RATES
# ============================================================================

print("\n" + "=" * 60)
print("RATIOS, PROPORTIONS, AND RATES (POLARS)")
print("=" * 60)

# 4A. Ratios
print("\n1. RATIOS")
gender_counts_dict = df.group_by('gender').agg(pl.count().alias('count')).to_dict(as_series=False)
gender_dict = dict(zip(gender_counts_dict['gender'], gender_counts_dict['count']))

female_count = gender_dict.get('F', 0)
male_count = gender_dict.get('M', 0)

female_to_male_ratio = female_count / male_count if male_count > 0 else 0
male_to_female_ratio = male_count / female_count if female_count > 0 else 0

print(f"Female discharges: {female_count}")
print(f"Male discharges: {male_count}")
print(f"Female-to-male ratio: {female_to_male_ratio:.2f}")
print(f"Male-to-female ratio: {male_to_female_ratio:.2f}")
print(f"Interpretation: For every 1 male discharged, {female_to_male_ratio:.2f} females were discharged")

# 4B. Proportions
print("\n2. PROPORTIONS")
total_discharges = len(df)
female_proportion = female_count / total_discharges
male_proportion = male_count / total_discharges

print(f"Proportion of female discharges: {female_proportion:.3f} ({female_proportion*100:.1f}%)")
print(f"Proportion of male discharges: {male_proportion:.3f} ({male_proportion*100:.1f}%)")

# 4C. Rates
print("\n3. RATES")

# Readmission rate
readmissions = df.select(pl.col('readmission_30d').sum()).item()
readmission_rate = (readmissions / total_discharges) * 100
print(f"30-day readmission rate: {readmission_rate:.1f}%")

# Mortality rate
deaths = df.filter(pl.col('discharge_disposition') == 'Death').height
mortality_rate = (deaths / total_discharges) * 100
print(f"In-hospital mortality rate: {mortality_rate:.1f}%")

# Surgery rate
surgeries = df.select(pl.col('surgery_performed').sum()).item()
surgery_rate = (surgeries / total_discharges) * 100
print(f"Surgical procedure rate: {surgery_rate:.1f}%")

# Hospital-acquired infection rate
infections = df.select(pl.col('infection_acquired').sum()).item()
infection_rate = (infections / total_discharges) * 100
print(f"Hospital-acquired infection rate: {infection_rate:.1f}%")

# ============================================================================
# STEP 5: CENTRAL TENDENCY AND VARIABILITY
# ============================================================================

print("\n" + "=" * 60)
print("CENTRAL TENDENCY AND VARIABILITY (POLARS)")
print("=" * 60)

# Focus on length of stay as example
los_stats = df.select(pl.col('length_of_stay')).drop_nulls()

# 5A. Central tendency measures
print("\n1. CENTRAL TENDENCY MEASURES")
central_stats = los_stats.select([
    pl.col('length_of_stay').mean().alias('mean'),
    pl.col('length_of_stay').median().alias('median'),
    pl.col('length_of_stay').mode().first().alias('mode')
])

mean_los = central_stats.select(pl.col('mean')).item()
median_los = central_stats.select(pl.col('median')).item()
mode_los = central_stats.select(pl.col('mode')).item()

print(f"Length of Stay (days):")
print(f"  Mean: {mean_los:.2f}")
print(f"  Median: {median_los:.2f}")
print(f"  Mode: {mode_los}")

# 5B. Variability measures
print("\n2. VARIABILITY MEASURES")
variability_stats = los_stats.select([
    pl.col('length_of_stay').std().alias('std'),
    pl.col('length_of_stay').var().alias('var'),
    (pl.col('length_of_stay').max() - pl.col('length_of_stay').min()).alias('range'),
    (pl.col('length_of_stay').quantile(0.75) - pl.col('length_of_stay').quantile(0.25)).alias('iqr')
])

std_los = variability_stats.select(pl.col('std')).item()
var_los = variability_stats.select(pl.col('var')).item()
range_los = variability_stats.select(pl.col('range')).item()
iqr_los = variability_stats.select(pl.col('iqr')).item()

print(f"  Standard Deviation: {std_los:.2f}")
print(f"  Variance: {var_los:.2f}")
print(f"  Range: {range_los:.2f}")
print(f"  Interquartile Range (IQR): {iqr_los:.2f}")

# 5C. Percentiles and quartiles
print("\n3. PERCENTILES AND QUARTILES")
percentiles = [0.25, 0.50, 0.75, 0.90, 0.95]
percentile_stats = los_stats.select([
    pl.col('length_of_stay').quantile(p).alias(f'p{int(p*100)}') for p in percentiles
])

print("Percentiles for Length of Stay:")
for i, p in enumerate([25, 50, 75, 90, 95]):
    value = percentile_stats.select(pl.col(f'p{p}')).item()
    print(f"  {p}th percentile: {value:.2f} days")

# ============================================================================
# STEP 6: DISTRIBUTION ASSESSMENT (SKEWNESS & KURTOSIS)
# ============================================================================

print("\n" + "=" * 60)
print("DISTRIBUTION ASSESSMENT (POLARS)")
print("=" * 60)

# Analyze multiple continuous variables
continuous_vars = ['age', 'length_of_stay', 'total_charges']

for var in continuous_vars:
    # Convert to numpy for scipy stats functions
    data = df.select(pl.col(var)).drop_nulls().to_numpy().flatten()
    
    print(f"\n{var.upper()} DISTRIBUTION:")
    
    # Skewness
    skewness = stats.skew(data)
    print(f"  Skewness: {skewness:.3f}")
    if abs(skewness) < 0.5:
        skew_interp = "approximately symmetric"
    elif skewness > 0:
        skew_interp = "positively skewed (right tail)"
    else:
        skew_interp = "negatively skewed (left tail)"
    print(f"  Interpretation: {skew_interp}")
    
    # Kurtosis
    kurtosis = stats.kurtosis(data)
    print(f"  Kurtosis: {kurtosis:.3f}")
    if abs(kurtosis) < 0.5:
        kurt_interp = "mesokurtic (normal-like)"
    elif kurtosis > 0:
        kurt_interp = "leptokurtic (peaked, heavy tails)"
    else:
        kurt_interp = "platykurtic (flat, light tails)"
    print(f"  Interpretation: {kurt_interp}")
    
    # Normality test
    test_data = data[:5000] if len(data) > 5000 else data
    shapiro_stat, shapiro_p = stats.shapiro(test_data)
    print(f"  Shapiro-Wilk test p-value: {shapiro_p:.6f}")
    normal_interp = "normally distributed" if shapiro_p > 0.05 else "not normally distributed"
    print(f"  Interpretation: Data is {normal_interp}")

# ============================================================================
# STEP 7: HEALTHCARE-SPECIFIC METRICS
# ============================================================================

print("\n" + "=" * 60)
print("HEALTHCARE-SPECIFIC METRICS (POLARS)")
print("=" * 60)

total_patients = len(df)

# 7A. Occupancy and utilization metrics
print("\n1. OCCUPANCY AND UTILIZATION METRICS")
avg_los = df.select(pl.col('length_of_stay').mean()).item()
print(f"  Average Length of Stay (ALOS): {avg_los:.2f} days")

# Simulated bed occupancy calculation
total_bed_days = df.select(pl.col('length_of_stay').sum()).item()
available_bed_days = 365 * 100  # Assuming 100 beds available 365 days
occupancy_rate = (total_bed_days / available_bed_days) * 100
print(f"  Estimated Bed Occupancy Rate: {occupancy_rate:.1f}%")

# 7B. Admission and discharge patterns
print("\n2. ADMISSION AND DISCHARGE PATTERNS")
discharge_summary = df.group_by('discharge_disposition').agg([
    pl.count().alias('count'),
    (pl.count() / total_patients * 100).alias('percentage')
]).sort('count', descending=True)

print("  Discharge Disposition Distribution:")
for row in discharge_summary.iter_rows(named=True):
    print(f"    {row['discharge_disposition']}: {row['count']} ({row['percentage']:.1f}%)")

# 7C. Quality metrics
print("\n3. QUALITY METRICS")
quality_metrics = df.select([
    (pl.col('readmission_30d').sum() / total_patients * 100).alias('readmission_rate'),
    ((pl.col('discharge_disposition') == 'Death').sum() / total_patients * 100).alias('mortality_rate'),
    (pl.col('infection_acquired').sum() / total_patients * 100).alias('infection_rate')
])

readmission_rate_calc = quality_metrics.select(pl.col('readmission_rate')).item()
mortality_rate_calc = quality_metrics.select(pl.col('mortality_rate')).item()
infection_rate_calc = quality_metrics.select(pl.col('infection_rate')).item()

print(f"  30-day Readmission Rate: {readmission_rate_calc:.1f}%")
print(f"  In-hospital Mortality Rate: {mortality_rate_calc:.1f}%")
print(f"  Hospital-Acquired Infection Rate: {infection_rate_calc:.1f}%")

# 7D. Case mix analysis
print("\n4. CASE MIX ANALYSIS")
diagnosis_dist = df.group_by('primary_diagnosis').agg([
    pl.count().alias('count'),
    (pl.count() / total_patients * 100).alias('percentage')
]).sort('percentage', descending=True)

print("  Primary Diagnosis Distribution:")
for row in diagnosis_dist.iter_rows(named=True):
    print(f"    {row['primary_diagnosis']}: {row['percentage']:.1f}%")

# ============================================================================
# STEP 8: BASIC VISUALIZATIONS
# ============================================================================

print("\n" + "=" * 60)
print("CREATING VISUALIZATIONS (POLARS DATA)")
print("=" * 60)

# Convert to pandas for plotting (seaborn works well with pandas)
df_pandas = df.to_pandas()

# Create a comprehensive dashboard using seaborn
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Healthcare Data Descriptive Analysis Dashboard (Polars)', fontsize=16)

# 1. Gender distribution
sns.countplot(data=df_pandas, x='gender', ax=axes[0,0])
axes[0,0].set_title('Gender Distribution')
axes[0,0].set_ylabel('Count')

# 2. Length of stay distribution
sns.histplot(data=df_pandas, x='length_of_stay', bins=20, ax=axes[0,1])
axes[0,1].set_title('Length of Stay Distribution')
axes[0,1].set_xlabel('Days')
axes[0,1].set_ylabel('Frequency')

# 3. Age distribution
sns.histplot(data=df_pandas, x='age', bins=20, ax=axes[0,2])
axes[0,2].set_title('Age Distribution')
axes[0,2].set_xlabel('Age (years)')
axes[0,2].set_ylabel('Frequency')

# 4. Discharge disposition
sns.countplot(data=df_pandas, x='discharge_disposition', ax=axes[1,0])
axes[1,0].set_title('Discharge Disposition')
axes[1,0].tick_params(axis='x', rotation=45)

# 5. Total charges (log scale due to skewness)
df_log_charges = df_pandas['total_charges'].dropna().apply(np.log)
sns.histplot(x=df_log_charges, bins=20, ax=axes[1,1])
axes[1,1].set_title('Total Charges (Log Scale)')
axes[1,1].set_xlabel('Log(Total Charges)')
axes[1,1].set_ylabel('Frequency')

# 6. Box plot for LOS by gender
sns.boxplot(data=df_pandas, x='gender', y='length_of_stay', ax=axes[1,2])
axes[1,2].set_title('Length of Stay by Gender')
axes[1,2].set_xlabel('Gender')
axes[1,2].set_ylabel('Length of Stay (days)')

plt.tight_layout()
plt.show()

print("Visualizations created successfully using seaborn with Polars data!")

# ============================================================================
# POLARS-SPECIFIC PERFORMANCE COMPARISON
# ============================================================================

print("\n" + "=" * 60)
print("POLARS PERFORMANCE FEATURES")
print("=" * 60)

print("\nPolars advantages demonstrated in this analysis:")
print("1. Lazy evaluation - operations are optimized before execution")
print("2. Memory efficiency - better handling of large datasets")
print("3. Parallel processing - automatic parallelization of operations")
print("4. Type safety - strong typing system prevents common errors")
print("5. Modern syntax - more intuitive API design")

# Example of lazy evaluation
print("\n5. LAZY EVALUATION EXAMPLE:")
lazy_query = df.lazy().filter(
    pl.col('age') > 65
).group_by('gender').agg([
    pl.count().alias('count'),
    pl.col('length_of_stay').mean().alias('avg_los')
])

print("Lazy query created (not executed yet):")
print("df.lazy().filter(pl.col('age') > 65).group_by('gender').agg([...])")

# Execute the lazy query
result = lazy_query.collect()
print("\nQuery executed:")
print(result)

# ============================================================================
# SUMMARY AND KEY TAKEAWAYS
# ============================================================================

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE - KEY TAKEAWAYS (POLARS VERSION)")
print("=" * 80)

print("\nKey Takeaways for Healthcare Data:")
print("1. Healthcare data is rarely normally distributed")
print("2. Length of stay and costs typically show positive skewness")
print("3. Ratios and proportions provide meaningful clinical insights")
print("4. Quality metrics (readmission, mortality, infection rates) are critical")
print("5. Visual inspection complements statistical measures")

print("\nPolars-specific benefits:")
print("1. Faster performance on large datasets")
print("2. More memory efficient operations")
print("3. Better handling of null values")
print("4. Expressive and readable syntax")
print("5. Built-in lazy evaluation for query optimization")

print("\nNext Steps:")
print("- Apply these techniques to your actual dataset")
print("- Consider data transformations for skewed variables")
print("- Implement quality checks and outlier detection")
print("- Take advantage of Polars' lazy evaluation for large datasets")
print("- Use Polars' streaming capabilities for very large files")

print("\nRemember: Polars excels with large datasets and complex operations!")