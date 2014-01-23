# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Sat Dec 21 21:47:55 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.setWindowModality(QtCore.Qt.NonModal)
        SettingsDialog.resize(400, 300)
        SettingsDialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(SettingsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtGui.QLabel(SettingsDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.ipAddress = QtGui.QLineEdit(SettingsDialog)
        self.ipAddress.setObjectName("ipAddress")
        self.gridLayout.addWidget(self.ipAddress, 2, 1, 1, 1)
        self.label = QtGui.QLabel(SettingsDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 10, 0, 1, 1)
        self.label_2 = QtGui.QLabel(SettingsDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.portNum = QtGui.QSpinBox(SettingsDialog)
        self.portNum.setMaximum(65535)
        self.portNum.setProperty("value", 69)
        self.portNum.setObjectName("portNum")
        self.gridLayout.addWidget(self.portNum, 3, 1, 1, 1)
        self.fromPort = QtGui.QSpinBox(SettingsDialog)
        self.fromPort.setMaximum(65535)
        self.fromPort.setProperty("value", 2048)
        self.fromPort.setObjectName("fromPort")
        self.gridLayout.addWidget(self.fromPort, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(SettingsDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.toPort = QtGui.QSpinBox(SettingsDialog)
        self.toPort.setMaximum(65535)
        self.toPort.setProperty("value", 65535)
        self.toPort.setObjectName("toPort")
        self.gridLayout.addWidget(self.toPort, 4, 2, 1, 1)
        self.timeout = QtGui.QDoubleSpinBox(SettingsDialog)
        self.timeout.setSingleStep(0.1)
        self.timeout.setProperty("value", 6.0)
        self.timeout.setObjectName("timeout")
        self.gridLayout.addWidget(self.timeout, 5, 1, 1, 1)
        self.label_5 = QtGui.QLabel(SettingsDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.retries = QtGui.QSpinBox(SettingsDialog)
        self.retries.setMaximum(99)
        self.retries.setProperty("value", 3)
        self.retries.setObjectName("retries")
        self.gridLayout.addWidget(self.retries, 6, 1, 1, 1)
        self.saveLastUsed = QtGui.QCheckBox(SettingsDialog)
        self.saveLastUsed.setChecked(True)
        self.saveLastUsed.setObjectName("saveLastUsed")
        self.gridLayout.addWidget(self.saveLastUsed, 7, 0, 1, 1)

        self.retranslateUi(SettingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "TFTP Server Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SettingsDialog", "TFTP Timeout (seconds)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsDialog", "Default IP Address", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SettingsDialog", "Default Port", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SettingsDialog", "Ephemeral Port Range", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SettingsDialog", "TFTP Retries", None, QtGui.QApplication.UnicodeUTF8))
        self.saveLastUsed.setText(QtGui.QApplication.translate("SettingsDialog", "Save last used settings", None, QtGui.QApplication.UnicodeUTF8))

