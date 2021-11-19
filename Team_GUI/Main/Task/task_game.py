import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import *
# 게임 소스
from game_source import brick_break_game
from game_source import tetris_game
from game_source import snake_game


class gameWindow(QDialog):
    def __init__(self, parent):  # 부모 윈도우(메모장)가 있기 때문에 parent 적어주기
        super(gameWindow, self).__init__(parent)
        uic.loadUi("Task/task_game.ui", self)

        # 윈도우 타이틀, 사이즈 설정
        #self.setGeometry(500, 500, 600, 400)  # x, y, w, h : 창 크기 조절
        self.setWindowTitle("Game")  # 윈도우 타이틀 설정
        self.show()
        
        self.label_bar.setStyleSheet('color: white;background-color:qlineargradient(spread:reflect, x1:1, y1:0, x2:0.995, y2:1, stop:0 rgba(200, 200, 200, 255), stop:0.305419 rgba(40, 40, 40, 255), stop:0.935961 rgba(10, 11, 18, 0), stop:1 rgba(100, 100, 100, 255)); border=0px')

        # 게임 커버
        self.label_game1.setPixmap(self.loadImageFromFile("image_source/game0_cover.png", 140))
        self.label_game1.setStyleSheet('border: 2px solid white;')
        self.label_game2.setPixmap(self.loadImageFromFile("image_source/game1_cover.jpg", 140))
        self.label_game2.setStyleSheet('border: 2px solid white;')
        self.label_game3.setPixmap(self.loadImageFromFile("image_source/game2_cover.png", 140))  
        self.label_game3.setStyleSheet('border: 2px solid white;')

        ### 기능연결 ###

        # 게임 플레이 버튼, lambda: "TypeError: argument 1 has unexpected type 'NoneType'" 방지하기 위해 사용 
        self.btn_game1.clicked.connect(lambda: self.playGame(0)) # brick game
        self.btn_game2.clicked.connect(lambda: self.playGame(1)) # tetris
        self.btn_game3.clicked.connect(lambda: self.playGame(2)) # snake

        # Back: Close Window
        self.btn_back.clicked.connect(self.backToMainWindow)
        self.btn_back.setIcon(QIcon('image_source/home.png'))
        self.btn_back.setIconSize(QSize(60,60))
        self.btn_back.setStyleSheet('border:0px;')

    # 이미지 로드
    # source_url의 이미지로 qPixmap 객체생성 후, 해당 객체 리턴
    def loadImageFromFile(self, source_url, width_size):
        self.qPixmapFileVar = QPixmap()  # qPixmap 객체 생성
        self.qPixmapFileVar.load(source_url)  # 이미지 로드
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(
            width_size)  # 크기 조절
        return self.qPixmapFileVar


    # 게임 실행 버튼
    def playGame(self, source_list_idx):
        if source_list_idx == 0:
            brick_break_game.main()
        elif source_list_idx == 1:
            tetris_game.main()
        elif source_list_idx == 2:
            snake_game.main()
        print("playig 게임 이름...")

    # 현재 dialog 창 종료
    def backToMainWindow(self):
        self.close()
        print("close dialog...")
