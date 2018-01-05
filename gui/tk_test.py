from PyQt5 import QtGui
import sys
from PyQt5.QtWidgets import QWidget,QApplication
'''
尝试使用PyQt5进行图形化界面开发
作者：刘志成
'''
if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())