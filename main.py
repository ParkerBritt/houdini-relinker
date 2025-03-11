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
    # main_window.exec()

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

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        # populate main layout
        self.layout.addWidget(QLabel("HELLO WORLD"))
        self.repath()

    def repath(self):
        file_references = hou.fileReferences()
        paths = [path for _, path in file_references]
        # print("paths:", paths)
        
        base_file_parm_map = dict()

        # print("common prefix:", os.path.commonpath(paths))
        for parm, path in hou.fileReferences():
            if(path.startswith("$HIP")):
                continue
            norm_path = os.path.normpath(path).replace("\\", "/")
            base_name = os.path.basename(norm_path)
            if base_name not in base_file_parm_map:
                base_file_parm_map[base_name] = {"parms":[parm]}
            else:
                base_file_parm_map[base_name]["parms"].append(parm)
            self.list_widget.addItem(base_name)

        search_path = "/base/path"
        hip_root_path = os.path.dirname(hou.hipFile.path())
        for root, dirs, files in os.walk(search_path):
            for file in files:
                if file in base_file_parm_map.keys():
                    # if(file != "water.obj"):
                    #     continue
                    found_path = os.path.join(root, file)
                    rel_path = os.path.relpath(found_path, hip_root_path)
                    hip_rel_path = os.path.join("$HIP", rel_path)
                    # print(hip_rel_path, os.path.exists(hip_rel_path))

                    for parm in base_file_parm_map[file]["parms"]:
                        print(parm.eval())
                        print("setting parm:", parm, "to:", hip_rel_path)
                        parm.set(hip_rel_path)

                    base_file_parm_map.pop(file)

        # print("\n\n\n\nfiles not found:")
        # for file in base_file_parm_map.keys():
        #     print(file)
            


    def on_cancel_seletion_button_clicked(self):
        self.close()
            
        
