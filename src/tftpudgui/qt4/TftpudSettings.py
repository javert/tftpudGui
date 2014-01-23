'''
Created on 21 Dec 2013

@author: huw
'''

from ConfigParser import ConfigParser

class TftpudSettings:
    '''
    A class to hold the settings for the TftpudServerGui application.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.saveLastUsed = False
        self.defaultDirectory = ''
        self.defaultIpAddress = ''
        self.defaultPort = 69
        self.ephemeralPorts = [2048, 65535]
        self.tftpTimeout = 6.0
        self.tftpRetries = 3
        
    def write(self, f):
        '''Write these TFTPUD settings to the given file handle.'''
        cfg = ConfigParser()
        netSection = 'Network'
        cfg.add_section(netSection)
        cfg.set(netSection, 'defaultIpAddress', self.defaultIpAddress)
        cfg.set(netSection, 'defaultPort', self.defaultPort)
        cfg.set(netSection, 'ephemeralPortsFrom', self.ephemeralPorts[0])
        cfg.set(netSection, 'ephemeralPortsTo', self.ephemeralPorts[1])
        
        tftpSection = 'TFTP'
        cfg.add_section(tftpSection)
        cfg.set(tftpSection, 'timeout', self.tftpTimeout)
        cfg.set(tftpSection, 'retries', self.tftpRetries)
        
        serverSection = 'Server'
        cfg.add_section(serverSection)
        cfg.set(serverSection, 'defaultDirectory', self.defaultDirectory)
        cfg.set(serverSection, 'saveLastUsed', self.saveLastUsed)
        
        cfg.write(f)
    
    def read(self, f):
        '''Read the settings from the given file handle.'''
        cfg = ConfigParser()
        cfg.readfp(f)
        
        netSection = 'Network'
        if cfg.has_section(netSection):
            if cfg.has_option(netSection, 'defaultIpAddress'):
                self.defaultIpAddress = cfg.get(netSection, 'defaultIpAddress')
            if cfg.has_option(netSection, 'defaultPort'):
                self.defaultPort = cfg.getint(netSection, 'defaultPort')
            if cfg.has_option(netSection, 'ephemeralPortsFrom'):
                self.ephemeralPorts[0] = cfg.getint(netSection, 'ephemeralPortsFrom')
            if cfg.has_option(netSection, 'ephemeralPortsTo'):
                self.ephemeralPorts[1] = cfg.getint(netSection, 'ephemeralPortsTo')
                        
        tftpSection = 'TFTP'
        if cfg.has_section(tftpSection):
            if cfg.has_option(tftpSection, 'timeout'):
                self.tftpTimeout = cfg.getfloat(tftpSection, 'timeout')
            if cfg.has_option(tftpSection, 'retries'):
                self.tftpRetries = cfg.getint(tftpSection, 'retries')
                        
        serverSection = 'Server'
        if cfg.has_section(serverSection):
            if cfg.has_option(serverSection, 'defaultDirectory'):
                self.defaultDirectory = cfg.get(serverSection, 'defaultDirectory')
            if cfg.has_option(serverSection, 'saveLastUsed'):
                self.saveLastUsed = cfg.getboolean(serverSection, 'saveLastUsed')
                
        