import sys
from PyQt5 import QtWidgets, uic

class MyApp(QtWidgets.QDialog):
    def __init__(self):
        super(MyApp, self).__init__()
        # Load the UI file
        uic.loadUi('C:\\Users\\Hp\\Music\\Semester 3rd\\Scrapping the data\\my_frame.ui', self)

        self.pushButton.clicked.connect(self.load_data)  
        
        self.show()

    def load_data(self):
        print("Loading data...")

    def sort_column(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
