from model import AbstractModel
from Task import Task

class Day(AbstractModel):

    tasks: Task

    def getDataFromDB(self):
        pass