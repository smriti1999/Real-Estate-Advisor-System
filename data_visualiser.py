from dataextractor import DataExtractor
import matplotlib.pyplot as plt


class DataVisualiser:
    @staticmethod
    # This static method visualizes the distribution of property values in a given dataframe
    def prop_val_distribution(dataframe, suburb, target_currency):

        # define dictionary for currency conversion
        currency_dict = {"AUD": 1, "USD": 0.66, "INR": 54.25, "CNY": 4.72, "JPY": 93.87, "HKD": 5.12,
                         "KRW": 860.92, "GBP": 0.51, "EUR": 0.60, "SGD": 0.88}

        # Check if the target currency is not in the dictionary
        if target_currency.upper() not in currency_dict and target_currency != -1:
            target_currency = 'AUD'

        # Check if the suburb is 'all' or not present in the unique suburb  values
        if suburb.lower() == 'all' or suburb.capitalize() not in dataframe['suburb'].unique():
            data = DataExtractor.currency_exchange(dataframe, currency_dict[target_currency])
        else:
            suburb_df = dataframe[dataframe['suburb'] == suburb.capitalize()]
            data = DataExtractor.currency_exchange(suburb_df, float(currency_dict[target_currency.upper()]))

        # Create a histogram plot of the property values.
        plt.figure(figsize=(10, 6))
        plt.hist(data)
        plt.xlabel(f'Price in {target_currency}')
        plt.ylabel('No of Houses')
        plt.title('Property Value Distribution')
        plt.savefig('property_value_distribution.png')

    @staticmethod
    def sales_trend(dataframe):
        # This method visualizes sales trends over the years using the provided dataframe

        # Extract the year from the 'sold_date' column by splitting the date string.
        dataframe['year'] = dataframe['sold_date'].str.split('/').str[2]

        # Count the number of sales per year.
        sales = dataframe['year'].value_counts()

        # Create a line plot to visualize the sales trends.
        plt.figure(figsize=(10, 6))
        plt.plot(sales.index, sales.values, color='blue')
        plt.xlabel('Year')
        plt.ylabel('No of Sales')
        plt.title('Sales Trends')
        # save the png file
        plt.savefig('sales_trend.png')

