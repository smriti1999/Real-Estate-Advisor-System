from data_visualiser import DataVisualiser
from dataextractor import DataExtractor
from datafinder import DataFinder


# This function displays a menu of options for data analysis,visualizing
def menu():
    print("Menu:")
    print("1.Suburb summary")
    print("2.Average land size in suburb")
    print("3.property value distribution graph")
    print("4.sales trend graph")
    print("5.Identifying property based on the price in suburb")
    print("6.exit")


# This function serves as the main program for the property investment advisor system.
def main():
    # Define a dictionary for currency conversion rates.
    currency_dict = {"AUD": 1, "USD": 0.66, "INR": 54.25, "CNY": 4.72, "JPY": 93.87, "HKD": 5.12,
                     "KRW": 860.92, "GBP": 0.51, "EUR": 0.60, "SGD": 0.88}
    print("starting the property investment advisor system..")
    currency_type = "AUD"  # Set the default currency type to Australian Dollars (AUD).
    print("loading data..")

    # Load property data from a CSV file.
    data = DataExtractor.extract_property_info('property_information.csv')
    suburb = input("Enter the suburb name or all to view details based on selection :")

    # Validate that the input contains only alphabetic characters.
    while not suburb.isalpha():
        print("Invalid suburb selected,please try again")
        suburb = input("Enter the suburb name or all to view details based on selection :")
    menu()

    # Prompt the user to enter a choice from the menu.
    choice = input("enter the choice:")
    while True:
        if choice == "1":
            DataExtractor.suburb_summary(data, suburb)
        elif choice == "2":
            land_size = DataExtractor.avg_land_size(data, suburb)
            if land_size is not None:
                print(f"Average Land Size for {suburb.capitalize()} is {round(land_size, ndigits=3)} square meters")
            else:
                print("No data available")
        elif choice == "3":
            currency_type = input("please currency type you want(INR/AUD/ etc):")
            try:
                DataVisualiser.prop_val_distribution(data, suburb, currency_type)
            except ValueError:
                print("Invalid currency type entered")
        elif choice == "4":
            DataVisualiser.sales_trend(data)
        elif choice == "5":
            try:
                target_price = input(f"Enter the amount you want to invest in digits for {currency_type}:")
                data['price_changed'] = DataExtractor.currency_exchange(data, currency_dict[currency_type.upper()])
                if DataFinder.locate_price(int(target_price), data, suburb):
                    print("The property is available!!")
                else:
                    print("The property is not available")
            except ValueError:
                print("Invalid target price entered")
        elif choice == "6":
            break
        else:
            print("Invalid choice..")
        menu()
        choice = input("enter the choice:")


if __name__ == "__main__":
    main()

# test code for dataextractor.py
# extractor = DataExtractor()
# df = extractor.extract_property_info('property_information.csv')
# print(len(df)) # output: 118771
# exchange_array = extractor.currency_exchange(df, 1)
# print(len(exchange_array)) # output: 118771
# extractor.suburb_summary(df, 'clayton') # prints summary of the suburb
# extractor.avg_land_size(df, 'clayton')  # output: 570.42

# testcode for data_visualiser.py
# visualiser = DataVisualiser()
# visualiser.prop_val_distribution(df, 'all', target_currency="AUD")
# generates the histogram graph

# visualiser.sales_trend(df)
# generates line chart

# testcode for datafinder.py
# target_price = 965000
# df['exchange_price']=extractor.currency_exchange(df,1)
# locate_price(target_price, df, 'Clayton')
# output : The property is available
