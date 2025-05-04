# 알람
# import schedule
# import time
# import winsound
# QT
import sys, os
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QSlider
from PyQt5.QtCore import QTimer, QTime, Qt
from enum import Enum
import pygame


if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS

else:
    base_path = os.path.abspath(".")

class STATE(Enum):
    REST = 0
    WORK = 1

class SoundPlayer:
    def __init__(self, file_path):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(file_path)
        self.sound.set_volume(0.5) # 0.0 ~ 1.0
    def play(self):
        self.sound.play()
        # self.sound.play(-1) # 무한반복, 테스트용
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def set_sound(self, volume):
        self.sound.set_volume(volume)

# def alarm_rest():
#     print("알람: 쉬는 시간")
#     winsound.Beep(750, 3000) # 100Hz, 1초 동안 알림


# def alarm_work():
#     print("알람: 공부 시간")
#     winsound.Beep(1250, 3000) # 100Hz, 1초 동안 알림

class AlarmWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.file_path = os.path.join(base_path, 'school_bell.mp3')
        self.bell = SoundPlayer(self.file_path)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_time)
        self.timer.start(1000)
        self.state = None

    def initUI(self):
        self.setWindowTitle('오재혁 알림')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.label_version = QLabel("version 1.0.1  2025.05.04")
        self.label_version.setStyleSheet('font-size: 10px; color: gray;')
        self.layout.addWidget(self.label_version)

        self.label = QLabel("대기 중...", self)
        self.label.setStyleSheet('font-size: 24px;')
        self.layout.addWidget(self.label)
        

        self.label_volume = QLabel("볼륨: 50%", self)
        self.layout.addWidget(self.label_volume)
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.set_volume)
        self.layout.addWidget(self.slider)


        self.setLayout(self.layout)

    def check_time(self):
        current_time = QTime.currentTime()
        minute = current_time.minute()

        # 매시 0분 ~ 49분까지 공부시간
        if 0 <= minute < 50:
            self.label.setText('공부시간')
            if self.state != STATE.WORK:
                # alarm_work()
                self.bell.play()
                self.state = STATE.WORK
        # 매시 50분 ~ 59분까지 쉬는시간
        else:
            self.label.setText('쉬는시간')
            if self.state != STATE.REST:
                self.bell.play()
                self.state = STATE.REST

    def set_volume(self, value):
        volume = value / 100.0
        self.bell.set_sound(volume)
        self.label_volume.setText(f"볼륨: {value}%")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AlarmWindow()
    window.show()
    sys.exit(app.exec_())





# # 매시 50분에 알람 설정
# schedule.every().hour.at(":50").do(alarm_rest)


# # 매시 정각에 알람 설정
# schedule.every().hour.at(":00").do(alarm_work)

# # 계속해서 스케줄 확인
# while True:
#     schedule.run_pending()
#     time.sleep(1)

