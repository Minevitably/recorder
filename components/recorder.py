import random

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
import sys

from components.thread import RecorderThread
from static.Form import Ui_Form
from components.table import MTableWidget, MLabel


class Recorder(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()

        # 是否正在录音
        self.is_recording = None
        # 录音线程
        self.recorder_thread = None
        # 音频帧
        self.frames = None
        # 表格组件
        self.tableWidget = None

        self.setupUi(self)
        # 替换表格组件
        self.replaceWidget()
        # 屏幕居中显示
        # 替换组件后手动更新窗口大小
        self.adjustSize()
        self.resize(self.minimumSize())
        self.centerOnScreen()
        # 注册事件
        self.setupEvent()

        self.initLabel()

        # 载入评分模型
        self.loadModel()

    def loadModel(self):
        """
        载入评分模型
        :return:
        """
        # TODO: 该方法未完成
        print("载入评分模型")

    def selectSentence(self):
        """
        选取要朗读的句子
        :return:
        """
        # TODO: 该方法未完成
        print("selectSentence")

    def record(self):
        """
        录音/停止
        :return:
        """
        print("record")
        if self.is_recording:
            self.is_recording = False
            # 开始录音
            icon = QIcon()
            icon.addFile(u":/pic/resources/start.png", QSize(), QIcon.Normal, QIcon.Off)
            self.recordBtn.setIcon(icon)
            self.recorder_thread.stop_recording()
        else:
            self.is_recording = True
            # 停止录音
            icon = QIcon()
            icon.addFile(u":/pic/resources/stop.png", QSize(), QIcon.Normal, QIcon.Off)
            self.recordBtn.setIcon(icon)
            self.recorder_thread.start_recording()

    def handle_frames(self, frames):
        """
        录音线程回调，将录制好的帧返回给窗口线程
        :param frames:
        :return:
        """
        # self.recorder_thread.save_recording("output.wav", frames)
        self.frames = frames

    def evaluate(self):
        """
        调用评分模型评分
        :return:
        """
        # TODO: 该方法未完成
        print("evaluate")
        if self.is_recording:
            QMessageBox.warning(self, "警告", "请勿在录音的过程中评分")
            return

        if self.frames is None:
            # 弹出警告框
            QMessageBox.warning(self, "警告", "还未录音")
        else:
            scoreDict = {}

            # 更新现有键的值，生成随机值
            for label in MLabel:
                scoreDict[label.value] = str(random.randint(0, 100))

            self.updateScore(scoreDict)
            pass

    def updateScore(self, scoreDict):
        """
        更新评分
        :param scoreDict: 各项评分
        :return: None
        """
        print("updateScore")
        self.tableWidget.updateScore(scoreDict)

    def setupEvent(self):
        """
        初始化事件
        :return: None
        """
        # 初始化录音线程
        self.recorder_thread = RecorderThread()
        self.recorder_thread.frames_ready.connect(self.handle_frames)
        self.is_recording = False

        # 录制按钮点击事件
        self.recordBtn.clicked.connect(self.record)

        # 评估按钮点击事件
        self.evaluateBtn.clicked.connect(self.evaluate)

    def initLabel(self):
        """
        评分Label默认值使用0
        :return:
        """
        scoreDict = {}
        for label in MLabel:
            scoreDict[label.value] = "0"

        self.updateScore(scoreDict)

    def replaceWidget(self):
        """
        替换组件
        :return: None
        """
        # 底部的表格
        self.tableWidget = MTableWidget()
        layout = self.bottomWiget.layout()
        layout.setContentsMargins(0, 0, 0, 0)  # 设置布局边距为0
        layout.setSpacing(0)  # 设置布局间距为0
        layout.itemAt(0).widget().deleteLater()

        layout.addWidget(self.tableWidget)

    def centerOnScreen(self):
        """
        窗口居中显示
        :return: None
        """
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
