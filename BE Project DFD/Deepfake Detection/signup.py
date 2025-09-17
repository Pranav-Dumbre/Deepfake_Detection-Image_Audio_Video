from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import PyQt5.QtWidgets as QtWidgets
#from login import Ui_Dialog
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from tkinter.constants import ALL
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re
import sys

import sys
import cv2
app1 = QtWidgets.QApplication(sys.argv)
screen = app1.primaryScreen()
size = screen.size()
BG_Image='A2.jpeg'
image = cv2.imread(BG_Image)
image=cv2.resize(image, (size.width(),size.height()))
cv2.imwrite('y.jpg', image)



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_signUp(object):

    def insertData(self):
        error = None
        username1 = self.uname_lineEdit.text()
        username = str(username1)
        email1 = self.email_lineEdit.text()
        if email1.find('@') == -1:
            error = True
            alrt = "please enter valid email"
            self.showdialog(alrt)
        else:
            email = str(email1)

        mob1 = self.mob_lineEdit.text()
        if len(mob1) != 10 or len(re.findall('\D', str(mob1), re.I)) > 0:
            error = True
            alrt = 'please enter valid number'
            self.showdialog(alrt)
        else:
            mob = str(mob1)
        password1 = self.password_lineEdit.text()
        password = str(password1)

        if not error:
            connection = sqlite3.connect("multiD.db")
            s = "insert into userdetails (username,email,mob,password) values('" + username + "','" + email + "','" + mob + "','" + password + "')"
            print("query is:-" + s)
            result = connection.execute(s)
            if result:
                s1 = "select * from userdetails"
                result = connection.execute(s1)
                print("Success  :: " + s1)
            connection.commit()
            connection.close()
            self.showmsg()

    def showmsg(self):
        self.showdialog1()

    def showdialog(self, alrt):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Registration Status")
        msg.setInformativeText(alrt)
        msg.setWindowTitle("Status")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        retval = msg.exec_()
        print
        "value of pressed message box button:", retval

    def showdialog1(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Registration Status")
        msg.setInformativeText("Registration successful")
        msg.setWindowTitle("Status")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        retval = msg.exec_()
        print
        "value of pressed message box button:", retval

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))

    def signInCheck(self):
        print("hello signin button")
        self.signInWindow = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        print("i'm in self signin")
        self.ui.setinUi(self.signInWindow)
        print("i'm in self setupUi method")
        self.signInWindow.show()
        print("i'm in self signin windows")

    def signInButton(self):
        self.signInCheck()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1200, 800)
        Dialog.setStyleSheet(_fromUtf8("background-image: url(Y.jpg); border: 2px solid orange"))
        # Dialog.setStyleSheet(_fromUtf8("border: 2px solid black"))


        # LABEL-1
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 100, 110, 30))
        self.label.setFont(QFont('Courier New', 10))
        self.label.setObjectName(_fromUtf8("label"))
        #font = QtGui.QFont()
        #font.setPointSize(12)
        #font.setBold(True)
        #font.setWeight(75)
        #self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.label.setStyleSheet("background-image: url(gray.jpg);;border: 2px solid red")

        # Lable-2
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 110, 20))
        self.label_2.setFont(QFont('Courier New', 10))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.label_2.setStyleSheet("background-image: url(gray.jpg);;border: 2px solid red")

        # Label-3
        self.label_M = QtWidgets.QLabel(Dialog)
        self.label_M.setGeometry(QtCore.QRect(50, 200, 110, 20))
        self.label_M.setFont(QFont('Courier New', 10))
        self.label_M.setObjectName(_fromUtf8("label_M"))
        self.label_M.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.label_M.setStyleSheet("background-image: url(gray.jpg);;border: 2px solid red")

        # Label-4
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 250, 110, 20))
        self.label_3.setFont(QFont('Courier New', 10))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.label_3.setStyleSheet("background-image: url(gray.jpg);;border: 2px solid red")

        
        # Username Edit
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(165, 100, 211, 27))
        self.uname_lineEdit.setFont(QFont('Courier New', 10))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
        self.uname_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.uname_lineEdit.setStyleSheet("background-image: url(gray.jpg);;border: 2px solid red")

        # Email Edit
        self.email_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(165, 150, 211, 27))
        self.email_lineEdit.setFont(QFont('Courier New', 10))
        self.email_lineEdit.setObjectName(_fromUtf8("email_lineEdit"))
        self.email_lineEdit.setStyleSheet("color: black")
        self.email_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.email_lineEdit.setStyleSheet("background-image: url(gray.jpg);;border: 2px solid red")

        # Mobile Edit
        self.mob_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.mob_lineEdit.setGeometry(QtCore.QRect(165, 200, 211, 27))
        self.mob_lineEdit.setFont(QFont('Courier New', 10))
        self.mob_lineEdit.setObjectName(_fromUtf8("mob_lineEdit"))
        self.mob_lineEdit.setStyleSheet("color: black")
        self.mob_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.mob_lineEdit.setStyleSheet("background-image: url(gray.jpg);;border: 2px solid red")

        # Password Edit
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(165, 250, 211, 27))
        self.password_lineEdit.setFont(QFont('Courier New', 10))
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.password_lineEdit.setStyleSheet("background-image: url(gray.jpg);;border: 2px solid red")

        # Signup Button
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(125, 300, 211, 27))
        self.signup_btn.setFont(QFont('Courier New', 10))
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        self.signup_btn.setStyleSheet("background-color: white")
        self.signup_btn.clicked.connect(self.insertData)
        self.signup_btn.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.signup_btn.setStyleSheet("background-image: url(milkwhite1.jpg);;border: 2px solid red")

        # Exit Button
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(125, 350, 211, 27))
        self.exit.setFont(QFont('Courier New', 10))
        self.exit.setObjectName(_fromUtf8("exit"))
        self.exit.setStyleSheet("background-color: white")
        self.exit.clicked.connect(self.closeall)
        self.exit.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.exit.setStyleSheet("background-image: url(milkwhite1.jpg);;border: 2px solid red")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def closeall(self):
        quit()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Registration Form", None))
        self.label.setText(_translate("Dialog", "NAME", None))
        self.label_2.setText(_translate("Dialog", "EMAIL", None))
        self.label_M.setText(_translate("Dialog", "MOBILE", None))
        self.label_3.setText(_translate("Dialog", "PASSWORD", None))
        self.signup_btn.setText(_translate("Dialog", "Click To Register", None))
        self.exit.setText(_translate("Dialog", "Click To Exit", None))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtGui.QMainWindow()
    Dialog = QtWidgets.QDialog()
    ui = Ui_signUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

