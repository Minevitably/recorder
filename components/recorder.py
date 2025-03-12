from PySide6.QtWidgets import QWidget, QApplication
import sys

from static.Form import Ui_Form
from components.table import MTableWidget


class Recorder(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        # 底部的表格
        self.tableWidget = None
        self.setupUi(self)
        # 替换表格组件
        self.replaceWidget()
        # 屏幕居中显示
        # 替换组件后手动更新窗口大小
        self.adjustSize()
        self.resize(self.minimumSize())
        self.centerOnScreen()

    def loadModel(self):
        """
        载入评分模型
        :return:
        """
        print("载入评分模型")

    def selectSentence(self):
        """
        选取要朗读的句子
        :return:
        """
        print("selectSentence")

    def record(self):
        """
        录音/停止
        :return:
        """
        print("record")

    def evaluate(self):
        """
        调用评分模型评分
        :return:
        """
        print("evaluate")

    def updateScore(self, scoreDict):
        """
        更新评分
        :param scoreDict: 各项评分
        :return: None
        """
        print("updateScore")


    def replaceWidget(self):
        layout = self.bottomWiget.layout()
        layout.setContentsMargins(0, 0, 0, 0)  # 设置布局边距为0
        layout.setSpacing(0)  # 设置布局间距为0
        layout.itemAt(0).widget().deleteLater()

        self.tableWidget = MTableWidget()
        layout.addWidget(self.tableWidget)

    def centerOnScreen(self):
        screen = QApplication.primaryScreen().geometry()  # 获取屏幕大小
        window_rect = self.frameGeometry()  # 获取窗口大小
        center_point = screen.center()  # 获取屏幕中心点
        window_rect.moveCenter(center_point)  # 将窗口中心移动到屏幕中心
        self.move(window_rect.topLeft())  # 设置窗口位置


def run():
    app = QApplication(sys.argv)
    w = Recorder()
    w.show()
    app.exec()
