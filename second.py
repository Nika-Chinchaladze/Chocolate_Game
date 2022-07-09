from PyQt5 import QtCore, QtGui, QtWidgets
from third import Ui_Third_page


class Ui_Second_page(object):

    def Third_Window(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = Ui_Third_page()
        self.ui.setupUi(self.window3)
        self.window3.show()

    def setupUi(self, Second_page):
        Second_page.setObjectName("Second_page")
        Second_page.resize(381, 582)
        Second_page.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.centralwidget = QtWidgets.QWidget(Second_page)
        self.centralwidget.setObjectName("centralwidget")
        
        self.rule_label = QtWidgets.QLabel(self.centralwidget)
        self.rule_label.setGeometry(QtCore.QRect(10, 20, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.rule_label.setFont(font)
        self.rule_label.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.rule_label.setFrameShape(QtWidgets.QFrame.Box)
        self.rule_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rule_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rule_label.setObjectName("rule_label")
        
        self.picture_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.picture_label_2.setGeometry(QtCore.QRect(10, 230, 361, 191))
        self.picture_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.picture_label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.picture_label_2.setText("")
        self.picture_label_2.setPixmap(QtGui.QPixmap("chocolate.jpg"))
        self.picture_label_2.setScaledContents(True)
        self.picture_label_2.setObjectName("picture_label_2")
        
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(110, 480, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_button.setFont(font)
        self.next_button.setObjectName("next_button")
        
        self.instruction_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.instruction_label_2.setGeometry(QtCore.QRect(10, 100, 361, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.instruction_label_2.setFont(font)
        self.instruction_label_2.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"color: rgb(0, 170, 0);")
        self.instruction_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.instruction_label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.instruction_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.instruction_label_2.setWordWrap(True)
        self.instruction_label_2.setObjectName("instruction_label_2")
        
        Second_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Second_page)
        self.statusbar.setObjectName("statusbar")
        Second_page.setStatusBar(self.statusbar)

        self.retranslateUi(Second_page)
        QtCore.QMetaObject.connectSlotsByName(Second_page)

    def retranslateUi(self, Second_page):
        _translate = QtCore.QCoreApplication.translate
        Second_page.setWindowTitle(_translate("Second_page", "MainWindow"))
        self.rule_label.setText(_translate("Second_page", "Game Rules !"))
        self.next_button.setText(_translate("Second_page", "NEXT"))
        self.instruction_label_2.setText(_translate("Second_page", f'1) In the beginning Player Can Choose, Who starts the Game \
                                                                 \n2) There are concrete amount of chocolates on the table and Maximum Bet is 45 \
                                                                 \n3) To win the Game Participant Must take every chocolate from the table, During the Last Try! \
                                                                 \n4) It means that, during the Last Try There must be 45 or Less amount of chocolates on the table'))

# ---------------------------------------------- LOGIC --------------------------------------------------- #
        # Call functions from buttons:
        self.next_button.clicked.connect(self.Third_Window)
        self.next_button.clicked.connect(Second_page.close)

# ------------------------------------------------ END ---------------------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Second_page = QtWidgets.QMainWindow()
    ui = Ui_Second_page()
    ui.setupUi(Second_page)
    Second_page.show()
    sys.exit(app.exec_())
