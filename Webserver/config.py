import configparser
import logging

MAIN_SECTION = "main"
CONFIG_STANDARD_LOCATION = "../config.yaml"

conf = None


class ConfigParser:
    def __init__(self, configPath):
        self.logger = logging.getLogger(__name__)

        self.configPath = configPath
        self.loadConfig()

    def loadConfig(self):
        self.parsedConf = configparser.ConfigParser(interpolation=None)

        self.parsedConf.optionxform = str

        try:
            self.parsedConf.read(self.configPath)
        except (Exception):
            self.logger.error('Error while reading config file "%s". Not found/not readable?', self.configPath)

        if self.parsedConf.has_section(MAIN_SECTION):
            self.useDatabase = self.parsedConf[MAIN_SECTION].getboolean('useDatabase', False)
            self.staticPath = self.parsedConf[MAIN_SECTION].get('staticPath', '../web')
            self.serverHost = self.parsedConf[MAIN_SECTION].get('server-host', '0.0.0.0')
            self.serverPort = self.parsedConf[MAIN_SECTION].getint('server-port', 3000)
            self.dataFile = self.parsedConf[MAIN_SECTION].get('dataFile', '../DataIn.txt')
            self.newDataQueryFile = self.parsedConf[MAIN_SECTION].get('newDataQueryFile', '../DataNew.txt')
            self.dataFileEncoding = self.parsedConf[MAIN_SECTION].get('dataFileEncoding', 'utf8')
            self.serverDebug = self.parsedConf[MAIN_SECTION].getboolean('serverDebug', False)

            self.mysqlCredentialName = self.parsedConf[MAIN_SECTION].get('mysql-credential-name', 'root')
            self.__mysqlCredentialpw = self.parsedConf[MAIN_SECTION].get('mysql-credential-pw', '')
            self.mysqlDataBaseName = self.parsedConf[MAIN_SECTION].get('mysql-database-name', 'Data')
            self.mysqlDataBaseHost = self.parsedConf[MAIN_SECTION].get('mysql-database-Host', '127.0.0.1')

        else:
            self.logger.error('Error: No Main section named "%s" found in config file %s', MAIN_SECTION, self.configPath)

        self.logger.info('Loaded config with: useDatabase: "%b"', self.useDatabase)
        self.logger.info('Loaded config with: staticPath: "%s"', self.staticPath)
        self.logger.info('Loaded config with: server-host: "%s"', self.serverHost)
        self.logger.info('Loaded config with: server-port: "%d"', self.serverPort)
        self.logger.info('Loaded config with: mysqlDataBaseHost: "%s"', self.mysqlDataBaseHost)
        self.logger.info('Loaded config with: mysqlDataBaseName: "%s"', self.mysqlDataBaseName)
        self.logger.info('Loaded config with: mysqlCredentials: "%s"', self.mysqlCredentialName)
        self.logger.info('Loaded config with: serverDebug: "%b"', self.serverDebug)
        self.logger.info('Loaded config with: dataFileEncoding: "%s"', self.dataFileEncoding)

    def reloadConfig(self):
        self.loadConfig()

    def popMySqlPasswd(self):
        if self.__mysqlCredentialpw is None:
            return ""
        pw = self.__mysqlCredentialpw
        del self.__mysqlCredentialpw
        return pw


def getConfigInstance():
    global conf
    if conf is None:
        conf = ConfigParser(CONFIG_STANDARD_LOCATION)
    return conf
