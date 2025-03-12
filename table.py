import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QTableWidget, QVBoxLayout, QWidget, QLabel


class MTableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.phonemeLabel = None
        self.sentenceAccLabel = None
        self.sentenceComLabel = None
        self.sentenceFluLabel = None
        self.sentenceProLabel = None
        self.sentenceTotLabel = None
        self.wordTotalLabel = None
        self.wordStressLabel = None
        self.wordAccuracyLabel = None
        self.setWindowTitle("Table Widget with QWidget")
        width = 800
        self.firstRowHeight = 60
        # 创建表格
        self.table = QTableWidget(1, 3)  # 1行3列
        headerLabels = ["Phoneme-score", "Word-score", "Sentence-score"]
        self.table.setHorizontalHeaderLabels(headerLabels)
        # 隐藏行头
        self.table.verticalHeader().hide()

        # 设置列宽度比例
        # total_width = width  # 设置总宽度
        total_width = width  # 设置总宽度
        proportions = [2, 3, 5]  # 各列占的比例

        for i, proportion in enumerate(proportions):
            column_width = (total_width * proportion) / sum(proportions)
            self.table.setColumnWidth(i, column_width)
        # 设置单元格高度
        self.table.setRowHeight(0, self.firstRowHeight)  # 第一行高度

        # 设置表格的大小策略
        self.table.setSizeAdjustPolicy(QTableWidget.SizeAdjustPolicy.AdjustToContents)  # 根据内容调整大小
        self.table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 隐藏垂直滚动条
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 隐藏水平滚动条

        phonemeLabel = QLabel()
        phonemeLabel.setText("98")
        phonemeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        wordTable = self.newWordTable(total_width * 0.3)
        sentenceTable = self.newSentenceTable(total_width * 0.5)

        self.table.setCellWidget(0, 0, phonemeLabel)
        self.table.setCellWidget(0, 1, wordTable)
        self.table.setCellWidget(0, 2, sentenceTable)

        # 显示网格线
        self.table.setShowGrid(True)  # 显示网格线

        # 布局
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # 设置布局边距为0
        layout.setSpacing(0)  # 设置布局间距为0
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.setMinimumWidth(width)
        # FIXME: 暂时通过这个方式避免表格过大
        self.setMaximumSize(800, 90)

    def newWordTable(self, total_width):
        """
        创建Word-score子表格
        :param total_width: 子表格宽度
        :return: QTableWidget
        """
        wordTable = QTableWidget(1, 3)  # 1行3列
        headerLabels = ["Accuracy:", "Stress:", "Total:"]
        wordTable.setHorizontalHeaderLabels(headerLabels)
        wordTable.verticalHeader().hide()

        self.wordAccuracyLabel = QLabel("90")
        self.wordStressLabel = QLabel("92")
        self.wordTotalLabel = QLabel("98")

        self.wordAccuracyLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wordStressLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wordTotalLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        wordTable.setCellWidget(0, 0, self.wordAccuracyLabel)
        wordTable.setCellWidget(0, 1, self.wordStressLabel)
        wordTable.setCellWidget(0, 2, self.wordTotalLabel)

        # 设置表格的大小策略
        wordTable.setSizeAdjustPolicy(QTableWidget.SizeAdjustPolicy.AdjustToContents)  # 根据内容调整大小
        wordTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 隐藏垂直滚动条
        wordTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 隐藏水平滚动条

        wordTableTotalWidth = total_width  # 设置表格总宽度
        proportions = [1, 1, 1]  # 各列占的比例

        for i, proportion in enumerate(proportions):
            column_width = (wordTableTotalWidth * proportion) / sum(proportions)
            wordTable.setColumnWidth(i, column_width)

        # 设置内层表格的最小高度
        wordTable.setMinimumHeight(self.firstRowHeight)
        wordTable.setMinimumWidth(total_width)
        return wordTable

    def newSentenceTable(self, total_width):
        """
        创建Sentence-score子表格
        :param total_width: 子表格宽度
        :return: QTableWidget
        """
        sentenceTable = QTableWidget(1, 5)  # 1行5列
        headerLabels = ["Accuracy:", "Completeness:", "Fluency:", "Prosodic", "Total:"]
        sentenceTable.setHorizontalHeaderLabels(headerLabels)
        sentenceTable.verticalHeader().hide()

        self.sentenceAccLabel = QLabel("90")
        self.sentenceComLabel = QLabel("92")
        self.sentenceFluLabel = QLabel("94")
        self.sentenceProLabel = QLabel("95")
        self.sentenceTotLabel = QLabel("93")

        self.sentenceAccLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sentenceComLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sentenceFluLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sentenceProLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sentenceTotLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        sentenceTable.setCellWidget(0, 0, self.sentenceAccLabel)
        sentenceTable.setCellWidget(0, 1, self.sentenceComLabel)
        sentenceTable.setCellWidget(0, 2, self.sentenceFluLabel)
        sentenceTable.setCellWidget(0, 3, self.sentenceProLabel)
        sentenceTable.setCellWidget(0, 4, self.sentenceTotLabel)

        # 设置表格的大小策略
        sentenceTable.setSizeAdjustPolicy(QTableWidget.SizeAdjustPolicy.AdjustToContents)  # 根据内容调整大小
        sentenceTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 隐藏垂直滚动条
        sentenceTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 隐藏水平滚动条

        sentenceTableTotalWidth = total_width  # 设置表格总宽度
        proportions = [1, 1.2, 1, 1, 1]  # 各列占的比例

        for i, proportion in enumerate(proportions):
            column_width = (sentenceTableTotalWidth * proportion) / sum(proportions)
            sentenceTable.setColumnWidth(i, column_width)
        # 设置内层表格的最小高度
        sentenceTable.setMinimumHeight(self.firstRowHeight)
        sentenceTable.setMinimumWidth(total_width)
        return sentenceTable


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MTableWidget()
    window.show()
    sys.exit(app.exec())
