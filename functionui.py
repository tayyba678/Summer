import sys
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QComboBox, QLineEdit, QPushButton
from PyQt5.QtCore import QTime

# Import the class generated from the .ui file (your my_form1.py)
from my_form1 import Ui_Dialog  # Replace `Ui_Dialog` with the class name in my_form1.py

class MyDialog(QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.ui = Ui_Dialog()  
        self.ui.setupUi(self)  
        self.table_widget = self.ui.QTableWidget  

        # Connect buttons using the correct button names
        self.ui.pushButton_2.clicked.connect(self.sort_column)  # Connect to Sort Column Button
        self.ui.pushButton_3.clicked.connect(self.search_column)  # Connect to Search Button

        self.load_data()
        
    def load_data(self):
        # Load data from CSV file
        try:
            self.data = pd.read_csv('C:/Users/Hp/Music/Semester 3rd/Scrapping the data/combined_ebay_mobile_data.csv')
            self.update_table()  # Initial table display
        except FileNotFoundError:
            print("File not found. Please check the file path.")

    def update_table(self):
        self.table_widget.clearContents()  # Clear existing table contents
        self.table_widget.setRowCount(self.data.shape[0])  # Set new row count
        self.table_widget.setColumnCount(self.data.shape[1])  # Ensure the column count is set
        self.table_widget.setHorizontalHeaderLabels(self.data.columns.tolist())  # Reset headers
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(self.data.iat[i, j])))

    def sort_column(self):
        selected_column = self.ui.comboBox.currentText()  # Get selected column
        selected_algorithm = self.ui.comboBox_2.currentText()  # Get selected algorithm
        start_time = QTime.currentTime()  # Start time for measuring performance

        if selected_algorithm == "Bubble Sort":
            self.bubble_sort(selected_column)
        elif selected_algorithm == "Insertion Sort":
            self.insertion_sort(selected_column)
        # Add other algorithms here...
        
        elapsed_time = start_time.msecsTo(QTime.currentTime())
        print(f"Sorting completed in {elapsed_time} ms")
        self.update_table()  # Refresh the table widget after sorting

    def bubble_sort(self, column):
        print("Bubble Sort is running...")
        # Extract the column data for sorting
        column_index = self.data.columns.get_loc(column)  # Get the column index
        array = self.data[column].tolist()  # Convert column to list
        n = len(array)

        # Bubble sort implementation
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    # Swap the values in the DataFrame as well
                    array[j], array[j + 1] = array[j + 1], array[j]
                    self.data.iloc[j, column_index], self.data.iloc[j + 1, column_index] = \
                        self.data.iloc[j + 1, column_index], self.data.iloc[j, column_index]

    def insertion_sort(self, column):
        print("Insertion Sort is running...")
        column_index = self.data.columns.get_loc(column)
        array = self.data[column].tolist()

        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        
            # Update the DataFrame with sorted data
            self.data.iloc[j + 1, column_index] = key

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
