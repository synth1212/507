<!-- Slide number: 1 -->
# Descriptives
Acute Care / Cleaning.
Hants Williams, PhD, RN

<!-- Slide number: 2 -->
# Main Cleaning Steps (regardless of py package):
1. Understanding data shape, what each row ‘means’ - atomic data
2. Cleaning column names
3. Managing null values
4. Data types and conversions
5. Removing duplicates
6. Outlier detection
7. Then do basic .descriptives() or pivot tables

<!-- Slide number: 3 -->
# Synthetic Data
Development and Testing Environments: Using synthetic data in development stages allows engineers and data scientists to build, test, and refine healthcare applications without exposing sensitive patient data, ensuring that software is robust and accurate before it interacts with real patient records

Privacy Preservation: Synthetic data allows researchers and practitioners to simulate and analyze health scenarios without accessing real patient data, ensuring privacy and reducing potential risks associated with data breaches.

Enhanced Research Opportunities: With synthetic data, researchers can generate diverse datasets that may not be readily available, enabling studies and experiments in areas with limited real-world data.

Regulatory Compliance: Synthetic data can be freely shared and analyzed without violating regulations like HIPAA, facilitating collaboration and transparency in healthcare research without compromising patient privacy.

<!-- Slide number: 4 -->
# Synthea
https://synthea.mitre.org/
Synthea by MITRE Corporation: A tool for generating realistic, privacy-preserving synthetic healthcare data.

Addressing Privacy Concerns: Enables research, development, and testing without using real patient data, ensuring confidentiality.

Rich Dataset: Provides synthetic patient electronic health records (EHRs) detailing conditions, procedures, medications, and demographics.

Applications: Allows professionals to test healthcare systems, validate algorithms, and develop software without risking sensitive patient information.

<!-- Slide number: 5 -->
# Sytnethic Claims Data
https://data.cms.gov/collection/synthetic-medicare-enrollment-fee-for-service-claims-and-prescription-drug-event
CMS Synthetic Claims Data: Realistic-but-not-real datasets provided by the Centers for Medicare and Medicaid Services.

Dataset Contents: Represents enrollment information and healthcare claims for 8,671 Medicare beneficiaries.

Utility: Helps users understand CMS claims data attributes, approximating the statistical characteristics of real data.

<!-- Slide number: 6 -->
# Faker
Generating your own fake data how you want it to look…
https://faker.readthedocs.io/en/master/
A Python library that generates fake data for a variety of purposes.

Capable of producing data such as names, addresses, email addresses, dates, and more.

Supports multiple languages and locales, allowing for culturally relevant data generation.

Useful for populating databases for testing, anonymizing data, and software development mock-ups.

Provides a simple and intuitive API for generating large quantities of realistic synthetic data quickly.

<!-- Slide number: 7 -->
# Masking Data
When we are working with our data, we might want to eventually share it publicly, how do we do so while maintaining privacy?
Important for:
Patient confidentiality
Regulatory compliance
Trust
Reduction of risk / breach
Collaboration - research

<!-- Slide number: 8 -->
# Masking Data
Generalization
Replacing specific values with broader ranges or categories

![Screenshot 2023-09-06 at 11.46.36 AM.png](Screenshot20230906at114636AMpng.jpg)

<!-- Slide number: 9 -->
# Masking Data
Perturbation
Adding random noise to data points to prevent exact reidentification

![Screenshot 2023-09-06 at 11.47.47 AM.png](Screenshot20230906at114747AMpng.jpg)

<!-- Slide number: 10 -->
# Masking Data
Suppression
Removing specific data points to prevent identification

![Screenshot 2023-09-06 at 11.48.22 AM.png](Screenshot20230906at114822AMpng.jpg)

<!-- Slide number: 11 -->
# Please review update chapter 2.1
https://book.datascience.appliedhealthinformatics.com/docs/Ch2/pandas

![Screenshot 2023-09-06 at 11.20.05 AM.png](Screenshot20230906at112005AMpng.jpg)

<!-- Slide number: 12 -->
# Descriptive Statistics
- Categorical: Quality checks via general counts / frequencies
- Continuous: Quantiles versus quartiles – M and SDs /
Packages {pip/pip3 install x, y, z)
Pandas
Tableone (https://pypi.org/project/tableone/)
ResearchPy (https://pypi.org/project/researchpy/)
If using VS Code:

![Screen Shot 2022-09-06 at 3.26.00 PM.png](ScreenShot20220906at32600PMpng.jpg)
Jupyter notebook extension

<!-- Slide number: 13 -->
# Descriptive statistics
Descriptive statistics summarizes the data, and are broken down into measures of:

1) Central tendency (mean, median, mode)
2) Measures of variability (SD, min/max, range, kurtosis, skewness)

<!-- Slide number: 14 -->
# Applicability of descriptive statistics
Majority of real-world requests are descriptive in nature, and do not require advanced analytics.

1) Did {X} or {Y} happen?
2) How much of {X} happened?
3) Can you describe what else happened around X event?

<!-- Slide number: 15 -->
Organizational Level of Data Readiness / Maturity
Gartner (March 2012) - ORGANIZATIONAL MODEL FOR DATA MATURITY

![Image](Image.jpg)
Descriptive Analytics: What happened

Diagnostic Analytics: Why did it happen

Predictive Analytics: What is going to happen

Prescriptive Analytics: Prescribing recommendations

<!-- Slide number: 16 -->
Frequency distribution
Ratios, Proportions, and Rates
3. Skewness
4. Central Tendency
5. Variability / SD - SEM

<!-- Slide number: 17 -->
# Frequency

<!-- Slide number: 18 -->
? most critical step ?

<!-- Slide number: 19 -->
The first step toward a good inferential/ML/advanced analysis is to examine your data for outliers and to view your data distribution for a given variable

<!-- Slide number: 20 -->
Frequency distribution refers to a tabular or graph that shows the distribution of values for a given variable taken from a sample of the population

<!-- Slide number: 21 -->

![Image](Image.jpg)
Gut check
The
Step

<!-- Slide number: 22 -->

![Image](Image.jpg)
…Everything else follows

…Doesn’t take a rocket scientist to interpret

…Executives prefer simplicity > complex

<!-- Slide number: 23 -->
Frequency distribution –

Absolute Frequency – count of all occurrences of feature

Relative Frequency- absolute / (total n)

Cumulative Frequency - sum of all absolute, equal or less

Relative Cumulative Frequency - cumulative / (total n)

<!-- Slide number: 24 -->
15 diabetic patients are asked how many times per day they check their blood sugar
| Patient 1 | 1 |
| --- | --- |
| Patient 2 | 1 |
| Patient 3 | 2 |
| Patient 4 | 0 |
| Patient 5 | 3 |
| Patient 6 | 2 |
| Patient 7 | 1 |
| Patient 8 | 4 |
| Patient 9 | 2 |
| Patient 10 | 3 |
| Patient 11 | 1 |
| Patient 12 | 0 |
| Patient 13 | 0 |
| Patient 14 | 1 |
| Patient 15 | 2 |

<!-- Slide number: 25 -->
| Patients - Times Checked Per Day | Absolute Frequency | Relative Frequency | Cumulative Frequency | Relative cumulative |
| --- | --- | --- | --- | --- |
| 0 | 3 | 3/15 | 3 | 3/15 |
| 1 | 5 | 5/15 | 3 + 5 = 8 | 8/15 |
| 2 | 4 | 4/15 | 3 + 5 + 4 = 12 | 12/15 |
| 3 | 2 | 2/15 | 3 + 5 + 4 + 2 = 14 | 14/15 |
| 4 | 1 | 1/15 | 3+5+4+2+1 = 15 | 15/15 |

Gut check ->
Does this make sense that 3/15 or 20% of diabetics from our sample do not check their blood sugar?

<!-- Slide number: 26 -->
# Frequency Table
The frequency table displays data with missing cases, and without the missing cases.

Depending on the % of the missing data we decide how to proceed with the analysis (descriptive or inferential).

<!-- Slide number: 27 -->

![Image](Image.jpg)

<!-- Slide number: 28 -->
# Grouping Frequency
When a set of scores cover a wide range of values, then a list of all the X values would be too long or when research design necessitates.

In a grouped f table, the X column lists groups of scores, called class intervals, rather than individual values.

Important, groupings shouldn’t lose precision.
Age (Interval/Scale variable) recoded to grouped variable
From Interval to Ordinal (recode)

<!-- Slide number: 29 -->
# Grouping Frequency: Cross Tabulation (PIVOT)
Cross-tabs: are tables that display how frequencies and/or percentages of the categories of one variable are related to the frequencies/percentages of another variable(s).

Cross-tabs helps us understand the candidate variables in our analysis better.

Even though cross-tables gives us an idea about our variables, it is NOT an inferential statistics. It is still a descriptive statistics.

<!-- Slide number: 30 -->
What is wrong with this frequency table?

![Image](Image.jpg)
https://pubmed.ncbi.nlm.nih.gov/15224203/

<!-- Slide number: 31 -->

![Image](Image.jpg)

<!-- Slide number: 32 -->
What is missing with this table?

![Image](Image.jpg)
Does not tell us unit of measurement
Does not tell us about null/missing value count
https://pubmed.ncbi.nlm.nih.gov/15224203/

<!-- Slide number: 33 -->
Measurement unit provided

![Image](Image.jpg)

<!-- Slide number: 34 -->
# Frequency Tables - Python - CrossTab

![Screen Shot 2020-09-09 at 2.51.41 PM.png](ScreenShot20200909at25141PMpng.jpg)
Create test dataframe

![Screen Shot 2020-09-09 at 2.51.55 PM.png](ScreenShot20200909at25155PMpng.jpg)
Use cross-tab function to generate frequencies for grade and age

![Screen Shot 2020-09-09 at 2.52.15 PM.png](ScreenShot20200909at25215PMpng.jpg)

![Screen Shot 2020-09-09 at 2.52.53 PM.png](ScreenShot20200909at25253PMpng.jpg)
Generate proportions

![Screen Shot 2020-09-09 at 2.55.05 PM.png](ScreenShot20200909at25505PMpng.jpg)
2-way frequency tables

<!-- Slide number: 35 -->
# Frequency Tables - Python - Tableone

![Screen Shot 2022-09-07 at 8.42.12 AM.png](ScreenShot20220907at84212AMpng.jpg)

![Screen Shot 2022-09-07 at 8.42.47 AM.png](ScreenShot20220907at84247AMpng.jpg)
https://pypi.org/project/tableone/
https://tableone.readthedocs.io/en/latest/quickstart.html

<!-- Slide number: 36 -->
Ratios, Proportions, and Rates
Ratios: Compare two independent quantities.
Proportions: Compare a part to the whole.
Rates: Express an event as a proportion of a population at risk, typically over time.

<!-- Slide number: 37 -->
# Ratios

![Screenshot 2024-09-25 at 8.49.27 AM.png](Screenshot20240925at84927AMpng.jpg)
Definition: A ratio is a comparison between two different quantities or categories.

Example: Female-to-male discharge ratio: If 457 females and 395 males were discharged in a given period:

This means for every 1 male discharged, 1.16 females were discharged.
For every 100 males discharged, approximately 116 females were discharged.

![Screenshot 2024-09-25 at 8.49.49 AM.png](Screenshot20240925at84949AMpng.jpg)
Female
Male

<!-- Slide number: 38 -->
# Ratios
Flipped example (Male-to-female ratio):

Interpretation: For every female discharged, 0.86 males were discharged. This means fewer males were discharged compared to females.
For every 100 females discharged, approximately 86 males were discharged.

![Screenshot 2024-09-25 at 9.28.27 AM.png](Screenshot20240925at92827AMpng.jpg)
Male
Female

<!-- Slide number: 39 -->
# Proportion
Definition: A proportion is a type of ratio where one quantity (x) is part of the whole (x + y).

Proportion of female discharges:

54% of all discharges were female.

![Screenshot 2024-09-25 at 8.51.44 AM.png](Screenshot20240925at85144AMpng.jpg)

![Screenshot 2024-09-25 at 8.51.58 AM.png](Screenshot20240925at85158AMpng.jpg)

<!-- Slide number: 40 -->
# Rates
Definition: A rate measures how often an event occurs in relation to the population at risk, over a specified time period.

x is the number of times the event occurred,
y is the population at risk,
10n is a scaling factor, often 102 = 100 to express the result as a percentage

![Screenshot 2024-09-25 at 8.55.42 AM.png](Screenshot20240925at85542AMpng.jpg)

<!-- Slide number: 41 -->
# Rates

![Screenshot 2024-09-25 at 8.58.23 AM.png](Screenshot20240925at85823AMpng.jpg)

![Screenshot 2024-09-25 at 8.58.38 AM.png](Screenshot20240925at85838AMpng.jpg)
C-Section Rate:

If 23 C-sections were performed out of 149 deliveries:

15.4% of deliveries were C-sections.

<!-- Slide number: 42 -->
# Distribution

<!-- Slide number: 43 -->

![Screen Shot 2020-08-26 at 2.31.52 PM.png](ScreenShot20200826at23152PMpng.jpg)

<!-- Slide number: 44 -->
Bell Curve (Gaussian distribution)

![Screen Shot 2020-08-26 at 2.31.52 PM.png](ScreenShot20200826at23152PMpng.jpg)

<!-- Slide number: 45 -->
The normal distribution has three properties that allow us to make probabilistic statements about differences:
1. The three measures of central tendency are identical in the normal
distribution. Median, mode, and mean all have the same value.

2. The curve is perfectly symmetrical (and looks like a bell). The distribution
of values above the middle is a mirror image of the distribution
of values below it.

3. The shape of the normal distribution can be expressed in a mathematical
equation that allows us to define the area under every part of the curve.

![Screen Shot 2020-08-26 at 2.31.52 PM.png](ScreenShot20200826at23152PMpng.jpg)

<!-- Slide number: 46 -->
# Skewness and Kurtosis
SKEWNESS: measures the SYMMETRY of the distribution

KURTOSIS: determines the ‘heaviness’ of the distribution tails; refers to degree of presence of outliers in the distribution

<!-- Slide number: 47 -->
Central Tendency - Skewness
Validity of estimates using normal distribution depends on how the sample approximates the normal curve.

Values close to zero indicate normal (near normal) distribution

If skewness is zero the distribution is symmetric

Positive skew indicates mean is > median & negative skew is when median is > mean

As values become increasingly positive or negative, they indicate skewness.

Skewness should be reported to help readers evaluate the appropriate use of statistical procedures/test.

<!-- Slide number: 48 -->
Central Tendency - Three Measures: Mean, Median & Mode

![Image](Image.jpg)
Neg skew = lower mean
Pos skew = higher mean

<!-- Slide number: 49 -->
Modality
Most common - frequently occurring value (e.g., MODE)

UNI - Bi - MULTI

![Image](Image.jpg)
1 mode
2 modes
3 + modes

<!-- Slide number: 50 -->
Central Tendency - Kurtosis
Kurtosis measures how peak or flat the distribution of a data is.

Leptokurtic (+ kurtosis) – is when kurtosis is > zero. The distribution is peaked / narrow that is, data are clustered around a smaller part of the curve and the tails are short. Very few outliers, data is grouped together.

Mesokurtic – when Kurtosis is = zero, an indication of a normal distribution

Platykurtic (- kurtosis) – when kurtosis is < zero. The distribution is flatter & wide. Thus tails are long - meaning there are a lot of outliers, potential variation

<!-- Slide number: 51 -->

![Image](Image.jpg)

<!-- Slide number: 52 -->

![Image](Image.jpg)
High kurtosis
Low kurtosis
Depending on context, platypus might be a bad platypus

<!-- Slide number: 53 -->
#3 - Shape Area
The Empirical Rule or 68-95-99.7%

![Image](Image.jpg)

![Image](Image.jpg)

<!-- Slide number: 54 -->
Non-normalcy in healthcare

<!-- Slide number: 55 -->
# Healthcare Data is Rarely Normally Distributed
In healthcare, data often does not follow the bell-shaped, symmetrical distribution of the normal (Gaussian) curve.

Normal distribution assumes that most data points cluster around the mean, with fewer extreme values on either side. However, this is not the case with most healthcare datasets due to various factors like skewness, outliers, and variability in patient characteristics.

<!-- Slide number: 56 -->
# Why Healthcare Data is Not Normally Distributed:
1. Skewed Data: Many healthcare metrics, such as length of stay (LOS) and cost data, tend to be positively skewed. A few patients might have very long stays or high costs, pulling the distribution tail to the right.

<!-- Slide number: 57 -->
# Why Healthcare Data is Not Normally Distributed:
2. Outliers: Healthcare data often contains extreme values. For example, a small percentage of patients may require extensive care or have rare complications that dramatically increase costs or hospital time.

<!-- Slide number: 58 -->
# Why Healthcare Data is Not Normally Distributed:
3. Multi-modal Distributions: Some healthcare data shows more than one peak, reflecting subpopulations within the larger dataset. For example, age data might show separate peaks for pediatric, adult, and elderly patients.

<!-- Slide number: 59 -->
Common Distributions of Healthcare Data

<!-- Slide number: 60 -->
# Common Distributions in Healthcare Data
A-1. Right-Skewed Distribution (Positive Skewness):

![Screenshot 2024-09-25 at 12.40.29 PM.png](Screenshot20240925at124029PMpng.jpg)
Example: The majority of patients might have short hospital stays, but a small group with complications may stay significantly longer.

<!-- Slide number: 61 -->
# Common Distributions in Healthcare Data
A-2. Left-Skewed Distribution (Negative Skewness):

![Screenshot 2024-09-25 at 1.02.01 PM.png](Screenshot20240925at10201PMpng.jpg)
Response time to treatments (e.g., how quickly patients recover from a specific condition): Most patients may recover quickly within a short period, but a few outliers may take longer to respond, causing a left skew.

<!-- Slide number: 62 -->
# Common Distributions in Healthcare Data
Log-normal distributions are common for metrics like income or medical costs, where taking the logarithm of the values produces a normal distribution.

Example: Total healthcare expenditures often follow a log-normal distribution because costs increase exponentially in certain cases.
B. Log-Normal Distribution

![Screenshot 2024-09-25 at 12.46.16 PM.png](Screenshot20240925at124616PMpng.jpg)

![Screenshot 2024-09-25 at 12.47.05 PM.png](Screenshot20240925at124705PMpng.jpg)

<!-- Slide number: 63 -->
# Common Distributions in Healthcare Data

![Screenshot 2024-09-25 at 12.49.27 PM.png](Screenshot20240925at124927PMpng.jpg)
C. Poisson distribution

![pasted-movie.png](pastedmoviepng.jpg)

![Screenshot 2024-09-25 at 12.49.45 PM.png](Screenshot20240925at124945PMpng.jpg)
Poisson distribution is common for count data, such as the number of hospital admissions, the number of infections in a specific period, or the number of patients seen by a physician in a day.

Example: The number of hospital-acquired infections (HAIs) over a week.
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10903957/
https://psychology.emory.edu/clinical/bliwise/Tutorials/CLT/CLT/poisson.htm

<!-- Slide number: 64 -->
Central Tendency Summary
When working with an interval/ratio variable the following descriptive statistics are important to understanding the nature of the data

Mean – is the first step that summarizes the data  by providing the average

SD – shows whether the data were dispersed from or clustered around the mean.

Skewness – shows the nature of the symmetry or asymmetry of the distribution (standardized).

Kurtosis – describes how peak or flat the distribution of the data is / outliers

<!-- Slide number: 65 -->
# Variability and Spread

<!-- Slide number: 66 -->
Range
Range: is the total number of values between the maximum & the minimum within a data set.

It shows the dispersion between the two extreme scores. It does not put into account all the other values in the distribution.

Range = max value - min value +1 (to include all values)

Example, AHI students with max age of 35 & min 21 range = 35-21+1 = 15 it includes 21.50 & 35.49.

If student age range changes to Max 41 & min 21, Range = 41-21+1= 21. Therefore, range indicates greater variation in students age.

Range is easily influenced by outliers

<!-- Slide number: 67 -->
Percentiles, Quartiles, and Interquartiles
Percentiles: used to represent relative position to other scores. If blood pressure score is in the 92nd percentile, that person’s score was higher than 92% of those who took the test.

Quartiles: divide a distribution into 4 equal parts or quarters, Q1, Q2, & Q3 (0.25, 0.50, & 0.75). A box plot (box & whiskers plot) also shows the visual spread of the scores.

<!-- Slide number: 68 -->
Percentiles, Quartiles, and Interquartiles

Inter Quartile rage: is the range for the middle 50%, i.e., > the bottom 25% and < top 25%.

Inter quartile range = Q3-Q1= (50%).

Quantile ? Given as decimal value (0.95; 0.27)

<!-- Slide number: 69 -->

![Image](Image.jpg)

![Image](Image.jpg)

![Image](Image.jpg)

<!-- Slide number: 70 -->
Standard Deviation
Average amount of deviation of values from the mean

The larger the SD, the greater the variability
in the scores within the distribution

The smaller the SD, the less variability in the
scores

The larger your sample size when conducting
research, the smaller the SD is likely to be.

<!-- Slide number: 71 -->

![Screen Shot 2020-09-02 at 3.42.27 PM.png](ScreenShot20200902at34227PMpng.jpg)
VARIANCE

![Screen Shot 2020-09-02 at 3.42.39 PM.png](ScreenShot20200902at34239PMpng.jpg)

<!-- Slide number: 72 -->
What they want to know….
Is the data normal - should it be trusted

<!-- Slide number: 73 -->
# Acute care descriptive outcomes tracked
1. Occupancy Rates
Inpatient Bed Occupancy Rate: The percentage of hospital beds occupied over a given period.

Room Occupancy Rate: The percentage of hospital rooms (not just beds) occupied over a given period.

Adjusted Occupancy Rate: This rate adjusts the standard occupancy rate by accounting for outpatient services. It’s used to reflect a hospital’s total patient volume (both inpatient and outpatient).

Bed Turnover Rate: The number of times each hospital bed is occupied by different patients over a given period.

<!-- Slide number: 74 -->
# Acute care descriptive outcomes tracked
2. Admissions and Discharge Rates
Admission Rate: The proportion of patients admitted to the hospital during a given period.

Discharge Rate: The proportion of discharges (including deaths) over a specific time period.

Readmission Rate: The percentage of patients who are readmitted to the hospital within a certain period (usually 30 days) after being discharged.

Inpatient Length of Stay (LOS): The number of days a patient spends in the hospital from admission to discharge.

Average Length of Stay (ALOS): The total length of stay for all patients divided by the number of discharges during the same period.

<!-- Slide number: 75 -->
# Acute care descriptive outcomes tracked

3. Mortality-Related Rates
Death Rates:
Gross Death Rate: The percentage of total hospital discharges that resulted in death.
Net Death Rate: Similar to the gross death rate but excludes deaths within 48 hours of admission.
Autopsy Rates: Includes gross, net, and specific rates (e.g., newborn, hospital autopsy rates) reflecting how many deaths lead to autopsies.

4. Infection Rates
Hospital Infection Rate: The proportion of patients who acquired infections during their hospital stay.
Postoperative Infection Rate: The percentage of infections in clean surgical cases after surgery.

<!-- Slide number: 76 -->
# Acute care descriptive outcomes tracked
5. Consultation Rate:  The percentage of patients receiving consultations from other physicians.

6. Case Mix Index (CMI): A measure used to assess the resource usage and complexity of care provided by the hospital, based on Diagnosis-Related Groups (DRGs).

7. Surgical Procedure Rate: The number of surgeries performed as a proportion of total admissions.

8. Patient Satisfaction Rate: Tracks the percentage of patients who report a positive experience with hospital services.