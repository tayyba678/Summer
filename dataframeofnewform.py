import sys
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

# Import the class generated from the .ui file (your my_form1.py)
from my_form1 import Ui_Dialog  # Replace `Ui_Dialog` with the class name in my_form1.py

class MyDialog(QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.ui = Ui_Dialog()  # Instantiate the UI class from my_form1.py
        self.ui.setupUi(self)  # Set up the UI
        self.table_widget = self.ui.QTableWidget  # Access table widget from UI

        if self.table_widget is None:
            print("tableWidget not found. Check the object name in the UI file.")
            return
        
        self.load_data()

    def load_data(self):
        # Load data from CSV file
        try:
            data = pd.read_csv('C:/Users/Hp/Music/Semester 3rd/Scrapping the data/ebay_mobile_samsung.csv')
            # Set the row count and column count
            self.table_widget.setRowCount(data.shape[0])
            self.table_widget.setColumnCount(data.shape[1])
            # Set the headers
            self.table_widget.setHorizontalHeaderLabels(data.columns.tolist())            
            # Populate the table with data
            for i in range(data.shape[0]):
                for j in range(data.shape[1]):
                    self.table_widget.setItem(i, j, QTableWidgetItem(str(data.iat[i, j])))
        except FileNotFoundError:
            print("File not found. Please check the file path.")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog() 
    window.show()
    sys.exit(app.exec_())
