from PySide2.QtGui import *
from PySide2.QtWidgets import *
from color import Ui_MainWindow
from cv_change import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        p1 = QPixmap('Scream3.jpg')
        self.label.setPixmap(p1)
        self.label.resize(p1.width(), p1.height())
        self.pushButton.clicked.connect(self.change_color)
        self.spinBox.setValue(30)

    def change_color(self):
        edit_colors = self.lineEdit.text()
        if edit_colors:
            edit_colors = transform_colors(edit_colors)
        K = int(self.spinBox.text())
        change_colors('Scream3.jpg', K, edit_colors)
        res_img = QPixmap('res.jpg')
        self.label_2.setPixmap(res_img)
        self.label_2.resize(res_img.width(), res_img.height())


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    mw = MainWindow()
    mw.show()
    app.exec_()

    # colors = transform_colors('a7a5c6 8797b2 6d8a96 5d707f 66ced6 64B7C1')
    # change_colors('Scream3.jpg', 8, colors)
