class AbstractModel:
    name: str
    id: int
    connectionId: int

    def getDataFromDB(self):
        pass