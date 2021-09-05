from PySide2.QtGui import *
from PySide2.QtWidgets import *
from color import Ui_MainWindow
from cv_change import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.start_img = 'Image/Scream3.jpg'
        p1 = QPixmap(self.start_img)
        self.label.setPixmap(p1)
        self.label.resize(p1.width(), p1.height())
        self.pushButton.clicked.connect(self.change_color)
        self.spinBox.setValue(30)

    def change_color(self):
        edit_colors = self.lineEdit.text()
        if edit_colors:
            edit_colors = transform_colors(edit_colors)
        K = int(self.spinBox.text())
        change_colors(self.start_img, K, edit_colors)
        res_img = QPixmap('res.jpg')
        self.label_2.setPixmap(res_img)
        self.label_2.resize(res_img.width(), res_img.height())


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    mw = MainWindow()
    mw.show()
    app.exec_()
