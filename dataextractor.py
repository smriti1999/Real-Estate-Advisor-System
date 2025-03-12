import pandas as pd
import numpy as np


class DataExtractor:
    @staticmethod
    # This static method reads property information from a CSV file
    def extract_property_info(file_path):

        # Read the data from the CSV file located at the specified 'file_path' using a comma separator
        return pd.read_csv(file_path, sep=",")

    @staticmethod
    # This static method performs currency exchange on property
    def currency_exchange(dataframe, exchange_rate):
        target_price = np.array(dataframe.price * exchange_rate)
        return target_price

    @staticmethod
    # This static method provides a summary of property data for a specific suburb
    def suburb_summary(dataframe, suburb):
        if suburb.lower() == 'all':
            print(dataframe.describe())
        else:
            suburb_data = dataframe[dataframe['suburb'] == suburb.capitalize()]
            if len(suburb_data) != 0:
                print(suburb_data.describe())
            else:
                print(f"No data available")

    @staticmethod
    # This method calculates the average land size for a specified suburb or the entire dataset.
    def avg_land_size(dataframe, suburb):

        # If 'all' is specified, use the entire dataframe.
        if suburb == 'all':
            dataf = dataframe
        else:
            # Filter the dataframe based on the specified suburb (capitalized).
            dataf = dataframe[dataframe['suburb'] == suburb.capitalize()]
            print(len(dataf))
        if len(dataf) != 0:

            # If there is data for the specified suburb or the entire dataset,
            # remove rows with a 'land_size' of -1 (indicating missing data).
            dataf = dataf[dataf['land_size'] != -1]

            # Convert land sizes in hectares ('ha') to square meters
            for j, row in dataf.iterrows():
                if row['land_size_unit'] == 'ha':
                    row['land_size'] = row['land_size']*10000

            # Calculate and return the rounded mean of 'land_size'.
            return round(dataf['land_size'].mean(), 2)

        else:
            return None
