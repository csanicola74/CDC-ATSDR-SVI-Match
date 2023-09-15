
# Social Vulnerability Index (SVI) Mapping Project

This project provides tools and scripts to map ZIP codes to county-level FIPS codes and tract-level FIPS codes using a ZIP_COUNTY crosswalk. It also maps the `RPL_THEMES` value from the `SVI_2020_US_county` dataset for each county FIPS.

## Project Structure

- `data/cleaned_sample_address_data.csv`: Contains address data with ZIP codes.
- `data/ZIP_COUNTY_032023.csv`: A crosswalk file mapping ZIP codes to county FIPS codes.
- `data/SVI_2020_US_county.csv`: Contains the SVI data for 2020 at the county level, including the `RPL_THEMES` values.
- `SVI_SUBJECT_MATCH.ipynb`: The Jupyter Notebook that contains the main Python script that performs the operations to produce the final merged dataframe.

## Requirements

- Python 3.7 or higher
- Pandas library

You can install the required packages using:
```bash
pip install pandas
```

## Instructions

1. Clone this repository:
```bash
git clone https://github.com/csanicola74/CDC-ATSDR-SVI-Match.git
cd CDC-ATSDR-SVI-Match
```

2. Ensure you have the required Python packages installed:
```bash
pip install -r requirements.txt
```

3. Run the script:
```bash
python svi_match.py
```

4. Check the output CSV file `final_merged_data.csv` in the main directory.

## Licensing

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

1. Fork the repository.
2. Create a new branch for your features or fixes.
3. Submit a pull request.

For major changes, please open an issue first to discuss what you would like to change.

## Credits

- [Caroline Sanicola](https://github.com/csanicola74) - Initial work

I welcome and appreciate any feedback, changes, or contributions. Feel free to make a pull request or open an issue.
