import pandas as pd

# Load the three CSV files into dataframes
address_data = pd.read_csv('cleaned_sample_address_data.csv')
zip_county_crosswalk = pd.read_csv('ZIP_COUNTY_032023.csv')
svi_data = pd.read_csv('SVI_2020_US_county.csv')

# Pivot the ZIP_COUNTY crosswalk to get each ZIP and its corresponding county FIPS in a single row
zip_county_pivot = zip_county_crosswalk.pivot_table(index='ZIP', values='COUNTY', aggfunc=lambda x: list(x)).reset_index()

# Convert the list of COUNTY FIPS to separate columns
max_counties_for_zip = zip_county_pivot['COUNTY'].apply(len).max()
for i in range(max_counties_for_zip):
    zip_county_pivot[f'COUNTY_{i+1}'] = zip_county_pivot['COUNTY'].apply(lambda x: x[i] if i < len(x) else None)
zip_county_pivot = zip_county_pivot.drop(columns=['COUNTY'])

# Merge the address_data with the reshaped zip_county_pivot
merged_data = pd.merge(address_data, zip_county_pivot, left_on='ZIP CODE', right_on='ZIP', how='left')
merged_data = merged_data.drop(columns=['ZIP'])

# Create a dictionary to map STCNTY (county FIPS) to RPL_THEMES
fips_to_rpl = dict(zip(svi_data['STCNTY'], svi_data['RPL_THEMES']))

# For each COUNTY column in the merged dataframe, map the RPL_THEMES value
for i in range(1, max_counties_for_zip + 1):
    merged_data[f'RPL_THEMES_{i}'] = merged_data[f'COUNTY_{i}'].map(fips_to_rpl)

# Save the final merged dataframe to a CSV file
merged_data.to_csv('final_merged_data.csv', index=False)
