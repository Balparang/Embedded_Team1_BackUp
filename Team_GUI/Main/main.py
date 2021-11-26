import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer # 로딩화면 위한 타이머
from PyQt5.QtGui import QMovie  # 로딩화면 gif 위한 모듈
from PyQt5.QtCore import QDateTime, Qt  # 시간 표기

# import task
from Task import task_email_02
from Task import run_email
from Task import task_musicplayer
from Task import task_news 
# from Task import task_calendar
from Task import task_game

from Task import task_loading
# from Task import task_calendar
from Task import tast_weather
from news_scrap import naver_current_weather, naver_current_weather_Icon # 날씨

# ui 로드
form_class = uic.loadUiType("main.ui")[0]   


# 메인 윈도우 클래스 조작
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.setGeometry(500, 500, 600, 400)  # x, y, w, h : 창 크기 조절 , 화면 정중앙에 띄우기 위해 임시주석처리
        self.setWindowTitle("Main") # 윈도우 타이틀 설정
        # self.setFixedSize(600, 400)
        
        # Loading Image
        # self.loading_screen = task_loading.LoadingScreen()   # 로딩함수 호출(로딩화면 로드)
        
        # 시간 계산
        self.datetime = QDateTime.currentDateTime()

        self.setStyleSheet('background-color:#3e3e3e;') # 테마

        # 날씨 아이콘
        wt = naver_current_weather_Icon()
        url = f"https://ssl.pstatic.net/static/weather/image/icon_weather/{wt}.svg"
        image = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(image)
        pixmap = pixmap.scaled(100, 100)
        self.label_icon1.setPixmap(pixmap)

        # 바
        self.label_bar.setStyleSheet('color: white;background-color:qlineargradient(spread:reflect, x1:1, y1:0, x2:0.995, y2:1, stop:0 rgba(200, 200, 200, 255), stop:0.305419 rgba(40, 40, 40, 255), stop:0.935961 rgba(10, 11, 18, 0), stop:1 rgba(100, 100, 100, 255)); border=0px')        
        
        
        # 버튼 기능연결, lambda: "TypeError: argument 1 has unexpected type 'NoneType'" 방지하기 위해 사용 
        # 이메일 
        self.btn_run_email.clicked.connect(self.openEmailWindow)
        self.btn_run_email.setIcon(QIcon('image_source/mail_4.png'))
        self.btn_run_email.setIconSize(QSize(200,200))
        self.btn_run_email.setStyleSheet('border:0px;')
        
        # 뮤직플레이어
        self.btn_run_musicplayer.clicked.connect(self.openMusicPlayerWindow)
        self.btn_run_musicplayer.setIcon(QIcon('image_source/music_1.png'))
        self.btn_run_musicplayer.setIconSize(QSize(110,110))
        self.btn_run_musicplayer.setStyleSheet('border:0px;')

        # 뉴스
        self.btn_run_news.clicked.connect(self.openNewsWindow)
        self.btn_run_news.setIcon(QIcon('image_source/news_3.png'))
        self.btn_run_news.setIconSize(QSize(115,115))
        self.btn_run_news.setStyleSheet('border:0px;')
        
        # 게임
        self.btn_run_game.clicked.connect(self.openGameWindow)
        self.btn_run_game.setIcon(QIcon('image_source/game_6.png'))
        self.btn_run_game.setIconSize(QSize(115,115))
        self.btn_run_game.setStyleSheet('border:0px;')

        # 캘린더
        # self.btn_run_calendar.clicked.connect(self.openCalendarWindow)
        # self.btn_run_calendar.setIcon(QIcon('image_source/cal_1.png'))
        # self.btn_run_calendar.setIconSize(QSize(125,125))
        # self.btn_run_calendar.setStyleSheet('border:0px;')

        # 시간 표시 상태바
        self.statusBar().showMessage(self.datetime.toString(Qt.DefaultLocaleShortDate)) 
        self.statusBar().setStyleSheet('font-size:14pt; color:white;')   # 날짜 시간 표시

        # 날씨 버튼
        weather = naver_current_weather()
        self.btn_weather.clicked.connect(self.openWeather)
        self.btn_weather.setText('\n\n\n\n\n\n'+weather)
        self.btn_weather.setStyleSheet('color:white;font-size:12pt; font:bold; border:0px;')
        
        
    ### 기능함수 ### 
    # 이미지 로드
    def loadImageFromFile(self, source_url, width_size): # source_url의 이미지로 qPixmap 객체생성 후, 해당 객체 리턴
        self.qPixmapFileVar = QPixmap()  # qPixmap 객체 생성
        self.qPixmapFileVar.load(source_url)  # 이미지 로드
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(width_size)  # 크기 조절
        return self.qPixmapFileVar
    
    # dialWindow
    def openEmailWindow(self):
        task_email_02.emailWindow(self)
        
    def openMusicPlayerWindow(self):
        task_musicplayer.musicPlayerWindow(self)
        
    def openNewsWindow(self):
        task_news.newsWindow(self)
        
    def openWeather(self):
        tast_weather.weatherWindow(self)
    
    # def openCalendarWindow(self):
    #     task_calendar.calendarWindow(self)
        
    def openGameWindow(self):
        task_game.gameWindow(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
