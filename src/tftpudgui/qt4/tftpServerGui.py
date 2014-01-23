# -*- coding: utf-8 -*-


from PySide import QtCore, QtGui, QtNetwork
from PySide.QtGui import QMessageBox

from ui_mainwindow import Ui_MainWindow
from SettingsDlg import SettingsDlg
from TftpudSettings import TftpudSettings

import os, sys

from tftpud.server.server import Server, ServerConfig


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    
    # Constants    
    settingsFileName = 'TftpudSettings.ini'
    settingsLocation = QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.DataLocation)
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        # Connect some signals to slots
        self.selectFolder.clicked.connect(self.onSelectFolder)
        self.browseFolder.clicked.connect(self.onOpenWorkingFolder)
        self.actionStart_Server.triggered.connect(self.onStartAction)
        self.actionStop_Serving.triggered.connect(self.onStopAction)
        self.actionAbout.triggered.connect(self.onAbout)
        self.actionSettings.triggered.connect(self.onSettings)
        
        # Get a list of the network interfaces available on this host.
        addresses = QtNetwork.QNetworkInterface.allAddresses()
        for addr in addresses:
            self.ipAddresses.addItem(addr.toString())
            
        # Add the current working directory to the folders
        self.folders.addItem(os.getcwd())
            
        self.statusbar.showMessage('Server not running')
        
        self.tftpServer = None
        
        # The settings for this application
        self.settings = TftpudSettings()
        self.importSettings()
        
    
    def importSettings(self):
        filename = os.path.join(MainWindow.settingsLocation, 
                               MainWindow.settingsFileName)
        if os.path.isfile(filename):
            f = open( filename, 'r' )
            self.settings.read(f)
            f.close()
            
            # Update the widgets from the settings
            if self.settings.defaultDirectory and os.path.isdir(self.settings.defaultDirectory) and self.settings.defaultDirectory != self.folders.currentText():
                self.folders.insertItem(0, self.settings.defaultDirectory)
                self.folders.setCurrentIndex(0)
                
            if self.settings.defaultIpAddress:
                i = self.ipAddresses.findText(self.settings.defaultIpAddress)
                if i >= 0:
                    self.ipAddresses.setCurrentIndex(i)
                    
            if self.settings.defaultPort != self.portNum.value():
                self.portNum.setValue(self.settings.defaultPort)
                    
        
    def saveSettings(self):
        f = open( os.path.join(MainWindow.settingsLocation, 
                               MainWindow.settingsFileName), 'w' )
        self.settings.write(f)
        f.close()
        
    def onAbout(self):
        aboutMsg = 'TFTP Until Dinner\n\nCopyright Huw Lewis 2014'
        aboutMsg += '\n\nA TFTP Server implemented in Python; User interface in Qt and PySide (LGPL)'
        aboutMsg += '\n\nLicensed under MIT license. See http://opensource.org/licenses/MIT'
        aboutMsg += '\n\ntftpudGui: https://github.com/javert/tftpudGui'
        aboutMsg += "\nTftpud: https://github.com/javert/tftpud"
        QMessageBox.about(self, 'TFTPUD', aboutMsg)
    
    def onSelectFolder(self):
        path = QtGui.QFileDialog.getExistingDirectory(caption='Select TFTP working directory',
                                                      dir=QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.DocumentsLocation))
        cbIndex = self.folders.findText(path)
        if cbIndex >= 0:
            self.folders.setCurrentIndex(cbIndex)
        else:
            # Add to the beginning of the list (using index -1)
            self.folders.insertItem(-1, path)
            self.folders.setCurrentIndex(0)
        
    def onOpenWorkingFolder(self):
        '''Open a file browser'''
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('file:////' + self.folders.currentText()))
        
    def receiveLogMessage(self, msg):
        self.log.append(msg)
        self.log.ensureCursorVisible()
        
    def onStartAction(self):
        '''Start the server'''
        
        tftpConfig = ServerConfig(self.ipAddresses.currentText())
        tftpConfig.listeningPort = int(self.portNum.value())
        tftpConfig.logger = self.receiveLogMessage
        tftpConfig.ephemeralPorts = self.settings.ephemeralPorts
        
        try:
        
            # Set the current dir for the server
            os.chdir(self.folders.currentText())
            
            # Create the server (which starts itself)
            self.tftpServer = Server(tftpConfig)
            
            self.actionStart_Server.setEnabled(False)
            self.startButton.setEnabled(False)
            self.actionStop_Serving.setEnabled(True)
            self.stopButton.setEnabled(True)
            
            self.statusbar.showMessage('Serving on ' + self.ipAddresses.currentText() + ', port ' + self.portNum.cleanText())
        except Exception, e:
            QMessageBox.critical(self, 'TFTPUD Failure', 'Failed to start server: ' + str(e))
            
    def onStopAction(self):
        self.statusbar.showMessage('Stopping server...')
        if self.tftpServer:
            self.tftpServer.stopServer(True)
        
        self.actionStop_Serving.setEnabled(False)
        self.stopButton.setEnabled(False)
        self.actionStart_Server.setEnabled(True)
        self.startButton.setEnabled(True)
        
        self.statusbar.showMessage('Server not running')
        
        if self.settings.saveLastUsed:
            self.settings.defaultIpAddress = self.ipAddresses.currentText()
            self.settings.defaultPort = self.portNum.value()
            self.settings.defaultDirectory = self.folders.currentText()
        
    def onSettings(self):
        dlg = SettingsDlg(self.settings)
        dlg.exec_()

def guiMain(argv):
    app = QtGui.QApplication(argv)
    mainWindow = MainWindow()
    mainWindow.show()
    exitCode = app.exec_()
    mainWindow.saveSettings()
    sys.exit(exitCode)
    
if __name__ == "__main__":
    guiMain(sys.argv)
