from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QIcon

from pynput import keyboard

import os
import sys
import json
import threading

class TransparentImageWidget(QWidget):
    def __init__(self):
        super().__init__()

        if os.path.exists('./config.json'):
            config = json.load(open('./config.json', 'r'))
        else:
            config = json.load(open(resource_path('config.json'), 'r'))

        self.toggle_key = config["toggle_key"]
        self.switch_key = config["switch_key"]
        self.overlay_opacity = config["overlay_opacity"]

        self.opacity = 0
        self.switched = False
        self.running = True

        self.initUIs()

    def initUIs(self):
        self.setWindowTitle("Kuro Overlay")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Overlay Image
        self.imageLabel = QLabel(self)
        self.imageLabel.setGeometry(0, 0, 1920, 1080)
        self.pixmap = QPixmap(resource_path("kuro_overlay.png"))

        self.updateImageOpacity()
        self.showFullScreen()
        
    def updateImageOpacity(self):
        tempPixmap = QPixmap(self.pixmap.size())
        tempPixmap.fill(Qt.transparent)

        painter = QPainter(tempPixmap)
        painter.setOpacity(self.opacity)
        painter.drawPixmap(0, 0, self.pixmap)
        painter.end()

        self.imageLabel.setPixmap(tempPixmap)

    def switchImage(self, newImagePath):
        self.pixmap = QPixmap(newImagePath)

        self.updateImageOpacity()

    def onKeyPressEvent(self): # Custom pynput
        def on_press(key):
            try:
                if key.char == self.toggle_key:
                    self.opacity = self.overlay_opacity if self.opacity == 0 else 0
                    self.updateImageOpacity()
                elif key.char == self.switch_key:
                    self.switchImage(resource_path("kuro_overlay.png") if self.switched else resource_path("kuro_overlay_new.png"))
                    self.switched = not self.switched

            except:
                pass
            
            return self.running
                
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def closeEvent(self, event):
        self.running = False

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def start():
    print("Starting Kuro Overlay...")
    print("Press 't' to toggle overlay ～(≧ ∇ ≦)/")
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path('izuna.ico')))

    overlay = TransparentImageWidget()

    keyListenerThread = threading.Thread(target=overlay.onKeyPressEvent)
    keyListenerThread.start()
    
    app.exec_()
    print("Exiting...～(≧ ω ≦)")
    sys.exit()

start()