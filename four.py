from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from time import sleep
from five import Ui_Fifth_page


class Ui_Fourth_page(object):

    def Fifth_Window(self):
        self.window5 = QtWidgets.QMainWindow()
        self.ui = Ui_Fifth_page()
        self.ui.setupUi(self.window5)
        self.window5.show()

    def setupUi(self, Fourth_page):        
        Fourth_page.setObjectName("Fourth_page")
        Fourth_page.resize(381, 620)
        Fourth_page.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.centralwidget = QtWidgets.QWidget(Fourth_page)
        self.centralwidget.setObjectName("centralwidget")

        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(10, 40, 60, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.info_label.setFont(font)
        self.info_label.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.info_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.info_label.setObjectName("info_label")
        
        self.total_label = QtWidgets.QLabel(self.centralwidget)
        self.total_label.setGeometry(QtCore.QRect(70, 40, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.total_label.setFont(font)
        self.total_label.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.total_label.setFrameShape(QtWidgets.QFrame.Box)
        self.total_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.total_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.total_label.setObjectName("total_label")
        
        self.picture_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.picture_label_4.setGeometry(QtCore.QRect(10, 100, 361, 191))
        self.picture_label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.picture_label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.picture_label_4.setText("")
        self.picture_label_4.setPixmap(QtGui.QPixmap("chocolate.jpg"))
        self.picture_label_4.setScaledContents(True)
        self.picture_label_4.setObjectName("picture_label_4")

        self.leave_label = QtWidgets.QLabel(self.centralwidget)
        self.leave_label.setGeometry(QtCore.QRect(150, 40, 60, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.leave_label.setFont(font)
        self.leave_label.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.leave_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.leave_label.setObjectName("info_label")
        
        self.left_label = QtWidgets.QLabel(self.centralwidget)
        self.left_label.setGeometry(QtCore.QRect(210, 40, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.left_label.setFont(font)
        self.left_label.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.left_label.setFrameShape(QtWidgets.QFrame.Box)
        self.left_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.left_label.setObjectName("left_label")
        
        self.who_started_label = QtWidgets.QLabel(self.centralwidget)
        self.who_started_label.setGeometry(QtCore.QRect(100, 10, 171, 21))
        self.who_started_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.who_started_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.who_started_label.setText("")
        self.who_started_label.setAlignment(QtCore.Qt.AlignCenter)
        self.who_started_label.setObjectName("who_started_label")
        
        self.player_bet_label = QtWidgets.QLabel(self.centralwidget)
        self.player_bet_label.setGeometry(QtCore.QRect(20, 300, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player_bet_label.setFont(font)
        self.player_bet_label.setAlignment(QtCore.Qt.AlignCenter)
        self.player_bet_label.setObjectName("player_bet_label")
        
        self.comp_bet_label = QtWidgets.QLabel(self.centralwidget)
        self.comp_bet_label.setGeometry(QtCore.QRect(237, 300, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comp_bet_label.setFont(font)
        self.comp_bet_label.setAlignment(QtCore.Qt.AlignCenter)
        self.comp_bet_label.setObjectName("comp_bet_label")
        
        self.enter_player_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_player_label.setGeometry(QtCore.QRect(10, 340, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_player_label.setFont(font)
        self.enter_player_label.setFrameShape(QtWidgets.QFrame.Box)
        self.enter_player_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.enter_player_label.setText("")
        self.enter_player_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_player_label.setObjectName("enter_player_label")
        
        self.enter_computer_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_computer_label.setGeometry(QtCore.QRect(240, 340, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_computer_label.setFont(font)
        self.enter_computer_label.setFrameShape(QtWidgets.QFrame.Box)
        self.enter_computer_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.enter_computer_label.setText("")
        self.enter_computer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_computer_label.setObjectName("enter_computer_label")
        
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(150, 340, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet("background-color: rgb(94, 190, 141);")
        self.submit_button.setObjectName("submit_button")
        
        self.one_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Display("1"))
        self.one_button.setGeometry(QtCore.QRect(10, 410, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.one_button.setFont(font)
        self.one_button.setObjectName("one_button")
        
        self.two_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Display("2"))
        self.two_button.setGeometry(QtCore.QRect(110, 410, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.two_button.setFont(font)
        self.two_button.setObjectName("two_button")
        
        self.three_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Display("3"))
        self.three_button.setGeometry(QtCore.QRect(210, 410, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.three_button.setFont(font)
        self.three_button.setObjectName("three_button")
        
        self.six_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Display("6"))
        self.six_button.setGeometry(QtCore.QRect(210, 460, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.six_button.setFont(font)
        self.six_button.setObjectName("six_button")

        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(310, 460, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("ring_button")
        
        self.five_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Display("5"))
        self.five_button.setGeometry(QtCore.QRect(110, 460, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.five_button.setFont(font)
        self.five_button.setObjectName("five_button")
        
        self.four_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Display("4"))
        self.four_button.setGeometry(QtCore.QRect(10, 460, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.four_button.setFont(font)
        self.four_button.setObjectName("four_button")
        
        self.nine_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Display("9"))
        self.nine_button.setGeometry(QtCore.QRect(210, 510, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nine_button.setFont(font)
        self.nine_button.setObjectName("nine_button")
        
        self.eight_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Display("8"))
        self.eight_button.setGeometry(QtCore.QRect(110, 510, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eight_button.setFont(font)
        self.eight_button.setObjectName("eight_button")
        
        self.seven_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Display("7"))
        self.seven_button.setGeometry(QtCore.QRect(10, 510, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.seven_button.setFont(font)
        self.seven_button.setObjectName("seven_button")

        self.next_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.Display("7"))
        self.next_button.setGeometry(QtCore.QRect(10, 560, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.next_button.setFont(font)
        self.next_button.setStyleSheet("background-color:  rgb(170, 170, 255);")
        self.next_button.setObjectName("next_button")
        self.next_button.setEnabled(False)
        
        self.zero_button = QtWidgets.QPushButton(self.centralwidget)
        self.zero_button.setGeometry(QtCore.QRect(310, 410, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.zero_button.setFont(font)
        self.zero_button.setObjectName("zero_button")
        
        self.box_button = QtWidgets.QPushButton(self.centralwidget)
        self.box_button.setGeometry(QtCore.QRect(310, 510, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.box_button.setFont(font)
        self.box_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.box_button.setObjectName("box_button")
        self.box_button.setEnabled(False)
        
        Fourth_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Fourth_page)
        self.statusbar.setObjectName("statusbar")
        Fourth_page.setStatusBar(self.statusbar)

        self.retranslateUi(Fourth_page)
        QtCore.QMetaObject.connectSlotsByName(Fourth_page)

# ----------------------------------------------- LOGIC --------------------------------------------- #        
        # call functions from here:
        self.submit_button.clicked.connect(self.Submit_Bet)
        self.clear_button.clicked.connect(self.Remove)
        self.zero_button.clicked.connect(self.OneZero)
        self.box_button.clicked.connect(self.show_popup)
        self.next_button.clicked.connect(self.Fifth_Window)
        self.next_button.clicked.connect(Fourth_page.close)
            
        
    # decline first zero and only one zero in the second position:
    def OneZero(self):
        screen = self.enter_player_label.text()
        if '5' in screen or '6' in screen or '7' in screen or '8' in screen or '9' in screen:
            self.enter_player_label.setText(f'{screen}')
        elif len(screen) == 1:
            self.enter_player_label.setText(f'{screen}0')


    # display buttons method:
    def Display(self, pressed):
        screen = self.enter_player_label.text()
        comp_screen = self.enter_computer_label.text()

        # remove symbols from Computer's Bet Label:
        if len(self.enter_computer_label.text()) >= 1 and comp_screen[0] != 'W':
            self.enter_computer_label.setText("")        
        
        # after loosing no more printing:
        if self.enter_player_label.text() == 'Empty Bets!':
            self.enter_player_label.setText(f'{screen}')
        # decline big bets -> more than 45:
        elif '5' in screen or '6' in screen or '7' in screen or '8' in screen or '9' in screen:
            self.enter_player_label.setText(f'{screen}')
        elif len(screen) == 2:
            self.enter_player_label.setText(f'{screen}')
        else:
            self.enter_player_label.setText(f'{screen}{pressed}')
    
    # remember participant's entries:   
    global answer
    global player_bets
    global computer_bets
    answer = []
    player_bets = []
    computer_bets = []

    # define method for submit button:
    def Submit_Bet(self):
        Leftlabel = int(self.left_label.text())
        
        # Player's Bet:
        entered = int(self.enter_player_label.text())
        player_bets.append(entered)
        # Action:
        self.left_label.setText(str(Leftlabel - entered))
        self.enter_player_label.setText("")

        # answer from computer, here is defined -> how much computer must take to win:
        sleep(2)
        Leftlabel = int(self.left_label.text())    
        if Leftlabel > 46:
            self.enter_computer_label.setText(f'{46 - entered}')
            comp_bet = int(self.enter_computer_label.text())
            self.left_label.setText(str(Leftlabel - comp_bet))
            computer_bets.append(comp_bet)
        
        elif Leftlabel < 46:
            self.enter_computer_label.setText(f'Winning Bet: {Leftlabel}')
            computer_bets.append(Leftlabel)
            self.left_label.setText(f'{0}')
            self.enter_player_label.setText('Empty Bets!')
        
        if self.enter_player_label.text() == "Empty Bets!":
            self.submit_button.setEnabled(False)
            self.box_button.setEnabled(True)
            self.next_button.setEnabled(True)
    
    # define method for clear_button:
    def Remove(self):
        screen = self.enter_player_label.text()
        if screen != "Empty Bets!":
            screen = screen[:-1]
            self.enter_player_label.setText(screen)
    
    # define method fro message_box:
    def show_popup(self, i):
        msg = QMessageBox()
        msg.setWindowTitle("Entered Values!")
        msg.setText("Here You Can See The Results!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Cancel)
        msg.setInformativeText("Computer Won The Game!")

        if self.who_started_label.text() == "Player Started":
            first_row = str('Player VS Computer')
            second_row = f'1) {player_bets[0]}  :  {computer_bets[0]}'
            third_row = f'2) {player_bets[1]}  :  {computer_bets[1]}'
            fourth_row = f'3) {player_bets[2]}  :  {computer_bets[2]}'
            fifth_row = f'4) {player_bets[3]}  :  {computer_bets[3]}'
            
            msg.setDetailedText(f'{first_row} \n{second_row} \n{third_row} \n{fourth_row} \n{fifth_row}')
        
        elif self.who_started_label.text() == "Computer Stared":
            first_row = str('Player VS Computer')
            begin = str('1) None  :  1')
            second_row = f'2) {player_bets[0]}  :  {computer_bets[0]}'
            third_row = f'3) {player_bets[1]}  :  {computer_bets[1]}'
            fourth_row = f'4) {player_bets[2]}  :  {computer_bets[2]}'
            fifth_row = f'5) {player_bets[3]}  :  {computer_bets[3]}'
            
            msg.setDetailedText(f'{first_row} \n{begin} \n{second_row} \n{third_row} \n{fourth_row} \n{fifth_row}')

        x = msg.exec_()

    

        
# ------------------------------------------------- END --------------------------------------------- #

    def retranslateUi(self, Fourth_page):
        _translate = QtCore.QCoreApplication.translate
        Fourth_page.setWindowTitle(_translate("Fourth_page", "MainWindow"))
        self.player_bet_label.setText(_translate("Fourth_page", "Player\'s Bet"))
        self.comp_bet_label.setText(_translate("Fourth_page", "Computer\'s Bet"))
        self.submit_button.setText(_translate("Fourth_page", "Submit"))
        self.one_button.setText(_translate("Fourth_page", "1"))
        self.two_button.setText(_translate("Fourth_page", "2"))
        self.three_button.setText(_translate("Fourth_page", "3"))
        self.six_button.setText(_translate("Fourth_page", "6"))
        self.five_button.setText(_translate("Fourth_page", "5"))
        self.four_button.setText(_translate("Fourth_page", "4"))
        self.nine_button.setText(_translate("Fourth_page", "9"))
        self.eight_button.setText(_translate("Fourth_page", "8"))
        self.seven_button.setText(_translate("Fourth_page", "7"))
        self.zero_button.setText(_translate("Fourth_page", "0"))
        self.box_button.setText(_translate("Fourth_page", "Msg.Box"))
        self.left_label.setText(_translate("Fourth_page", ""))
        self.leave_label.setText(_translate("Fourth_page", "Left:"))
        self.total_label.setText(_translate("Fourth_page", ""))
        self.info_label.setText(_translate("Fourth_page", "Total:"))
        self.clear_button.setText(_translate("Fourth_page", "C"))
        self.next_button.setText(_translate("Fourth_page", "NEXT"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fourth_page = QtWidgets.QMainWindow()
    ui = Ui_Fourth_page()
    ui.setupUi(Fourth_page)
    Fourth_page.show()
    sys.exit(app.exec_())
