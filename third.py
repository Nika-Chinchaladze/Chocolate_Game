from PyQt5 import QtCore, QtGui, QtWidgets
from four import Ui_Fourth_page
from time import sleep

class Ui_Third_page(object):

    def Fourth_Window(self):
        self.window4 = QtWidgets.QMainWindow()
        self.ui = Ui_Fourth_page()
        self.ui.setupUi(self.window4)
        self.window4.show()

    def setupUi(self, Third_page):
        Third_page.setObjectName("Third_page")
        Third_page.resize(381, 582)
        Third_page.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.centralwidget = QtWidgets.QWidget(Third_page)
        self.centralwidget.setObjectName("centralwidget")
        
        self.choose_label = QtWidgets.QLabel(self.centralwidget)
        self.choose_label.setGeometry(QtCore.QRect(10, 20, 361, 181))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.choose_label.setFont(font)
        self.choose_label.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.choose_label.setFrameShape(QtWidgets.QFrame.Box)
        self.choose_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choose_label.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_label.setObjectName("choose_label")
        
        self.picture_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.picture_label_3.setGeometry(QtCore.QRect(10, 230, 361, 191))
        self.picture_label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.picture_label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.picture_label_3.setText("")
        self.picture_label_3.setPixmap(QtGui.QPixmap("chocolate.jpg"))
        self.picture_label_3.setScaledContents(True)
        self.picture_label_3.setObjectName("picture_label_3")
        
        self.player_button = QtWidgets.QPushButton(self.centralwidget)
        self.player_button.setGeometry(QtCore.QRect(30, 460, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.player_button.setFont(font)
        self.player_button.setObjectName("player_button")
        
        self.computer_button = QtWidgets.QPushButton(self.centralwidget)
        self.computer_button.setGeometry(QtCore.QRect(220, 460, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.computer_button.setFont(font)
        self.computer_button.setObjectName("computer_button")
        
        Third_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Third_page)
        self.statusbar.setObjectName("statusbar")
        Third_page.setStatusBar(self.statusbar)

        self.retranslateUi(Third_page)
        QtCore.QMetaObject.connectSlotsByName(Third_page)

    def retranslateUi(self, Third_page):
        _translate = QtCore.QCoreApplication.translate
        Third_page.setWindowTitle(_translate("Third_page", "MainWindow"))
        self.choose_label.setText(_translate("Third_page", "Choose Who Starts The Game!"))
        self.player_button.setText(_translate("Third_page", "Player"))
        self.computer_button.setText(_translate("Third_page", "Computer"))

# ---------------------------------------------- LOGIC --------------------------------------------------- #
        # Call functions from buttons:
        self.player_button.clicked.connect(self.Fourth_Window)
        self.player_button.clicked.connect(self.Player_Started)
        self.player_button.clicked.connect(Third_page.close)

        self.computer_button.clicked.connect(self.Fourth_Window)
        self.computer_button.clicked.connect(self.Computer_Started)
        self.computer_button.clicked.connect(Third_page.close)
    
    # Connection, From Third_Page write Text In Fourth_Page: Boom!
    def Player_Started(self):
        self.ui.who_started_label.setText("Player Started")
        self.ui.total_label.setText(f'{184}')
        self.ui.left_label.setText(f'{184}')
    def Computer_Started(self):
        self.ui.who_started_label.setText("Computer Stared")
        self.ui.total_label.setText(f'{185}')
        # define Computer's First Bet:
        sleep(1)
        self.ui.enter_computer_label.setText(f'{1}')
        self.ui.left_label.setText(f'{184}')
# ------------------------------------------------ END ---------------------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Third_page = QtWidgets.QMainWindow()
    ui = Ui_Third_page()
    ui.setupUi(Third_page)
    Third_page.show()
    sys.exit(app.exec_())
