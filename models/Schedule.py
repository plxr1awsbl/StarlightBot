from model import AbstractModel
from Day import Day


class Schedule(AbstractModel):

    days: Day

    def getDataFromDB(self):
        pass