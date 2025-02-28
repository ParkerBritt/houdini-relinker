from PySide2.QtWidgets import (
QInputDialog,
QMessageBox,
QListWidgetItem,
QDialog,
QLabel,
QLineEdit,
QVBoxLayout,
QHBoxLayout,
QPushButton,
QPlainTextEdit,
QWidget,
QApplication,
QListWidget,
QListWidgetItem,
QStackedWidget,
QTabWidget,
QAbstractItemView,
QCheckBox,
)
from PySide2.QtGui import QIcon
import os, re
import hou

def main():
    print("\n\n\n\n\n\n\n")
    # main window
    main_window = MainWindow()
    
    # start process
    main_window.exec()

class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        # window customizations
        self.setWindowTitle("title")
        self.setStyleSheet(hou.qt.styleSheet())
        
        # generate layouts
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # populate main layout
        self.layout.addWidget(QLabel("HELLO WORLD"))

    def on_cancel_seletion_button_clicked(self):
        self.close()
            
        
