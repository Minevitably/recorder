# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import static.apprcc_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(348, 394)
        Form.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TitleLabel = QLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(18)
        font.setBold(True)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.TitleLabel)

        self.selectSentenceLabel = QLabel(Form)
        self.selectSentenceLabel.setObjectName(u"selectSentenceLabel")
        self.selectSentenceLabel.setMinimumSize(QSize(0, 60))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        self.selectSentenceLabel.setFont(font1)
        self.selectSentenceLabel.setAlignment(Qt.AlignCenter)
        self.selectSentenceLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.selectSentenceLabel)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.recordBtn = QPushButton(self.widget_3)
        self.recordBtn.setObjectName(u"recordBtn")
        self.recordBtn.setMinimumSize(QSize(70, 70))
        self.recordBtn.setMaximumSize(QSize(70, 70))
        self.recordBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.recordBtn.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/pic/resources/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.recordBtn.setIcon(icon)
        self.recordBtn.setIconSize(QSize(70, 70))
        self.recordBtn.setCheckable(False)
        self.recordBtn.setFlat(True)

        self.horizontalLayout_4.addWidget(self.recordBtn)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.evaluateBtn = QPushButton(self.widget)
        self.evaluateBtn.setObjectName(u"evaluateBtn")
        self.evaluateBtn.setMinimumSize(QSize(0, 40))
        self.evaluateBtn.setMaximumSize(QSize(90, 16777215))
        self.evaluateBtn.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.evaluateBtn)


        self.verticalLayout.addWidget(self.widget)

        self.bottomWiget = QWidget(Form)
        self.bottomWiget.setObjectName(u"bottomWiget")
        self.bottomWiget.setAutoFillBackground(False)
        self.horizontalLayout_3 = QHBoxLayout(self.bottomWiget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.bottomWiget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.bottomWiget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"Pronunciation evaluation", None))
        self.selectSentenceLabel.setText(QCoreApplication.translate("Form", u"We call it bear", None))
        self.recordBtn.setText("")
        self.evaluateBtn.setText(QCoreApplication.translate("Form", u"\u8bc4\u4f30", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Phoneme-score", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Word-score", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Sentence-score", None));
    # retranslateUi

