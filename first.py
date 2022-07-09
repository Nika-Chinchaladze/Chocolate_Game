from PyQt5 import QtCore, QtGui, QtWidgets
from second import Ui_Second_page


class Ui_First_page(object):

    def Second_Window(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Second_page()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, First_page):
        First_page.setObjectName("First_page")
        First_page.resize(381, 582)
        First_page.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.centralwidget = QtWidgets.QWidget(First_page)
        self.centralwidget.setObjectName("centralwidget")
        
        self.hello_label = QtWidgets.QLabel(self.centralwidget)
        self.hello_label.setGeometry(QtCore.QRect(10, 20, 361, 191))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.hello_label.setFont(font)
        self.hello_label.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.hello_label.setFrameShape(QtWidgets.QFrame.Box)
        self.hello_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hello_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hello_label.setObjectName("hello_label")
        
        self.picture_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.picture_label_1.setGeometry(QtCore.QRect(10, 230, 361, 191))
        self.picture_label_1.setFrameShape(QtWidgets.QFrame.Box)
        self.picture_label_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.picture_label_1.setText("")
        self.picture_label_1.setPixmap(QtGui.QPixmap("chocolate.jpg"))
        self.picture_label_1.setScaledContents(True)
        self.picture_label_1.setObjectName("picture_label_1")
        
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(110, 480, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        
        First_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(First_page)
        self.statusbar.setObjectName("statusbar")
        First_page.setStatusBar(self.statusbar)

        self.retranslateUi(First_page)
        QtCore.QMetaObject.connectSlotsByName(First_page)

    def retranslateUi(self, First_page):
        _translate = QtCore.QCoreApplication.translate
        First_page.setWindowTitle(_translate("First_page", "MainWindow"))
        self.hello_label.setText(_translate("First_page", "Welcome To Chocolate Game !"))
        self.start_button.setText(_translate("First_page", "START"))

# ------------------------------------- LOGIC ------------------------------------------------ #
        # Call functions from buttons:
        self.start_button.clicked.connect(self.Second_Window)
        self.start_button.clicked.connect(First_page.close)

# -------------------------------------- END ------------------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    First_page = QtWidgets.QMainWindow()
    ui = Ui_First_page()
    ui.setupUi(First_page)
    First_page.show()
    sys.exit(app.exec_())
