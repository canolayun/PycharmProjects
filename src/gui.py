import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from . import process


class MainWindow(QWidget): #class 자식(부모)
    def __init__(self):                 #초기화 함수
        super().__init__()
        # 부모 클래스의 초기화 메소드 호출
        # 자식 클래스에서 def __init__()을 사용하려면 위의 구문을 써야함.
        self.setupUI()

    #setupUI 정의 -> gui의 메인 구성요소를 담고 있음
    def setupUI(self):
        self.setWindowTitle("Project B3") #name on title bar :이름 추천받아욤
        self.setGeometry(100, 100, 300, 400)
        # ↑ 창의 위치를 모니터 좌상단으로부터 (가로,세로, 창의크기 가로,창의크기 세로)
        self.setWindowIcon(QIcon('B3.png'))
        # ↑ 창의 상단바에 아이콘 추가



        #회색 라벨(꾸미기용)
        self.square_label = QLabel(self)
        self.square_label.setStyleSheet(
                                 "background-color: #D5D5D5;"
                                 "border-radius: 7px;")
        self.square_label.move(20,20)   #라벨 위치
        self.square_label.resize(260,80)#라벨 크기

        #waferlabel
        self.wafer_label = QLabel("Wafer  ", self)
        self.wafer_label.setGeometry(40, 35, 150, 20)
        font = self.wafer_label.font() #폰트 정의
        font.setPointSize(10)
        font.setFamily('Consolas')
        font.setBold(True)
        self.wafer_label.setStyleSheet('color: #002266')
        self.wafer_label.setFont(font) #폰트 적용



        #coordinate label
        self.coordinate_label = QLabel("Coordinate  ", self)
        self.coordinate_label.setGeometry(40, 70, 150, 20)
        font2 = self.coordinate_label.font()
        font2.setPointSize(10)
        font2.setFamily('Consolas')
        font2.setBold(True)
        self.coordinate_label.setStyleSheet('color: #002266')
        self.coordinate_label.setFont(font2)

        # Input wafer
        self.Input_Wafer = QLineEdit("All", self)
        self.Input_Wafer.move(170, 35)
        self.Input_Wafer.setStyleSheet("color: white;"
                                       "background-color: #002266;"
                                       "border-style: solid;"
                                       "border-width: 2px;"
                                       "border-radius: 5px;"
                                       "border-color: #002266")
        self.Input_Wafer.move(170, 35)
        self.Input_Wafer.resize(80, 20)

        # input coordinate
        self.Input_coordinate = QLineEdit("All", self)
        self.Input_coordinate.setStyleSheet("color: white;"
                                            "background-color: #002266;"
                                            "border-style: solid;"
                                            "border-width: 2px;"
                                            "border-radius: 5px;"
                                            "border-color: #002266")
        self.Input_coordinate.move(170, 70)
        self.Input_coordinate.resize(80, 20)


        # #input_wafer label
        # self.Input_Wafer = QLineEdit("D07", self)
        # self.Input_Wafer.setGeometry(160, 35 , 30, 20)
        #
        # cb_wafer_label = QComboBox(self)
        # cb_wafer_label.addItem('D07')
        # cb_wafer_label.addItem('D08')
        # cb_wafer_label.addItem('D23')
        # cb_wafer_label.addItem('D24')
        # cb_wafer_label.move(160, 35)
        #
        # cb_wafer_label.activated[str].connect(self.onActivated_wafer_label)

        #Input coordinate
        #x-values
        # self.Input_coordinate_x = QLineEdit('-1', self)
        # self.Input_coordinate_x.setGeometry(160, 70, 20, 20)
        #
        # cbx = QComboBox(self)
        # cbx.addItem('-1')
        # cbx.addItem('-2')
        # cbx.addItem('-3')
        # cbx.addItem('-4')
        # cbx.move(160, 70)
        #
        # cbx.activated[str].connect(self.onActivated_x)

        # # y-values
        # self.Input_coordinate_y = QLineEdit('-1', self)
        # self.Input_coordinate_y.setGeometry(220, 70, 20, 20)
        #
        # cby = QComboBox(self)
        # cby.addItem('-1')
        # cby.addItem('-2')
        # cby.addItem('-3')
        # cby.addItem('-4')
        # cby.move(220, 70)
        #
        # cby.activated[str].connect(self.onActivated_y)


        self.showEdit = QCheckBox("Show", self)
        self.showEdit.move(100, 120)
        self.showEdit.toggle()

        self.saveEdit = QCheckBox("Save Figure", self)
        self.saveEdit.move(100, 150)
        self.saveEdit.toggle()

        self.csvEdit = QCheckBox("Save CSV", self)
        self.csvEdit.move(100, 180)
        self.csvEdit.toggle()

        self.label3 = QLabel('', self)
        self.label3.move(50, 170)

        self.btnOpenFolder = QPushButton("Set Data Folder", self) #openfolder button
        self.btnOpenFolder.setStyleSheet("color: white;"
                              "background-color: #002266;"
                              "border-style: solid;"
                              "border-width: 2px;"
                              "border-radius: 3px;"
                              "border-color: #white")
        self.btnOpenFolder.resize(150, 45) #button size 150*30
        self.btnOpenFolder.move(75, 220) # button location
        self.btnOpenFolder.clicked.connect(self.find_folder) #'clicked' signal이 find_folder 메소드에 연결


        self.btnOpenSave = QPushButton("Open Result Folder", self)
        self.btnOpenSave.setStyleSheet("color: white;"
                              "background-color: #002266;"
                              "border-style: solid;"
                              "border-width: 2px;"
                              "border-radius: 3px;"
                              "border-color: #white")
        self.btnOpenSave.resize(150, 45)
        self.btnOpenSave.move(75, 270)
        self.btnOpenSave.clicked.connect(self.open_folder)


        self.btnSave = QPushButton("OK", self)
        self.btnSave.setStyleSheet("color: white;"
                      "background-color: #002266;"
                      "border-style: solid;"
                      "border-width: 2px;"
                      "border-radius: 4px;"
                      "border-color: #white")
        self.btnSave.resize(150,45)
        self.btnSave.move(75, 320)
        self.btnSave.clicked.connect(self.btnInput_clicked)


        self.center() #창을 모니터 화면의 가운데에 배치

    # def onActivated_x(self, text):
    #     self.Input_coordinate_x.setText(text)
    #     self.Input_coordinate_x.adjustSize()
    #
    # def onActivated_y(self, text):
    #     self.Input_coordinate_y.setText(text)
    #     self.Input_coordinate_y.adjustSize()
    #
    # def onActivated_wafer_label(self, text):
    #     self.Input_Wafer.setText(text)
    #     self.Input_Wafer.adjustSize()

    def center(self):
        qr = self.frameGeometry()  #frameGeometry() 메서드 사용해서 창의 위치와 크기 정보 가져옴
        cp = QDesktopWidget().availableGeometry().center() #사용하는 모니터 화면의 가운데 위치를 파악
        qr.moveCenter(cp) #창의 직사각형 위치를 화면의 중심 위치로 이동
        self.move(qr.topLeft()) #현재 창을 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동

    def find_folder(self): #define find_folder function
        FileFolder = QFileDialog.getExistingDirectory(self, 'Find Folder')
        self.label3.setText(FileFolder)

    def open_folder(self):
        process.open() #수정해야될 부분

    def btnInput_clicked(self):
        wafer = self.Input_Wafer.text()
        coordinate = self.Input_coordinate.text()
        save = self.saveEdit.isChecked()
        show = self.showEdit.isChecked()
        csv = self.csvEdit.isChecked()
        data_path = self.label3.text()
        try:
            if wafer == '' or coordinate == '':
                raise ValueError('There is blank')
            else:
                process.work(wafer, coordinate, save, show, csv, data_path)
                a = QMessageBox.information(self, 'Message', str('Done!'))
        except ValueError as e:
            QMessageBox.information(self, 'Error', str(e))
        except:
            QMessageBox.information(self, 'Error', 'Error Unknown')

