from PyQt5 import QtCore, QtGui
import numpy as np
import pandas as pd
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets

from help_window import Ui_MainWindow as um
file_pass = 'C:/Users/user/jypyter정리/18-1자유학기/주가예측프로젝트/demo/미니프로젝트'

class Ui_MainWindow(QMainWindow):
    def __init__(self,parent=None):
        #테이블widget에서 보여질 추천 종목 데이터(array 또는 pandas 형식)
        super(Ui_MainWindow, self).__init__(parent)
        self.df_test=np.load('./invest_0601_array.npy')
        self.setupUi(self)

#도움말 클릭하면 열릴 새로운 페이지       
    def openWindow(self):
        
        self.Window=QtWidgets.QMainWindow()    
        self.ui=um() 
        self.ui.setupUi(self.Window)
        self.Window.show()
        
#프로그램 실행하면 보여질 UI들 setup
    def setupUi(self, MainWindow):

        MainWindow.resize(675, 730)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        #메인 화면 구성. 여기다가 스택위젯 넣고, 그 스택위젯의 인덱스 번호가 바껴가면서 화면이 변경
        self.Main_Window = QWidget(MainWindow)

        #stackedWidget 인스턴스 생성
        self.stackedWidget = QStackedWidget(self.Main_Window)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 675, 730))
        
        #MainWidget 구성 (처음 보여지는 메인 위젯) - stackedWidget index = 0
        self.centralwidget = QWidget(MainWindow)
        self.mainWidget()
        self.Num_mainWidget=self.stackedWidget.addWidget(self.centralwidget)
    
        self.RecommendTableWidgetData()
        
        
        # find Widget 구성 (검색창 뜨는 위젯) - stackedWidget index = 2
        self.find_widget = QWidget()
        self.setFindStock()
        self.Num_findWidget = self.stackedWidget.addWidget(self.find_widget) 
    
        
        
        #메인 화면 보여지기 (stackedwidget의 메인 위젯이랑 다른 개념)
        MainWindow.setCentralWidget(self.Main_Window)
        
        #메인 화면의 제목 이름과 버튼이름들 설정
        self.retranslateUi(MainWindow)
        
        #처음에 보여질 widget
        self.stackedWidget.setCurrentIndex(0)
        
        
        #메인 widget에서의 버튼
        self.Find_Bt.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(self.Num_findWidget))
        self.Recommend_Bt.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(self.Num_recommendTableWidget))
        
        #추천종목 리스트 widget에서의 버튼
        self.table_back_Bt.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(self.Num_mainWidget))
        
        #검색하는 widget에서의 버튼
        self.find_back_bt.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(self.Num_mainWidget))
        self.Find_table_Bt.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(self.Num_findedTableWidget))        
        
#stacked widget 1페이지 : 메인화면 : 도움말, 추천종목보기, 종목검색 버튼 있음
    def mainWidget(self):
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(90, 30, 90, 20)
        self.background_name = QLabel(self.centralwidget)
        self.background_name.setMaximumSize(QtCore.QSize(16777215, 150))
        self.background_name.setStyleSheet("border-image: url({0}/급등이.png);".format(file_pass))
        self.verticalLayout.addWidget(self.background_name)
        
        self.background_image = QLabel(self.centralwidget)
        self.background_image.setMinimumSize(QtCore.QSize(0, 130))
        self.background_image.setMaximumSize(QtCore.QSize(16777215, 250))
        self.background_image.setStyleSheet("border-image: url({0}/2메인사진.png);".format(file_pass))
        self.verticalLayout.addWidget(self.background_image)

        self.helpButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.helpButton)
        self.helpButton.setText("도움말 보기")
        
        self.helpButton.clicked.connect(self.openWindow)
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(100, 0, 100, 0)
        self.verticalLayout_2.setSpacing(40)
        
        self.Recommend_Bt = QPushButton(self.centralwidget)
        self.Recommend_Bt.setMinimumSize(QtCore.QSize(0, 80))
        self.Recommend_Bt.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(13)
        self.Recommend_Bt.setFont(font)
        self.Recommend_Bt.setStyleSheet("border-image: url({0}/메인 버튼.png);".format(file_pass))
        
        self.Recommend_Bt.setObjectName("Recommend_Bt")
        self.verticalLayout_2.addWidget(self.Recommend_Bt)
        self.Find_Bt = QtWidgets.QPushButton(self.centralwidget)
        self.Find_Bt.setMinimumSize(QtCore.QSize(0, 80))
        self.Find_Bt.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Find_Bt.setFont(font)
        self.Find_Bt.setStyleSheet("border-image: url({0}/메인 버튼.png);".format(file_pass))
        
        self.verticalLayout_2.addWidget(self.Find_Bt)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        
#추천페이지의 UI를 셋팅하는 함수
    def RecommendTableWidgetWindow(self):
        self.verticalLayoutWidget_recommend.setGeometry(QtCore.QRect(-1, -1, 541, 571))
        self.verticalLayoutWidget_recommend.setObjectName("verticalLayoutWidget_recommend")
        
        self.verticalLayout_recommend = QVBoxLayout(self.verticalLayoutWidget_recommend)
        self.verticalLayout_recommend.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_recommend.setObjectName("verticalLayout_recommend")
        
        self.horizontalLayout_recommend = QHBoxLayout()
        self.horizontalLayout_recommend.setObjectName("horizontalLayout_recommend")
        
        
        self.table_back_Bt = QPushButton(self.verticalLayoutWidget_recommend)
        
        
        self.table_back_Bt.setMaximumSize(QtCore.QSize(60, 60))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(file_pass+"/home2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.table_back_Bt.setIcon(icon)
        self.table_back_Bt.setIconSize(QtCore.QSize(50, 50))
        self.horizontalLayout_recommend.addWidget(self.table_back_Bt)
        
        self.datelabel = QtWidgets.QLabel(self.verticalLayoutWidget_recommend)
        self.datelabel.setMinimumSize(QtCore.QSize(0, 40))
        self.datelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.datelabel.setText("6월8일추천종목")
        
        
        
        self.recommend_tableWidget = QTableWidget(self.verticalLayoutWidget_recommend)
        
        self.verticalLayout_recommend.addLayout(self.horizontalLayout_recommend)
        self.verticalLayout_recommend.addWidget(self.datelabel)
        self.verticalLayout_recommend.addWidget(self.recommend_tableWidget)
        
        self.table_back_Bt.setText("")

#추천페이지에 보여질 table의 데이터를 세팅하는 함수
    def RecommendTableWidgetData(self):
        
        self.verticalLayoutWidget_recommend = QWidget()
        
        self.RecommendTableWidgetWindow()
        
        num_row = 20
        num_col = self.df_test.shape[1]
        Columns=['종목이름','5일보유시 예상수익률']
        
        df_test = self.df_test[:num_row]
        df_test = np.array(df_test,dtype='U10')
        
        column_headers = Columns

        self.recommend_tableWidget.resize(30+100*num_col, 30*(num_row+5))
        self.recommend_tableWidget.setRowCount(num_row)
        self.recommend_tableWidget.setColumnCount(num_col)
        self.recommend_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        
        self.recommend_tableWidget.setHorizontalHeaderLabels(column_headers)
        
        for row in range(num_row):
            for col in range(num_col):
                item = QTableWidgetItem(df_test[row][col][:5])
                self.recommend_tableWidget.setItem(row, col, item)
        self.recommend_tableWidget.resizeColumnsToContents()
        self.recommend_tableWidget.resizeRowsToContents()
        
        
        self.Num_recommendTableWidget= self.stackedWidget.addWidget(self.verticalLayoutWidget_recommend)
        
#종목검색결과페이지에 사용될 UI들을 정의하는 함수
    def FindTableWidgetWindow(self):
        
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 541, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        
        self.find_table_back_Bt = QPushButton(self.verticalLayoutWidget)
        
        self.find_table_back_Bt.setMaximumSize(QtCore.QSize(60, 60))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(file_pass+"/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_table_back_Bt.setIcon(icon)
        self.find_table_back_Bt.setIconSize(QtCore.QSize(50, 50))
        self.horizontalLayout.addWidget(self.find_table_back_Bt)
        
        self.find_table_home_Bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.find_table_home_Bt.setMaximumSize(QtCore.QSize(60, 60))
        self.find_table_home_Bt.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(file_pass+"/home2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_table_home_Bt.setIcon(icon1)
        self.find_table_home_Bt.setIconSize(QtCore.QSize(50, 50))
        self.horizontalLayout.addWidget(self.find_table_home_Bt)
        
        self.commentlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.commentlabel.setMinimumSize(QtCore.QSize(0, 40))
        self.commentlabel.setAcceptDrops(False)
        self.commentlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.commentlabel.setObjectName("comment_label")
        
        self.horizontalLayout_2_emotion = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2_emotion.setObjectName("horizontalLayout_2")
        self.emotion = QtWidgets.QLabel(self.verticalLayoutWidget_recommend)
        self.emotion.setMinimumSize(QtCore.QSize(200, 200))
        self.emotion.setMaximumSize(QtCore.QSize(200, 200))
        self.emotion.setText("")
        self.emotion.setObjectName("label_2")
        self.horizontalLayout_2_emotion.addWidget(self.emotion)
        self.verticalLayout.addLayout(self.horizontalLayout_2_emotion)
        
        
        
        
        self.find_tableWidget = QTableWidget(self.verticalLayoutWidget)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.verticalLayout.addWidget(self.commentlabel)
        self.verticalLayout.addWidget(self.datelabel)
        self.verticalLayout.addWidget(self.find_tableWidget)
        
        self.find_table_back_Bt.setText("")
        self.find_table_home_Bt.setText("")
        
#종목검색결과 페이지에 표시될 테이블 데이터를 만드는 함수        
    def FindTableWidgetData(self): #검색 시 결과 표시
        self.verticalLayoutWidget = QWidget()
        
        self.FindTableWidgetWindow()
        
        self.idx=self.df_test[:,0]==self.lineEdit.text()
        print(self.lineEdit.text())
        self.df_test_finded =self.df_test[self.idx.reshape((self.idx.shape[0],))]
        
        num_row = self.df_test_finded.shape[0]
        num_col = self.df_test_finded.shape[1]
        Columns=['종목이름','5일보유시 예상수익률']
        
        self.df_test_finded = self.df_test_finded.reshape(num_row,num_col)
        self.df_test_finded = np.array(self.df_test_finded,dtype='U10')
        
        column_headers = Columns
        
        self.find_tableWidget.resize(30+100*num_col, 30*(num_row+5))
        self.find_tableWidget.setRowCount(num_row)
        self.find_tableWidget.setColumnCount(num_col)
        self.find_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)        
        self.find_tableWidget.setHorizontalHeaderLabels(column_headers)
        
        for row in range(num_row):
            for col in range(num_col):
                item = QTableWidgetItem(self.df_test_finded[row][col][:5])
                self.find_tableWidget.setItem(row, col, item)
        self.find_tableWidget.resizeColumnsToContents()
        self.find_tableWidget.resizeRowsToContents()
#예측수익률에 따라 comment
        def commentor(data):
            
            determin=data.astype(float)
            
            if determin>10 :
                msg="에너지 강세형 : 거래바닥을 형성하며 주가가 횡보하고 있거나\n\
최근 급상승하고 있는 종목이라면 \n\
향후 일주일간도 상승추세를 보여줄 확률이 높습니다."
                strength="surprise"
            elif determin>0:
                msg="주가가 상승추세에 있지만, 아직 본격적인 상승은 없을 것으로 예상됩니다.\n \
종목의 재료가 충분히 강한지 체크해보시고 진입하시길 추천합니다."
                strength="littlegood"
            elif determin>-5:
                msg="주가 상승의 에너지가 부족합니다. \n\
한 박자 쉬고 진입하시기를 추천드립니다."
                strength="notgood"
            elif determin<-5:
                msg="해당종목은 현재 매도세가 강하므로, \n\
이 앞 일주일간은 투자를 삼가십시오."
                strength="bad"
            else:
                msg="종목을 입력하세요"
                strength="nothing"
            return msg,strength
        #print(type(self.df_test_finded[:,1]))
    
        m,s=commentor(self.df_test_finded[:,1])
        self.emotion.setStyleSheet("\n"
"border-image: url(./미니프로젝트/{0}.png);".format(s))

        self.commentlabel.setText(m)
        self.lineEdit.setText('')
        
        self.Num_findedTableWidget = self.stackedWidget.addWidget(self.verticalLayoutWidget) #Current Index 3
        
        self.find_table_back_Bt.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(self.Num_findWidget))
        self.find_table_home_Bt.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(self.Num_mainWidget))

#종목검색할 수 있는 페이지의 UI
    def setFindStockWindow(self): 
        
        self.find_verticalLayout = QVBoxLayout(self.find_widget)
        self.find_verticalLayout.setObjectName("find_verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.find_back_bt = QPushButton(self.find_widget)
        self.find_back_bt.setMinimumSize(QtCore.QSize(60, 60))
        self.find_back_bt.setMaximumSize(QtCore.QSize(60, 60))
        self.find_back_bt.setBaseSize(QtCore.QSize(0, 0))
        self.find_back_bt.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(file_pass+"/home2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_back_bt.setIcon(icon)
        self.find_back_bt.setIconSize(QtCore.QSize(50, 50))
        self.find_back_bt.setObjectName("pushButton")
        self.gridLayout.addWidget(self.find_back_bt, 0, 0, 1, 1)
        self.find_verticalLayout.addLayout(self.gridLayout)
        self.find_horizontalLayout = QHBoxLayout()
        self.find_horizontalLayout.setContentsMargins(30, -1, -1, 0)
        self.find_horizontalLayout.setSpacing(30)
        self.find_horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.find_widget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setObjectName("label")
        self.find_horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.find_widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.find_horizontalLayout.addWidget(self.lineEdit)
        self.Find_table_Bt = QtWidgets.QPushButton(self.find_widget)
        self.Find_table_Bt.setMinimumSize(QtCore.QSize(55, 55))
        self.Find_table_Bt.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(file_pass+"/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Find_table_Bt.setIcon(icon1)
        self.Find_table_Bt.setIconSize(QtCore.QSize(50, 50))
        self.Find_table_Bt.setObjectName("pushButton_2")
        self.find_horizontalLayout.addWidget(self.Find_table_Bt)
        self.find_verticalLayout.addLayout(self.find_horizontalLayout)
        self.find_horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.find_horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.find_horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.find_widget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(500, 500))
        self.label_2.setStyleSheet("border-image: url({0}/캐릭터(작은거).png);".format(file_pass))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.find_horizontalLayout_2.addWidget(self.label_2)
        self.find_verticalLayout.addLayout(self.find_horizontalLayout_2)
        
        self.label.setText("종목 이름")
        self.lineEdit.setText("원하는 종목을 입력하세요.")
        
#UI들의 연결 정의하는 함수. 수신-송신 이벤트 정
    def setFindStock(self):  
        
        self.setFindStockWindow()
        
        self.lineEdit.returnPressed.connect(self.Find_table_Bt.click)
        self.Find_table_Bt.clicked.connect(self.FindTableWidgetData)
        
        total_stock=pd.read_excel('./total_stock.xls')
        model = QStringListModel()
        model.setStringList(total_stock.종목명.values)
        
        completer = QCompleter()
        completer.setModel(model)
        self.lineEdit.setCompleter(completer)
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("급등이")
        
        self.Recommend_Bt.setText("추천 종목")
        self.Find_Bt.setText("종목 검색")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mySW = Ui_MainWindow()
    mySW.show()
    sys.exit(app.exec_())
