# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(784, 662)
        Dialog.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.0454545, y1:0.454545, x2:1, y2:0, stop:0 rgba(118, 38, 65, 255), stop:1 rgba(255, 255, 255, 255))")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 61))
        self.label.setStyleSheet("\n"
"font: 48pt \"Showcard Gothic\";\n"
"background-color: transparent;\n"
"border: none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 71, 21))
        self.label_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"font: 18pt \"Algerian\";\n"
"background-color: transparent;\n"
"border: none;\n"
"color:white")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 80, 271, 20))
        self.lineEdit.setStyleSheet("background-color: transparent;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 80, 91, 17))
        self.pushButton.setStyleSheet("background-color: transparent;\n"
"font: 9pt \"Algerian\";\n"
"border: 2px solid white;\n"
"background-color: transparent;\n"
"color:white")
        self.pushButton.setObjectName("pushButton")
        self.gridWidget = QtWidgets.QWidget(Dialog)
        self.gridWidget.setGeometry(QtCore.QRect(30, 130, 771, 141))
        self.gridWidget.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px; /* Optional: Adds rounded corners */")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.QTableWidget = QtWidgets.QTableWidget(self.gridWidget)
        self.QTableWidget.setStyleSheet("border: 2px solid white;\n"
"background-color: transparent;")
        self.QTableWidget.setObjectName("QTableWidget")
        self.QTableWidget.setColumnCount(8)
        self.QTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.QTableWidget.setHorizontalHeaderItem(7, item)
        self.gridLayout.addWidget(self.QTableWidget, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(40, 290, 111, 20))
        self.comboBox.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"font: 87 10pt \"Arial Black\";\n"
"border: 1px solid white;\n"
"background-color: transparent;\n"
"color:white")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 290, 91, 16))
        self.pushButton_2.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;\n"
"font: 87 8pt \"Arial Black\";\n"
"color:white")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 280, 161, 21))
        self.lineEdit_2.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(630, 280, 91, 21))
        self.comboBox_2.setStyleSheet("border: 1px solid white;\n"
"font: 87 9pt \"Arial Black\";\n"
"background-color: transparent;\n"
"color:white;\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(740, 280, 51, 21))
        self.pushButton_3.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 87 9pt \"Arial Black\";\n"
"color:white")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 360, 191, 20))
        self.label_3.setStyleSheet("\n"
"background-color: transparent;\n"
"color:white;\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 390, 131, 21))
        self.lineEdit_3.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(180, 390, 61, 21))
        self.comboBox_3.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color:white")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 390, 113, 21))
        self.lineEdit_4.setStyleSheet("border: 1px solid white;\n"
"background-color: transparent;")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "             ScrapeSort Nexus"))
        self.label_2.setText(_translate("Dialog", "Enter"))
        self.pushButton.setText(_translate("Dialog", "Scrapp Data"))
        item = self.QTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Rows"))
        item = self.QTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Phone Names"))
        item = self.QTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Condition"))
        item = self.QTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Price"))
        item = self.QTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Shipping Cost"))
        item = self.QTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Location"))
        item = self.QTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Seller Info"))
        item = self.QTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Quantity Sold"))
        self.comboBox.setItemText(0, _translate("Dialog", "Bubble Sort"))
        self.comboBox.setItemText(1, _translate("Dialog", "Selection Sort"))
        self.comboBox.setItemText(2, _translate("Dialog", "Insertion Sort "))
        self.comboBox.setItemText(3, _translate("Dialog", "Merge Sort "))
        self.comboBox.setItemText(4, _translate("Dialog", "Quick Sort"))
        self.comboBox.setItemText(5, _translate("Dialog", "Counting Sort"))
        self.comboBox.setItemText(6, _translate("Dialog", "Radix Sort"))
        self.comboBox.setItemText(7, _translate("Dialog", "Bucket Sort"))
        self.pushButton_2.setText(_translate("Dialog", "Sort Column"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Contains"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Starts withs"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Ends withs"))
        self.pushButton_3.setText(_translate("Dialog", "Search"))
        self.label_3.setText(_translate("Dialog", " Multi column sorting"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "AND"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "OR"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "NOT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.showMaximized()
    sys.exit(app.exec_())
