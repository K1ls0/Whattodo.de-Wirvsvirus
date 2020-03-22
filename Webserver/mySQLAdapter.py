import os
import logging
from config import getConfigInstance
import mysql.connector

logger = logging.getLogger(__name__)
config = getConfigInstance()


class SQLAdapter:
    def __init__(self):
        self.cnx = None
        try:
            self.cnx = mysql.connector.connect(user=config.mysqlCredentialName, password=config.popMySqlPasswd(), host=config.mysqlDataBaseHost, database=config.mysqlDataBaseName)
            self.cursor = self.cnx.cursor()
        except(Exception):
            logger.error("Couldn't connect to SQL Server, Any request will be rejected")

    def __del__(self):
        if self.cnx is not None:
            self.cnx.close()

    def queryNew(self, data):
        pass

    def getAllTags(self):
        pass

    def getByTags(self, tags, include):
        pass
