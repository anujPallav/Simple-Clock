from PyQt5 import QtGui from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QWidget, QLabel, QApplication from PyQt5.QtCore import QTimer, Qt from PyQt5.QtGui import * import time import sys

class window: def init(self): self.widget = QWidget()

    self.vertical_box = QVBoxLayout(self.widget)
    self.time_label = QLabel(self.widget)   

    self.vertical_box.addWidget(self.time_label)
    
    self.widget.setWindowIcon(QIcon("clock.png"))
    self.widget.setWindowTitle("Clock")
    self.widget.setFixedSize(890,100)
    self.widget.show()

    self.time_label.setAlignment(Qt.AlignCenter)
    
    self.timer = QTimer()
    self.timer.timeout.connect(self.clock_handler)
    self.timer.start(1000)

def widget_style(self):
    DAY_LIGHT_VAR = ["AM","PM"]

    self.day_light = time.strftime('%p')
    self.week_day_name = time.strftime('%A')

    if self.day_light in DAY_LIGHT_VAR[0]:
        self.widget.setStyleSheet("background-color:#F08080;")
        self.time_label.setStyleSheet("color:#212F3D;"
                                            "font:50px;"
                                            "font-family:Comic Sans MS, Comic Sans, cursive;"
                                            "letter-spacing:10px;")
    elif self.day_light in DAY_LIGHT_VAR[1]:
        self.widget.setStyleSheet("background-color:#273746;")
        self.time_label.setStyleSheet("color:#BDC3C7;"
                                            "font:50px;"
                                            "font-family:Ink Free;"
                                            "letter-spacing:8px;")
    else:
        print('NONE')

def _clock_manager(self):
    self.time = (time.localtime())
    TIME = f"{self.time[3]}:{self.time[4]}:{self.time[5]}-{self.day_light} {self.week_day_name}/{self.time[2]}"
    self.time_label.setText(TIME)
    self.time_label.adjustSize()
      


def clock_handler(self):
    self.widget_style()
    self._clock_manager()
if name == 'main': app = QApplication(sys.argv) win = window() sys.exit(app.exec_())
