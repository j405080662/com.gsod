class Station:
    def __init__(self,data):
        self.name = str(data[0]+'--'+data[1])
        self.value = [data[2],data[3]]
    def out(self):
        return "Station [name=" + self.name + ", value=" + str(self.value)+ "]"