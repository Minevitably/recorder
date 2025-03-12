from PySide6.QtWidgets import QWidget, QApplication
import sys

from Form import Ui_Form
from table import MTableWidget


class Recorder(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        # 底部的表格
        self.tableWidget = None

        self.setupUi(self)
        self.replaceWidget()
        self.centerOnScreen()

    def replaceWidget(self):
        # 小目标存取页面的相册组件
        layout = self.bottomWiget.layout()
        layout.setContentsMargins(0, 0, 0, 0)  # 设置布局边距为0
        layout.setSpacing(0)  # 设置布局间距为0
        layout.itemAt(0).widget().deleteLater()
        self.tableWidget = MTableWidget()
        layout.addWidget(self.tableWidget)

    def centerOnScreen(self):
        # 替换组件后手动更新窗口大小
        self.adjustSize()

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
