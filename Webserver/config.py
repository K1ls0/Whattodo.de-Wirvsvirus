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
            self.serverPort = self.parsedConf[MAIN_SECTION].get('server-port', '3000')

        else:
            self.logger.error('Error: No Main section named "%s" found in config file %s', MAIN_SECTION, self.configPath)

        self.logger.info('Loaded config with: useDatabase: "%b"', self.useDatabase)
        self.logger.info('Loaded config with: staticPath: "%s"', self.staticPath)

    def reloadConfig(self):
        self.loadConfig()


def getConfigInstance():
    global conf
    if conf is None:
        conf = ConfigParser(CONFIG_STANDARD_LOCATION)
    return conf
