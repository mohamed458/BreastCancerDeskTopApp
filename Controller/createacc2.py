# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\moham\BreastCancerDeskTop\createacc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys,signupres

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1198, 800)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1201, 801))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(500, 50, 251, 91))
        font = QtGui.QFont()
        font.setFamily("12 Calibri")
        font.setPointSize(42)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 42pt bold \"Calibri\";\n"
"color:rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 381, 41))
        self.label_2.setStyleSheet("font: 75 20pt bold \"Calibri\";\n"
"color:rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.emailfield = QtWidgets.QLineEdit(self.bgwidget)
        self.emailfield.setGeometry(QtCore.QRect(40, 310, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.emailfield.setFont(font)
        self.emailfield.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:2px solid rgpa(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82 , 101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;")
        self.emailfield.setObjectName("emailfield")
        self.passwordfield = QtWidgets.QLineEdit(self.bgwidget)
        self.passwordfield.setGeometry(QtCore.QRect(40, 400, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.passwordfield.setFont(font)
        self.passwordfield.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:2px solid rgpa(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82 , 101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;")
        self.passwordfield.setObjectName("passwordfield")
        self.error = QtWidgets.QLabel(self.bgwidget)
        self.error.setGeometry(QtCore.QRect(440, 540, 341, 20))
        self.error.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color:red;")
        self.error.setText("")
        self.error.setObjectName("error")
        self.confirmpasswordfield = QtWidgets.QLineEdit(self.bgwidget)
        self.confirmpasswordfield.setGeometry(QtCore.QRect(40, 490, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.confirmpasswordfield.setFont(font)
        self.confirmpasswordfield.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:2px solid rgpa(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82 , 101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;")
        self.confirmpasswordfield.setObjectName("confirmpasswordfield")
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 0, 781, 801))
        self.label_3.setStyleSheet("background-image:url(:/im/—Pngtree—pink ribbon of breast cancer_8423017.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.signup = QtWidgets.QPushButton(self.bgwidget)
        self.signup.setGeometry(QtCore.QRect(510, 610, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.signup.setFont(font)
        self.signup.setStyleSheet("QPushButton#signup{\n"
"    Background-color:rgba(85,98,112,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"} \n"
"QPushButton#signup:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(254, 81, 171, 0.8);\n"
"    background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#signup:hover{\n"
"    background-color:rgba(254, 81, 171, 0.8)\n"
"}")
        self.signup.setObjectName("signup")
        self.back = QtWidgets.QPushButton(self.bgwidget)
        self.back.setGeometry(QtCore.QRect(480, 670, 341, 51))
        self.back.setStyleSheet("background-color:rgba(0,0,0,0);text-decoration: underline;QLabel:hover;color:rgb(0, 0, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.back.setObjectName("back")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sign Up"))
        self.label_2.setText(_translate("Dialog", "Register a new account"))
        self.emailfield.setPlaceholderText(_translate("Dialog", "UserName"))
        self.passwordfield.setPlaceholderText(_translate("Dialog", "Password"))
        self.confirmpasswordfield.setPlaceholderText(_translate("Dialog", "Confirm Password"))
        self.signup.setText(_translate("Dialog", "S i g n u p"))
        self.back.setText(_translate("Dialog", "Already have account"))
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Dialog()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
