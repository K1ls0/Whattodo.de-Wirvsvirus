import os
from config import getConfigInstance

config = getConfigInstance()


class SQLAdapter:
    def __init__(self):
        lines = []
        with open(config.dataFile, 'r+') as f:
            for line in f:
                lines.append(line)
        for c in lines:
            print(c)
