class DataFinder:
    @staticmethod
    def reverse_insertion_sort(target_list): # This is a static method for sorting a list in reverse order .
        for i in range(1, len(target_list)): # Loop through the list, starting from the second element (index 1).
            curr_num = target_list[i] # Get the current number to be inserted in the sorted section of the list.
            j = i - 1  # Initialize 'j' to the index before the current element.
            # While 'j' is greater than or equal to 0 and the current number is greater.
            # than the element at index 'j', shift the elements to the right to make space for 'curr_num'
            while j >= 0 and curr_num > target_list[j]:
                target_list[j + 1] = target_list[j]
                j -= 1
            target_list[j + 1] = curr_num # Insert 'curr_num' into the sorted section of the list
        return target_list # Return the sorted list in reverse order.

    @staticmethod
    def binary_search(sorted_list, target): # This function performs a binary search on a sorted list
        # Initialize the lower and upper bounds for the search.
        low = 0
        high = len(sorted_list) - 1
        while low <= high: # Continue the search while the lower bound is less than or equal to the upper bound.
            mid = (low + high) // 2
            # Check if the middle element is equal to the target.
            if sorted_list[mid] == target:
                return True
            # If the target is smaller than the middle element, update the upper bound.
            elif target > sorted_list[mid]:
                high = mid - 1
            else:   # If the target is larger than the middle element, update the lower bound.
                low = mid + 1
        return False # If the loop exits , return False

    @staticmethod
    # This function attempts to locate a target price in a dataset based on a target suburb
    def locate_price(target_price, data, target_suburb):
        try:
            # Filter the data based on the target suburb and capitalize the input
            suburb_data = data[data['suburb'] == target_suburb.capitalize()]
            # Extract the 'price_changed' column from the filtered data and sort it in reverse order.
            sorted_data = DataFinder.reverse_insertion_sort(suburb_data['price_changed'].tolist())
            return DataFinder.binary_search(sorted_data, target_price)
        except ValueError: # Handle an exception if the input price is not valid.
            print("Not a valid price input")
