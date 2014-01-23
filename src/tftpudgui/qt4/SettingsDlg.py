'''
Created on 21 Dec 2013

@author: huw
'''
from PySide import QtCore, QtGui
from ui_settings import Ui_SettingsDialog
import sys

class SettingsDlg(QtGui.QDialog, Ui_SettingsDialog):
    '''
    The TFTPUD settings dialog.
    '''

    def __init__(self, settings):
        '''
        Constructor
        '''
        super(SettingsDlg, self).__init__()
        self.setupUi(self)
        
        self.settings = settings
        
        # set the values in the widgets from these settings
        self.ipAddress.setText(settings.defaultIpAddress)
        self.portNum.setValue(settings.defaultPort)
        self.fromPort.setValue(settings.ephemeralPorts[0])
        self.toPort.setValue(settings.ephemeralPorts[1])
        self.timeout.setValue(settings.tftpTimeout)
        self.retries.setValue(settings.tftpRetries)
        self.saveLastUsed.setChecked(settings.saveLastUsed)
                
    def accept(self):
        '''On dialog OK. Save the config details for the client to query.'''
        QtGui.QDialog.accept(self)
        
        self.settings.defaultIpAddress = self.ipAddress.text()
        self.settings.defaultPort = self.portNum.value()
        self.settings.ephemeralPorts[0] = self.fromPort.value()
        self.settings.ephemeralPorts[1] = self.toPort.value()
        self.settings.tftpTimeout = self.timeout.value()
        self.settings.tftpRetries = self.retries.value()
        self.settings.saveLastUsed = self.saveLastUsed.isChecked()
        
    def reject(self):
        '''On dialog CANCEL. Do nothing.'''
        QtGui.QDialog.reject(self)
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dlg = SettingsDlg()
    dlg.exec_()
    #app.exec_()