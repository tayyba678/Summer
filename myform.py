import sys
from PyQt5 import QtWidgets, uic

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        # Load the .ui file
        uic.loadUi('my_form.ui', self)

        # Example: Connect a button to a function
        self.my_button = self.findChild(QtWidgets.QPushButton, 'my_button')  # Replace with your button's object name
        self.my_button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
