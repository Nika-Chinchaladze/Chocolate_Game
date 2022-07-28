from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Fifth_page(object):

    def Try_Again(self):
        from third import Ui_Third_page

        self.window2pac = QtWidgets.QMainWindow()
        self.again = Ui_Third_page()
        self.again.setupUi(self.window2pac)
        self.window2pac.show()

    def setupUi(self, Fifth_page):
        Fifth_page.setObjectName("Fifth_page")
        Fifth_page.resize(381, 600)
        Fifth_page.setStyleSheet("background-color: rgb(238, 238, 238);")
        
        self.centralwidget = QtWidgets.QWidget(Fifth_page)
        self.centralwidget.setObjectName("centralwidget")
        
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(10, 10, 361, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.result_label.setFont(font)
        self.result_label.setFrameShape(QtWidgets.QFrame.Box)
        self.result_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setWordWrap(True)
        self.result_label.setObjectName("result_label")
        
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(80, 530, 221, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.close_button.setFont(font)
        self.close_button.setObjectName("close_button")

        self.try_button = QtWidgets.QPushButton(self.centralwidget)
        self.try_button.setGeometry(QtCore.QRect(80, 450, 221, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.try_button.setFont(font)
        self.try_button.setObjectName("try_button")
        
        self.try_picture_label = QtWidgets.QLabel(self.centralwidget)
        self.try_picture_label.setGeometry(QtCore.QRect(10, 120, 361, 301))
        self.try_picture_label.setFrameShape(QtWidgets.QFrame.Box)
        self.try_picture_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.try_picture_label.setText("")
        self.try_picture_label.setPixmap(QtGui.QPixmap("try.jpg"))
        self.try_picture_label.setScaledContents(True)
        self.try_picture_label.setObjectName("try_picture_label")
        
        Fifth_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Fifth_page)
        self.statusbar.setObjectName("statusbar")
        Fifth_page.setStatusBar(self.statusbar)

        self.retranslateUi(Fifth_page)
        QtCore.QMetaObject.connectSlotsByName(Fifth_page)

# ---------------------------------------------- LOGIC ----------------------------------------- #
        # call functions from here:
        self.close_button.clicked.connect(Fifth_page.close)
        self.try_button.clicked.connect(self.Try_Again)
        self.try_button.clicked.connect(Fifth_page.close)

# ----------------------------------------------- END ------------------------------------------- #

    def retranslateUi(self, Fifth_page):
        _translate = QtCore.QCoreApplication.translate
        Fifth_page.setWindowTitle(_translate("Fifth_page", "MainWindow"))
        self.result_label.setText(_translate("Fifth_page", "Computer Won The Game! All Chocolates Stay Here!"))
        self.close_button.setText(_translate("Fifth_page", "Close"))
        self.try_button.setText(_translate("Fifth_page", "Try Again"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fifth_page = QtWidgets.QMainWindow()
    ui = Ui_Fifth_page()
    ui.setupUi(Fifth_page)
    Fifth_page.show()
    sys.exit(app.exec_())
