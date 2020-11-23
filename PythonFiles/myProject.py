from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
import random
import numpy as np

import pyqtgraph as pg
import pyqtgraph.exporters


class appWindow(QMainWindow):
    def __init__(self):
        super(appWindow, self).__init__()
        self.setWindowIcon(QIcon('../dataset/images/favicon.ico'))
        self.ui = loadUi('../UI/truly.ui', self)

        # 退出程序btn_exit
        self.ui.btn_exit.clicked.connect(self.clickExit)
        # 生成图像btn_draw
        self.ui.btn_draw.clicked.connect(self.createImageOfAnime)

        # 保存图像
        self.ui.btn_save.clicked.connect(self.saveImage)

        # 清除后台信息
        self.ui.btn_clean.clicked.connect(self.cleanUpConsloe)

    # 退出程序
    def clickExit(self):
        appExit = QApplication.instance()
        appExit.quit()

    # 生成多张图像
    def mulImages(self):
        pass

    # 清除控制台信息
    def cleanUpConsloe(self):
        self.ui.textEdit.clear()

    # 生成二次元图像
    def createImageOfAnime(self):
        try:
            x = np.random.normal(size=1000)
            y = np.random.normal(size=1000)
            r_symbol = random.choice(['o', 's', 't', 't1', 't2', 't3', 'd', '+', 'x', 'p', 'h', 'star'])
            r_color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'd', 'l', 's'])
            text = "x:{}\ny:{}\n{}\n{}\n".format(x, y, r_symbol, r_color)
            self.ui.imageWindow.clear()
            self.ui.imageWindow.plot(x, y, pen=None, symbol=r_symbol, symbolBrush=r_color)
            self.loadInfoToConsole(text)
        except Exception as e:
            print(str(e))

    # 加载特征信息到控制台
    def loadInfoToConsole(self, text):
        self.ui.textEdit.setPlainText(text)

    # 保存图片到本地
    def saveImage(self):
        try:
            exporter = pg.exporters.ImageExporter(self.ui.imageWindow.plotItem)
            exporter.parameters()['width'] = 256
            imageId = random.randint(1, 10000000)
            exporter.export('{}.png'.format(imageId))
            self.loadInfoToConsole('AnimeFaces{}保存成功!'.format(imageId))
        except Exception as e:
            print(str(e))


def setUpui():
    app = QApplication(sys.argv)
    mainWindow = appWindow()
    mainWindow.show()
    sys.exit(app.exec_())


# 加载二次元动漫程序
def setAnimeFaces():
    pass


if __name__ == '__main__':
    setUpui()
