import sys
import pandas as pd
from PyQt5 import QtWidgets
import random
from PyQt5.QtCore import QTime
from my_form1 import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
import re
sys.setrecursionlimit(15000)  # Increase the limit if necessary

class MyDialog(QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.table_widget = self.ui.QTableWidget

        # Connect buttons
        self.ui.pushButton_2.clicked.connect(self.sort_column)  # Sort button
        self.ui.pushButton_3.clicked.connect(self.search_column)  # Search button

        # Connect header click signal to handle_column_click
        self.table_widget.horizontalHeader().sectionClicked.connect(self.handle_column_click)

        self.load_data()
        self.selected_column_index = -1  # Variable to store the selected column index

    def load_data(self):
        # Load data from CSV file
        try:
            self.data = pd.read_csv('C:\\Users\\Hp\\Music\\Semester 3rd\\Scrapping the data\\combined_ebay_mobile_data.csv')
            self.table_widget.setRowCount(self.data.shape[0])
            self.table_widget.setColumnCount(self.data.shape[1])
            self.table_widget.setHorizontalHeaderLabels(self.data.columns.tolist())
            for i in range(self.data.shape[0]):
                for j in range(self.data.shape[1]):
                    self.table_widget.setItem(i, j, QTableWidgetItem(str(self.data.iat[i, j])))
        except FileNotFoundError:
            print("File not found. Please check the file path.")

    def handle_column_click(self, column_index):
        # Handles the column click and stores the selected column index.
        print(f"Column {column_index} clicked")
        self.selected_column_index = column_index  # Save the clicked column index
        column_name = self.data.columns[column_index]  # Get the column name
        print(f"Selected column: {column_name}")

    def sort_column(self):
        # Sort the column selected by clicking the header.
        if self.selected_column_index == -1:
            print("No column selected. Please click on a column header to select.")
            return

        selected_column = self.data.columns[self.selected_column_index]  # Use the clicked column
        selected_algorithm = self.ui.comboBox.currentText()  # Get selected algorithm
        print(selected_algorithm)

        start_time = QTime.currentTime()  # Start time for performance measurement

        if selected_algorithm == "Bubble Sort":
            self.bubble_sort(selected_column)            
        elif selected_algorithm == "Insertion Sort ":
            self.insertion_sort(selected_column)
        elif selected_algorithm == "Selection Sort":
            self.selection_sort(selected_column)
        elif selected_algorithm == "Merge Sort ":
            self.merge_sort(selected_column)
        elif selected_algorithm == "Quick Sort":
            self.quick_sort(selected_column)
        elif selected_algorithm == "Counting Sort":
            self.counting_sort(selected_column)
        elif selected_algorithm == "Radix Sort":
            self.radix_sort(selected_column)
        elif selected_algorithm == "Bucket Sort":
            self.bucket_sort(selected_column)
        else:
            print("Unknown sorting algorithm selected.")

        elapsed_time = start_time.msecsTo(QTime.currentTime())
        print(f"Sorting completed in {elapsed_time} ms")

    def bubble_sort(self, column):
        
        print(f"Bubble Sort is running on column: {column}")

        # Extract the column data for sorting
        array = self.data[column].tolist()

        if column in ["Price", "Shipping Cost"]:
            # Helper function to clean and extract monetary values
            def clean_value(value):
                if "not found" in value.lower() or "not specified" in value.lower() or "free" in value.lower():
                    return None
                match = re.search(r'\$(\d{1,3}(?:,\d{3})*\.\d{2})', value)
                return float(match.group(1).replace(',', '')) if match else None

            # Clean and prepare the array for sorting
            cleaned_array = [(clean_value(val), val) for val in array]
            
            # Separate valid and invalid values
            valid_values = [item for item in cleaned_array if item[0] is not None]
            invalid_values = [item for item in cleaned_array if item[0] is None]

            # Bubble Sort on valid values (monetary ones)
            n = len(valid_values)
            for i in range(n - 1):
                swapped = False
                for j in range(0, n - i - 1):
                    if valid_values[j][0] > valid_values[j + 1][0]:
                        valid_values[j], valid_values[j + 1] = valid_values[j + 1], valid_values[j]
                        swapped = True
                if not swapped:
                    break

            # Combine sorted valid values with invalid ones
            sorted_array = [item[1] for item in valid_values] + [item[1] for item in invalid_values]
            self.data[column] = sorted_array

        elif column in ["Phone Name", "Condition"]:
            # Normalize for comparison
            def normalize(name):
                return name.strip().lower()

            # Bubble Sort implementation
            n = len(array)
            for i in range(n - 1):
                swapped = False
                for j in range(0, n - i - 1):
                    if normalize(array[j]) > normalize(array[j + 1]):
                        array[j], array[j + 1] = array[j + 1], array[j]
                        swapped = True
                if not swapped:
                    break
            self.data[column] = array

        elif column == "Seller Info":
            # Extract percentage ratings
            def extract_percentage(seller):
                match = re.search(r'(\d{1,3}\.\d)%', seller)
                return float(match.group(1)) if match else 0.0

            # Separate valid and invalid sellers
            valid_sellers = [seller for seller in array if "Seller info not found" not in seller]
            invalid_sellers = [seller for seller in array if "Seller info not found" in seller]

            # Bubble Sort on valid sellers
            n = len(valid_sellers)
            for i in range(n - 1):
                swapped = False
                for j in range(0, n - i - 1):
                    if extract_percentage(valid_sellers[j]) < extract_percentage(valid_sellers[j + 1]):
                        valid_sellers[j], valid_sellers[j + 1] = valid_sellers[j + 1], valid_sellers[j]
                        swapped = True
                if not swapped:
                    break

            # Combine sorted valid sellers with 'Seller info not found' entries
            sorted_array = valid_sellers + invalid_sellers
            self.data[column] = sorted_array

        elif column == "Quantity Sold":
            # Extract quantity sold
            def extract_quantity(sold_entry):
                match = re.search(r'(\d{1,3}(?:,\d{3})*)', sold_entry)
                return int(match.group(1).replace(',', '')) if match else 0

            # Separate valid and invalid sold entries
            valid_sold = [entry for entry in array if "Quantity sold not found" not in entry]
            invalid_sold = [entry for entry in array if "Quantity sold not found" in entry]

            # Bubble Sort on valid sold entries
            n = len(valid_sold)
            for i in range(n - 1):
                swapped = False
                for j in range(0, n - i - 1):
                    if extract_quantity(valid_sold[j]) > extract_quantity(valid_sold[j + 1]):
                        valid_sold[j], valid_sold[j + 1] = valid_sold[j + 1], valid_sold[j]
                        swapped = True
                if not swapped:
                    break

            # Combine sorted valid sold entries with invalid ones
            sorted_array = valid_sold + invalid_sold
            self.data[column] = sorted_array

        elif column == "Location":
            # Extract country from location
            def extract_country(location):
                match = re.search(r'from\s+(.+)', location)
                return match.group(1).strip().lower() if match else ''

            # Separate valid and invalid locations
            valid_locations = [location for location in array if "Location not found" not in location]
            invalid_locations = [location for location in array if "Location not found" in location]

            # Bubble Sort on valid locations based on country
            n = len(valid_locations)
            for i in range(n - 1):
                swapped = False
                for j in range(0, n - i - 1):
                    if extract_country(valid_locations[j]) > extract_country(valid_locations[j + 1]):
                        valid_locations[j], valid_locations[j + 1] = valid_locations[j + 1], valid_locations[j]
                        swapped = True
                if not swapped:
                    break

            # Combine sorted valid locations with invalid ones
            sorted_array = valid_locations + invalid_locations
            self.data[column] = sorted_array

        # Update the table with the sorted data
        self.update_table()


    def insertion_sort(self, column):
        print(f"Insertion Sort is running on column: {column}")

        array = self.data[column].tolist()
        n = len(array)

        for i in range(1, n):
            key = array[i]
            j = i-1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        
        self.data[column] = array
        self.update_table()

    def selection_sort(self, column):
        print(f"Selection Sort is running on column: {column}")
        array = self.data[column].tolist()

        # Selection Sort implementation
        n = len(array)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.compare(array[j], array[min_index]):
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]

        self.data[column] = array
        self.update_table()

    def merge_sort(self, column):
        
        print(f"Merge Sort is running on column: {column}")
        array = self.data[column].tolist()

        # Merge Sort implementation
        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if self.compare(left[i], right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        def sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = sort(arr[:mid])
            right = sort(arr[mid:])
            return merge(left, right)

        sorted_array = sort(array)
        self.data[column] = sorted_array
        self.update_table()


    def quick_sort(self, column):
        print(f"Quick Sort is running on column: {column}")

        try:
            array = self.data[column].tolist()  # Get the column data as a list
            print(f"Initial array length for sorting: {len(array)}")  # Debug: Show initial array length
            
            # Iterative Quick Sort implementation
            stack = [(0, len(array) - 1)]  # Stack to keep track of indices to sort

            while stack:
                low, high = stack.pop()
                if low < high:
                    pivot_index = self.partition(array, low, high)
                    stack.append((low, pivot_index - 1))  # Left part
                    stack.append((pivot_index + 1, high))  # Right part

            self.data[column] = array  # Update the sorted data back to the DataFrame
            self.update_table()  # Call method to update the table view
        except Exception as e:
            print(f"An error occurred during sorting: {e}")

    def partition(self, array, low, high):
        pivot = array[high]  # Choosing the last element as pivot
        i = low - 1  # Pointer for the smaller element
        for j in range(low, high):
            if self.compare(array[j], pivot):  # Compare function for ordering
                i += 1
                array[i], array[j] = array[j], array[i]  # Swap
        array[i + 1], array[high] = array[high], array[i + 1]  # Place the pivot in the correct position
        return i + 1

    def radix_sort(self, column):
        print(f"Radix Sort is running on column: {column}")

        # Check if the column contains numeric data
        if all(isinstance(i, (int, float)) for i in self.data[column]):
            def counting_sort_for_radix(array, exp):
                n = len(array)
                output = [0] * n
                count = [0] * 10

                for i in range(n):
                    index = int(array[i]) // exp
                    count[index % 10] += 1
                
                for i in range(1, 10):
                    count[i] += count[i - 1]

                for i in range(n - 1, -1, -1):
                    index = int(array[i]) // exp
                    output[count[index % 10] - 1] = array[i]
                    count[index % 10] -= 1

                for i in range(n):
                    array[i] = output[i]

            array = self.data[column].tolist()
            max_value = max(array)
            
            exp = 1
            while max_value // exp > 0:
                counting_sort_for_radix(array, exp)
                exp *= 10
            
            self.data[column] = array
        else:
            print("Radix Sort can only be applied to numeric data.")
            return

        self.update_table()


    def bucket_sort(self, column):
        print(f"Bucket Sort is running on column: {column}")

        # Check if the column contains numeric data
        if all(isinstance(i, (int, float)) for i in self.data[column]):
            array = self.data[column].tolist()
            max_value = max(array)
            bucket_count = 10  # Number of buckets
            buckets = [[] for _ in range(bucket_count)]

            for value in array:
                index = min(int(value * bucket_count / (max_value + 1)), bucket_count - 1)  # Ensure index is within bounds
                buckets[index].append(value)

            sorted_array = []
            for bucket in buckets:
                sorted_array.extend(sorted(bucket))

            self.data[column] = sorted_array
        else:
            print("Bucket Sort can only be applied to numeric data.")
            return

        self.update_table()


    def update_table(self):
        """Update the QTableWidget to reflect the sorted DataFrame."""
        self.table_widget.clearContents()  # Clear the current contents
        self.table_widget.setRowCount(self.data.shape[0])  # Set the new row count
        self.table_widget.setColumnCount(self.data.shape[1])  # Set the column count
        self.table_widget.setHorizontalHeaderLabels(self.data.columns.tolist())  # Reset headers
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(self.data.iat[i, j])))

    def search_column(self):
        selected_column = self.ui.comboBox_2.currentText()  # Get selected column for search
        search_term = self.ui.searchLineEdit.text()  # Get search term
        filter_type = self.ui.comboBox_2.currentText()  # Get filter type
        results = []

        if filter_type == "Contains":
            results = self.data[self.data[selected_column].str.contains(search_term, na=False)]
        elif filter_type == "Starts with":
            results = self.data[self.data[selected_column].str.startswith(search_term, na=False)]
        elif filter_type == "Ends with":
            results = self.data[self.data[selected_column].str.endswith(search_term, na=False)]

        # Clear the table and display search results
        self.update_table_with_results(results)

    def update_table_with_results(self, results):
        self.table_widget.clearContents()  # Clear existing table contents
        self.table_widget.setRowCount(results.shape[0])  # Set new row count
        for i in range(results.shape[0]):
            for j in range(results.shape[1]):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(results.iat[i, j])))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.show()
    sys.exit(app.exec_())
